# Brand assets

`clockwork-symbol.png` is the standalone Clockwork symbol from the [Clockwork website](https://www.clockworkmedia.co.za/).

- Source: [original PNG](https://www.clockworkmedia.co.za/wp-content/uploads/2026/07/Logo-Animation-dark.png)
- Retrieved: 2026-10-20
- Modifications: none.
- The Clockwork brand asset is separate from the MIT licenses covering imported skills.

## Theme-aware SVGs

`clockwork-symbol-light.svg` and `clockwork-symbol-dark.svg` recreate the radial symbol as twelve rotated rectangles, using the source PNG as a visual reference. These are locally recreated vectors, not official upstream SVG files. The light-theme version uses the brand's dark color, `#07091B`; the dark-theme version uses white. Both have transparent backgrounds.

The README selects the variant with GitHub's supported `<picture>` and `prefers-color-scheme` markup. The light variant is the fallback. The original PNG is retained for reference.
