# Image2 Prompt: Intro Comparison Figure (F02 — Figma-flat revision)

Target file: assets/fig/intro_fig_compare.png
Size: 1840×820 px

---

## STYLE MANDATE — Figma-reproducible flat vector

- ONLY use: filled rectangles, outlines, small filled circles (dots), solid/dashed lines, arrowheads, plain color fills
- ZERO inferno/viridis/magma gradients, ZERO photorealistic CT textures, ZERO 3D/perspective, ZERO shadows
- Every element must be drawable in Figma using basic rectangle + circle + pen tools
- White (#FFFFFF) background throughout
- Thin #DDDDDD outer border around the whole figure

---

## Overall layout: 2 rows × 3 columns

```
┌─────────────────────────────────────────────────────────────────┐
│  [row chip]  │  Sparse Input  │  Gaussian Allocation  │  Error  │
│  Conventional│                │                       │         │
├── dashed separator ─────────────────────────────────────────────┤
│  [row chip]  │  Sparse Input  │  Gaussian Allocation  │  Error  │
│  XRA-GS      │                │                       │         │
└─────────────────────────────────────────────────────────────────┘
```

**Column header strip** (very top, above both rows):
- Three centered text labels: "Sparse Input" / "Gaussian Allocation" / "Rendering & Error"
- Style: 9pt bold dark gray #333333, on white background strip

**Row divider**: single thin dashed line #CCCCCC between the two rows

**Row label chips** (far left of each row, vertically centered):
- Top row: small rounded rectangle, fill #F0F0F0, text "Conventional" in #888888 (no baked text — leave placeholder space)
- Bottom row: small rounded rectangle, fill #FCE4E5, text "XRA-GS (Ours)" in #D7263D (leave placeholder space)

---

## Column 1 — Sparse Input (both rows identical except bottom adds FDK box)

- Two upright thin rectangles side by side, fill #E8E8E8, border #888888 1pt — represent X-ray projection views
- Two solid arrows pointing toward the rectangles from slightly different angles (left-leaning and right-leaning), color #555555 1.5pt — represent beam directions

**Bottom row only — add FDK support box:**
- One additional small upright rectangle, fill #F5F5F5, border #999999 1pt dashed — represents coarse FDK prior
- Positioned below or beside the two main projection rectangles
- Leave blank space inside for LaTeX "FDK support" label

---

## Column 2 — Gaussian Allocation

Organ silhouette (same in both rows):
- One closed outline shape (oval or rounded rectangle), stroke #666666 1.5pt, fill #F7F7F7
- One smaller inner shape inside representing inner structure, stroke #666666 1pt, fill #EEEEEE

**Top row (Conventional):**
- ~28 small filled circles, color #888888, diameter 4pt
- Heavy clustering ALONG the boundary of the outer outline (~20 circles on/near boundary, ~8 inside)
- Visual impression: boundary is dense, interior is sparse/empty

**Bottom row (XRA-GS):**
- ~28 small filled circles, color #7B5CA6 (soft purple), diameter 4pt
- Uniformly distributed throughout interior and boundary — no heavy clustering at boundary
- Below the silhouette (bottom row only): three small rounded rectangle chips in a row connected by short solid arrows:
  - Chip 1: fill #7B5CA6 — placeholder for "SPS" label
  - Chip 2: fill #3CA897 — placeholder for "GAP" label
  - Chip 3: fill #E07B39 — placeholder for "ADM" label
  - Chips connected: Chip1 →→ Chip2 →→ Chip3 (solid black 1pt arrows)

---

## Column 3 — Rendering & Error

Each row contains two sub-panels side by side (equal width):

**Left sub-panel — Rendered projection:**
- Upright rectangle, fill #DCDCDC (light gray = clean render), border #AAAAAA 1pt
- Top row: add 2–3 thin horizontal stripes of fill #BBBBBB slightly darker — represent streak artifacts
- Bottom row: same plain light gray rectangle, no stripes (cleaner render)

**Right sub-panel — Error map (flat two-zone version, NOT inferno gradient):**
- Upright rectangle with hard-edge two-zone fill:
  - Top row: upper ~65% of the rectangle filled #FFAA55 (warm amber = high error), lower ~35% filled #FFD9A0 (lighter = moderate error). Both flat solid fills, hard boundary between zones.
  - Bottom row: upper ~80% of rectangle filled #E0E0E0 (cool light gray = low error), lower ~20% filled #FFCC88 (small warm spot = residual error). Flat solid fills.
- Border #AAAAAA 1pt on both sub-panels

---

## Color palette

| Element | Color |
|---|---|
| Conventional dots | #888888 neutral gray |
| XRA-GS dots | #7B5CA6 soft purple |
| SPS chip | #7B5CA6 |
| GAP chip | #3CA897 |
| ADM chip | #E07B39 |
| Organ outline | #666666 stroke, #F7F7F7 fill |
| Projection rectangles | #E8E8E8 fill, #888888 border |
| FDK box | #F5F5F5 fill, #999999 dashed border |
| High-error zone | #FFAA55 warm amber |
| Low-error zone | #E0E0E0 light gray |
| Row divider | #CCCCCC dashed |
| Background | #FFFFFF |

---

## Must-pass checks

1. Two rows clearly separated by dashed line; row label chips on far left
2. Column 1 is IDENTICAL between rows (except FDK box in bottom row only)
3. Column 2: conventional dots cluster on boundary; XRA-GS dots spread interior — contrast immediately obvious
4. Column 2 bottom row: SPS/GAP/ADM chips appear below the silhouette (bottom row only)
5. Column 3 error maps: top row is dominated by warm color, bottom row by cool gray — flat solid fills, no gradient
6. NO text baked into image except column headers and row chips; leave space for all other LaTeX labels
7. All elements flat 2D — zero 3D, zero gradients, zero shadows
