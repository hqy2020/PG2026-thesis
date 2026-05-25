# Abstract Top-Conference Revision Suggestions (2026-05-25)

## 1. Core Diagnosis

Current location: `main.tex` abstract block, currently line 57.

The current abstract has the right broad topic, but it is weaker than a top-conference abstract in both framing and evidence. It explains that XRA-GS redesigns Gaussian evolution, yet it does not open with the locked task name `Sparse Tomographic View Synthesis`, does not use the fixed module labels `SPS / GAP / ADM`, and ends with a generic state-of-the-art claim rather than checkable numbers.

Compared with the reference papers, the current abstract is weaker in six places:

1. **The central insight is buried inside a long limitation sentence.**
   - Current wording explains that prior methods inherit gradient-driven densification and over-allocate capacity to anatomical boundaries.
   - This is the right insight, but the sentence is very long and makes the novelty feel like a descriptive observation rather than the paper's main claim.
   - Top-conference abstracts usually isolate the core finding as a crisp bottleneck: e.g., "we identify X as the failure mode" before introducing the method.

2. **The locked task name is missing from the first sentence.**
   - The abstract currently starts from generic "3D Gaussian Splatting has been extended to X-ray novel view synthesis."
   - For this manuscript, the abstract should define the paper around `Sparse Tomographic View Synthesis`, not around generic X-ray NVS.
   - Otherwise the title, introduction, and abstract do not reinforce the same task identity.

3. **The module names are described but not named.**
   - The current abstract says "support-profile seeding strategy", "geometry-aware pruning", and "adaptive density modulation", but does not use the fixed abbreviations `SPS / GAP / ADM`.
   - This weakens consistency with the method section, ablation table, and figure labels.
   - A top-conference abstract can name the modules once, but should avoid turning the abstract into a component inventory.

4. **The module list still takes too much abstract space.**
   - The current abstract spends one full sentence explaining the three components in low-level prose.
   - This is understandable, but in an abstract it risks sounding like an implementation list.
   - Reference abstracts such as CoR-GS, R2-Gaussian, X-Field, DGR, and X-LRM usually compress components into a mechanism-level summary, then reserve detailed roles for the introduction and method section.

5. **The experimental evidence is too vague at the exact moment it should be strongest.**
   - Current ending: "state-of-the-art PSNR2D and competitive SSIM2D across all view-count settings."
   - This is weaker than the available evidence because it does not report the five-organ average gains, the 2/3/4-view setting, or the tie behavior in 4-view SSIM2D.
   - A stronger top-conference ending should report the verifiable numbers directly: average PSNR2D gains over R2-Gaussian and X-Field, plus SSIM2D values for the methods with available same-protocol logs.

6. **The abstract currently omits the ablation evidence.**
   - The method is built around `SPS / GAP / ADM`, but the abstract only lists the components and does not say that ablation supports the design.
   - Existing table evidence can support a restrained ablation sentence: `SPS` improves the 2-view initialization regime, and `GAP` gives the largest observed PSNR2D increment.
   - Since intermediate SSIM2D values remain pending, the abstract should not overclaim SSIM-level module effects.

## 2. What The Reference Abstracts Do Better

The reference papers have different topics, but their abstract rhythm is consistent:

- **X-Gaussian / R2-Gaussian**: start from X-ray or CT importance, identify the representation/rendering mismatch, then end with concrete quality and speed gains.
- **CoR-GS**: presents a specific empirical observation before the method, making the contribution feel discovered rather than assembled.
- **FSGS / DNGaussian**: state the sparse-view trade-off early, then connect each module to that trade-off.
- **X-Field**: frames the core gap as a physics mismatch between visible-light representations and X-ray attenuation.
- **DGR / X-LRM**: define the task and representation gap directly, then close with dataset-scale or metric-scale evidence.

For `XRA-GS`, the closest abstract pattern should be:

`task value -> capacity-allocation bottleneck -> XRA-GS mechanism -> ablation support -> strongest benchmark evidence`

This keeps the paper aligned with top-conference style while preserving the fixed manuscript logic.

## 3. Recommended Abstract Skeleton

Use five sentences:

1. **Task and value.**
   - Define `Sparse Tomographic View Synthesis`.
   - Mention low-dose / fast CT acquisition.
   - Avoid adding too many application nouns.

2. **Gap and core insight.**
   - Prior X-ray/CT 3DGS methods already improve radiative rendering.
   - The remaining failure is Gaussian evolution: gradient-driven densification over-allocates capacity to high-contrast boundaries and under-represents attenuation-bearing interiors.

3. **Method.**
   - Introduce `XRA-GS` as `X-ray Attenuation-Aligned Gaussian Splatting`.
   - Compress `SPS / GAP / ADM` into one mechanism-level phrase.

4. **Ablation.**
   - State only what the current tables support.
   - Recommended claim: `SPS` improves the 2-view initialization regime, and `GAP` gives the largest observed PSNR2D increment.

5. **Main result.**
   - Report the five-organ `2/3/4` view protocol.
   - Include PSNR2D gains over `R2-Gaussian` and `X-Field$^*$`.
   - Include same-protocol SSIM2D values without sounding apologetic.

## 4. LaTeX-Ready Draft

```tex
Sparse Tomographic View Synthesis seeks to synthesize unseen X-ray projections from only a few acquired views, enabling lower-dose and faster CT acquisition without changing the scanning geometry. Although recent X-ray/CT Gaussian methods align rendering with radiative attenuation, their Gaussian growth still follows the error- or gradient-driven densification inherited from visible-light 3DGS, which over-allocates primitives to high-contrast anatomical boundaries and leaves attenuation-bearing interiors underrepresented. We propose \spags, an \tracefull\ framework that treats sparse-view CT as a capacity-allocation problem and redesigns Gaussian evolution through path-anchored seeding, boundary redundancy recovery, and position-dependent density modulation, instantiated as \sps, \gap, and \adm. Progressive ablation shows that \sps\ improves the 2-view initialization regime, while \gap\ provides the largest observed PSNR2D gain by reclaiming redundant boundary Gaussians. On a unified benchmark spanning five organs and 2/3/4 input views against six representative baselines, \spags\ achieves the highest average PSNR2D at every sparsity level, improving over \rtwo\ by $+0.11/+0.39/+0.07$\,dB and over X-Field$^*$ by $+0.87/+3.25/+2.79$\,dB; for methods with same-protocol SSIM2D logs, it reaches $0.797/0.904/0.924$ and ties the best 4-view SSIM2D at the third decimal place.
```

## 5. Why This Version Is Stronger

- It makes the paper's core claim explicit: sparse-view CT is treated as a **capacity-allocation problem**, not just another rendering modification.
- It avoids spending the abstract on three separate module definitions while still preserving `SPS -> GAP -> ADM`.
- It adds ablation evidence without overstating incomplete intermediate SSIM2D logs.
- It converts the final sentence from cautious wording into checkable evidence.
- It matches the strongest reference-paper habit: the final sentence contains concrete benchmark scope and metric gains.

## 6. Replacement Notes

Before replacing the current abstract in `main.tex`, re-check:

- `assets/tables/tab_experiment_comparison.tex`
  - `\spags` average PSNR2D: `21.44 / 28.22 / 29.20`
  - `\rtwo` average PSNR2D: `21.33 / 27.83 / 29.13`
  - Gain over `\rtwo`: `+0.11 / +0.39 / +0.07` dB
  - Gain over `X-Field$^*$`: `+0.87 / +3.25 / +2.79` dB

- `assets/tables/tab_experiment_comparison_ssim.tex`
  - `\spags` SSIM2D: `0.797 / 0.904 / 0.924`
  - `\rtwo` SSIM2D: `0.794 / 0.903 / 0.924`
  - Therefore: lead at 2v and 3v, tie at 4v to the third decimal place.

- `assets/tables/tab_experiment_component.tex`
  - `\sps` raises 2-view PSNR2D from `21.27` to `21.44`.
  - `\gap` raises 3-view PSNR2D from `28.01` to `28.22`, the largest observed intermediate PSNR2D increment.
  - Intermediate SSIM2D values remain pending, so do not claim module-level SSIM2D improvements.

If the abstract is applied to `main.tex`, run:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```
