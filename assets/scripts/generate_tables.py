#!/usr/bin/env python3
"""Generate LaTeX tables from all_experiments_unified.csv"""

import csv
import io
from collections import defaultdict

CSV_RAW = """experiment_type,method,config,organ,views,psnr,ssim,n_gaussians
main_comparison,corgs,corgs,abdomen,2,18.5048,0.8645,
main_comparison,corgs,corgs,abdomen,3,22.4487,0.9089,
main_comparison,corgs,corgs,abdomen,4,23.0292,0.9269,
main_comparison,corgs,corgs,chest,2,14.9579,0.5754,
main_comparison,corgs,corgs,chest,3,18.5481,0.7077,
main_comparison,corgs,corgs,chest,4,20.2945,0.7636,
main_comparison,corgs,corgs,foot,2,20.1715,0.6913,
main_comparison,corgs,corgs,foot,3,25.5323,0.8511,
main_comparison,corgs,corgs,foot,4,26.8267,0.8767,
main_comparison,corgs,corgs,head,2,16.2353,0.7993,
main_comparison,corgs,corgs,head,3,20.3649,0.8644,
main_comparison,corgs,corgs,head,4,23.3981,0.9088,
main_comparison,corgs,corgs,pancreas,2,16.1481,0.8088,
main_comparison,corgs,corgs,pancreas,3,23.2489,0.8974,
main_comparison,corgs,corgs,pancreas,4,23.958,0.9084,
main_comparison,dngaussian,dngaussian,abdomen,2,14.3015,0.7663,
main_comparison,dngaussian,dngaussian,abdomen,3,16.0184,0.8258,
main_comparison,dngaussian,dngaussian,abdomen,4,15.7637,0.8486,
main_comparison,dngaussian,dngaussian,chest,2,18.8383,0.6675,
main_comparison,dngaussian,dngaussian,chest,3,20.5466,0.75,
main_comparison,dngaussian,dngaussian,chest,4,20.9943,0.7791,
main_comparison,dngaussian,dngaussian,foot,2,19.3257,0.7801,
main_comparison,dngaussian,dngaussian,foot,3,23.5098,0.8569,
main_comparison,dngaussian,dngaussian,foot,4,24.7237,0.8666,
main_comparison,dngaussian,dngaussian,head,2,15.7208,0.7296,
main_comparison,dngaussian,dngaussian,head,3,18.0411,0.8097,
main_comparison,dngaussian,dngaussian,head,4,16.2416,0.7924,
main_comparison,dngaussian,dngaussian,pancreas,2,19.0617,0.8082,
main_comparison,dngaussian,dngaussian,pancreas,3,22.4283,0.8848,
main_comparison,dngaussian,dngaussian,pancreas,4,25.4747,0.8982,
main_comparison,fsgs,fsgs,abdomen,2,18.7516,0.858,
main_comparison,fsgs,fsgs,abdomen,3,23.3421,0.9068,
main_comparison,fsgs,fsgs,abdomen,4,23.6261,0.9276,
main_comparison,fsgs,fsgs,chest,2,17.8612,0.6451,
main_comparison,fsgs,fsgs,chest,3,19.9929,0.7429,
main_comparison,fsgs,fsgs,chest,4,21.0266,0.7729,
main_comparison,fsgs,fsgs,foot,2,22.1747,0.6843,
main_comparison,fsgs,fsgs,foot,3,25.3716,0.85,
main_comparison,fsgs,fsgs,foot,4,27.0769,0.876,
main_comparison,fsgs,fsgs,head,2,19.4343,0.8334,
main_comparison,fsgs,fsgs,head,3,21.5278,0.8732,
main_comparison,fsgs,fsgs,head,4,24.9099,0.9105,
main_comparison,fsgs,fsgs,pancreas,2,23.0328,0.8564,
main_comparison,fsgs,fsgs,pancreas,3,25.2745,0.9031,
main_comparison,fsgs,fsgs,pancreas,4,26.2211,0.9148,
main_comparison,r2_gaussian,r2_gaussian,abdomen,2,24.8491,0.9028,
main_comparison,r2_gaussian,r2_gaussian,abdomen,3,29.2597,0.9363,
main_comparison,r2_gaussian,r2_gaussian,abdomen,4,30.5576,0.9617,
main_comparison,r2_gaussian,r2_gaussian,chest,2,21.049,0.711,
main_comparison,r2_gaussian,r2_gaussian,chest,3,26.2163,0.8367,
main_comparison,r2_gaussian,r2_gaussian,chest,4,25.4703,0.8546,
main_comparison,r2_gaussian,r2_gaussian,foot,2,19.3859,0.6722,
main_comparison,r2_gaussian,r2_gaussian,foot,3,28.4751,0.8977,
main_comparison,r2_gaussian,r2_gaussian,foot,4,30.0362,0.913,
main_comparison,r2_gaussian,r2_gaussian,head,2,23.5401,0.8718,
main_comparison,r2_gaussian,r2_gaussian,head,3,26.5952,0.9223,
main_comparison,r2_gaussian,r2_gaussian,head,4,28.6644,0.955,
main_comparison,r2_gaussian,r2_gaussian,pancreas,2,17.8274,0.8122,
main_comparison,r2_gaussian,r2_gaussian,pancreas,3,28.6079,0.9199,
main_comparison,r2_gaussian,r2_gaussian,pancreas,4,30.9011,0.936,
main_comparison,xrags,xrags,abdomen,2,25.2557,0.9068,
main_comparison,xrags,xrags,abdomen,3,29.546,0.9374,
main_comparison,xrags,xrags,abdomen,4,30.9046,0.9627,
main_comparison,xrags,xrags,chest,2,21.216,0.7065,
main_comparison,xrags,xrags,chest,3,26.6337,0.839,
main_comparison,xrags,xrags,chest,4,26.0341,0.8586,
main_comparison,xrags,xrags,foot,2,19.9211,0.6798,
main_comparison,xrags,xrags,foot,3,28.6395,0.8993,
main_comparison,xrags,xrags,foot,4,29.9532,0.9149,
main_comparison,xrags,xrags,head,2,24.258,0.8694,
main_comparison,xrags,xrags,head,3,26.6472,0.9176,
main_comparison,xrags,xrags,head,4,29.6833,0.9518,
main_comparison,xrags,xrags,pancreas,2,19.0944,0.8241,
main_comparison,xrags,xrags,pancreas,3,29.3678,0.9247,
main_comparison,xrags,xrags,pancreas,4,30.9536,0.9361,
main_comparison,xgaussian,xgaussian,abdomen,2,18.9287,0.8595,
main_comparison,xgaussian,xgaussian,abdomen,3,23.5399,0.9077,
main_comparison,xgaussian,xgaussian,abdomen,4,23.8482,0.9257,
main_comparison,xgaussian,xgaussian,chest,2,17.7894,0.6488,
main_comparison,xgaussian,xgaussian,chest,3,20.2879,0.7427,
main_comparison,xgaussian,xgaussian,chest,4,20.9004,0.7689,
main_comparison,xgaussian,xgaussian,foot,2,22.3446,0.6882,
main_comparison,xgaussian,xgaussian,foot,3,25.4755,0.8481,
main_comparison,xgaussian,xgaussian,foot,4,26.9227,0.874,
main_comparison,xgaussian,xgaussian,head,2,19.6189,0.8347,
main_comparison,xgaussian,xgaussian,head,3,21.5161,0.8697,
main_comparison,xgaussian,xgaussian,head,4,24.4586,0.9079,
main_comparison,xgaussian,xgaussian,pancreas,2,23.2098,0.8502,
main_comparison,xgaussian,xgaussian,pancreas,3,25.1195,0.9006,
main_comparison,xgaussian,xgaussian,pancreas,4,25.5541,0.9124,
main_comparison,xfield,xfield,chest,2,19.5655,0.6843,
main_comparison,xfield,xfield,chest,3,23.9411,0.809,
main_comparison,xfield,xfield,chest,4,24.4517,0.8255,
main_comparison,xfield,xfield,head,2,22.4942,0.8413,
main_comparison,xfield,xfield,head,3,25.0575,0.8878,
main_comparison,xfield,xfield,head,4,26.7789,0.9089,
main_comparison,xfield,xfield,abdomen,2,22.2029,0.719,
main_comparison,xfield,xfield,abdomen,3,24.8687,0.8632,
main_comparison,xfield,xfield,abdomen,4,27.1854,0.9103,
main_comparison,xfield,xfield,pancreas,2,18.1187,0.6871,
main_comparison,xfield,xfield,pancreas,3,24.936,0.8474,
main_comparison,xfield,xfield,pancreas,4,26.3598,0.9004,
main_comparison,xfield,xfield,foot,2,20.4541,0.6522,
main_comparison,xfield,xfield,foot,3,26.0315,0.8405,
main_comparison,xfield,xfield,foot,4,27.2468,0.8556,
component_ablation,r2_gaussian,Baseline (R²-Gaussian),chest,3,26.3812,0.8393,57010
component_ablation,r2_gaussian,Baseline (R²-Gaussian),head,3,26.7799,0.9242,49941
component_ablation,r2_gaussian,Baseline (R²-Gaussian),abdomen,3,29.1994,0.936,50487
component_ablation,r2_gaussian,Baseline (R²-Gaussian),foot,3,28.5968,0.8979,50019
component_ablation,r2_gaussian,Baseline (R²-Gaussian),pancreas,3,28.6867,0.9204,53696
component_ablation,xrags+SPS,B + SPS,chest,3,26.934,0.8422,55568
component_ablation,xrags+SPS,B + SPS,head,3,26.582,0.916,49606
component_ablation,xrags+SPS,B + SPS,abdomen,3,29.4769,0.9352,50464
component_ablation,xrags+SPS,B + SPS,foot,3,28.5697,0.9008,49938
component_ablation,xrags+SPS,B + SPS,pancreas,3,29.1172,0.9218,52843
component_ablation,xrags+ADM,B + ADM,chest,3,26.4846,0.8396,
component_ablation,xrags+ADM,B + ADM,head,3,26.9209,0.9245,
component_ablation,xrags+ADM,B + ADM,abdomen,3,29.3289,0.937,
component_ablation,xrags+ADM,B + ADM,foot,3,28.7218,0.8985,
component_ablation,xrags+ADM,B + ADM,pancreas,3,28.8388,0.9211,
component_ablation,xrags+GAP,B + GAP,chest,3,26.1096,0.837,113829
component_ablation,xrags+GAP,B + GAP,head,3,26.7288,0.9243,105504
component_ablation,xrags+GAP,B + GAP,abdomen,3,29.2309,0.9376,105269
component_ablation,xrags+GAP,B + GAP,foot,3,28.5987,0.8961,103944
component_ablation,xrags+GAP,B + GAP,pancreas,3,28.8341,0.9235,106413
component_ablation,xrags,Full XRA-GS,chest,3,26.9478,0.8409,
component_ablation,xrags,Full XRA-GS,head,3,26.7267,0.9181,
component_ablation,xrags,Full XRA-GS,abdomen,3,29.4578,0.9368,
component_ablation,xrags,Full XRA-GS,foot,3,28.517,0.9003,
component_ablation,xrags,Full XRA-GS,pancreas,3,29.3247,0.9245,
sps_alpha_sweep,xrags+SPS,SPS α=0.0,chest,3,26.8378,0.843,
sps_alpha_sweep,xrags+SPS,SPS α=0.1,chest,3,26.9256,0.8444,
sps_alpha_sweep,xrags+SPS,SPS α=0.2,chest,3,26.934,0.8422,
sps_alpha_sweep,xrags+SPS,SPS α=0.5,chest,3,26.6699,0.847,
sps_alpha_sweep,xrags+SPS,SPS α=1.0,chest,3,27.0674,0.848,
sps_alpha_sweep,xrags+SPS,SPS α=0.0,head,3,26.5703,0.9145,
sps_alpha_sweep,xrags+SPS,SPS α=0.1,head,3,26.7325,0.9148,
sps_alpha_sweep,xrags+SPS,SPS α=0.2,head,3,26.582,0.916,
sps_alpha_sweep,xrags+SPS,SPS α=0.5,head,3,26.6554,0.9162,
sps_alpha_sweep,xrags+SPS,SPS α=1.0,head,3,26.6648,0.9167,
sps_alpha_sweep,xrags+SPS,SPS α=0.0,abdomen,3,29.3444,0.9352,
sps_alpha_sweep,xrags+SPS,SPS α=0.1,abdomen,3,29.4457,0.9341,
sps_alpha_sweep,xrags+SPS,SPS α=0.2,abdomen,3,29.4769,0.9352,
sps_alpha_sweep,xrags+SPS,SPS α=0.5,abdomen,3,29.4095,0.9354,
sps_alpha_sweep,xrags+SPS,SPS α=1.0,abdomen,3,29.1595,0.9357,
sps_alpha_sweep,xrags+SPS,SPS α=0.0,foot,3,28.6261,0.9026,
sps_alpha_sweep,xrags+SPS,SPS α=0.1,foot,3,28.5996,0.9031,
sps_alpha_sweep,xrags+SPS,SPS α=0.2,foot,3,28.5697,0.9008,
sps_alpha_sweep,xrags+SPS,SPS α=0.5,foot,3,28.6858,0.9015,
sps_alpha_sweep,xrags+SPS,SPS α=1.0,foot,3,28.3805,0.8999,
sps_alpha_sweep,xrags+SPS,SPS α=0.0,pancreas,3,29.0755,0.9227,
sps_alpha_sweep,xrags+SPS,SPS α=0.1,pancreas,3,28.9517,0.9208,
sps_alpha_sweep,xrags+SPS,SPS α=0.2,pancreas,3,29.1172,0.9218,
sps_alpha_sweep,xrags+SPS,SPS α=0.5,pancreas,3,29.1174,0.9214,
sps_alpha_sweep,xrags+SPS,SPS α=1.0,pancreas,3,29.0313,0.9215,
gap_tau_sweep,xrags+GAP,GAP τ=0.005,chest,3,26.2193,0.8342,
gap_tau_sweep,xrags+GAP,GAP τ=0.010,chest,3,27.1131,0.8426,
gap_tau_sweep,xrags+GAP,GAP τ=0.015,chest,3,27.1985,0.8437,
gap_tau_sweep,xrags+GAP,GAP τ=0.020,chest,3,27.2365,0.8453,
gap_tau_sweep,xrags+GAP,GAP τ=0.030,chest,3,26.8585,0.8432,
gap_tau_sweep,xrags+GAP,GAP τ=0.005,head,3,26.7425,0.9248,
gap_tau_sweep,xrags+GAP,GAP τ=0.010,head,3,26.6944,0.9166,
gap_tau_sweep,xrags+GAP,GAP τ=0.015,head,3,26.629,0.9149,
gap_tau_sweep,xrags+GAP,GAP τ=0.020,head,3,26.4372,0.9146,
gap_tau_sweep,xrags+GAP,GAP τ=0.030,head,3,26.741,0.9237,
gap_tau_sweep,xrags+GAP,GAP τ=0.005,abdomen,3,29.0724,0.9355,
gap_tau_sweep,xrags+GAP,GAP τ=0.010,abdomen,3,29.6883,0.9362,
gap_tau_sweep,xrags+GAP,GAP τ=0.015,abdomen,3,29.725,0.9362,
gap_tau_sweep,xrags+GAP,GAP τ=0.020,abdomen,3,29.6459,0.936,
gap_tau_sweep,xrags+GAP,GAP τ=0.030,abdomen,3,29.5295,0.9369,
gap_tau_sweep,xrags+GAP,GAP τ=0.005,foot,3,28.4955,0.8972,
gap_tau_sweep,xrags+GAP,GAP τ=0.010,foot,3,28.5332,0.9023,
gap_tau_sweep,xrags+GAP,GAP τ=0.015,foot,3,28.6665,0.9026,
gap_tau_sweep,xrags+GAP,GAP τ=0.020,foot,3,28.356,0.9014,
gap_tau_sweep,xrags+GAP,GAP τ=0.030,foot,3,28.5878,0.8953,
gap_tau_sweep,xrags+GAP,GAP τ=0.005,pancreas,3,28.7668,0.9235,
gap_tau_sweep,xrags+GAP,GAP τ=0.010,pancreas,3,29.3917,0.9227,
gap_tau_sweep,xrags+GAP,GAP τ=0.015,pancreas,3,29.435,0.9234,
gap_tau_sweep,xrags+GAP,GAP τ=0.020,pancreas,3,29.4023,0.9231,
gap_tau_sweep,xrags+GAP,GAP τ=0.030,pancreas,3,29.0392,0.9261,
adm_iter_sweep,xrags,ADM warmup=0,chest,3,27.165,0.8422,
adm_iter_sweep,xrags,ADM warmup=5000,chest,3,26.8177,0.8394,
adm_iter_sweep,xrags,ADM warmup=10000,chest,3,26.9313,0.84,
adm_iter_sweep,xrags,ADM warmup=15000,chest,3,26.9464,0.84,
adm_iter_sweep,xrags,ADM warmup=20000,chest,3,26.906,0.8403,
adm_iter_sweep,xrags,ADM warmup=25000,chest,3,26.4585,0.839,
adm_iter_sweep,xrags,ADM warmup=0,head,3,26.852,0.9248,
adm_iter_sweep,xrags,ADM warmup=5000,head,3,26.7846,0.9244,
adm_iter_sweep,xrags,ADM warmup=10000,head,3,26.9138,0.924,
adm_iter_sweep,xrags,ADM warmup=15000,head,3,26.8039,0.9244,
adm_iter_sweep,xrags,ADM warmup=20000,head,3,26.832,0.9245,
adm_iter_sweep,xrags,ADM warmup=25000,head,3,26.862,0.9239,
adm_iter_sweep,xrags,ADM warmup=0,abdomen,3,29.3961,0.9378,
adm_iter_sweep,xrags,ADM warmup=5000,abdomen,3,29.2456,0.9373,
adm_iter_sweep,xrags,ADM warmup=10000,abdomen,3,29.1792,0.9368,
adm_iter_sweep,xrags,ADM warmup=15000,abdomen,3,29.2934,0.9368,
adm_iter_sweep,xrags,ADM warmup=20000,abdomen,3,29.3358,0.9369,
adm_iter_sweep,xrags,ADM warmup=25000,abdomen,3,29.263,0.9368,
adm_iter_sweep,xrags,ADM warmup=0,foot,3,29.0228,0.8993,
adm_iter_sweep,xrags,ADM warmup=5000,foot,3,28.6958,0.8993,
adm_iter_sweep,xrags,ADM warmup=10000,foot,3,28.604,0.899,
adm_iter_sweep,xrags,ADM warmup=15000,foot,3,28.6798,0.8994,
adm_iter_sweep,xrags,ADM warmup=20000,foot,3,28.7293,0.8992,
adm_iter_sweep,xrags,ADM warmup=25000,foot,3,28.6779,0.8992,
adm_iter_sweep,xrags,ADM warmup=0,pancreas,3,29.057,0.9221,
adm_iter_sweep,xrags,ADM warmup=5000,pancreas,3,28.8919,0.921,
adm_iter_sweep,xrags,ADM warmup=10000,pancreas,3,28.9076,0.9213,
adm_iter_sweep,xrags,ADM warmup=15000,pancreas,3,28.9458,0.9214,
adm_iter_sweep,xrags,ADM warmup=20000,pancreas,3,29.0118,0.9217,
adm_iter_sweep,xrags,ADM warmup=25000,pancreas,3,28.9533,0.9214,"""

ORGANS = ["chest", "head", "abdomen", "foot", "pancreas"]
VIEWS = [2, 3, 4]
METHODS_ORDER = ["corgs", "dngaussian", "fsgs", "xgaussian", "r2_gaussian", "xfield", "xrags"]

METHOD_LABELS = {
    "corgs": r"CoR-GS~\cite{zhang2024cor} {\tiny[ECCV'24]}",
    "dngaussian": r"DNGaussian~\cite{li2024dn} {\tiny[CVPR'24]}",
    "fsgs": r"FSGS~\cite{zhu2024fsgs} {\tiny[ECCV'24]}",
    "xgaussian": r"X-Gaussian~\cite{cai2024xgaussian} {\tiny[ECCV'24]}",
    "r2_gaussian": r"\rtwo~\cite{hu2024r2} {\tiny[NeurIPS'24]}",
    "xfield": r"X-Field~\cite{xfield2025} {\tiny[NeurIPS'25]}",
    "xrags": r"\textbf{\XRAGS}\ (Ours)",
}

COLORS = {1: "FF9396", 2: "FFC991", 3: "FFF6A9"}


def parse_csv():
    reader = csv.DictReader(io.StringIO(CSV_RAW.strip()))
    rows = list(reader)
    return rows


def get_main_data(rows):
    data = {}
    for r in rows:
        if r["experiment_type"] != "main_comparison":
            continue
        m, o, v = r["method"], r["organ"], int(r["views"])
        data[(m, o, v)] = {"psnr": float(r["psnr"]), "ssim": float(r["ssim"])}
    return data


def compute_averages(data, metric):
    avgs = {}
    for m in METHODS_ORDER:
        for v in VIEWS:
            vals = [data[(m, o, v)][metric] for o in ORGANS]
            avgs[(m, v)] = sum(vals) / len(vals)
    return avgs


def rank_column(values_by_method, reverse=True):
    sorted_methods = sorted(values_by_method.items(), key=lambda x: x[1], reverse=reverse)
    ranks = {}
    for i, (m, _) in enumerate(sorted_methods):
        ranks[m] = i + 1
    return ranks


def fmt_psnr(val):
    return f"{val:.2f}"


def fmt_ssim(val):
    return f"{val:.4f}"


def cellcolor(rank):
    if rank in COLORS:
        return rf"\cellcolor[HTML]{{{COLORS[rank]}}}"
    return ""


def generate_comparison_table(data, metric, caption, label):
    fmt = fmt_psnr if metric == "psnr" else fmt_ssim
    avgs = compute_averages(data, metric)

    columns = []
    for o in ORGANS:
        for v in VIEWS:
            columns.append((o, v))
    for v in VIEWS:
        columns.append(("avg", v))

    col_ranks = {}
    for col in columns:
        vals = {}
        for m in METHODS_ORDER:
            if col[0] == "avg":
                vals[m] = avgs[(m, col[1])]
            else:
                vals[m] = data[(m, col[0], col[1])][metric]
        col_ranks[col] = rank_column(vals)

    arrow = r"$\uparrow$" if metric == "psnr" else r"$\uparrow$"
    metric_upper = metric.upper()

    lines = []
    lines.append(r"\begin{table*}[t]")
    lines.append(r"\centering")
    lines.append(rf"\caption{{{metric_upper} comparison on the novel view synthesis task. We colorize the \colorbox[HTML]{{FF9396}}{{best}}, \colorbox[HTML]{{FFC991}}{{second-best}}, and \colorbox[HTML]{{FFF6A9}}{{third-best}} numbers. All methods are evaluated under the unified five-organ protocol.}}")
    lines.append(rf"\label{{{label}}}")
    lines.append(r"\scriptsize")
    lines.append(r"\renewcommand{\arraystretch}{1.05}")
    lines.append(r"\setlength{\tabcolsep}{2.8pt}")
    lines.append(r"\resizebox{\textwidth}{!}{%")
    lines.append(r"\begin{tabular}{@{}l*{18}{c}@{}}")
    lines.append(r"\toprule")
    lines.append(r"\multirow{2}{*}{\textbf{Method}}")
    for org in ORGANS:
        lines.append(rf"  & \multicolumn{{3}}{{c}}{{\textbf{{{org.capitalize()}}}}}")
    lines.append(r"  & \multicolumn{3}{c}{\textbf{Average}} \\")
    lines.append(r"\cmidrule(lr){2-4}\cmidrule(lr){5-7}\cmidrule(lr){8-10}\cmidrule(lr){11-13}\cmidrule(lr){14-16}\cmidrule(lr){17-19}")
    view_headers = "  & " + " & ".join([rf"\textbf{{{v}-view}}" for v in VIEWS] * 6) + r" \\"
    lines.append(view_headers)
    lines.append(r"\midrule")

    natural_methods = ["corgs", "dngaussian", "fsgs"]
    xray_methods = ["xgaussian", "r2_gaussian", "xfield"]

    lines.append(r"\multicolumn{19}{c}{\emph{Natural-scene sparse-view 3DGS methods}} \\")
    lines.append(r"\midrule")

    for m in natural_methods:
        lines.append(_format_method_row(m, data, avgs, col_ranks, columns, fmt, metric))

    lines.append(r"\midrule")
    lines.append(r"\multicolumn{19}{c}{\emph{X-ray/CT reconstruction methods}} \\")
    lines.append(r"\midrule")

    for m in xray_methods:
        lines.append(_format_method_row(m, data, avgs, col_ranks, columns, fmt, metric))

    lines.append(r"\midrule")
    lines.append(_format_method_row("xrags", data, avgs, col_ranks, columns, fmt, metric))

    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}%")
    lines.append(r"}")
    lines.append(r"\renewcommand{\arraystretch}{1.0}")
    lines.append(r"\end{table*}")

    return "\n".join(lines) + "\n"


def _format_method_row(m, data, avgs, col_ranks, columns, fmt, metric):
    label = METHOD_LABELS[m]
    cells = []
    for col in columns:
        if col[0] == "avg":
            val = avgs[(m, col[1])]
        else:
            val = data[(m, col[0], col[1])][metric]
        rank = col_ranks[col].get(m, 99)
        cc = cellcolor(rank)
        formatted = fmt(val)
        if cc:
            cells.append(f"{cc}{formatted}")
        else:
            cells.append(formatted)

    first_half = cells[:9]
    second_half = cells[9:]
    row = f"{label}\n  & " + " & ".join(first_half) + "\n  & " + " & ".join(second_half) + r" \\"
    return row


def get_ablation_data(rows):
    sections = {
        "component": defaultdict(dict),
        "sps_alpha": defaultdict(dict),
        "gap_tau": defaultdict(dict),
        "adm_iter": defaultdict(dict),
    }

    for r in rows:
        exp = r["experiment_type"]
        config = r["config"]
        organ = r["organ"]

        if exp == "component_ablation":
            sections["component"][(config, organ)] = {
                "psnr": float(r["psnr"]), "ssim": float(r["ssim"])
            }
        elif exp == "sps_alpha_sweep":
            sections["sps_alpha"][(config, organ)] = {
                "psnr": float(r["psnr"]), "ssim": float(r["ssim"])
            }
        elif exp == "gap_tau_sweep":
            sections["gap_tau"][(config, organ)] = {
                "psnr": float(r["psnr"]), "ssim": float(r["ssim"])
            }
        elif exp == "adm_iter_sweep":
            sections["adm_iter"][(config, organ)] = {
                "psnr": float(r["psnr"]), "ssim": float(r["ssim"])
            }

    return sections


def avg_5organ(section_data, config, metric):
    vals = [section_data[(config, o)][metric] for o in ORGANS]
    return sum(vals) / len(vals)


def generate_ablation_table(ablation_data):
    lines = []
    lines.append(r"\begin{table}[t]")
    lines.append(r"\centering")
    lines.append(r"\caption{Ablation results with our choices in \textbf{bold}. We colorize the \colorbox[HTML]{FF9396}{best}, \colorbox[HTML]{FFC991}{second-best}, and \colorbox[HTML]{FFF6A9}{third-best} numbers.}")
    lines.append(r"\label{tab:ablation_component}")
    lines.append(r"\footnotesize")
    lines.append(r"\setlength{\tabcolsep}{4pt}")
    lines.append(r"\begin{tabular}{@{}lcc@{}}")
    lines.append(r"\toprule")
    lines.append(r"Configuration & PSNR$\uparrow$ & SSIM$\uparrow$ \\")
    lines.append(r"\midrule")

    # Section 1: Component analysis
    lines.append(r"\multicolumn{3}{c}{\emph{Component analysis (5-organ avg, 3-view)}} \\")
    lines.append(r"\midrule")

    comp_configs = [
        ("Baseline (R²-Gaussian)", r"Baseline (\rtwo)", False),
        ("B + SPS", r"B\,+\,\sps", False),
        ("B + GAP", r"B\,+\,\gap", False),
        ("B + ADM", r"B\,+\,\adm", False),
        ("Full XRA-GS", r"\textbf{Full \XRAGS}", False),
    ]

    comp_vals = {}
    for csv_name, _, _ in comp_configs:
        comp_vals[csv_name] = {
            "psnr": avg_5organ(ablation_data["component"], csv_name, "psnr"),
            "ssim": avg_5organ(ablation_data["component"], csv_name, "ssim"),
        }

    psnr_ranks = rank_column({k: v["psnr"] for k, v in comp_vals.items()})
    ssim_ranks = rank_column({k: v["ssim"] for k, v in comp_vals.items()})

    for csv_name, latex_name, _ in comp_configs:
        p = comp_vals[csv_name]["psnr"]
        s = comp_vals[csv_name]["ssim"]
        pc = cellcolor(psnr_ranks[csv_name])
        sc = cellcolor(ssim_ranks[csv_name])
        lines.append(f"{latex_name} & {pc}{p:.2f} & {sc}{s:.4f} \\\\")

    # Section 2: SPS alpha sweep
    lines.append(r"\midrule")
    lines.append(r"\multicolumn{3}{c}{\emph{\sps\ mixture coefficient $\alpha$ (5-organ avg, 3-view)}} \\")
    lines.append(r"\midrule")

    alpha_configs = [
        ("SPS α=0.0", r"$\alpha$\,=\,0.0"),
        ("SPS α=0.1", r"$\alpha$\,=\,0.1"),
        ("SPS α=0.2", r"$\boldsymbol{\alpha}$\textbf{\,=\,0.2}"),
        ("SPS α=0.5", r"$\alpha$\,=\,0.5"),
        ("SPS α=1.0", r"$\alpha$\,=\,1.0"),
    ]

    alpha_vals = {}
    for csv_name, _ in alpha_configs:
        alpha_vals[csv_name] = {
            "psnr": avg_5organ(ablation_data["sps_alpha"], csv_name, "psnr"),
            "ssim": avg_5organ(ablation_data["sps_alpha"], csv_name, "ssim"),
        }

    psnr_ranks = rank_column({k: v["psnr"] for k, v in alpha_vals.items()})
    ssim_ranks = rank_column({k: v["ssim"] for k, v in alpha_vals.items()})

    for csv_name, latex_name in alpha_configs:
        p = alpha_vals[csv_name]["psnr"]
        s = alpha_vals[csv_name]["ssim"]
        pc = cellcolor(psnr_ranks[csv_name])
        sc = cellcolor(ssim_ranks[csv_name])
        lines.append(f"{latex_name} & {pc}{p:.2f} & {sc}{s:.4f} \\\\")

    # Section 3: GAP tau sweep
    lines.append(r"\midrule")
    lines.append(r"\multicolumn{3}{c}{\emph{\gap\ proximity threshold $\tau$ (5-organ avg, 3-view)}} \\")
    lines.append(r"\midrule")

    tau_configs = [
        ("GAP τ=0.005", r"$\tau$\,=\,0.005"),
        ("GAP τ=0.010", r"$\tau$\,=\,0.010"),
        ("GAP τ=0.015", r"$\boldsymbol{\tau}$\textbf{\,=\,0.015}"),
        ("GAP τ=0.020", r"$\tau$\,=\,0.020"),
        ("GAP τ=0.030", r"$\tau$\,=\,0.030"),
    ]

    tau_vals = {}
    for csv_name, _ in tau_configs:
        tau_vals[csv_name] = {
            "psnr": avg_5organ(ablation_data["gap_tau"], csv_name, "psnr"),
            "ssim": avg_5organ(ablation_data["gap_tau"], csv_name, "ssim"),
        }

    psnr_ranks = rank_column({k: v["psnr"] for k, v in tau_vals.items()})
    ssim_ranks = rank_column({k: v["ssim"] for k, v in tau_vals.items()})

    for csv_name, latex_name in tau_configs:
        p = tau_vals[csv_name]["psnr"]
        s = tau_vals[csv_name]["ssim"]
        pc = cellcolor(psnr_ranks[csv_name])
        sc = cellcolor(ssim_ranks[csv_name])
        lines.append(f"{latex_name} & {pc}{p:.2f} & {sc}{s:.4f} \\\\")

    # Section 4: ADM iter sweep
    lines.append(r"\midrule")
    lines.append(r"\multicolumn{3}{c}{\emph{\adm\ activation iteration (5-organ avg, 3-view)}} \\")
    lines.append(r"\midrule")

    iter_configs = [
        ("ADM warmup=0", r"Iter\,=\,0"),
        ("ADM warmup=5000", r"Iter\,=\,5K"),
        ("ADM warmup=10000", r"Iter\,=\,10K"),
        ("ADM warmup=15000", r"\textbf{Iter\,=\,15K}"),
        ("ADM warmup=20000", r"Iter\,=\,20K"),
        ("ADM warmup=25000", r"Iter\,=\,25K"),
    ]

    iter_vals = {}
    for csv_name, _ in iter_configs:
        iter_vals[csv_name] = {
            "psnr": avg_5organ(ablation_data["adm_iter"], csv_name, "psnr"),
            "ssim": avg_5organ(ablation_data["adm_iter"], csv_name, "ssim"),
        }

    psnr_ranks = rank_column({k: v["psnr"] for k, v in iter_vals.items()})
    ssim_ranks = rank_column({k: v["ssim"] for k, v in iter_vals.items()})

    for csv_name, latex_name in iter_configs:
        p = iter_vals[csv_name]["psnr"]
        s = iter_vals[csv_name]["ssim"]
        pc = cellcolor(psnr_ranks[csv_name])
        sc = cellcolor(ssim_ranks[csv_name])
        lines.append(f"{latex_name} & {pc}{p:.2f} & {sc}{s:.4f} \\\\")

    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")

    return "\n".join(lines) + "\n"


def main():
    rows = parse_csv()
    main_data = get_main_data(rows)
    ablation_data = get_ablation_data(rows)

    psnr_table = generate_comparison_table(main_data, "psnr", "", "tab:psnr_nvs")
    ssim_table = generate_comparison_table(main_data, "ssim", "", "tab:ssim_nvs")
    ablation_table = generate_ablation_table(ablation_data)

    base = "/Users/openingcloud/Documents/PG2026-thesis/assets/tables"
    with open(f"{base}/tab_experiment_quantitative_nvs_psnr.tex", "w") as f:
        f.write(psnr_table)
    print("Wrote PSNR table")

    with open(f"{base}/tab_experiment_quantitative_nvs_ssim.tex", "w") as f:
        f.write(ssim_table)
    print("Wrote SSIM table")

    with open(f"{base}/tab_experiment_ablation_component.tex", "w") as f:
        f.write(ablation_table)
    print("Wrote ablation table")

    # Print summary of key changes
    print("\n=== Key data summary ===")
    print("\nXRAGS averages:")
    for v in VIEWS:
        psnr_avg = compute_averages(main_data, "psnr")[("xrags", v)]
        ssim_avg = compute_averages(main_data, "ssim")[("xrags", v)]
        print(f"  {v}-view: PSNR={psnr_avg:.2f}, SSIM={ssim_avg:.4f}")

    print("\nAblation component (5-organ avg, 3-view):")
    for config in ["Baseline (R²-Gaussian)", "B + SPS", "B + GAP", "B + ADM", "Full XRA-GS"]:
        p = avg_5organ(ablation_data["component"], config, "psnr")
        s = avg_5organ(ablation_data["component"], config, "ssim")
        print(f"  {config}: PSNR={p:.2f}, SSIM={s:.4f}")

    print("\nADM iter (5-organ avg, 3-view):")
    for config in ["ADM warmup=0", "ADM warmup=5000", "ADM warmup=10000",
                    "ADM warmup=15000", "ADM warmup=20000", "ADM warmup=25000"]:
        p = avg_5organ(ablation_data["adm_iter"], config, "psnr")
        s = avg_5organ(ablation_data["adm_iter"], config, "ssim")
        print(f"  {config}: PSNR={p:.2f}, SSIM={s:.4f}")


if __name__ == "__main__":
    main()
