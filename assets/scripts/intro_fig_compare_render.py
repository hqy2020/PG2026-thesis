"""[COLD-BACKUP ONLY — DO NOT RUN AS MAIN FLOW]

Per CLAUDE.md §8, the main path for generating intro_fig_compare.png is the
image2 API (see assets/scripts/intro_fig_compare_image2_generate.py). This
matplotlib-based renderer plus the companion intro_fig_compare.drawio source
are kept only as a cold fallback, to be used solely when three or more
image2 iterations fail to meet the top-conference figure criteria.

If you find yourself running this script, document why image2 was rejected.

Output: assets/fig/intro_fig_compare.png (2400 x 900 at dpi=300, ~8 x 3 inches).
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle, Ellipse


BLUE = "#1F77B4"
ORANGE = "#FF7F0E"
GREEN = "#2CA02C"
GRAY_DARK = "#444444"
GRAY_MID = "#888888"
GRAY_LIGHT = "#CCCCCC"
PHANTOM_FILL = "#F4F4F4"
PHANTOM_EDGE = "#666666"
ORGAN_FILL = "#E5E5E5"

# Slightly larger canvas so 4 panels + colorbars + row labels all breathe.
FIG_W_IN, FIG_H_IN, DPI = 8.0, 3.0, 300


def gaussian_blur(arr, sigma=1.0):
    radius = max(1, int(round(3 * sigma)))
    x = np.arange(-radius, radius + 1)
    kernel = np.exp(-x ** 2 / (2 * sigma ** 2))
    kernel /= kernel.sum()
    out = np.apply_along_axis(lambda row: np.convolve(row, kernel, mode="same"), 1, arr)
    out = np.apply_along_axis(lambda col: np.convolve(col, kernel, mode="same"), 0, out)
    return out


def add_rotated_label(fig, x, y, w, h, text, color):
    ax = fig.add_axes([x, y, w, h])
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    ax.text(0.5, 0.5, text, rotation=90, ha="center", va="center",
            fontsize=6.0, fontweight="bold", color=color)


def add_col_title(fig, x, y, w, h, text):
    ax = fig.add_axes([x, y, w, h])
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    ax.text(0.5, 0.5, text, ha="center", va="center", fontsize=6.8, fontweight="bold")


def panel_ax(fig, x, y, w, h, frame=True):
    ax = fig.add_axes([x, y, w, h])
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.set_xticks([]); ax.set_yticks([])
    if frame:
        for spine in ax.spines.values():
            spine.set_edgecolor(GRAY_LIGHT)
            spine.set_linewidth(0.5)
    else:
        for spine in ax.spines.values():
            spine.set_visible(False)
    return ax


def draw_phantom(ax, fdk_support=False):
    if fdk_support:
        ax.add_patch(Ellipse((0.55, 0.5), 0.82, 0.70, fc=ORANGE, ec="none", alpha=0.18, zorder=0))
        ax.text(0.06, 0.93, "FDK support", fontsize=4.6, color=ORANGE,
                va="top", ha="left", fontweight="bold")
    ax.add_patch(Ellipse((0.55, 0.5), 0.62, 0.52, fc=PHANTOM_FILL,
                         ec=PHANTOM_EDGE, lw=0.7, zorder=1))
    for (cx, cy), w, h in [
        ((0.48, 0.55), 0.13, 0.10),
        ((0.66, 0.42), 0.10, 0.12),
        ((0.55, 0.32), 0.09, 0.07),
    ]:
        ax.add_patch(Ellipse((cx, cy), w, h, fc=ORGAN_FILL,
                             ec=PHANTOM_EDGE, lw=0.5, zorder=2))


def draw_rays(ax):
    det_x = 0.95
    ax.plot([det_x, det_x], [0.12, 0.88], color=GRAY_DARK, lw=1.0, solid_capstyle="butt")
    src_x = 0.06
    for sy, dy in [(0.30, 0.20), (0.50, 0.55), (0.70, 0.78)]:
        n_seg = 30
        xs = np.linspace(src_x, det_x, n_seg + 1)
        ys = np.linspace(sy, dy, n_seg + 1)
        for k in range(n_seg):
            t = k / (n_seg - 1)
            alpha = 0.30 + 0.55 * t
            ax.plot(xs[k:k + 2], ys[k:k + 2], color=BLUE, lw=1.0,
                    alpha=alpha, solid_capstyle="butt")
        ax.add_patch(Circle((src_x, sy), 0.014, fc=BLUE, ec="none"))


def draw_capacity_top(ax):
    ax.add_patch(Ellipse((0.5, 0.5), 0.72, 0.58, fc="none", ec=PHANTOM_EDGE, lw=0.7))
    rng = np.random.default_rng(7)
    for _ in range(24):
        theta = rng.uniform(0, 2 * np.pi)
        r = rng.uniform(0.92, 1.00)
        ax.add_patch(Circle((0.5 + 0.36 * r * np.cos(theta),
                             0.5 + 0.29 * r * np.sin(theta)),
                            0.013, fc=GRAY_MID, ec="none", alpha=0.95))
    for _ in range(5):
        theta = rng.uniform(0, 2 * np.pi)
        r = rng.uniform(0.0, 0.45)
        ax.add_patch(Circle((0.5 + 0.36 * r * np.cos(theta),
                             0.5 + 0.29 * r * np.sin(theta)),
                            0.013, fc=GRAY_MID, ec="none", alpha=0.6))
    ax.add_patch(FancyArrowPatch((0.96, 0.92), (0.82, 0.78),
                                 arrowstyle="-|>", mutation_scale=5,
                                 color=ORANGE, lw=0.9))
    ax.text(0.97, 0.95, "boundary-driven\nredundancy",
            ha="right", va="top", fontsize=4.6, color=ORANGE, fontweight="bold")
    draw_mini_bars(ax, 0.04, 0.06, 0.30, 0.16,
                   values=[0.80, 0.20], labels=["B", "I"],
                   colors=[ORANGE, GRAY_LIGHT])


def draw_capacity_bottom(ax):
    ax.add_patch(Ellipse((0.5, 0.5), 0.72, 0.58, fc="none", ec=PHANTOM_EDGE, lw=0.7))
    rng = np.random.default_rng(11)
    for _ in range(24):
        theta = rng.uniform(0, 2 * np.pi)
        r = rng.uniform(0.0, 0.82)
        ax.add_patch(Circle((0.5 + 0.36 * r * np.cos(theta),
                             0.5 + 0.29 * r * np.sin(theta)),
                            0.013, fc=GREEN, ec="none", alpha=0.85))
    for _ in range(6):
        theta = rng.uniform(0, 2 * np.pi)
        r = rng.uniform(0.93, 1.00)
        ax.add_patch(Circle((0.5 + 0.36 * r * np.cos(theta),
                             0.5 + 0.29 * r * np.sin(theta)),
                            0.011, fc=GRAY_MID, ec="none", alpha=0.65))
    ax.text(0.97, 0.95, "path-anchored\ninterior coverage",
            ha="right", va="top", fontsize=4.6, color=GREEN, fontweight="bold")
    draw_mini_bars(ax, 0.04, 0.06, 0.30, 0.16,
                   values=[0.35, 0.65], labels=["B", "I"],
                   colors=[GRAY_LIGHT, GREEN])


def draw_mini_bars(ax, x0, y0, w, h, values, labels, colors):
    ax.add_patch(Rectangle((x0, y0), w, h, fc="white", ec=GRAY_LIGHT, lw=0.4))
    n = len(values)
    bw = (w * 0.7) / n
    gap = (w - bw * n) / (n + 1)
    for i, (v, lab, c) in enumerate(zip(values, labels, colors)):
        bx = x0 + gap * (i + 1) + bw * i
        bh = (h - 0.05) * v
        ax.add_patch(Rectangle((bx, y0 + 0.025), bw, bh, fc=c, ec="none"))
        ax.text(bx + bw / 2, y0 + 0.008, lab, ha="center", va="bottom",
                fontsize=4.3, color=GRAY_DARK)
        ax.text(bx + bw / 2, y0 + 0.025 + bh + 0.005,
                f"{int(v * 100)}%", ha="center", va="bottom",
                fontsize=4.0, color=GRAY_DARK)


def draw_badges(fig, x, y, w, h):
    ax = fig.add_axes([x, y, w, h])
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    labels = [
        ("SPS  FDK-anchored\nseeding", BLUE, "init"),
        ("GAP  boundary\nrecycling", ORANGE, "mid"),
        ("ADM  position-aware\nrefinement", GREEN, "late"),
    ]
    n = 3
    bw = 0.30
    gap = (1 - bw * n) / (n + 1)
    for i, (text, color, stage) in enumerate(labels):
        bx = gap * (i + 1) + bw * i
        ax.add_patch(FancyBboxPatch(
            (bx, 0.20), bw, 0.55,
            boxstyle="round,pad=0.005,rounding_size=0.04",
            fc="white", ec=color, lw=1.0,
        ))
        ax.text(bx + bw / 2, 0.475, text, ha="center", va="center",
                fontsize=4.3, color=GRAY_DARK)
        ax.add_patch(FancyArrowPatch(
            (bx + bw / 2, 0.82), (bx + bw / 2, 0.98),
            arrowstyle="-|>", mutation_scale=5,
            color=GRAY_MID, lw=0.7, linestyle=(0, (2, 1.5)),
        ))
        ax.text(bx + bw / 2, 0.07, stage, ha="center", va="center",
                fontsize=4.0, color=GRAY_MID, style="italic")


def draw_projection(ax, mode):
    ny, nx = 80, 110
    x = np.linspace(-1.2, 1.2, nx)
    y = np.linspace(-1, 1, ny)
    X, Y = np.meshgrid(x, y)
    base = np.exp(-(X ** 2 / 0.55 + Y ** 2 / 0.85))
    if mode == "flat":
        edge = np.clip(base - 0.55, 0, 1) * 2.0
        interior = base * 0.20
        img = np.clip(edge + interior, 0, 1)
        annotation, ann_color = "interior under-represented", GRAY_DARK
    else:
        rng = np.random.default_rng(3)
        tex = rng.standard_normal((ny, nx)) * 0.14
        tex_smooth = gaussian_blur(tex, sigma=1.4)
        img = np.clip(base * 0.82 + tex_smooth * base, 0, 1)
        annotation, ann_color = "interior attenuation preserved", GREEN
    ax.imshow(img, cmap="gray_r", extent=[0, 1, 0, 1], aspect="auto")
    ax.text(0.04, 0.06, annotation, ha="left", va="bottom",
            fontsize=4.6, color=ann_color, fontweight="bold",
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.85, pad=1.2))


def make_error_cmap():
    return LinearSegmentedColormap.from_list(
        "err",
        [(0.0, "#08306B"), (0.18, "#2171B5"), (0.40, "#41AB5D"),
         (0.70, "#FDAE61"), (1.0, "#D7191C")],
    )


def draw_error_map(ax, mode, cmap, vmax=1.0):
    ny, nx = 80, 110
    x = np.linspace(-1.2, 1.2, nx)
    y = np.linspace(-1, 1, ny)
    X, Y = np.meshgrid(x, y)
    base = np.exp(-(X ** 2 / 0.55 + Y ** 2 / 0.85))
    rng = np.random.default_rng(42 if mode == "flat" else 23)
    noise = rng.standard_normal((ny, nx))
    noise_s = gaussian_blur(noise, sigma=2.0)
    noise_norm = noise_s / (np.abs(noise_s).max() + 1e-6)
    if mode == "flat":
        interior_mask = (base > 0.50).astype(float)
        err = interior_mask * (0.55 + 0.35 * noise_norm)
        err += (1 - interior_mask) * (0.15 + 0.10 * np.abs(noise_norm))
    else:
        err = 0.12 + 0.06 * (0.5 + 0.5 * noise_norm)
    err = np.clip(err, 0, vmax)
    ax.imshow(err, cmap=cmap, extent=[0, 1, 0, 1], aspect="auto", vmin=0, vmax=vmax)


def draw_shared_colorbar(fig, x, y, w, h, cmap, vmax=1.0):
    ax = fig.add_axes([x, y, w, h])
    gradient = np.linspace(0, 1, 256).reshape(-1, 1)
    ax.imshow(gradient, cmap=cmap, aspect="auto", origin="lower")
    ax.set_xticks([])
    ax.set_yticks([0, 255])
    ax.set_yticklabels(["0", "max"], fontsize=4.2)
    ax.tick_params(axis="y", length=2, pad=1, colors=GRAY_DARK,
                   right=True, left=False, labelright=True, labelleft=False)
    for spine in ax.spines.values():
        spine.set_edgecolor(GRAY_LIGHT)
        spine.set_linewidth(0.5)
    ax.text(0.5, 1.06, "err", transform=ax.transAxes,
            ha="center", va="bottom", fontsize=4.2, color=GRAY_DARK)


def draw_middle_separator(fig, y):
    ax = fig.add_axes([0.045, y, 0.92, 0.04])
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    ax.plot([0.0, 1.0], [0.5, 0.5], color=GRAY_LIGHT, lw=0.6,
            linestyle=(0, (3, 2)))
    ax.text(0.5, 0.5, "  Misallocation  →  Reallocation  ",
            ha="center", va="center", fontsize=6.5, fontweight="bold",
            color=GRAY_DARK,
            bbox=dict(facecolor="white", edgecolor=GRAY_LIGHT, lw=0.4, pad=2.0))


def main():
    out_dir = Path(__file__).resolve().parents[1] / "fig"
    out_path = out_dir / "intro_fig_compare.png"

    fig = plt.figure(figsize=(FIG_W_IN, FIG_H_IN), dpi=DPI)
    fig.patch.set_facecolor("white")

    label_w = 0.03
    left = 0.045
    right_margin = 0.045
    col_gap = 0.015
    # Reserve space at right for colorbar.
    cb_w = 0.018
    cb_gap = 0.006
    panel_w = (1 - left - right_margin - col_gap * 3 - cb_w - cb_gap) / 4
    col_xs = [left + i * (panel_w + col_gap) for i in range(4)]
    cb_x = col_xs[3] + panel_w + cb_gap

    title_h = 0.07
    title_y = 1 - title_h - 0.01

    top_y = 0.55
    bot_y = 0.08
    row_h = 0.30

    # Row labels.
    add_rotated_label(fig, 0.005, top_y, label_w, row_h,
                      "Conventional 3DGS — gradient-driven densification",
                      GRAY_DARK)
    add_rotated_label(fig, 0.005, bot_y, label_w, row_h,
                      "XRA-GS (Ours) — attenuation-aligned evolution",
                      BLUE)

    # Column titles centered above each panel.
    titles = ["X-ray Path Integral", "Where Gaussians Live",
              "Synthesized Projection", "Residual to GT"]
    for cx, t in zip(col_xs, titles):
        add_col_title(fig, cx, title_y, panel_w, title_h, t)

    cmap = make_error_cmap()
    vmax = 1.0

    # ---- Top row ----
    ax = panel_ax(fig, col_xs[0], top_y, panel_w, row_h)
    draw_phantom(ax, fdk_support=False)
    draw_rays(ax)
    ax = panel_ax(fig, col_xs[1], top_y, panel_w, row_h)
    draw_capacity_top(ax)
    ax = panel_ax(fig, col_xs[2], top_y, panel_w, row_h)
    draw_projection(ax, mode="flat")
    ax = panel_ax(fig, col_xs[3], top_y, panel_w, row_h)
    draw_error_map(ax, mode="flat", cmap=cmap, vmax=vmax)
    draw_shared_colorbar(fig, cb_x, top_y + row_h * 0.05, cb_w, row_h * 0.90,
                         cmap, vmax=vmax)

    # Middle separator between rows.
    sep_y = (top_y + bot_y + row_h - 0.04) / 2
    draw_middle_separator(fig, sep_y)

    # ---- Bottom row ----
    ax = panel_ax(fig, col_xs[0], bot_y, panel_w, row_h)
    draw_phantom(ax, fdk_support=True)
    draw_rays(ax)

    # Bottom Col-2 split: scatter (upper 65%) + badges (lower 35%).
    scatter_h = row_h * 0.62
    badge_h = row_h * 0.36
    scatter_y = bot_y + badge_h + 0.005
    ax = panel_ax(fig, col_xs[1], scatter_y, panel_w, scatter_h)
    draw_capacity_bottom(ax)
    draw_badges(fig, col_xs[1], bot_y, panel_w, badge_h)

    ax = panel_ax(fig, col_xs[2], bot_y, panel_w, row_h)
    draw_projection(ax, mode="rich")
    ax = panel_ax(fig, col_xs[3], bot_y, panel_w, row_h)
    draw_error_map(ax, mode="rich", cmap=cmap, vmax=vmax)
    draw_shared_colorbar(fig, cb_x, bot_y + row_h * 0.05, cb_w, row_h * 0.90,
                         cmap, vmax=vmax)

    fig.savefig(out_path, dpi=DPI, facecolor="white")
    plt.close(fig)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
