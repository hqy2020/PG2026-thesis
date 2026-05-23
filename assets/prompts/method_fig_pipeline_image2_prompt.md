# Image2 Prompt: Method Pipeline Figure (F03 — Figma-flat revision)

Target file: assets/fig/method_fig_pipeline.png
Size: 1980×800 px

---

## STYLE MANDATE — Figma-reproducible flat vector

- ONLY use: filled rectangles, rounded rectangles, circles/ellipses, solid lines, dashed lines, arrowheads, small dot clusters
- ZERO gradients, ZERO textures, ZERO shadows, ZERO 3D effects, ZERO realistic imagery
- Every element must be drawable in Figma with basic shape tools
- White (#FFFFFF) background throughout
- NO text, NO labels, NO letters anywhere in the image

---

## Layout — strictly left → right, five zones

```
[Input]  →→  [SPS]  →→  ╔══ Training Loop ══╗  →→  [Output]
  gray        purple     ║  [ADM]  ↔  [GAP]  ║       gray
                         ╚═══════════════════╝
                              ↑ dashed arc above
```

---

## Zone 1 — Input (leftmost ~12% width)

- Two thin upright rectangles stacked with slight offset, solid fill #F0F0F0, border #888888 1.5pt
- No decorations, no ray lines, no texture

## Zone 2 — SPS block (~18% width)

- One large rounded rectangle, solid fill #7B5CA6, no border
- Below the block: 6 small filled circles (dots), fill #7B5CA6, diameter ~6pt, arranged in a loose curved cluster (not a grid)

## Zone 3 — Training Loop (~40% width)

**Outer frame:**
- Large rounded rectangle, border #999999 2pt dashed (4pt dash / 3pt gap), NO fill (transparent interior)

**Above the outer frame — feedback arc:**
- One curved arrow going from top-right corner of the loop box, arcing upward, ending at top-left corner with an arrowhead
- Style: #555555 dashed 2pt, arrowhead only at the left end
- Arc must span the full width of the loop box and be clearly visible

**Inside left — ADM block:**
- Rounded rectangle, solid fill #E07B39, no border
- Occupies left ~46% of loop interior, vertically centered

**Inside right — GAP block:**
- Rounded rectangle, solid fill #3CA897, no border
- Occupies right ~46% of loop interior, vertically centered

**Between ADM and GAP:**
- Double-headed horizontal arrow (←→), solid black #1A1A1A 1.5pt, centered between the two blocks

## Zone 4 — Output (rightmost ~12% width)

- Same two-rectangle stack as Zone 1, identical style

---

## Inter-zone arrows (data flow)

- Zone 1 → Zone 2: solid right-pointing arrow, #1A1A1A 2pt
- Zone 2 → Zone 3: solid right-pointing arrow, #1A1A1A 2pt
- Zone 3 → Zone 4: solid right-pointing arrow, #1A1A1A 2pt

---

## Color palette

| Element | Color |
|---|---|
| SPS block | #7B5CA6 |
| ADM block | #E07B39 |
| GAP block | #3CA897 |
| Input/Output boxes | #F0F0F0 fill, #888888 border |
| Data-flow arrows | #1A1A1A solid |
| Loop feedback arc | #555555 dashed |
| ADM↔GAP double arrow | #1A1A1A solid |
| Loop frame border | #999999 dashed |
| Background | #FFFFFF |

---

## Must-pass checks

1. NO text anywhere
2. Feedback arc clearly closes the loop visually (arcs above the loop box, spans full width)
3. SPS block is OUTSIDE and BEFORE the loop box
4. ADM (orange) on LEFT inside loop; GAP (teal) on RIGHT inside loop
5. All shapes are flat 2D — no drop shadows, no gradients, no 3D
6. The five zones read cleanly left to right: Input → SPS → Loop → Output
