"""Render qualitative NVS comparison figure: 4 organs × 5 methods grid with zoom-in boxes.

Output: assets/fig/experiment_fig_qual_nvs.png
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "fig" / "experiment_fig_qual_nvs.png"

ROWS = [
    ("Chest",    "chest_01"),
    ("Foot",     "foot_00"),
    ("Head",     "head_46"),
    ("Pancreas", "pancreas_00"),
]

COLS = [
    ("GT",            "gt"),
    ("DNGaussian",    "dngs"),
    (r"R²-Gaussian",  "r2gs"),
    ("X-Field",       "xfield"),
    ("RAttAGS (Ours)", "rattags"),
]

RED = (255, 68, 68)
BLUE = (68, 136, 255)
BOX_LINE_W = 3
ZOOM_BORDER = 4

IMG_SIZE = 360
ZOOM_H = IMG_SIZE // 2
ZOOM_W = int(IMG_SIZE * 0.35)
CELL_W = IMG_SIZE + ZOOM_W + 2
CELL_H = IMG_SIZE

COL_GAP = 4
ROW_GAP = 4
LABEL_W = 56
HEADER_H = 52

ZOOM_REGIONS = {
    "chest_01":    {"red": (0.15, 0.35, 0.18, 0.18), "blue": (0.58, 0.45, 0.18, 0.18)},
    "foot_00":     {"red": (0.18, 0.51, 0.14, 0.14), "blue": (0.53, 0.68, 0.14, 0.14)},
    "head_46":     {"red": (0.55, 0.38, 0.14, 0.14), "blue": (0.20, 0.38, 0.14, 0.14)},
    "pancreas_00": {"red": (0.38, 0.28, 0.14, 0.14), "blue": (0.40, 0.56, 0.14, 0.14)},
}


def load_font(size):
    for name in [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNSText.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]:
        try:
            return ImageFont.truetype(name, size)
        except (OSError, IOError):
            continue
    return ImageFont.load_default()


def load_font_bold(size):
    for name in [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNSText-Bold.otf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ]:
        try:
            return ImageFont.truetype(name, size, index=1)
        except (OSError, IOError):
            try:
                return ImageFont.truetype(name, size)
            except (OSError, IOError):
                continue
    return ImageFont.load_default()


def crop_zoom(img, region):
    w, h = img.size
    rx, ry, rw, rh = region
    x0 = int(rx * w)
    y0 = int(ry * h)
    x1 = int((rx + rw) * w)
    y1 = int((ry + rh) * h)
    x0, y0 = max(0, x0), max(0, y0)
    x1, y1 = min(w, x1), min(h, y1)
    return img.crop((x0, y0, x1, y1))


def draw_rect_on_img(draw, img_size, region, color, line_w):
    w, h = img_size
    rx, ry, rw, rh = region
    x0 = int(rx * w)
    y0 = int(ry * h)
    x1 = int((rx + rw) * w)
    y1 = int((ry + rh) * h)
    draw.rectangle([x0, y0, x1, y1], outline=color, width=line_w)


def build_cell(img_path, prefix):
    img = Image.open(img_path).convert("RGB").resize((IMG_SIZE, IMG_SIZE), Image.LANCZOS)

    regions = ZOOM_REGIONS[prefix]
    red_region = regions["red"]
    blue_region = regions["blue"]

    zoom_red = crop_zoom(img, red_region).resize((ZOOM_W - 2 * ZOOM_BORDER, ZOOM_H - 2 * ZOOM_BORDER), Image.LANCZOS)
    zoom_blue = crop_zoom(img, blue_region).resize((ZOOM_W - 2 * ZOOM_BORDER, ZOOM_H - 2 * ZOOM_BORDER), Image.LANCZOS)

    draw = ImageDraw.Draw(img)
    draw_rect_on_img(draw, (IMG_SIZE, IMG_SIZE), red_region, RED, BOX_LINE_W)
    draw_rect_on_img(draw, (IMG_SIZE, IMG_SIZE), blue_region, BLUE, BOX_LINE_W)

    cell = Image.new("RGB", (CELL_W, CELL_H), (255, 255, 255))
    cell.paste(img, (0, 0))

    zoom_x = IMG_SIZE + 2
    zr_canvas = Image.new("RGB", (ZOOM_W, ZOOM_H), RED)
    zr_canvas.paste(zoom_red, (ZOOM_BORDER, ZOOM_BORDER))
    cell.paste(zr_canvas, (zoom_x, 0))

    zb_canvas = Image.new("RGB", (ZOOM_W, ZOOM_H), BLUE)
    zb_canvas.paste(zoom_blue, (ZOOM_BORDER, ZOOM_BORDER))
    cell.paste(zb_canvas, (zoom_x, ZOOM_H))

    cell_draw = ImageDraw.Draw(cell)
    rx, ry, rw, rh = red_region
    red_box_right = int((rx + rw) * IMG_SIZE)
    red_box_top = int(ry * IMG_SIZE)
    red_box_bot = int((ry + rh) * IMG_SIZE)
    cell_draw.line([(red_box_right, red_box_top), (zoom_x, 0)], fill=RED, width=1)
    cell_draw.line([(red_box_right, red_box_bot), (zoom_x, ZOOM_H - 1)], fill=RED, width=1)

    bx, by, bw, bh = blue_region
    blue_box_right = int((bx + bw) * IMG_SIZE)
    blue_box_top = int(by * IMG_SIZE)
    blue_box_bot = int((by + bh) * IMG_SIZE)
    cell_draw.line([(blue_box_right, blue_box_top), (zoom_x, ZOOM_H)], fill=BLUE, width=1)
    cell_draw.line([(blue_box_right, blue_box_bot), (zoom_x, CELL_H - 1)], fill=BLUE, width=1)

    return cell


def main():
    n_rows = len(ROWS)
    n_cols = len(COLS)

    canvas_w = LABEL_W + n_cols * CELL_W + (n_cols - 1) * COL_GAP
    canvas_h = HEADER_H + n_rows * CELL_H + (n_rows - 1) * ROW_GAP

    canvas = Image.new("RGB", (canvas_w, canvas_h), (255, 255, 255))
    draw = ImageDraw.Draw(canvas)

    font_header = load_font_bold(30)
    font_label = load_font_bold(26)

    for ci, (col_title, _) in enumerate(COLS):
        x_center = LABEL_W + ci * (CELL_W + COL_GAP) + CELL_W // 2
        bbox = draw.textbbox((0, 0), col_title, font=font_header)
        tw = bbox[2] - bbox[0]
        draw.text((x_center - tw // 2, (HEADER_H - (bbox[3] - bbox[1])) // 2), col_title, fill=(0, 0, 0), font=font_header)

    for ri, (row_label, prefix) in enumerate(ROWS):
        y_center = HEADER_H + ri * (CELL_H + ROW_GAP) + CELL_H // 2

        label_img = Image.new("RGB", (CELL_H, LABEL_W), (255, 255, 255))
        ld = ImageDraw.Draw(label_img)
        bbox = ld.textbbox((0, 0), row_label, font=font_label)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        ld.text(((CELL_H - tw) // 2, (LABEL_W - th) // 2 - 2), row_label, fill=(0, 0, 0), font=font_label)
        label_img = label_img.rotate(90, expand=True)
        canvas.paste(label_img, (0, HEADER_H + ri * (CELL_H + ROW_GAP)))

        for ci, (_, method_suffix) in enumerate(COLS):
            fname = f"{prefix}_{method_suffix}.png"
            img_path = DATA / fname
            if not img_path.exists():
                print(f"WARN: missing {img_path}")
                continue

            cell = build_cell(img_path, prefix)
            cx = LABEL_W + ci * (CELL_W + COL_GAP)
            cy = HEADER_H + ri * (CELL_H + ROW_GAP)
            canvas.paste(cell, (cx, cy))

    canvas.save(OUT, dpi=(300, 300))
    print(f"Saved: {OUT}  ({canvas.size[0]}×{canvas.size[1]})")


def export_cells():
    """Export individual cell images with zoom-in for LaTeX tabular layout."""
    out_dir = DATA
    for _, prefix in ROWS:
        for _, method_suffix in COLS:
            fname = f"{prefix}_{method_suffix}.png"
            img_path = DATA / fname
            if not img_path.exists():
                print(f"WARN: missing {img_path}")
                continue
            cell = build_cell(img_path, prefix)
            out_path = out_dir / f"cell_{prefix}_{method_suffix}.png"
            cell.save(out_path, dpi=(300, 300))
            print(f"Saved: {out_path}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--cells":
        export_cells()
    else:
        main()
