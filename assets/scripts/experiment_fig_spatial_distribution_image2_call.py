"""Generate experiment_fig_spatial_distribution.png via gpt-image-2 API.

Delegates to the universal image2_generate.py script.

Usage:
    python assets/scripts/experiment_fig_spatial_distribution_image2_call.py

Prerequisites:
    export IMAGE2_API_KEY='sk-xxxx'
    (or set IMAGE2_API_KEY in repo-root .env)
"""
import subprocess
import sys
import pathlib

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]


def main() -> int:
    cmd = [
        sys.executable,
        str(REPO_ROOT / "assets" / "scripts" / "image2_generate.py"),
        "--prompt", "experiment_fig_spatial_distribution_image2_prompt",
        "--output", "experiment_fig_spatial_distribution",
        "--size", "1536x512",  # 3:1 ratio, within API limit
        "--quality", "high",
    ]
    print("Generating F10: Gaussian spatial distribution concept figure...")
    result = subprocess.run(cmd, cwd=str(REPO_ROOT))
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
