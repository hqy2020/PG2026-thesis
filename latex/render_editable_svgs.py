from pathlib import Path
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures"
FONT = "PingFang SC, Microsoft YaHei, Noto Sans CJK SC, sans-serif"


def svg_doc(width: int, height: int, body: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrow" markerWidth="14" markerHeight="14" refX="12" refY="7" orient="auto" markerUnits="userSpaceOnUse">
      <path d="M0,0 L14,7 L0,14 z" fill="#111111"/>
    </marker>
    <linearGradient id="grayVolume" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f4f4f4"/>
      <stop offset="60%" stop-color="#d8d8d8"/>
      <stop offset="100%" stop-color="#bebebe"/>
    </linearGradient>
    <radialGradient id="spotBlue" cx="50%" cy="50%" r="60%">
      <stop offset="0%" stop-color="#9bb7ea" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#9bb7ea" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="spotPurple" cx="50%" cy="50%" r="60%">
      <stop offset="0%" stop-color="#9d8fe3" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#9d8fe3" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="spotOrange" cx="50%" cy="50%" r="60%">
      <stop offset="0%" stop-color="#efb07e" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#efb07e" stop-opacity="0"/>
    </radialGradient>
    <style>
      .label {{ font-family: {FONT}; fill: #111111; }}
      .muted {{ fill: #5b6472; }}
      .small {{ font-size: 20px; }}
      .mid {{ font-size: 24px; }}
      .title {{ font-size: 28px; font-weight: 600; }}
      .section {{ font-size: 34px; font-weight: 600; }}
      .heavy {{ font-weight: 700; }}
      .thin {{ stroke-width: 2; }}
      .dash {{ stroke-dasharray: 8 8; }}
    </style>
  </defs>
  <rect width="100%" height="100%" fill="#ffffff"/>
{body}
</svg>
"""


def rect(x, y, w, h, rx=22, fill="#ffffff", stroke="#b8bec8", sw=2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def line(x1, y1, x2, y2, stroke="#111111", sw=2.5, dashed=False, arrow=False):
    dash = ' stroke-dasharray="8 8"' if dashed else ""
    marker = ' marker-end="url(#arrow)"' if arrow else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round"{dash}{marker}/>'


def text(x, y, value, size=24, anchor="middle", fill="#111111", weight=500, cls="label"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" fill="{fill}" class="{cls}">{escape(value)}</text>'


def circle(cx, cy, r, fill="#5b8fda", stroke="none", sw=0, opacity=1.0):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}"/>'


def ellipse(cx, cy, rx, ry, fill="none", stroke="#d35d58", sw=2, opacity=1.0, dashed=False):
    dash = ' stroke-dasharray="7 6"' if dashed else ""
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}"{dash}/>'


def polygon(points, fill="#e8edf5", stroke="#b8bec8", sw=2, opacity=1.0):
    pts = " ".join(f"{x},{y}" for x, y in points)
    return f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}"/>'


def wire_cube(x, y, w, h, dx=26, dy=-18, stroke="#989ea8", fill="none"):
    back = [(x + dx, y + dy), (x + w + dx, y + dy), (x + w + dx, y + h + dy), (x + dx, y + h + dy)]
    front = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
    pieces = [
        polygon(front, fill=fill, stroke=stroke, sw=2),
        polygon(back, fill="none", stroke=stroke, sw=2),
    ]
    for p1, p2 in zip(front, back):
        pieces.append(line(p1[0], p1[1], p2[0], p2[1], stroke=stroke, sw=2))
    return "".join(pieces)


def soft_blob(cx, cy, rx, ry, gradient_id):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="url(#{gradient_id})"/>'


def scatter(x, y, w, h, points, fill="#5b8fda", r=6, varying=False):
    pieces = []
    for idx, (px, py) in enumerate(points):
        rr = r + (idx % 3) * 1.7 if varying else r
        pieces.append(circle(x + px * w, y + py * h, rr, fill=fill, opacity=0.82))
    return "".join(pieces)


def dashed_box(x, y, w, h, color):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="none" stroke="{color}" stroke-width="2" stroke-dasharray="8 7"/>'


POINTS_SPARSE = [(0.16, 0.30), (0.42, 0.27), (0.70, 0.32), (0.28, 0.60), (0.55, 0.56), (0.82, 0.66)]
POINTS_MID = [
    (0.12, 0.26), (0.29, 0.22), (0.50, 0.26), (0.73, 0.20),
    (0.18, 0.48), (0.37, 0.43), (0.62, 0.45), (0.86, 0.42),
    (0.26, 0.70), (0.49, 0.66), (0.72, 0.69),
]
POINTS_DENSE = [
    (0.12, 0.24), (0.24, 0.19), (0.36, 0.29), (0.51, 0.20), (0.66, 0.25), (0.80, 0.18),
    (0.16, 0.42), (0.30, 0.48), (0.44, 0.43), (0.60, 0.50), (0.75, 0.45), (0.88, 0.40),
    (0.22, 0.64), (0.38, 0.66), (0.54, 0.72), (0.70, 0.67), (0.84, 0.61),
]


def title_pill(x, y, w, h, label, stroke="#9ca7b5", fill="#ffffff", color="#1f2937"):
    return "".join([
        rect(x, y, w, h, rx=14, fill=fill, stroke=stroke, sw=2),
        text(x + w / 2, y + h / 2 + 10, label, size=26, fill=color, weight=600),
    ])


def thumbnail_stack(x, y, w, h, n=4):
    pieces = []
    for i in range(n):
        ox = x + i * 16
        oy = y + i * 8
        pieces.append(rect(ox, oy, w, h, rx=4, fill="#0f0f10", stroke="#2a2a2d", sw=1.5))
        pieces.append(soft_blob(ox + w * 0.55, oy + h * 0.50, w * 0.22, h * 0.33, "spotBlue"))
        pieces.append(circle(ox + w * 0.56, oy + h * 0.50, min(w, h) * 0.22, fill="none", stroke="#f2f2f4", sw=2, opacity=0.7))
    return "".join(pieces)


def ct_volume_box(x, y, w, h, accent="spotBlue"):
    return "".join([
        wire_cube(x, y, w, h, dx=22, dy=-18),
        soft_blob(x + w * 0.60, y + h * 0.44, w * 0.26, h * 0.30, accent),
        circle(x + w * 0.58, y + h * 0.44, min(w, h) * 0.18, fill="none", stroke="#d7d7d7", sw=2, opacity=0.75),
    ])


def mini_icon_points(box_x, box_y, box_w, box_h, fill="#7c8797"):
    return scatter(box_x + 18, box_y + 18, box_w - 36, box_h - 36, POINTS_SPARSE, fill=fill, r=4)


def mini_icon_planes(box_x, box_y, box_w, box_h):
    p1 = [(box_x + 18, box_y + box_h - 24), (box_x + 60, box_y + 18), (box_x + box_w - 18, box_y + 32), (box_x + box_w - 58, box_y + box_h - 10)]
    p2 = [(box_x + 36, box_y + box_h - 8), (box_x + 78, box_y + 8), (box_x + box_w - 4, box_y + 22), (box_x + box_w - 42, box_y + box_h + 2)]
    return polygon(p1, fill="#dfeafb", stroke="#8fb3df", sw=2, opacity=0.72) + polygon(p2, fill="#dcefe8", stroke="#84bfa7", sw=2, opacity=0.72)


def mini_icon_depth(box_x, box_y, box_w, box_h):
    shades = ["#d7d9dc", "#c2c7cd", "#adb3bb", "#989fa8", "#7d848e"]
    pieces = []
    step_w = (box_w - 40) / len(shades)
    for i, shade in enumerate(shades):
        px = box_x + 18 + i * step_w
        points = [(px, box_y + box_h - 18), (px, box_y + 22 + i * 8), (px + step_w + 2, box_y + 22 + i * 8), (px + step_w + 2, box_y + box_h - 18)]
        pieces.append(polygon(points, fill=shade, stroke=shade, sw=1))
    return "".join(pieces)


def mini_icon_curve(box_x, box_y, box_w, box_h):
    return (
        line(box_x + 22, box_y + box_h - 20, box_x + 22, box_y + 20, stroke="#b9c0c8", sw=1.5)
        + line(box_x + 22, box_y + box_h - 20, box_x + box_w - 22, box_y + box_h - 20, stroke="#b9c0c8", sw=1.5)
        + '<path d="M {0} {1} C {2} {3}, {4} {5}, {6} {7}" fill="none" stroke="#5b8fda" stroke-width="3"/>'.format(
            box_x + 30, box_y + box_h - 28,
            box_x + box_w * 0.38, box_y + 22,
            box_x + box_w * 0.56, box_y + box_h - 10,
            box_x + box_w - 28, box_y + 34
        )
    )


def mini_icon_bar(box_x, box_y, box_w, box_h):
    xs = [0.18, 0.34, 0.52, 0.70]
    hs = [0.44, 0.62, 0.36, 0.56]
    pieces = []
    for frac_x, frac_h in zip(xs, hs):
        px = box_x + frac_x * box_w
        ph = frac_h * (box_h - 34)
        pieces.append(rect(px, box_y + box_h - 18 - ph, 16, ph, rx=3, fill="#eceff3", stroke="#9aa4b2", sw=1.5))
    return "".join(pieces)


def mini_icon_network(box_x, box_y, box_w, box_h):
    nodes_left = [(box_x + 34, box_y + 32), (box_x + 34, box_y + box_h - 32)]
    nodes_mid = [(box_x + box_w / 2, box_y + 24), (box_x + box_w / 2, box_y + box_h / 2), (box_x + box_w / 2, box_y + box_h - 24)]
    nodes_right = [(box_x + box_w - 34, box_y + 40), (box_x + box_w - 34, box_y + box_h - 40)]
    pieces = []
    for x1, y1 in nodes_left:
        for x2, y2 in nodes_mid:
            pieces.append(line(x1, y1, x2, y2, stroke="#b0b6bf", sw=1.6))
    for x1, y1 in nodes_mid:
        for x2, y2 in nodes_right:
            pieces.append(line(x1, y1, x2, y2, stroke="#b0b6bf", sw=1.6))
    for cx, cy in nodes_left + nodes_mid + nodes_right:
        pieces.append(circle(cx, cy, 6, fill="#ffffff", stroke="#46505d", sw=2))
    return "".join(pieces)


def icon_ct_disc(cx, cy, r):
    return "".join([
        circle(cx, cy, r, fill="#52565c", opacity=0.92),
        circle(cx, cy, r * 0.78, fill="#d7dade", opacity=0.95),
        circle(cx, cy, r * 0.54, fill="#80858d", opacity=0.85),
        circle(cx, cy, r * 0.22, fill="#d9dcdf", opacity=0.95),
    ])


def panel_with_label(x, y, w, h, label, stroke, content):
    return "".join([
        rect(x, y, w, h, rx=24, fill="#ffffff", stroke=stroke, sw=2.2),
        text(x + w / 2, y + 54, label, size=28, weight=600),
        content,
    ])


def intro_svg():
    w, h = 1800, 680
    parts = [
        title_pill(260, 52, 320, 62, "主流 sparse-view 3DGS 路线"),
        title_pill(920, 52, 250, 62, "CT / X-ray 路线"),
        title_pill(1428, 52, 290, 62, "SPAGS 路线（本文方法）", stroke="#df655f", color="#d2332d"),
        line(760, 118, 760, 610, stroke="#c5c9cf", sw=2, dashed=True),
        line(1286, 118, 1286, 610, stroke="#c5c9cf", sw=2, dashed=True),
        text(94, 228, "补点扩张", size=28, anchor="middle"),
        text(94, 374, "双场协同", size=28, anchor="middle"),
        text(94, 520, "深度约束", size=28, anchor="middle"),
        text(874, 260, "辐射建模", size=28, anchor="middle"),
        text(874, 476, "偏差修正", size=28, anchor="middle"),
    ]

    left_rows = [
        (170, 162, [("点集", mini_icon_points), ("扩张", mini_icon_points), ("体空间", lambda x, y, ww, hh: wire_cube(x + 16, y + 18, ww - 54, hh - 46, 18, -14)), ("稠密覆盖", mini_icon_points)]),
        (170, 308, [("双平面", mini_icon_planes), ("双场", mini_icon_points), ("协同图", mini_icon_network), ("融合场", lambda x, y, ww, hh: mini_icon_planes(x, y, ww, hh) + soft_blob(x + ww * 0.60, y + hh * 0.60, 34, 18, "spotBlue"))]),
        (170, 454, [("深度图", mini_icon_depth), ("几何约束", lambda x, y, ww, hh: mini_icon_network(x, y, ww, hh)), ("高斯更新", mini_icon_points), ("新视角", lambda x, y, ww, hh: mini_icon_planes(x, y, ww, hh) + soft_blob(x + ww * 0.50, y + hh * 0.58, 42, 18, "spotBlue"))]),
    ]

    for row_y, cards in [(162, left_rows[0][2]), (308, left_rows[1][2]), (454, left_rows[2][2])]:
        x = 170
        for idx, (label, icon_fn) in enumerate(cards):
            parts.append(rect(x, row_y, 112, 92, rx=16))
            parts.append(text(x + 56, row_y - 10, label, size=18, fill="#4e5663"))
            parts.append(icon_fn(x, row_y, 112, 92))
            if idx < len(cards) - 1:
                parts.append(line(x + 118, row_y + 46, x + 170, row_y + 46, arrow=True))
            x += 166

    mid_cards_top = [("辐射核", mini_icon_bar), ("投影曲线", mini_icon_curve), ("体重建", lambda x, y, ww, hh: wire_cube(x + 22, y + 18, ww - 46, hh - 42, 16, -12))]
    mid_cards_bottom = [("CT 截面", lambda x, y, ww, hh: icon_ct_disc(x + ww / 2, y + hh / 2, 26)), ("偏差曲线", mini_icon_curve), ("体素校正", lambda x, y, ww, hh: wire_cube(x + 22, y + 18, ww - 46, hh - 42, 16, -12))]
    for row_y, cards in [(176, mid_cards_top), (392, mid_cards_bottom)]:
        x = 904
        for idx, (label, icon_fn) in enumerate(cards):
            parts.append(rect(x, row_y, 118, 104, rx=16))
            parts.append(text(x + 59, row_y - 10, label, size=18, fill="#4e5663"))
            parts.append(icon_fn(x, row_y, 118, 104))
            if idx < len(cards) - 1:
                parts.append(line(x + 126, row_y + 52, x + 180, row_y + 52, arrow=True))
            x += 172

    parts.append(rect(1376, 260, 126, 182, rx=18, stroke="#df655f", sw=2.2))
    parts.append(rect(1548, 260, 126, 182, rx=18, stroke="#df655f", sw=2.2))
    parts.append(rect(1720, 260, 126, 182, rx=18, stroke="#df655f", sw=2.2))
    parts.append(text(1439, 212, "空间先验", size=22))
    parts.append(text(1611, 212, "几何剪枝", size=22))
    parts.append(text(1783, 212, "密度调制", size=22))
    parts.append(icon_ct_disc(1439, 347, 36))
    parts.append(line(1475, 351, 1540, 351, arrow=True))
    parts.append(line(1644, 351, 1710, 351, arrow=True))
    parts.append(soft_blob(1439, 398, 50, 24, "spotOrange"))
    parts.append(scatter(1399, 408, 84, 54, POINTS_SPARSE, fill="#d84b42", r=5))
    for cx, cy, dashed in [(1586, 322, False), (1614, 335, False), (1651, 317, False), (1568, 375, True), (1616, 382, True), (1655, 371, True)]:
        parts.append(ellipse(cx, cy, 11, 7, fill="#f4d2cf" if not dashed else "none", stroke="#da625b", sw=2, dashed=dashed))
    parts.append(scatter(1736, 314, 86, 104, [(0.14, 0.18), (0.48, 0.24), (0.74, 0.18), (0.20, 0.60), (0.55, 0.48), (0.81, 0.66)], fill="#d84b42", r=8, varying=True))
    return svg_doc(w, h, "\n".join(parts))


def pipeline_svg():
    w, h = 1900, 760
    parts = [
        rect(42, 86, 246, 168, rx=22),
        text(165, 52, "稀疏 CT 投影", size=34, weight=600),
        thumbnail_stack(64, 118, 78, 122, n=5),
        rect(42, 312, 246, 228, rx=22),
        text(165, 360, "FDK 粗重建", size=34, weight=600),
        ct_volume_box(98, 406, 144, 110, accent="spotBlue"),
        line(294, 312, 384, 312, arrow=True, sw=3),
        line(294, 426, 384, 426, arrow=True, sw=3),
        text(580, 82, "阶段 1：SPS", size=36, fill="#2f66c6", weight=700),
        text(976, 82, "阶段 2：GAP", size=36, fill="#1b9a8d", weight=700),
        text(1420, 82, "阶段 3：ADM", size=36, fill="#ef6c11", weight=700),
        panel_with_label(388, 124, 398, 420, "先验采样", "#5b8fda", ct_volume_box(466, 254, 210, 140, accent="spotBlue") + scatter(436, 210, 296, 238, POINTS_DENSE, fill="#4f86dc", r=5.5) + polygon([(432, 420), (462, 404), (484, 458), (454, 474)], fill="#d9e7fb", stroke="#5b8fda", sw=4) + line(456, 440, 546, 330, stroke="#5b8fda", sw=2.3, dashed=True) + line(456, 440, 604, 292, stroke="#5b8fda", sw=2.3, dashed=True) + line(456, 440, 672, 338, stroke="#5b8fda", sw=2.3, dashed=True) + dashed_box(448, 470, 280, 62, "#5b8fda") + text(588, 510, "空间先验引导的高斯初始化", size=22, fill="#315ea5")),
        panel_with_label(836, 124, 398, 420, "几何剪枝", "#54b8ae", ct_volume_box(918, 248, 214, 146, accent="spotBlue") + scatter(904, 214, 264, 220, POINTS_MID, fill="#49aa99", r=8, varying=True) + line(1042, 366, 1114, 366, arrow=True, stroke="#8d939b", sw=3) + scatter(1118, 232, 96, 170, [(0.18, 0.24), (0.64, 0.20), (0.76, 0.46), (0.30, 0.68), (0.58, 0.82)], fill="#49aa99", r=6, varying=True) + ''.join(ellipse(cx, cy, 12, 12, fill="none", stroke="#49aa99", sw=2.3, dashed=True) for cx, cy in [(1148, 258), (1186, 286), (1168, 344), (1128, 392)]) + dashed_box(900, 470, 270, 62, "#54b8ae") + text(1035, 510, "基于几何冗余的高斯剪枝", size=22, fill="#267b72")),
        panel_with_label(1284, 124, 398, 420, "密度调制", "#ef8e4d", ct_volume_box(1366, 262, 210, 132, accent="spotOrange") + scatter(1330, 226, 280, 210, [(0.12, 0.22), (0.30, 0.18), (0.48, 0.30), (0.72, 0.20), (0.88, 0.28), (0.18, 0.58), (0.38, 0.66), (0.64, 0.56), (0.80, 0.74)], fill="#e69249", r=7, varying=True) + ''.join(ellipse(cx, cy, 10, 10, fill="none", stroke="#eea16a", sw=2, dashed=True) for cx, cy in [(1368, 248), (1416, 282), (1548, 258)]) + line(1482, 366, 1548, 366, arrow=True, stroke="#8d939b", sw=3) + dashed_box(1352, 470, 264, 62, "#ef8e4d") + text(1484, 510, "基于空间编码的密度修正", size=22, fill="#b45b17")),
        rect(1734, 178, 132, 226, rx=22),
        text(1800, 148, "新视角 X-ray 结果", size=30, weight=600),
        rect(1760, 232, 102, 146, rx=4, fill="#111111", stroke="#2f3033", sw=1.5),
        icon_ct_disc(1811, 306, 44),
        line(1688, 334, 1728, 334, arrow=True, sw=3),
        line(356, 572, 1720, 572, stroke="#a4a9b1", sw=2, dashed=True),
        line(772, 560, 772, 588, stroke="#a4a9b1", sw=2),
        line(1234, 560, 1234, 588, stroke="#a4a9b1", sw=2),
        text(580, 622, "结构先验引入", size=22, fill="#4e5663"),
        text(1005, 622, "结构冗余优化", size=22, fill="#4e5663"),
        text(1468, 622, "密度精细修正", size=22, fill="#4e5663"),
    ]
    return svg_doc(w, h, "\n".join(parts))


def sps_svg():
    w, h = 1700, 700
    parts = [
        text(146, 66, "稀疏投影", size=30, weight=600),
        thumbnail_stack(42, 104, 72, 110, n=4),
        text(146, 300, "FDK 粗重建", size=30, weight=600),
        ct_volume_box(60, 344, 148, 112, accent="spotBlue"),
        rect(286, 146, 286, 330, rx=24),
        text(429, 112, "概率采样", size=30, weight=600),
        ct_volume_box(340, 212, 166, 126, accent="spotPurple"),
        soft_blob(424, 326, 56, 122, "spotPurple"),
        line(238, 196, 278, 196, arrow=True, sw=3),
        line(238, 398, 278, 398, arrow=True, sw=3),
        text(636, 314, "+", size=54, weight=500, fill="#6a7380"),
        rect(700, 176, 270, 270, rx=24),
        text(835, 142, "均匀补偿", size=30, weight=600),
        wire_cube(770, 238, 128, 128, dx=24, dy=-18),
        scatter(784, 252, 120, 116, POINTS_DENSE, fill="#6f90df", r=4.5),
        rect(1096, 146, 286, 330, rx=24),
        text(1239, 112, "初始高斯", size=30, weight=600),
        ct_volume_box(1154, 212, 166, 126, accent="spotPurple"),
        scatter(1146, 202, 190, 210, POINTS_DENSE + [(0.42, 0.86), (0.70, 0.84), (0.26, 0.76)], fill="#8a7be0", r=5.3),
        line(578, 312, 690, 312, arrow=True, sw=3),
        line(976, 312, 1088, 312, arrow=True, sw=3),
        text(428, 514, "高密度区域优先采样", size=22, fill="#6a7380"),
        text(836, 478, "少量均匀样本补全空域", size=22, fill="#6a7380"),
        text(1238, 514, "形成更稳健的初始高斯分布", size=22, fill="#6a7380"),
    ]
    return svg_doc(w, h, "\n".join(parts))


def gap_svg():
    w, h = 1780, 700
    parts = [
        rect(52, 170, 260, 280, rx=24),
        text(182, 134, "边界区域", size=30, weight=600),
        ct_volume_box(98, 226, 150, 118, accent="spotPurple"),
        scatter(92, 198, 178, 188, [(0.18, 0.12), (0.26, 0.22), (0.36, 0.30), (0.48, 0.36), (0.58, 0.44), (0.68, 0.56), (0.76, 0.68), (0.84, 0.82), (0.60, 0.20), (0.74, 0.32), (0.82, 0.50)], fill="#7685b6", r=5.2),
        line(320, 308, 410, 308, arrow=True, sw=3),
        text(558, 134, "邻域评估", size=30, weight=600),
        rect(432, 180, 352, 256, rx=24),
        circle(608, 308, 98, fill="none", stroke="#b9c0c8", sw=2),
    ]
    neighbor_pts = [(0.50, 0.18), (0.24, 0.38), (0.76, 0.36), (0.18, 0.66), (0.50, 0.78), (0.82, 0.68)]
    for px, py in neighbor_pts:
        cx = 608 - 98 + px * 196
        cy = 308 - 98 + py * 196
        parts.append(line(608, 308, cx, cy, stroke="#b7bec7", sw=1.7))
        parts.append(circle(cx, cy, 8, fill="#6e7fbc"))
    parts.append(circle(608, 308, 10, fill="#d24f47"))
    parts.append(text(608, 468, "计算局部邻近度与梯度活跃性", size=22, fill="#5f6875"))
    parts.append(line(790, 308, 884, 308, arrow=True, sw=3))
    parts.append(text(1038, 134, "几何冗余", size=30, weight=600))
    parts.append(rect(906, 180, 260, 256, rx=24))
    for cx, cy, dashed in [(962, 246, True), (1022, 228, False), (1084, 248, False), (952, 330, True), (1020, 320, False), (1102, 338, True)]:
        parts.append(ellipse(cx, cy, 16, 10, fill="#f2d9d5" if not dashed else "none", stroke="#db635b", sw=2.2, dashed=dashed))
    scatter(944, 230, 170, 160, [(0.16, 0.16), (0.38, 0.22), (0.60, 0.16), (0.22, 0.56), (0.46, 0.52), (0.72, 0.62)], fill="#8294d0", r=4.6)
    parts.append(text(1036, 468, "保留有效高斯，标记待剪冗余", size=22, fill="#5f6875"))
    parts.append(line(1172, 308, 1260, 308, arrow=True, sw=3))
    parts.append(text(1466, 134, "剪枝后结构", size=30, weight=600))
    parts.append(rect(1284, 170, 280, 280, rx=24))
    parts.append(ct_volume_box(1342, 226, 154, 118, accent="spotBlue"))
    parts.append(scatter(1330, 206, 194, 186, [(0.20, 0.14), (0.44, 0.22), (0.68, 0.20), (0.26, 0.48), (0.58, 0.52), (0.78, 0.66), (0.38, 0.72)], fill="#8b84db", r=6.2))
    parts.append(text(1424, 468, "边界附近分布更均匀", size=22, fill="#5f6875"))
    return svg_doc(w, h, "\n".join(parts))


def adm_svg():
    w, h = 1760, 700
    parts = [
        rect(50, 198, 216, 204, rx=24),
        text(158, 152, "位置输入", size=30, weight=600),
        wire_cube(96, 250, 108, 92, dx=20, dy=-16),
        text(158, 386, "x = (x, y, z, t)", size=22, fill="#5d6673"),
        line(274, 300, 368, 300, arrow=True, sw=3),
        rect(388, 166, 276, 276, rx=24),
        text(526, 124, "三平面编码", size=30, weight=600),
        polygon([(458, 368), (506, 228), (622, 240), (574, 382)], fill="#dfeafb", stroke="#8fb3df", sw=2.2, opacity=0.84),
        polygon([(438, 336), (554, 208), (554, 380), (438, 508)], fill="#e9f6ef", stroke="#8cbfa5", sw=2.2, opacity=0.78),
        polygon([(492, 204), (636, 204), (582, 368), (438, 368)], fill="#fdf2dc", stroke="#e5b96b", sw=2.2, opacity=0.68),
        line(672, 300, 748, 300, arrow=True, sw=3),
        rect(760, 182, 262, 236, rx=24),
        text(892, 144, "双头网络", size=30, weight=600),
    ]
    for x in [804, 860, 918]:
        parts.append(rect(x, 248, 22, 110, rx=6, fill="#eef1f4", stroke="#9fa8b3", sw=2))
    for x in [964, 1002]:
        parts.append(rect(x, 230, 22, 148, rx=6, fill="#eef1f4", stroke="#9fa8b3", sw=2))
    parts += [
        line(1030, 250, 1110, 250, arrow=True, sw=3),
        line(1030, 350, 1110, 350, arrow=True, sw=3),
        rect(1126, 176, 212, 148, rx=22),
        rect(1126, 334, 212, 148, rx=22),
        text(1232, 142, "密度偏移", size=28, fill="#ef6c11", weight=600),
        text(1232, 512, "置信度", size=28, fill="#2f66c6", weight=600),
        line(1148, 292, 1310, 238, stroke="#ef8e4d", sw=3),
        line(1148, 448, 1230, 400, stroke="#5b8fda", sw=3),
        line(1230, 400, 1310, 448, stroke="#5b8fda", sw=3),
        line(1346, 300, 1432, 300, arrow=True, sw=3),
        rect(1450, 198, 248, 204, rx=24),
        text(1574, 152, "密度校正", size=30, weight=600),
        scatter(1492, 238, 160, 120, [(0.10, 0.22), (0.36, 0.18), (0.64, 0.22), (0.24, 0.58), (0.54, 0.54), (0.82, 0.62)], fill="#eb9648", r=6.5, varying=True),
        ''.join(ellipse(cx, cy, 10, 10, fill="none", stroke="#efab72", sw=2, dashed=True) for cx, cy in [(1520, 268), (1594, 252)]),
    ]
    return svg_doc(w, h, "\n".join(parts))


def main():
    figures = {
        "fig_intro_compare.svg": intro_svg(),
        "fig_pipeline.svg": pipeline_svg(),
        "fig_sps.svg": sps_svg(),
        "fig_gap.svg": gap_svg(),
        "fig_adm.svg": adm_svg(),
    }
    for name, content in figures.items():
        (FIG_DIR / name).write_text(content, encoding="utf-8")
        print(f"wrote {name}")


if __name__ == "__main__":
    main()
