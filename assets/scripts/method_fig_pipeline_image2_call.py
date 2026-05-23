"""Generate the Method Pipeline figure (F03) via the image2 API.

This script is a thin wrapper around the ``POST /v1/images/generations``
endpoint described in ``assets/data/image2.md``. It reads the prompt from
``assets/prompts/method_fig_pipeline_image2_prompt.md`` and saves the
returned PNG to ``assets/fig/fig_method_pipeline.png``.

Usage:
    export IMAGE2_API_KEY="sk-xxxx"
    python assets/scripts/method_fig_pipeline_image2_call.py

Environment overrides:
    IMAGE2_API_KEY      required, bearer token for the image2 endpoint
    IMAGE2_BASE_URL     optional, defaults to https://mikucode.xyz
    IMAGE2_MODEL        optional, defaults to gpt-image-2
    IMAGE2_SIZE         optional, defaults to 1980x800 (wide double-column)
    IMAGE2_QUALITY      optional, defaults to high
"""

from __future__ import annotations

import base64
import os
import pathlib
import sys

import requests


REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
PROMPT_FILE = REPO_ROOT / "assets" / "prompts" / "method_fig_pipeline_image2_prompt.md"
OUTPUT_FILE = REPO_ROOT / "assets" / "fig" / "method_fig_pipeline.png"

BASE_URL = os.environ.get("IMAGE2_BASE_URL", "https://mikucode.xyz").rstrip("/")
MODEL = os.environ.get("IMAGE2_MODEL", "gpt-image-2")
SIZE = os.environ.get("IMAGE2_SIZE", "1980x800")
QUALITY = os.environ.get("IMAGE2_QUALITY", "high")


def load_prompt(prompt_path: pathlib.Path) -> str:
    """Return the full prompt text from the markdown spec file."""
    if not prompt_path.is_file():
        raise FileNotFoundError(f"Prompt file not found: {prompt_path}")
    text = prompt_path.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError(f"Prompt file is empty: {prompt_path}")
    return text


def main() -> int:
    api_key = (os.environ.get("IMAGE2_API_KEY") or "").strip()
    if not api_key:
        sys.stderr.write(
            "ERROR: IMAGE2_API_KEY is not set. Export it before running.\n"
        )
        return 2

    prompt = load_prompt(PROMPT_FILE)
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "n": 1,
        "size": SIZE,
        "quality": QUALITY,
        "output_format": "png",
    }

    response = requests.post(
        f"{BASE_URL}/v1/images/generations",
        headers={"Authorization": f"Bearer {api_key}"},
        json=payload,
        timeout=180,
    )
    response.raise_for_status()
    data = response.json().get("data") or []
    if not data:
        raise RuntimeError("API returned no image data")
    image = data[0]

    if image.get("b64_json"):
        OUTPUT_FILE.write_bytes(base64.b64decode(image["b64_json"]))
    elif image.get("url"):
        img_resp = requests.get(image["url"], timeout=180, verify=False)
        img_resp.raise_for_status()
        OUTPUT_FILE.write_bytes(img_resp.content)
    else:
        raise RuntimeError("API returned neither b64_json nor url")

    print(f"saved to {OUTPUT_FILE.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
