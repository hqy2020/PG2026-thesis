# Image2 Prompt: ADM Module Figure (F06 — Figma-flat revision)

Target file: assets/fig/method_fig_adm.png
Size: 1800×720 px

---

## STYLE MANDATE — Figma-reproducible flat vector

- ONLY use: flat filled rectangles, rounded rectangles, circles/dots, solid/dashed arrows, plain fills
- ZERO K-Planes 3D fan perspective, ZERO inferno/viridis gradients, ZERO shadows, ZERO textures
- Every element must be drawable in Figma with rectangle + pen tools in under 2 minutes
- White (#FFFFFF) background; thin #CCCCCC border around each panel
- Panel labels (a)(b)(c): bold black on small white square chip, top-left of each panel

---

## Three panels, equal width, left → right

---

### Panel (a) — K-Planes spatial context (flat version)

- Three stacked horizontal rectangles, slightly offset vertically (staircase layout, NOT fan/perspective):
  - Top rect: fill #C8B8E8 (light purple tint), ~80% panel width, height ~18% panel height
  - Middle rect: fill #B8D8D4 (light teal tint), slightly narrower (~75%), same height, offset down ~20pt
  - Bottom rect: fill #F5D8B8 (light orange tint), slightly narrower (~70%), offset down another ~20pt
- A small filled circle (dot), #333333, diameter 6pt, positioned at the right-center edge of the stack — represents a Gaussian center
- Three short solid arrows from the dot pointing to the right edge of each rectangle (one per plane)
- Sub-caption below: "K-Planes spatial context"

---

### Panel (b) — Dual-head MLP flow diagram

A pure box-and-arrow flow, strictly left → right, then splitting into two output branches:

```
[Gaussians] →→ [K-Planes] →→ [MLP] →→→ [Δσ(x)]  (top branch)
                                    ↘→→ [g(x)]    (bottom branch)
                                               ↘ both converge → [ρ_final]
```

Box styles:
- "Gaussians" box: fill #F5F5F5, border #AAAAAA 1pt, rounded corners
- "K-Planes" box: fill #F5F5F5, border #AAAAAA 1pt, rounded corners
- "MLP" box: fill #FFFFFF, border #333333 2pt, rounded corners, taller than wide
- "Δσ(x)" box: fill #E07B39 (warm orange), no border, rounded corners
- "g(x)" box: fill #5B7C99 (slate blue), no border, rounded corners
- "ρ_final" box: fill #F5F5F5, border #AAAAAA 1pt, rounded corners

Arrows:
- All flow arrows: #1A1A1A solid 1.5pt with arrowheads
- From MLP: one arrow going upper-right to Δσ(x), one arrow going lower-right to g(x)
- From Δσ(x) and g(x): both arrows converge to ρ_final

Reserved blank area: bottom ~20% of panel — empty white for LaTeX formula overlay

Sub-caption below: "Dual-head density prediction"

---

### Panel (c) — Density modulation effect

- Same organ cross-section outline as SPS/GAP panels (closed shape, stroke #666666 1.5pt)
- Interior split into two flat-color zones (hard boundary, no gradient):
  - "Amplified" zone (high-attenuation region, ~40% of interior): solid fill #FFCC88 (warm amber)
  - "Damped" zone (low-attenuation region, ~60% of interior): solid fill #CCCCCC (neutral gray)
- Two short annotation arrows inside panel:
  - Arrow pointing to #FFCC88 zone: leave blank space next to arrowhead for LaTeX "ADM amplifies" label
  - Arrow pointing to #CCCCCC zone: leave blank space for "ADM damps" label
- Sub-caption below: "ADM density modulation effect"

---

## Color palette

| Element | Color |
|---|---|
| K-Planes rects (tints) | #C8B8E8 / #B8D8D4 / #F5D8B8 |
| MLP box | #FFFFFF fill, #333333 2pt border |
| Δσ(x) box | #E07B39 warm orange |
| g(x) box | #5B7C99 slate blue |
| ρ_final box | #F5F5F5 fill, #AAAAAA border |
| Amplified zone | #FFCC88 warm amber |
| Damped zone | #CCCCCC neutral gray |
| Flow arrows | #1A1A1A solid 1.5pt |
| Organ outline | #666666 1.5pt |
| Panel border | #CCCCCC 0.5pt |
| Background | #FFFFFF |

---

## Must-pass checks

1. Panel (a): three flat stacked rectangles in staircase layout — NOT a 3D fan/perspective view
2. Panel (b): clearly shows TWO separate output heads from MLP (orange Δσ, slate-blue g)
3. Panel (c): two flat solid-fill zones — NOT inferno/gradient colormap
4. Slate blue #5B7C99 for g(x) — NOT teal #3CA897 (teal is reserved for GAP module)
5. Bottom of panel (b) reserves blank space for LaTeX formula
6. All boxes and shapes are flat 2D — zero drop shadows, zero 3D
