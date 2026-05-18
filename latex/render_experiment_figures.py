import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


ROOT = "/Users/openingcloud/Documents/GardenOfOpeningClouds/1-Information/PG2026论文投稿/PG2026-thesis"
FIG_DIR = os.path.join(ROOT, "figures")

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["PingFang SC", "Hiragino Sans GB", "Arial Unicode MS", "Noto Sans CJK SC", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False


PALETTE = {
    "baseline": "#8FA0A5",
    "sps": "#E6862A",
    "adm": "#2FAE60",
    "sps_adm": "#357FB8",
    "gap": "#EF4A3A",
    "sps_gap": "#8F4AAE",
    "adm_gap": "#2CB6A0",
    "full": "#C63C2E",
    "accent": "#C63C2E",
    "gold": "#F5C84C",
    "grid": "#D6DCE5",
    "line_blue": "#2F84C2",
    "line_red": "#C63C2E",
}


def style_axis(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_linewidth(1.0)
    ax.spines["bottom"].set_linewidth(1.0)
    ax.tick_params(axis="both", labelsize=11, width=1.0)
    ax.grid(axis="y", linestyle=(0, (3, 3)), color=PALETTE["grid"], linewidth=0.8, alpha=0.7)


def save_dual(fig, stem):
    fig.savefig(os.path.join(FIG_DIR, f"{stem}.pdf"), bbox_inches="tight")
    fig.savefig(os.path.join(FIG_DIR, f"{stem}.png"), dpi=260, bbox_inches="tight")


def render_ablation():
    labels = ["R2-Gaussian", "+SPS", "+ADM", "SPS+ADM", "+GAP", "SPS+GAP", "ADM+GAP", "SPAGS"]
    values = {
        "2 视角": [21.27, 21.44, 21.31, 21.51, 21.28, 21.42, 21.43, 21.44],
        "3 视角": [27.80, 28.01, 27.91, 28.09, 28.22, 28.22, 28.22, 28.22],
        "4 视角": [29.10, 29.16, 29.18, 29.17, 29.20, 29.09, 29.36, 29.20],
    }
    deltas = {
        "2 视角": [None, "+0.17", "+0.04", "+0.24", "+0.01", "+0.15", "+0.16", "+0.17"],
        "3 视角": [None, "+0.21", "+0.11", "+0.29", "+0.42", "+0.42", "+0.42", "+0.42"],
        "4 视角": [None, "+0.06", "+0.08", "+0.07", "+0.10", "+0.01", "+0.26", "+0.10"],
    }
    colors = [
        PALETTE["baseline"],
        PALETTE["sps"],
        PALETTE["adm"],
        PALETTE["sps_adm"],
        PALETTE["gap"],
        PALETTE["sps_gap"],
        PALETTE["adm_gap"],
        PALETTE["full"],
    ]

    fig, axes = plt.subplots(1, 3, figsize=(14.2, 4.2), constrained_layout=True)
    for ax, (title, vals) in zip(axes, values.items()):
        x = np.arange(len(labels))
        bars = ax.bar(x, vals, width=0.56, color=colors, edgecolor="white", linewidth=0.6)

        top = max(vals)
        for idx, (bar, v) in enumerate(zip(bars, vals)):
            if abs(v - top) < 1e-6:
                bar.set_edgecolor(PALETTE["gold"])
                bar.set_linewidth(2.2)

        for idx, (bar, v) in enumerate(zip(bars, vals)):
            ax.text(bar.get_x() + bar.get_width() / 2, v + 0.012 * (max(vals) - min(vals) + 1), f"{v:.2f}",
                    ha="center", va="bottom", fontsize=9, color="#1F2937", fontweight="semibold")
            if deltas[title][idx]:
                ax.text(bar.get_x() + bar.get_width() / 2, v + 0.065 * (max(vals) - min(vals) + 1), deltas[title][idx],
                        ha="center", va="bottom", fontsize=8, color="#7A8798")

        ax.set_title(title, fontsize=12, fontweight="semibold", pad=8)
        ax.set_xticks(x)
        ax.set_xticklabels(labels, rotation=32, ha="right", fontsize=9)
        ax.set_ylabel("平均 PSNR (dB)", fontsize=12)
        span = max(vals) - min(vals)
        ax.set_ylim(min(vals) - 0.18 * span, max(vals) + 0.28 * span)
        style_axis(ax)

    fig.savefig(os.path.join(FIG_DIR, "fig_ablation_final.png"), dpi=240, bbox_inches="tight")
    plt.close(fig)


def render_ablation_3view():
    labels = ["Baseline", "+SPS", "+ADM", "+SPS+ADM", "+GAP", "+SPS+GAP", "Full"]
    values = [27.80, 28.01, 27.91, 28.09, 28.22, 28.22, 28.22]
    colors = [
        PALETTE["baseline"],
        PALETTE["sps"],
        PALETTE["adm"],
        PALETTE["sps_adm"],
        PALETTE["gap"],
        PALETTE["sps_gap"],
        PALETTE["full"],
    ]

    fig, ax = plt.subplots(figsize=(7.2, 3.2), constrained_layout=True)
    x = np.arange(len(labels))
    bars = ax.bar(x, values, width=0.62, color=colors, edgecolor="white", linewidth=0.8)

    best = max(values)
    for bar, value in zip(bars, values):
        if abs(value - best) < 1e-6:
            bar.set_edgecolor(PALETTE["gold"])
            bar.set_linewidth(2.4)
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value + 0.013,
            f"{value:.2f}",
            ha="center",
            va="bottom",
            fontsize=10,
            color="#1F2937",
            fontweight="semibold",
        )

    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=25, ha="right", fontsize=10)
    ax.set_ylabel("Avg. PSNR (dB)", fontsize=12)
    ax.set_ylim(27.76, 28.28)
    style_axis(ax)
    save_dual(fig, "fig_ablation_3view")
    plt.close(fig)


def render_gap_sweep():
    threshold_x = [0.010, 0.015, 0.020]
    threshold_y = [28.11, 28.21, 28.15]
    ratio_x = [2, 3, 5]
    ratio_y = [28.22, 28.21, 28.18]
    baseline = 28.09

    fig, axes = plt.subplots(1, 2, figsize=(11.0, 3.9), constrained_layout=True)

    ax = axes[0]
    ax.plot(threshold_x, threshold_y, color=PALETTE["line_blue"], linewidth=2.0, marker="o", markersize=8)
    ax.axhline(baseline, linestyle=(0, (4, 3)), color="#A8B0BA", linewidth=1.1, label="SPS+ADM 基线")
    for x, y in zip(threshold_x, threshold_y):
        ax.text(x, y + 0.013, f"{y:.2f}", ha="center", va="bottom", fontsize=10, color="#1F2937", fontweight="semibold")
    ax.set_title("阈值扫描", fontsize=12, fontweight="semibold", pad=8)
    ax.set_xlabel("邻近阈值 τ", fontsize=12)
    ax.set_ylabel("平均 PSNR (dB)", fontsize=12)
    ax.set_xticks(threshold_x)
    ax.set_ylim(28.00, 28.30)
    style_axis(ax)
    ax.legend(loc="upper right", fontsize=9, frameon=True, edgecolor="#D6DCE5")

    ax = axes[1]
    ax.plot(ratio_x, ratio_y, color=PALETTE["line_red"], linewidth=2.0, marker="s", markersize=8)
    ax.axhline(baseline, linestyle=(0, (4, 3)), color="#A8B0BA", linewidth=1.1, label="SPS+ADM 基线")
    for x, y in zip(ratio_x, ratio_y):
        ax.text(x, y + 0.013, f"{y:.2f}", ha="center", va="bottom", fontsize=10, color="#1F2937", fontweight="semibold")
    ax.set_title("最大剪枝比扫描", fontsize=12, fontweight="semibold", pad=8)
    ax.set_xlabel("剪枝上限 β (%)", fontsize=12)
    ax.set_ylabel("平均 PSNR (dB)", fontsize=12)
    ax.set_xticks(ratio_x)
    ax.set_xticklabels(["2", "3", "5"])
    ax.set_ylim(28.00, 28.30)
    style_axis(ax)
    ax.legend(loc="upper right", fontsize=9, frameon=True, edgecolor="#D6DCE5")

    fig.suptitle("GAP 超参数敏感性分析", fontsize=13, fontweight="semibold", y=1.03)
    fig.savefig(os.path.join(FIG_DIR, "fig_gap_sweep.png"), dpi=240, bbox_inches="tight")
    plt.close(fig)


def render_hparam_compact():
    sweeps = [
        {
            "title": "SPS $\\alpha$",
            "x": [0.2, 0.3, 0.4],
            "y": [28.01, 27.95, 27.90],
            "color": PALETTE["line_blue"],
            "marker": "o",
            "xlabel": "$\\alpha$",
            "xticks": [0.2, 0.3, 0.4],
        },
        {
            "title": "GAP $\\tau$",
            "x": [0.010, 0.015, 0.020],
            "y": [28.11, 28.21, 28.15],
            "color": PALETTE["line_red"],
            "marker": "s",
            "xlabel": "$\\tau$",
            "xticks": [0.010, 0.015, 0.020],
        },
        {
            "title": "GAP $\\beta_{\\mathrm{prune}}$",
            "x": [2, 3, 5],
            "y": [28.22, 28.21, 28.18],
            "color": PALETTE["adm_gap"],
            "marker": "D",
            "xlabel": "$\\beta_{\\mathrm{prune}}$ (%)",
            "xticks": [2, 3, 5],
        },
        {
            "title": "ADM warm-up",
            "x": [12, 15, 18],
            "y": [28.16, 28.22, 28.14],
            "color": PALETTE["sps"],
            "marker": "^",
            "xlabel": "Iteration (K)",
            "xticks": [12, 15, 18],
        },
    ]

    fig, axes = plt.subplots(2, 2, figsize=(7.2, 5.2), constrained_layout=True)
    axes = axes.flatten()
    for idx, (ax, sweep) in enumerate(zip(axes, sweeps)):
        xs = sweep["x"]
        ys = sweep["y"]
        ax.plot(xs, ys, color=sweep["color"], linewidth=2.3, marker=sweep["marker"], markersize=7.5)

        best_idx = int(np.argmax(ys))
        ax.scatter(
            [xs[best_idx]],
            [ys[best_idx]],
            s=120,
            facecolor="white",
            edgecolor=sweep["color"],
            linewidth=2.0,
            zorder=4,
        )

        ax.set_title(sweep["title"], fontsize=12, fontweight="semibold", pad=6)
        ax.set_xlabel(sweep["xlabel"], fontsize=11)
        if idx % 2 == 0:
            ax.set_ylabel("Avg. PSNR (dB)", fontsize=11)
        ax.set_xticks(sweep["xticks"])
        ax.set_ylim(27.88, 28.24)
        style_axis(ax)

    save_dual(fig, "fig_hparam_compact")
    plt.close(fig)


if __name__ == "__main__":
    os.makedirs(FIG_DIR, exist_ok=True)
    render_ablation()
    render_ablation_3view()
    render_gap_sweep()
    render_hparam_compact()
    print("Rendered experiment figures.")
