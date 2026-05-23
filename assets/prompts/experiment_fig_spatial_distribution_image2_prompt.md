Target file: assets/fig/experiment_fig_spatial_distribution.png
Size: 1800x500

A clean, professional scientific illustration for a medical imaging paper (white background, publication-quality academic style), showing how 3D Gaussian primitives evolve through four stages of an X-ray CT reconstruction algorithm called XRA-GS. The image is a wide horizontal panel (4:1 aspect ratio) divided into four equal vertical sections separated by thin light-gray dividing lines.

Each section shows a 3D point cloud view of small semi-transparent circular dots representing Gaussian primitives distributed around a roughly cylindrical anatomical region (resembling a cross-section of a human organ — smooth, elongated volume). The viewpoint is the same isometric 3D perspective in all four panels. All four panels have identical axis scales and camera angle to allow direct visual comparison.

PANEL (a) — labeled "(a) Uniform Init" at the bottom center, gray count label "~50K" below:
Neutral gray dots (#888888), uniformly and densely scattered throughout the entire volume with no spatial preference — filling boundary regions, interior, and exterior uniformly. Dense cloud with no organization.

PANEL (b) — labeled "(b) + SPS" at the bottom, purple count label "~42K" below:
Soft purple dots (#7B5CA6). The dots have shifted toward a central elongated region following the X-ray path direction. Still some scattered dots near the outer boundary but more weight concentrated toward the interior anatomical path. Slightly less chaotic than (a).

PANEL (c) — labeled "(c) + SPS + GAP" at the bottom, teal count label "~38K" below:
Teal dots (#3CA897). Noticeably fewer dots, with the outer boundary cluster clearly pruned. Dots are more compactly grouped around a central core structure aligned along the projection axis. The reduction in boundary density is visually obvious compared to (b).

PANEL (d) — labeled "(d) Full XRA-GS" at the bottom, warm orange count label "~35K" below:
Warm orange dots (#E07B39). The most compact, organized distribution — dots concentrated precisely along the interior attenuation path structure. Almost no peripheral scatter. Clean, focused spatial arrangement.

ABOVE ALL FOUR PANELS: a narrow horizontal strip (approximately 1/6 of total height) running the full width, showing a stylized 1D X-ray attenuation profile curve. The background of this strip uses a dark magma colormap gradient from left (low intensity, dark purple) to right (medium intensity, orange-yellow). The profile shows a smooth bell-shaped curve representing typical CT attenuation values along the projection axis. The curve color transitions from gray in panel (a) to purple in (b) to teal in (c) to orange in (d), matching each panel's dot color.

Panel label indicators (a)(b)(c)(d) appear in the upper-left corner of each main panel in 9pt bold sans-serif black text.

Style: Pure white background. Minimal, clean. No grid lines. No decorative borders. Dots are small (approximately 4pt radius), semi-transparent (50% opacity). The overall feel is like a figure from a CVPR or ICCV paper — precise, uncluttered, and immediately interpretable. Font: Helvetica or Arial, all text in black or matching panel color. No Chinese text. No emoji.
