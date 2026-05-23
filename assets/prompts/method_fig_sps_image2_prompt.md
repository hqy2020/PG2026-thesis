# Image2 Prompt: SPS Module Figure (F04 — Figma-flat revision)

Target file: assets/fig/method_fig_sps.png
Size: 1800×720 px

---

## STYLE MANDATE — Figma-reproducible flat vector

- ONLY use: outlines, filled rectangles, solid/dashed lines, small filled circles (dots), simple 1D curve
- ZERO viridis/colormap gradients, ZERO textures, ZERO shadows, ZERO 3D
- Every element drawable in Figma with basic shape + pen tools
- White (#FFFFFF) background; thin #CCCCCC border around each panel
- Panel labels (a)(b)(c): bold black on a small white square chip, top-left corner of each panel

---

## Three panels, equal width, left → right

---

### Panel (a) — FDK input + attenuation profile

**Top half:**
- One simple closed outline shape (oval/rounded rectangle) representing an organ cross-section, stroke #666666 1.5pt, fill #F5F5F5
- One smaller closed shape inside representing inner structure, stroke #666666 1pt, fill #E8E8E8
- A horizontal dashed line crossing the shape at mid-height, stroke #999999 1pt dashed — represents "scan line"

**Bottom half:**
- A simple 1D curve (polyline or smooth bezier), color #7B5CA6 1.5pt
- Curve has 2–3 peaks roughly aligned with the inner structure above
- Flat baseline on both ends

Sub-caption below panel: "Coarse FDK + attenuation profile"

---

### Panel (b) — Density-weighted sampling map

**Body:**
- Same outer and inner outlines as panel (a), stroke #666666
- Inside the inner shape: solid fill #7B5CA6 at ~40% opacity (flat solid color block, NOT gradient) — represents high-attenuation support region
- Outside the inner shape but inside the outer shape: solid fill #DDDDDD — represents low-attenuation background
- Two short arrow + label annotations:
  - One arrow pointing INTO the purple fill area (no text baked in — leave space for LaTeX "high p(x)" label)
  - One arrow pointing INTO the gray background area (leave space for "low p(x)" label)

**Reserved blank area:**
- Bottom-right ~25% × 15% of panel: leave empty white space for LaTeX equation overlay

Sub-caption below panel: "Density-weighted sampling map"

---

### Panel (c) — Random init vs SPS init

Panel (c) is split into two equal sub-frames by a thin vertical line (#CCCCCC 1pt):

**Left sub-frame — Random init:**
- Same outer outline as (a), stroke #666666, no fill
- ~35 small filled circles, color #AAAAAA, diameter 4pt, scattered uniformly across entire frame (not clustered)

**Right sub-frame — SPS init:**
- Same outer outline, stroke #666666, no fill
- ~35 small filled circles, color #7B5CA6, diameter 4pt
- Circles concentrated inside and along the inner shape boundary; only ~4–5 circles outside as sparse coverage
- Visual contrast to left sub-frame must be immediately obvious

Sub-caption below panel: "Random vs path-anchored Gaussians"

---

## Color palette

| Element | Color |
|---|---|
| Organ outline / scan line | #666666 / #999999 |
| Inner shape fill (low) | #E8E8E8 |
| High-p(x) region fill | #7B5CA6 @ 40% (flat) |
| Low-p(x) region fill | #DDDDDD (flat) |
| Attenuation curve | #7B5CA6 1.5pt |
| Random init dots | #AAAAAA |
| SPS init dots | #7B5CA6 |
| Panel border | #CCCCCC 0.5pt |
| Background | #FFFFFF |

---

## Must-pass checks

1. All three panels share the same organ outline shape
2. Panel (b) color blocks are flat solid fills — NOT viridis/rainbow gradients
3. Panel (c): gray dots uniformly spread vs purple dots clustered — contrast must be immediately visible
4. No text or equations baked into image; annotation arrows leave space for LaTeX labels
5. Bottom-right of panel (b) is blank white
6. Reading order (a)→(b)→(c) is unambiguous
