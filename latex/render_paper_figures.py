import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle


ROOT = "/Users/openingcloud/Documents/GardenOfOpeningClouds/1-Information/PG2026论文投稿/PG2026-thesis"
FIG_DIR = os.path.join(ROOT, "figures")


def setup_fig(w, h):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
    ax.axis("off")
    return fig, ax


def rounded_box(ax, x, y, w, h, text, fc="#ffffff", ec="#64748b", lw=1.6, fs=12, weight="normal"):
    box = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.12,rounding_size=0.08",
        facecolor=fc,
        edgecolor=ec,
        linewidth=lw,
    )
    ax.add_patch(box)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, fontweight=weight, color="#0f172a")


def stage_band(ax, x, y, w, h, label, fc, ec):
    rounded_box(ax, x, y, w, h, label, fc=fc, ec=ec, lw=2.0, fs=14, weight="bold")


def arrow(ax, x1, y1, x2, y2, color="#334155", lw=1.8):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="->", color=color, lw=lw))


def gaussian_cluster(ax, cx, cy, scale=0.7, color="#7c3aed"):
    offsets = [
        (-0.45, 0.18), (-0.18, 0.34), (0.12, 0.30), (0.40, 0.16),
        (-0.28, -0.02), (0.05, 0.00), (0.35, -0.10), (-0.05, -0.28),
        (0.26, -0.30), (-0.36, -0.28),
    ]
    for ox, oy in offsets:
        ax.add_patch(Circle((cx + ox * scale, cy + oy * scale), 0.09 * scale, facecolor="white", edgecolor=color, linewidth=2.0))


def heatmap_panel(ax, x, y, w, h):
    rect = Rectangle((x, y), w, h, facecolor="#dcfce7", edgecolor="#16a34a", linewidth=1.5)
    ax.add_patch(rect)
    for cx, cy, r, c in [
        (x + 0.42 * w, y + 0.55 * h, 0.16 * w, "#fde047"),
        (x + 0.58 * w, y + 0.48 * h, 0.20 * w, "#fb923c"),
        (x + 0.50 * w, y + 0.46 * h, 0.12 * w, "#ef4444"),
    ]:
        ax.add_patch(Circle((cx, cy), r, color=c, alpha=0.65))


def draw_ct_projections(ax, x, y, w, h):
    for i in range(2):
        yy = y + i * (h * 0.52)
        rect = Rectangle((x, yy), w, h * 0.45, facecolor="#0f172a", edgecolor="#0f172a")
        ax.add_patch(rect)
        ax.add_patch(Circle((x + w * 0.48, yy + h * 0.23), h * 0.15, facecolor="#e2e8f0", edgecolor="#cbd5e1", linewidth=1.2))
        ax.add_patch(Circle((x + w * 0.48, yy + h * 0.23), h * 0.11, facecolor="#94a3b8", edgecolor="#94a3b8", linewidth=0))
        ax.add_patch(Rectangle((x + w * 0.38, yy + h * 0.17), w * 0.20, h * 0.12, facecolor="#1e293b", edgecolor="none"))


def draw_intro_compare():
    fig, ax = setup_fig(15.5, 6.2)
    ax.text(7.75, 5.9, "Abstract Pipeline Comparison Across Sparse-View 3DGS Methods", ha="center", va="center", fontsize=18, fontweight="bold")

    methods = [
        ("FSGS", "#e0f2fe", "#0284c7"),
        ("CoR-GS", "#e0f2fe", "#0284c7"),
        ("DNGaussian", "#e0f2fe", "#0284c7"),
        ("X-Gaussian", "#e0f2fe", "#0284c7"),
        ("R2-Gaussian", "#e0f2fe", "#0284c7"),
        ("SPAGS (Ours)", "#fee2e2", "#dc2626"),
    ]
    row_labels = ["Initialization", "Geometry Control", "Density Update", "Output Bias"]
    y_positions = [4.8, 3.55, 2.3, 1.05]

    for i, label in enumerate(row_labels):
        ax.text(0.6, y_positions[i] + 0.23, label, ha="left", va="center", fontsize=13, fontweight="bold", color="#334155")

    for idx, (name, fc, ec) in enumerate(methods):
        x = 2.2 + idx * 2.15
        rounded_box(ax, x, 5.15, 1.8, 0.5, name, fc=fc, ec=ec, lw=2.2, fs=12, weight="bold")
        if name == "SPAGS (Ours)":
            rounded_box(ax, x, 4.55, 1.8, 0.5, "Spatial-aware", fc="#fff1f2", ec="#dc2626", lw=1.8, fs=11, weight="bold")

        texts = {
            0: ["COLMAP/SfM", "Unpool sparse gaps", "Pseudo-view depth", "Coverage-first"],
            1: ["Twin field init", "Co-pruning", "Co-regularize render", "Disagreement-first"],
            2: ["Gaussian init", "Depth regularize", "Global-local norm", "Geometry-first"],
            3: ["Scanner-aware uniform", "Radiative rasterization", "X-ray attenuation", "Physics-first"],
            4: ["FDK-based init", "Bias-rectified kernel", "Voxel regularization", "Reconstruction-first"],
            5: ["FDK prior seeding", "Proximity pruning", "Adaptive modulation", "Redundancy-aware"],
        }[idx]
        colors = ["#eff6ff", "#f0fdf4", "#fffbeb", "#f8fafc"]
        edges = ["#60a5fa", "#4ade80", "#f59e0b", "#94a3b8"]
        for ridx, txt in enumerate(texts):
            rounded_box(ax, x, y_positions[ridx], 1.8, 0.48, txt, fc=colors[ridx], ec=edges[ridx], lw=1.4, fs=11)

    ax.text(7.75, 0.35, "Main distinction: SPAGS injects spatial awareness into initialization, pruning, and density modulation simultaneously.", ha="center", va="center", fontsize=12, color="#475569")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, "fig_intro_compare.png"), dpi=220, bbox_inches="tight")
    plt.close(fig)


def draw_pipeline():
    fig, ax = setup_fig(15.5, 6.4)
    ax.text(7.75, 6.05, "SPAGS Full Pipeline for Sparse-View CT Novel View Synthesis", ha="center", va="center", fontsize=18, fontweight="bold")

    stage_band(ax, 0.7, 5.2, 4.1, 0.55, "Stage 1  SPS  Spatial Prior Seeding", "#eff6ff", "#2563eb")
    stage_band(ax, 5.2, 5.2, 4.1, 0.55, "Stage 2  GAP  Geometry-aware Pruning", "#f0fdf4", "#16a34a")
    stage_band(ax, 9.7, 5.2, 4.2, 0.55, "Stage 3  ADM  Adaptive Density Modulation", "#fffbeb", "#d97706")

    draw_ct_projections(ax, 0.8, 3.4, 1.5, 1.45)
    rounded_box(ax, 2.7, 3.8, 1.5, 0.8, "FDK\nCoarse Volume", fc="#dbeafe", ec="#3b82f6", fs=12, weight="bold")
    rounded_box(ax, 0.8, 2.2, 1.5, 0.75, "Sparse CT\nProjections", fc="#f8fafc", ec="#64748b", fs=12, weight="bold")
    rounded_box(ax, 2.7, 2.2, 1.5, 0.75, "Mixed Sampling\n80% weighted\n20% uniform", fc="#dbeafe", ec="#2563eb", fs=11)
    rounded_box(ax, 0.8, 1.05, 3.4, 0.7, "50K anatomy-aware initial Gaussians", fc="#ede9fe", ec="#7c3aed", fs=12, weight="bold")
    gaussian_cluster(ax, 3.9, 1.38, scale=0.8)
    arrow(ax, 2.35, 4.05, 2.65, 4.05)
    arrow(ax, 2.35, 2.55, 2.65, 2.55)
    arrow(ax, 3.45, 2.15, 2.4, 1.52)

    rounded_box(ax, 5.5, 3.9, 1.4, 0.75, "World-space\nKNN score", fc="#dcfce7", ec="#16a34a", fs=12, weight="bold")
    rounded_box(ax, 7.2, 3.9, 1.4, 0.75, "Gradient-aware\nfilter", fc="#dcfce7", ec="#16a34a", fs=12, weight="bold")
    rounded_box(ax, 5.5, 2.45, 3.1, 0.85, "Prune redundant Gaussians near over-clustered boundaries", fc="#fee2e2", ec="#dc2626", fs=11, weight="bold")
    gaussian_cluster(ax, 6.15, 1.35, scale=0.95)
    gaussian_cluster(ax, 8.0, 1.35, scale=0.72)
    ax.text(6.15, 0.72, "Before", ha="center", fontsize=11, color="#64748b")
    ax.text(8.0, 0.72, "After", ha="center", fontsize=11, color="#64748b")
    arrow(ax, 4.5, 1.4, 5.3, 1.4)
    arrow(ax, 6.95, 4.25, 7.15, 4.25)

    rounded_box(ax, 10.0, 3.8, 1.3, 0.8, "K-Planes\nxy / xz / yz", fc="#fef3c7", ec="#d97706", fs=12, weight="bold")
    rounded_box(ax, 11.6, 3.8, 1.2, 0.8, "Dual-head\nMLP", fc="#fef3c7", ec="#d97706", fs=12, weight="bold")
    rounded_box(ax, 13.1, 3.8, 1.1, 0.8, "Offset +\nConfidence", fc="#fef3c7", ec="#d97706", fs=12, weight="bold")
    rounded_box(ax, 10.0, 2.35, 4.2, 0.8, "Zero-mean density modulation conditioned on spatial context", fc="#fff7ed", ec="#ea580c", fs=11, weight="bold")
    rounded_box(ax, 10.7, 0.95, 2.8, 0.78, "High-fidelity novel X-ray views", fc="#e0f2fe", ec="#0ea5e9", fs=13, weight="bold")
    arrow(ax, 9.0, 1.4, 9.8, 1.4)
    arrow(ax, 11.25, 4.18, 11.55, 4.18)
    arrow(ax, 12.8, 4.18, 13.05, 4.18)
    arrow(ax, 12.1, 3.7, 12.1, 3.18)
    arrow(ax, 12.1, 2.3, 12.1, 1.78)

    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, "fig_pipeline.png"), dpi=220, bbox_inches="tight")
    plt.close(fig)


def draw_sps():
    fig, ax = setup_fig(14.5, 4.4)
    ax.text(7.25, 4.08, "SPS: Spatial Prior Seeding", ha="center", va="center", fontsize=18, fontweight="bold")
    draw_ct_projections(ax, 0.6, 1.3, 2.0, 2.1)
    rounded_box(ax, 0.6, 0.45, 2.0, 0.55, "Sparse CT projections", fc="#f8fafc", ec="#475569", fs=12, weight="bold")
    rounded_box(ax, 3.1, 1.35, 2.1, 1.15, "FDK coarse volume\nwith usable anatomical prior", fc="#dbeafe", ec="#2563eb", fs=13, weight="bold")
    rounded_box(ax, 5.8, 1.35, 2.15, 1.15, "Density map\nand sampling probability", fc="#dbeafe", ec="#2563eb", fs=13, weight="bold")
    rounded_box(ax, 8.55, 1.35, 2.25, 1.15, "Mixed seeding\n80% weighted\n20% uniform", fc="#dbeafe", ec="#2563eb", fs=12, weight="bold")
    rounded_box(ax, 11.35, 1.35, 2.3, 1.15, "50K initial Gaussians\nfocused on anatomy", fc="#ede9fe", ec="#7c3aed", fs=13, weight="bold")
    gaussian_cluster(ax, 12.48, 2.0, scale=1.05)
    arrow(ax, 2.7, 1.95, 3.0, 1.95)
    arrow(ax, 5.25, 1.95, 5.7, 1.95)
    arrow(ax, 8.0, 1.95, 8.45, 1.95)
    arrow(ax, 10.9, 1.95, 11.25, 1.95)
    ax.text(7.25, 0.42, "Key idea: use FDK as a coarse structural prior so initialization allocates Gaussians where anatomy actually exists.", ha="center", va="center", fontsize=12, color="#475569")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, "fig_sps.png"), dpi=220, bbox_inches="tight")
    plt.close(fig)


def draw_gap():
    fig, ax = setup_fig(14.5, 4.6)
    ax.text(7.25, 4.22, "GAP: Geometry-aware Pruning", ha="center", va="center", fontsize=18, fontweight="bold")
    rounded_box(ax, 0.5, 3.28, 3.0, 0.58, "Over-clustered boundary region", fc="#f8fafc", ec="#475569", fs=13, weight="bold")
    gaussian_cluster(ax, 2.0, 2.05, scale=1.55)
    rounded_box(ax, 4.1, 3.28, 2.7, 0.58, "KNN proximity score", fc="#dcfce7", ec="#16a34a", fs=13, weight="bold")
    heatmap_panel(ax, 4.35, 1.2, 2.2, 1.65)
    rounded_box(ax, 7.2, 3.28, 2.8, 0.58, "Gradient-aware filtering", fc="#dcfce7", ec="#16a34a", fs=13, weight="bold")
    rounded_box(ax, 7.35, 1.95, 2.5, 0.8, "Keep active Gaussians\nRemove inactive redundant ones", fc="#f0fdf4", ec="#22c55e", fs=11, weight="bold")
    rounded_box(ax, 10.45, 3.28, 3.1, 0.58, "Refined sparse-but-sufficient layout", fc="#fee2e2", ec="#dc2626", fs=13, weight="bold")
    gaussian_cluster(ax, 11.7, 2.05, scale=1.0)
    ax.add_patch(Circle((12.8, 2.35), 0.17, facecolor="white", edgecolor="#ef4444", linewidth=2.5))
    ax.plot([12.68, 12.92], [2.23, 2.47], color="#ef4444", linewidth=2.2)
    ax.plot([12.92, 12.68], [2.23, 2.47], color="#ef4444", linewidth=2.2)
    arrow(ax, 3.45, 2.15, 4.0, 2.15)
    arrow(ax, 6.65, 2.15, 7.1, 2.15)
    arrow(ax, 10.0, 2.15, 10.35, 2.15)
    ax.text(7.25, 0.42, "Key idea: sparse-view CT suffers more from structural redundancy than from missing coverage.", ha="center", va="center", fontsize=12, color="#475569")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, "fig_gap.png"), dpi=220, bbox_inches="tight")
    plt.close(fig)


def draw_adm():
    fig, ax = setup_fig(14.8, 4.6)
    ax.text(7.4, 4.2, "ADM: Adaptive Density Modulation", ha="center", va="center", fontsize=18, fontweight="bold")
    rounded_box(ax, 0.7, 2.05, 1.7, 0.9, "Gaussian\nposition", fc="#f8fafc", ec="#475569", fs=13, weight="bold")
    rounded_box(ax, 3.0, 2.0, 3.1, 1.05, "K-Planes encoder\nxy / xz / yz", fc="#fef3c7", ec="#d97706", fs=14, weight="bold")
    rounded_box(ax, 6.7, 2.0, 2.0, 1.05, "Dual-head\nMLP", fc="#fef3c7", ec="#d97706", fs=14, weight="bold")
    rounded_box(ax, 9.3, 2.05, 1.9, 0.9, "Offset\n$\Delta\\rho$", fc="#fff7ed", ec="#ea580c", fs=13, weight="bold")
    rounded_box(ax, 9.3, 0.95, 1.9, 0.9, "Confidence\n$c$", fc="#fff7ed", ec="#ea580c", fs=13, weight="bold")
    rounded_box(ax, 11.7, 1.5, 2.3, 1.1, "Zero-mean\nmodulation", fc="#fffbeb", ec="#ca8a04", fs=14, weight="bold")
    rounded_box(ax, 11.9, 0.35, 1.9, 0.7, "Final density", fc="#e0f2fe", ec="#0284c7", fs=13, weight="bold")
    arrow(ax, 2.45, 2.5, 2.95, 2.5)
    arrow(ax, 6.15, 2.5, 6.65, 2.5)
    arrow(ax, 8.75, 2.5, 9.25, 2.5)
    arrow(ax, 8.75, 2.05, 9.25, 1.4)
    arrow(ax, 11.25, 2.45, 11.65, 2.15)
    arrow(ax, 11.25, 1.4, 11.65, 1.85)
    arrow(ax, 12.85, 1.45, 12.85, 1.05)
    ax.text(7.4, 0.18, "Key idea: learn anatomy-dependent density corrections from spatial context rather than applying identical updates everywhere.", ha="center", va="center", fontsize=12, color="#475569")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, "fig_adm.png"), dpi=220, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    os.makedirs(FIG_DIR, exist_ok=True)
    draw_intro_compare()
    draw_pipeline()
    draw_sps()
    draw_gap()
    draw_adm()
    print("Rendered clean paper figures.")
