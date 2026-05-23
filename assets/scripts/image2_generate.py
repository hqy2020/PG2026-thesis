"""Universal image2 generation script for XRA-GS paper figures (concept/schematic only).

Reads a prompt file from assets/prompts/, calls the gpt-image-2 API, and saves
the result to assets/fig/. See assets/data/image2.md for API documentation.

API Key / proxy settings are loaded automatically from <repo_root>/.env if present.
No manual export needed once .env is configured.

Usage (single figure):
    python assets/scripts/image2_generate.py --prompt <prompt_stem> --output <output_stem>

    # Example: generate intro comparison figure
    python assets/scripts/image2_generate.py \\
        --prompt intro_fig_compare_image2_prompt \\
        --output intro_fig_compare

    # Example: generate method pipeline figure with custom size
    python assets/scripts/image2_generate.py \\
        --prompt method_fig_pipeline_image2_prompt \\
        --output fig_method_pipeline \\
        --size 1980x800

Usage (list known prompts):
    python assets/scripts/image2_generate.py --list

.env file (repo root, auto-loaded, never committed):
    IMAGE2_API_KEY=sk-xxxx
    NO_PROXY=mikucode.xyz       # bypass local proxy (Clash/V2Ray etc.)

Environment variables (override .env if set in shell):
    IMAGE2_API_KEY      required  Bearer token for the mikucode.xyz endpoint
    IMAGE2_BASE_URL     optional  Defaults to https://mikucode.xyz
    IMAGE2_MODEL        optional  Defaults to gpt-image-2
    IMAGE2_QUALITY      optional  Defaults to high
    NO_PROXY            optional  Comma-separated list of hosts to bypass proxy

Argument reference:
    --prompt  STEM   Filename stem under assets/prompts/ (without .md extension)
    --output  STEM   Filename stem for the output PNG under assets/fig/ (without .png extension)
    --size    WxH    Override image dimensions, e.g. 1840x820 (default) or 1980x800
    --quality LEVEL  Override quality: auto | low | medium | high (default: high)
    --list           Print all prompt files found under assets/prompts/ and exit
"""

from __future__ import annotations

import argparse
import base64
import os
import pathlib
import sys

import requests


REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]


def _load_dotenv(env_path: pathlib.Path) -> None:
    """Load key=value pairs from a .env file into os.environ.

    - Shell environment variables take precedence (existing vars are not overwritten).
    - Lines starting with # and blank lines are ignored.
    - Inline comments (#...) are stripped.
    - Surrounding quotes on values are removed.
    """
    if not env_path.is_file():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.split("#", 1)[0].strip().strip("\"'")
        if key and key not in os.environ:
            os.environ[key] = value


# Auto-load .env before reading any env vars
_load_dotenv(REPO_ROOT / ".env")
PROMPTS_DIR = REPO_ROOT / "assets" / "prompts"
FIGS_DIR = REPO_ROOT / "assets" / "fig"

BASE_URL = os.environ.get("IMAGE2_BASE_URL", "https://mikucode.xyz").rstrip("/")
MODEL = os.environ.get("IMAGE2_MODEL", "gpt-image-2")
DEFAULT_SIZE = "1840x820"
DEFAULT_QUALITY = os.environ.get("IMAGE2_QUALITY", "high")


def list_prompts() -> None:
    prompt_files = sorted(PROMPTS_DIR.glob("*.md"))
    if not prompt_files:
        print("No prompt files found in", PROMPTS_DIR)
        return
    print(f"Available prompts in {PROMPTS_DIR.relative_to(REPO_ROOT)}:\n")
    for f in prompt_files:
        # Read first non-empty line after '# ' as description
        desc = ""
        for line in f.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("Target file:"):
                desc = line.replace("Target file:", "→").strip()
                break
        print(f"  {f.stem}")
        if desc:
            print(f"      {desc}")
    print()
    print("Run with: python assets/scripts/image2_generate.py --prompt <stem> --output <stem>")


def load_prompt(prompt_path: pathlib.Path) -> str:
    if not prompt_path.is_file():
        raise FileNotFoundError(
            f"Prompt file not found: {prompt_path}\n"
            f"Run --list to see available prompts."
        )
    text = prompt_path.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError(f"Prompt file is empty: {prompt_path}")
    return text


def generate(prompt_text: str, output_file: pathlib.Path, size: str, quality: str, api_key: str) -> None:
    output_file.parent.mkdir(parents=True, exist_ok=True)

    payload = {
        "model": MODEL,
        "prompt": prompt_text,
        "n": 1,
        "size": size,
        "quality": quality,
        "output_format": "png",
    }

    print(f"Sending request → {BASE_URL}/v1/images/generations")
    print(f"  model={MODEL}  size={size}  quality={quality}")
    print(f"  output → {output_file.relative_to(REPO_ROOT)}")

    response = requests.post(
        f"{BASE_URL}/v1/images/generations",
        headers={"Authorization": f"Bearer {api_key}"},
        json=payload,
        timeout=240,
    )
    response.raise_for_status()

    data = response.json().get("data") or []
    if not data:
        raise RuntimeError("API returned no image data")
    image = data[0]

    if image.get("b64_json"):
        output_file.write_bytes(base64.b64decode(image["b64_json"]))
    elif image.get("url"):
        img_resp = requests.get(image["url"], timeout=180)
        img_resp.raise_for_status()
        output_file.write_bytes(img_resp.content)
    else:
        raise RuntimeError("API returned neither b64_json nor url")

    size_kb = output_file.stat().st_size // 1024
    print(f"Saved: {output_file.relative_to(REPO_ROOT)}  ({size_kb} KB)")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate a schematic figure via gpt-image-2 API.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--prompt", metavar="STEM",
                        help="Filename stem under assets/prompts/ (without .md)")
    parser.add_argument("--output", metavar="STEM",
                        help="Filename stem for output PNG under assets/fig/ (without .png)")
    parser.add_argument("--size", metavar="WxH", default=DEFAULT_SIZE,
                        help=f"Image dimensions, default: {DEFAULT_SIZE}")
    parser.add_argument("--quality", metavar="LEVEL", default=DEFAULT_QUALITY,
                        choices=["auto", "low", "medium", "high"],
                        help=f"Quality level, default: {DEFAULT_QUALITY}")
    parser.add_argument("--list", action="store_true",
                        help="List available prompt files and exit")
    args = parser.parse_args()

    if args.list:
        list_prompts()
        return 0

    if not args.prompt or not args.output:
        parser.print_help()
        sys.stderr.write("\nError: --prompt and --output are required.\n")
        return 2

    api_key = os.environ.get("IMAGE2_API_KEY")
    if not api_key:
        sys.stderr.write(
            "Error: IMAGE2_API_KEY is not set.\n"
            "  export IMAGE2_API_KEY='sk-xxxx'\n"
        )
        return 2

    prompt_path = PROMPTS_DIR / f"{args.prompt}.md"
    output_path = FIGS_DIR / f"{args.output}.png"
    prompt_text = load_prompt(prompt_path)

    generate(prompt_text, output_path, args.size, args.quality, api_key)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
