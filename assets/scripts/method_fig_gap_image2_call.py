"""Generate the GAP Module figure (F05) via the image2 API.

Reads ``assets/prompts/method_fig_gap_image2_prompt.md`` and saves the returned
PNG to ``assets/fig/method_fig_gap.png``.
"""

from __future__ import annotations

import base64
import os
import pathlib
import sys

import requests


REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
PROMPT_FILE = REPO_ROOT / "assets" / "prompts" / "method_fig_gap_image2_prompt.md"
OUTPUT_FILE = REPO_ROOT / "assets" / "fig" / "method_fig_gap.png"

BASE_URL = os.environ.get("IMAGE2_BASE_URL", "https://mikucode.xyz").rstrip("/")
MODEL = os.environ.get("IMAGE2_MODEL", "gpt-image-2")
SIZE = os.environ.get("IMAGE2_SIZE", "1800x720")
QUALITY = os.environ.get("IMAGE2_QUALITY", "high")


def load_prompt(prompt_path: pathlib.Path) -> str:
    if not prompt_path.is_file():
        raise FileNotFoundError(f"Prompt file not found: {prompt_path}")
    text = prompt_path.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError(f"Prompt file is empty: {prompt_path}")
    return text


def main() -> int:
    api_key = (os.environ.get("IMAGE2_API_KEY") or "").strip()
    if not api_key:
        sys.stderr.write("ERROR: IMAGE2_API_KEY is not set. Export it before running.\n")
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
