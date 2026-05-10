import argparse
import json
import os
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec
from matplotlib.patches import Rectangle


ROOT = Path("/Users/openingcloud/Documents/GardenOfOpeningClouds/1-Information/PG2026论文投稿/PG2026-thesis")
FIG_DIR = ROOT / "figures"
LATEX_DIR = ROOT / "latex"

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = [
    "Arial",
    "Helvetica",
    "PingFang SC",
    "Hiragino Sans GB",
    "Noto Sans CJK SC",
    "DejaVu Sans",
]
plt.rcParams["axes.unicode_minus"] = False


PALETTE = {
    "baseline": "#8FA0A5",
    "sps": "#E6862A",
    "adm": "#2FAE60",
    "gap": "#EF4A3A",
    "full": "#C63C2E",
    "grid": "#D6DCE5",
    "roi_a": "#E64646",
    "roi_b": "#2F84C2",
    "border": "#D9DEE5",
    "text": "#111827",
}


def load_manifest(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def resolve_path(path_str: str) -> Path:
    path = Path(path_str)
    return path if path.is_absolute() else ROOT / path


def load_image(path_str: str) -> np.ndarray:
    path = resolve_path(path_str)
    if not path.exists():
        raise FileNotFoundError(f"Missing image: {path}")
    img = plt.imread(path)
    if img.ndim == 3:
        img = img[..., :3].mean(axis=-1)
    return img.astype(np.float32)


def hide_axes(ax):
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)


def apply_window(img: np.ndarray, window):
    vmin, vmax = window
    return img, vmin, vmax


def draw_cell(ax, img: np.ndarray, window, title=None, ylabel=None, border=False):
    img, vmin, vmax = apply_window(img, window)
    ax.imshow(img, cmap="gray", vmin=vmin, vmax=vmax)
    hide_axes(ax)
    if title:
        ax.set_title(title, fontsize=9, pad=4)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=9, rotation=90, labelpad=10)
    if border:
        ax.add_patch(
            Rectangle(
                (0, 0),
                1,
                1,
                transform=ax.transAxes,
                fill=False,
                linewidth=0.6,
                edgecolor=PALETTE["border"],
            )
        )


def build_input_montage(input_paths, window):
    imgs = [load_image(p) for p in input_paths]
    widths = [img.shape[1] for img in imgs]
    heights = [img.shape[0] for img in imgs]
    target_h = max(heights)
    resized = []
    for img in imgs:
        if img.shape[0] == target_h:
            resized.append(img)
            continue
        scale = target_h / img.shape[0]
        target_w = max(1, int(round(img.shape[1] * scale)))
        x_old = np.linspace(0.0, 1.0, img.shape[1])
        x_new = np.linspace(0.0, 1.0, target_w)
        tmp = np.vstack([np.interp(x_new, x_old, row) for row in img])
        if tmp.shape[0] != target_h:
            y_old = np.linspace(0.0, 1.0, tmp.shape[0])
            y_new = np.linspace(0.0, 1.0, target_h)
            tmp = np.vstack([np.interp(y_new, y_old, tmp[:, col]) for col in range(tmp.shape[1])]).T
        resized.append(tmp)
    spacer = np.zeros((target_h, 6), dtype=np.float32)
    montage = resized[0]
    for img in resized[1:]:
        montage = np.concatenate([montage, spacer, img], axis=1)
    return montage


def render_qual_main(manifest_path: str):
    manifest = load_manifest(manifest_path)
    methods = manifest["methods"]
    scenes = manifest["scenes"]
    cols = 2 + len(methods)
    fig = plt.figure(figsize=(7.1, 4.2), constrained_layout=False)
    gs = GridSpec(len(scenes), cols, figure=fig, wspace=0.02, hspace=0.05)

    header = ["Input", "GT"] + methods
    for r, scene in enumerate(scenes):
        window = scene["window"]
        montage = build_input_montage(scene["inputs"], window)
        ax = fig.add_subplot(gs[r, 0])
        draw_cell(ax, montage, window, title=header[0] if r == 0 else None, ylabel=scene["name"], border=True)

        ax = fig.add_subplot(gs[r, 1])
        draw_cell(ax, load_image(scene["gt"]), window, title=header[1] if r == 0 else None, border=True)

        for c, method in enumerate(methods, start=2):
            path = scene["predictions"].get(method)
            ax = fig.add_subplot(gs[r, c])
            if not path:
                ax.text(0.5, 0.5, "Unavailable", ha="center", va="center", fontsize=8, color="#6B7280")
                hide_axes(ax)
            else:
                draw_cell(ax, load_image(path), window, title=method if r == 0 else None, border=True)

    out_path = FIG_DIR / manifest.get("output", "fig_qual_main.png")
    fig.savefig(out_path, dpi=360, bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)
    return out_path


def render_qual_zoom(manifest_path: str):
    manifest = load_manifest(manifest_path)
    methods = manifest["methods"]
    cases = manifest["cases"]
    fig = plt.figure(figsize=(7.1, 3.0), constrained_layout=False)
    gs = GridSpec(len(cases) * 2, len(methods), figure=fig, wspace=0.02, hspace=0.06)

    roi_colors = [PALETTE["roi_a"], PALETTE["roi_b"]]
    for case_idx, case in enumerate(cases):
        window = case["window"]
        rois = case["rois"] if "rois" in case else [{"label": "ROI", "box": case["roi"], "color": roi_colors[0]}]
        for method_idx, method in enumerate(methods):
            img = load_image(case["images"][method])
            ax_full = fig.add_subplot(gs[case_idx * 2, method_idx])
            draw_cell(ax_full, img, window, title=method if case_idx == 0 else None, ylabel=case["name"] if method_idx == 0 else None, border=True)
            for roi_idx, roi in enumerate(rois):
                x0, y0, x1, y1 = roi["box"]
                color = roi.get("color", roi_colors[roi_idx % len(roi_colors)])
                ax_full.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fill=False, linewidth=1.2, edgecolor=color))

            ax_zoom = fig.add_subplot(gs[case_idx * 2 + 1, method_idx])
            # default: show first ROI; if multiple ROIs are needed, use separate manifests or extend layout
            x0, y0, x1, y1 = rois[0]["box"]
            crop = img[y0:y1, x0:x1]
            draw_cell(ax_zoom, crop, window, border=True)
            ax_zoom.text(0.02, 0.04, rois[0].get("label", "ROI"), transform=ax_zoom.transAxes, fontsize=8, color=rois[0].get("color", roi_colors[0]), ha="left", va="bottom")

    out_path = FIG_DIR / manifest.get("output", "fig_qual_zoom.png")
    fig.savefig(out_path, dpi=400, bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)
    return out_path


def render_spatial_distribution(manifest_path: str):
    manifest = load_manifest(manifest_path)
    stages = manifest["stages"]
    fig = plt.figure(figsize=(7.1, 3.6), constrained_layout=False)
    gs = GridSpec(2, len(stages), figure=fig, wspace=0.03, hspace=0.05)

    for idx, stage in enumerate(stages):
        structure = load_image(stage["structure"])
        render = load_image(stage["render"])
        structure_window = stage.get("structure_window", [float(np.min(structure)), float(np.max(structure))])
        render_window = stage.get("render_window", [float(np.min(render)), float(np.max(render))])

        ax_top = fig.add_subplot(gs[0, idx])
        draw_cell(ax_top, structure, structure_window, title=stage["name"], ylabel="Structure" if idx == 0 else None, border=True)

        ax_bottom = fig.add_subplot(gs[1, idx])
        draw_cell(ax_bottom, render, render_window, ylabel="Render/Slice" if idx == 0 else None, border=True)

    out_path = FIG_DIR / manifest.get("output", "fig_spatial_distribution.png")
    fig.savefig(out_path, dpi=360, bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)
    return out_path


def residual_map(pred: np.ndarray, gt: np.ndarray) -> np.ndarray:
    return np.abs(pred.astype(np.float32) - gt.astype(np.float32))


def render_ablation_visual(manifest_path: str):
    manifest = load_manifest(manifest_path)
    variants = manifest["variants"]
    cases = manifest["cases"]
    fig = plt.figure(figsize=(7.1, 3.8), constrained_layout=False)
    outer = GridSpec(len(cases), len(variants), figure=fig, wspace=0.03, hspace=0.08)

    for case_idx, case in enumerate(cases):
        window = case["window"]
        gt = load_image(case["gt"])
        for var_idx, variant in enumerate(variants):
            slot = GridSpecFromSubplotSpec(2, 1, subplot_spec=outer[case_idx, var_idx], height_ratios=[5, 1], hspace=0.02)
            pred = load_image(case["images"][variant])
            ax_main = fig.add_subplot(slot[0, 0])
            draw_cell(ax_main, pred, window, title=variant if case_idx == 0 else None, ylabel=case["name"] if var_idx == 0 else None, border=True)

            ax_res = fig.add_subplot(slot[1, 0])
            res = residual_map(pred, gt)
            vmax = case.get("residual_vmax", float(np.percentile(res, 99)))
            ax_res.imshow(res, cmap="magma", vmin=0.0, vmax=vmax)
            hide_axes(ax_res)
            ax_res.text(0.02, 0.06, "|pred-gt|", transform=ax_res.transAxes, fontsize=7, color="white", ha="left", va="bottom")

    out_path = FIG_DIR / manifest.get("output", "fig_ablation_visual.png")
    fig.savefig(out_path, dpi=360, bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)
    return out_path


RENDERERS = {
    "qual_main": render_qual_main,
    "qual_zoom": render_qual_zoom,
    "spatial_distribution": render_spatial_distribution,
    "ablation_visual": render_ablation_visual,
}


def parse_args():
    parser = argparse.ArgumentParser(description="Render camera-ready experiment figures from JSON manifests.")
    parser.add_argument(
        "target",
        choices=sorted(RENDERERS.keys()),
        help="Figure type to render.",
    )
    parser.add_argument(
        "--manifest",
        required=True,
        help="Path to JSON manifest. Relative paths are resolved from the repo root.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    manifest = args.manifest
    if not os.path.isabs(manifest):
        manifest = str((Path.cwd() / manifest).resolve())
    out = RENDERERS[args.target](manifest)
    print(f"Rendered: {out}")


if __name__ == "__main__":
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    main()
