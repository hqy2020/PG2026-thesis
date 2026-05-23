"""Add column header labels to intro_fig_compare.png.

The existing image (1840x820) has no explicit column headers at the top.
This script adds white-background header chips at the top of each column:
  - "Sparse Input"       (col 1)
  - "Gaussian Allocation" (col 2)
  - "Rendering & Error"  (col 3)

Runs in-place; a backup is saved as intro_fig_compare_backup.png.
"""

import pathlib
import shutil

from PIL import Image, ImageDraw, ImageFont

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
FIG_PATH = REPO_ROOT / "assets" / "fig" / "intro_fig_compare.png"
BACKUP_PATH = REPO_ROOT / "assets" / "fig" / "intro_fig_compare_backup.png"

# Column header labels (matching F02 requirements)
HEADERS = ["Sparse Input", "Gaussian Allocation", "Rendering & Error"]

# Layout parameters (image width = 1840, row-chip approx 85px wide)
ROW_CHIP_WIDTH = 85
IMAGE_WIDTH = 1840
N_COLS = 3
COL_WIDTH = (IMAGE_WIDTH - ROW_CHIP_WIDTH) / N_COLS  # ~585 px

# X-center for each column header
COL_CENTERS = [
    int(ROW_CHIP_WIDTH + COL_WIDTH * (i + 0.5)) for i in range(N_COLS)
]  # [377, 962, 1547]

# Padding added at top of image for the header strip
HEADER_HEIGHT = 40
TEXT_Y = 8          # text baseline from top of new strip
FONT_SIZE = 22      # ≈9pt at typical 150dpi paper-column width


def load_font(size: int):
    """Try to load a clean sans-serif font; fall back to default if not found."""
    candidates = [
        "/Library/Fonts/Arial.ttf",
        "/Library/Fonts/Helvetica.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNSDisplay.ttf",
        "/System/Library/Fonts/SFNS.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ]
    for path in candidates:
        if pathlib.Path(path).exists():
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()


def main() -> None:
    if not FIG_PATH.exists():
        raise FileNotFoundError(f"Source figure not found: {FIG_PATH}")

    # Backup
    shutil.copy2(FIG_PATH, BACKUP_PATH)
    print(f"Backup saved to {BACKUP_PATH.relative_to(REPO_ROOT)}")

    img = Image.open(FIG_PATH).convert("RGBA")
    W, H = img.size  # expected 1840, 820

    # Create a new canvas with extra space at the top
    new_H = H + HEADER_HEIGHT
    canvas = Image.new("RGBA", (W, new_H), (255, 255, 255, 255))
    canvas.paste(img, (0, HEADER_HEIGHT))

    draw = ImageDraw.Draw(canvas)
    font = load_font(FONT_SIZE)
    dark_gray = (55, 55, 55, 255)

    for header, cx in zip(HEADERS, COL_CENTERS):
        # Measure text bounding box for background box
        bbox = draw.textbbox((0, 0), header, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        pad_x, pad_y = 8, 4
        x0 = cx - tw // 2 - pad_x
        y0 = TEXT_Y - pad_y
        x1 = cx + tw // 2 + tw % 2 + pad_x
        y1 = TEXT_Y + th + pad_y

        # White background rounded rectangle
        draw.rounded_rectangle([x0, y0, x1, y1], radius=5,
                                fill=(255, 255, 255, 240),
                                outline=(200, 200, 200, 255), width=1)

        # Header text (bold, dark gray)
        draw.text((cx - tw // 2, TEXT_Y), header, font=font, fill=dark_gray)

    # Save as PNG (RGB, no alpha)
    canvas.convert("RGB").save(FIG_PATH, format="PNG", optimize=False, dpi=(300, 300))
    print(f"Updated {FIG_PATH.relative_to(REPO_ROOT)}  (size: {W}×{new_H})")


if __name__ == "__main__":
    main()
