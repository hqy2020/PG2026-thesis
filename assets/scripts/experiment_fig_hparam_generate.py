"""Generate experiment_fig_hparam.png — 2×2 hyperparameter sensitivity plots.

Reads experiment_tab_hparam_sensitivity.csv from assets/data/.
Outputs experiment_fig_hparam.png to assets/fig/.

Usage:
    python assets/scripts/experiment_fig_hparam_generate.py

Data requirements (fill NaN values in the CSV before running):
    assets/data/experiment_tab_hparam_sensitivity.csv
    Columns: param, value, psnr2d, ssim2d, is_default

Visual style:
    Primary y-axis (left):  SSIM2D ↑  — solid Crimson Red line, 1.5pt
    Secondary y-axis (right): PSNR2D ↑ — dashed Slate Blue line, 1.5pt
    Default config point: filled black circle •, annotated "default"
    Background: white; no gridlines except subtle horizontal ticks
    Font: sans-serif (matches VISUAL_STYLE.md)
"""
from __future__ import annotations

import pathlib
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA_PATH = REPO_ROOT / "assets" / "data" / "experiment_tab_hparam_sensitivity.csv"
OUT_PATH  = REPO_ROOT / "assets" / "fig" / "experiment_fig_hparam.png"

# ---------------------------------------------------------------------------
# Visual constants (VISUAL_STYLE.md)
# ---------------------------------------------------------------------------
CRIMSON   = "#D7263D"   # SSIM2D primary axis
SLATE     = "#5B7C99"   # PSNR2D secondary axis
GRAY_TICK = "#BBBBBB"

PANEL_CONFIGS = [
    ("sps_alpha",   r"SPS mixture coeff. $\alpha$",  r"$\alpha$"),
    ("gap_tau",     r"GAP threshold $\tau$",          r"$\tau$"),
    ("gap_beta",    r"GAP pruning ratio $\beta_\mathrm{prune}$", r"$\beta$"),
    ("adm_warmup",  r"ADM warm-up start (fraction)",  "warmup"),
]

# ADM warmup: convert from fraction of 30K to iteration count for display
ADM_WARMUP_TICKS = {0.00: "0", 0.10: "3K", 0.25: "7.5K\n(default)", 0.50: "15K", 0.75: "22.5K"}


def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH, comment="#")
    df["psnr2d"] = pd.to_numeric(df["psnr2d"], errors="coerce")
    df["ssim2d"] = pd.to_numeric(df["ssim2d"], errors="coerce")
    return df


def plot_panel(ax_l: plt.Axes, sub_df: pd.DataFrame, xlabel: str, title: str, param: str) -> None:
    ax_r = ax_l.twinx()

    x      = sub_df["value"].values
    ssim   = sub_df["ssim2d"].values
    psnr   = sub_df["psnr2d"].values
    dflt_mask = sub_df["is_default"].values.astype(bool)

    if not np.all(np.isnan(ssim)):
        ax_l.plot(x, ssim, color=CRIMSON, linewidth=1.5, label="SSIM2D", zorder=3)
        if dflt_mask.any():
            ax_l.scatter(x[dflt_mask], ssim[dflt_mask],
                         color="black", s=40, zorder=5, clip_on=False)
    if not np.all(np.isnan(psnr)):
        ax_r.plot(x, psnr, color=SLATE, linewidth=1.5, linestyle="--", label="PSNR2D", zorder=3)
        if dflt_mask.any():
            ax_r.scatter(x[dflt_mask], psnr[dflt_mask],
                         color="black", s=40, zorder=5, clip_on=False)

    # Annotate default
    if dflt_mask.any():
        ax_l.annotate("default", xy=(x[dflt_mask][0], ax_l.get_ylim()[0]),
                      xytext=(0, -18), textcoords="offset points",
                      fontsize=7, ha="center", color="black")

    ax_l.set_xlabel(xlabel, fontsize=8)
    ax_l.set_ylabel("SSIM2D ↑", fontsize=8, color=CRIMSON)
    ax_r.set_ylabel("PSNR2D ↑ (dB)", fontsize=8, color=SLATE)
    ax_l.tick_params(axis="y", labelcolor=CRIMSON, labelsize=7)
    ax_r.tick_params(axis="y", labelcolor=SLATE, labelsize=7)
    ax_l.tick_params(axis="x", labelsize=7)
    ax_l.set_title(title, fontsize=8, fontweight="bold", pad=4)

    # Clean spines
    for spine in ["top"]:
        ax_l.spines[spine].set_visible(False)
        ax_r.spines[spine].set_visible(False)


def main() -> int:
    if not DATA_PATH.exists():
        print(f"ERROR: data file not found: {DATA_PATH}", file=sys.stderr)
        return 1

    df = load_data()
    if df[["psnr2d", "ssim2d"]].isna().all().all():
        print("WARNING: all data values are NaN — figure will be empty placeholders.", file=sys.stderr)
        print("Fill in experiment_tab_hparam_sensitivity.csv before running.", file=sys.stderr)

    fig, axes = plt.subplots(2, 2, figsize=(7, 5.5))
    fig.subplots_adjust(hspace=0.45, wspace=0.55)

    panel_labels = ["(a)", "(b)", "(c)", "(d)"]
    for ax, (param, title, short), label in zip(axes.flat, PANEL_CONFIGS, panel_labels):
        sub = df[df["param"] == param].sort_values("value")
        if sub.empty:
            ax.text(0.5, 0.5, f"No data\n({param})", ha="center", va="center",
                    transform=ax.transAxes, fontsize=9, color="gray")
            ax.set_title(title, fontsize=8, fontweight="bold")
        else:
            plot_panel(ax, sub, short, title, param)
        ax.text(0.01, 0.97, label, transform=ax.transAxes,
                fontsize=9, fontweight="bold", va="top")

    fig.savefig(OUT_PATH, dpi=300, bbox_inches="tight", facecolor="white")
    print(f"Saved: {OUT_PATH.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
