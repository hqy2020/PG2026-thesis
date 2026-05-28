"""Generate intro_fig_compare.png via the gpt-image-2 model.

Supports two HTTP back-ends for image2:
  - sync     : OpenAI Python SDK against an OpenAI-Images-REST-compatible
               base_url (e.g. zenmux.ai). One POST returns b64_json/url.
  - evolink  : evolink.ai async task pattern. POST /v1/images/generations
               returns {"id": "task-...", "status": "processing"}; poll
               GET /v1/tasks/{id} until status == "completed", then download
               result_data[0].url.

Both modes read credentials from .env:
    IMAGE2_API_KEY   - bearer token
    IMAGE2_BASE_URL  - e.g. https://api.evolink.ai/v1  or  https://zenmux.ai/api/v1
    IMAGE2_MODEL     - e.g. gpt-image-2  or  openai/gpt-image-2
    IMAGE2_MODE      - 'evolink' or 'sync' (auto-detected from base_url if absent)

Reads the prompt from `assets/prompts/intro_fig_compare_image2_prompt.md`,
extracting the block under marker `## image2 PROMPT (中文`. Falls back to
the whole file if the marker is missing.

Backs up an existing target PNG to `<name>_backup.png` only on the first
overwrite (never clobbers an existing backup).

Run:
    set -a; source .env; set +a
    python3 assets/scripts/intro_fig_compare_image2_generate.py \
        [--size 1792x672] [--quality high] [--out assets/fig/intro_fig_compare.png]

A third route (gpt-image-2 skill via codex CLI / ChatGPT subscription) is
*not* covered here; use:
    bash ~/.claude/skills/gpt-image-2/scripts/gen.sh \
        --prompt "$(cat /tmp/intro_prompt_cn.txt)" --out <abs/out.png>
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import pathlib
import sys
import time
import urllib.error
import urllib.request

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
ENV_FILE = REPO_ROOT / ".env"
PROMPT_FILE = REPO_ROOT / "assets" / "prompts" / "intro_fig_compare_image2_prompt.md"
DEFAULT_OUTPUT = REPO_ROOT / "assets" / "fig" / "intro_fig_compare.png"

PROMPT_BLOCK_MARKER = "## image2 PROMPT (中文"

POLL_INTERVAL_S = 8
POLL_TIMEOUT_S = 900


def load_env(env_file: pathlib.Path) -> None:
    if not env_file.exists():
        return
    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip())


def read_prompt(prompt_file: pathlib.Path) -> str:
    text = prompt_file.read_text(encoding="utf-8")
    if PROMPT_BLOCK_MARKER in text:
        block = text.split(PROMPT_BLOCK_MARKER, 1)[1]
        next_idx = block.find("\n## ")
        if next_idx >= 0:
            block = block[:next_idx]
        block = block.split("\n", 1)[1] if "\n" in block else block
        return block.strip()
    return text.strip()


def backup_existing(output: pathlib.Path) -> None:
    backup = output.with_name(output.stem + "_backup" + output.suffix)
    if output.exists() and not backup.exists():
        output.rename(backup)
        print(f"[backup] {output.name} -> {backup.name}")


def _http_json(method: str, url: str, headers: dict, body: dict | None = None, timeout: int = 60):
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read().decode("utf-8", errors="ignore") or "{}")


def call_evolink(prompt: str, base_url: str, api_key: str, model: str,
                 size: str, quality: str, out: pathlib.Path) -> int:
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    payload = {"model": model, "prompt": prompt, "n": 1, "size": size, "quality": quality}
    print(f"[evolink] POST {base_url}/images/generations size={size} quality={quality}")
    t0 = time.time()
    code, data = _http_json("POST", f"{base_url}/images/generations", headers, payload, timeout=60)
    if code != 200:
        print(f"[evolink] submit failed HTTP={code}: {data}")
        return 0
    task_id = data.get("id")
    if not task_id:
        print(f"[evolink] no task id in response: {data}")
        return 0
    est = data.get("task_info", {}).get("estimated_time", "?")
    print(f"[evolink] task_id={task_id} estimated={est}s")

    last_progress = -1
    deadline = t0 + POLL_TIMEOUT_S
    while time.time() < deadline:
        time.sleep(POLL_INTERVAL_S)
        code, d = _http_json("GET", f"{base_url}/tasks/{task_id}", headers, timeout=30)
        if code != 200:
            print(f"[evolink] poll HTTP={code}: {d}")
            continue
        status = d.get("status")
        progress = d.get("progress", 0)
        if progress != last_progress:
            print(f"[evolink] +{int(time.time()-t0)}s status={status} progress={progress}")
            last_progress = progress
        if status in ("completed", "succeeded", "success"):
            urls = d.get("results") or [r.get("url") for r in d.get("result_data", []) if r.get("url")]
            if not urls:
                print(f"[evolink] terminal but no urls: {d}")
                return 0
            raw = urllib.request.urlopen(urls[0], timeout=300).read()
            out.write_bytes(raw)
            dt = time.time() - t0
            print(f"[evolink] wrote {out.relative_to(REPO_ROOT)} ({len(raw)/1024:.1f} KB) total {dt:.1f}s")
            return len(raw)
        if status in ("failed", "cancelled", "error"):
            print(f"[evolink] terminal FAIL status={status} data={d}")
            return 0
    print(f"[evolink] timeout after {POLL_TIMEOUT_S}s")
    return 0


def call_sync_openai(prompt: str, base_url: str, api_key: str, model: str,
                     size: str, quality: str, out: pathlib.Path) -> int:
    try:
        from openai import OpenAI
    except ImportError:
        print("[sync] openai SDK not installed; pip install openai", file=sys.stderr)
        return 0
    client = OpenAI(base_url=base_url, api_key=api_key, timeout=600.0, max_retries=2)
    print(f"[sync] base={base_url} model={model} size={size} quality={quality}")
    t0 = time.time()
    result = client.images.generate(model=model, prompt=prompt, n=1,
                                    size=size, quality=quality, timeout=600.0)
    img = result.data[0]
    b64 = getattr(img, "b64_json", None)
    url = getattr(img, "url", None)
    if b64:
        raw = base64.b64decode(b64)
    elif url:
        raw = urllib.request.urlopen(url, timeout=300).read()
    else:
        print("[sync] response missing b64_json and url", file=sys.stderr)
        return 0
    out.write_bytes(raw)
    dt = time.time() - t0
    print(f"[sync] wrote {out.relative_to(REPO_ROOT)} ({len(raw)/1024:.1f} KB) in {dt:.1f}s")
    return len(raw)


def detect_mode(base_url: str) -> str:
    if "evolink" in base_url:
        return "evolink"
    return "sync"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--size", default="1792x672",
                        help="WxH; longest side <= 3840, each side multiple of 16, ratio <= 3:1")
    parser.add_argument("--quality", default="high",
                        choices=["auto", "low", "medium", "high"])
    parser.add_argument("--out", default=str(DEFAULT_OUTPUT),
                        help="Output PNG path (default: assets/fig/intro_fig_compare.png)")
    parser.add_argument("--mode", default=None,
                        choices=["sync", "evolink"],
                        help="Override transport mode; default auto-detect from IMAGE2_BASE_URL")
    parser.add_argument("--no-backup", action="store_true",
                        help="Do not move existing png to backup before overwriting")
    args = parser.parse_args()

    load_env(ENV_FILE)
    api_key = os.environ.get("IMAGE2_API_KEY")
    base_url = os.environ.get("IMAGE2_BASE_URL", "https://api.evolink.ai/v1")
    model = os.environ.get("IMAGE2_MODEL", "gpt-image-2")
    if not api_key:
        sys.stderr.write("IMAGE2_API_KEY not set. Source .env first.\n")
        return 2
    mode = args.mode or os.environ.get("IMAGE2_MODE") or detect_mode(base_url)

    prompt = read_prompt(PROMPT_FILE)
    fp = hashlib.sha1(prompt.encode("utf-8")).hexdigest()[:10]
    print(f"[prompt] file={PROMPT_FILE.relative_to(REPO_ROOT)} "
          f"len={len(prompt)} sha1[:10]={fp}")
    print(f"[req] mode={mode} base={base_url} model={model}")

    out = pathlib.Path(args.out).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    if not args.no_backup:
        backup_existing(out)

    if mode == "evolink":
        nb = call_evolink(prompt, base_url, api_key, model, args.size, args.quality, out)
    else:
        nb = call_sync_openai(prompt, base_url, api_key, model, args.size, args.quality, out)
    return 0 if nb > 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
