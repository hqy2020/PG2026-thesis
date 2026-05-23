# Image2 Prompt: GAP Module Figure (F05 — Figma-flat revision)

Target file: assets/fig/method_fig_gap.png
Size: 1800×720 px

---

## STYLE MANDATE — Figma-reproducible flat vector

- ONLY use: outlines, flat solid fills, small ellipses (Gaussians), ✕ markers, ○ markers, arrows
- ZERO magma/colormap gradients, ZERO KNN connection webs, ZERO textures, ZERO shadows
- White (#FFFFFF) background for all panels; #F7F7F7 very light gray fill inside organ outline
- Panel labels (a)(b)(c): bold black on small white square chip, top-left of each panel

---

## Three panels, equal width, left → right

All three panels share the same organ outline shape and the same Gaussian ellipse positions.

---

### Panel (a) — Before pruning: over-densified boundary

- Organ cross-section: closed outline shape (oval or rounded rect), stroke #666666 1.5pt, fill #F7F7F7
- ~30 small ellipses (Gaussian markers), fill #3CA897 (teal), no stroke, size ~8pt × 5pt
  - ~18 ellipses clustered densely along the boundary contour of the organ outline
  - ~12 ellipses scattered more loosely in the interior
- Sub-caption below: "Boundary over-densification"

---

### Panel (b) — Pruning criterion applied

- Same organ outline, same fill, same #3CA897 teal ellipses at identical positions as panel (a)
- Overlay markers on ~6 ellipses judged redundant (those in the densest boundary clusters):
  - Red ✕ marks: color #D7263D, line width 2pt, placed centered on those 6 ellipses
- Overlay markers on ~4 representative "kept" ellipses in less-dense regions:
  - Green hollow circle ○: color #2A9D5C, stroke 1.5pt, diameter 10pt, placed centered on those ellipses
- Reserved blank area: bottom-right ~25% × 15% of panel — empty white for LaTeX equation overlay
- Sub-caption below: "Geometry-aware pruning filter"

---

### Panel (c) — After pruning: cleaner distribution

- Same organ outline, same fill
- Same teal ellipses as panel (a), MINUS the 6 that had red ✕ marks
- Remaining ~24 ellipses: fill #3CA897, no stroke
- A small annotation chip at top-right inside panel (no baked text — leave space for "−β·N" LaTeX label): just a small light-gray rectangle as placeholder
- Sub-caption below: "After redundancy recovery"

---

## Color palette

| Element | Color |
|---|---|
| Organ outline | #666666 1.5pt stroke |
| Panel background fill | #F7F7F7 inside outline, #FFFFFF outside |
| Retained Gaussians | #3CA897 teal, filled ellipse |
| Pruned marker | #D7263D red ✕, 2pt stroke |
| Kept marker | #2A9D5C green ○, 1.5pt hollow circle |
| Panel border | #CCCCCC 0.5pt |
| Background | #FFFFFF |

---

## Must-pass checks

1. All three panels: same organ outline, same Gaussian positions (except (c) removes pruned ones)
2. NO colormap background — panel fill is flat #F7F7F7 only
3. Red ✕ = pruned, Green ○ = kept — never reversed
4. Pruned ≈ 6 markers; retained ≈ 24 — visible ~20% reduction in boundary density
5. Bottom-right of panel (b) is blank white for equation
6. No KNN connection lines or complex webs
