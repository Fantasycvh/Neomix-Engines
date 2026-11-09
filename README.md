# Neomix Engines

Optional native engine packages for Neomix. This repository hosts versioned
GitHub Release assets, pinned manifests, third-party notices and source snapshots.
It does not contain the Neomix app, user conversations, credentials or app data.

## TikZ v1

- Platform: Android arm64-v8a, API 26 or newer.
- Package: `tikz-engine-arm64-v8a-v1.zip` (38,245,878 bytes).
- Engine ID: `v1-3684708eb9e7eceb`.
- Compiler: native Tectonic 0.17.0 with ICU 78.3 and Graphite2 1.3.15.
- TeX data includes PGF/TikZ 3.1.12, PGFPlots 1.18.3 and tikz-cd 1.0.
- CJK font: Noto Sans SC Regular 2.004, stored as `droidsans.ttf` for compatibility.
- PDF/SVG display libraries and libc++ are supplied by the app, not this package.

Download: [tikz-v1 release](https://github.com/Fantasycvh/Neomix-Engines/releases/tag/tikz-v1)

Fixed app download URL:

```text
https://github.com/Fantasycvh/Neomix-Engines/releases/download/tikz-v1/tikz-engine-arm64-v8a-v1.zip
```

SHA-256:

```text
3684708eb9e7ecebcc71ff431097c2e7e5da40d299217b0d6fe4014a5e25244c
```

Use a Neomix build whose embedded manifest matches this engine ID. Install from
Display settings / TikZ engine, or import the ZIP locally. Installation is optional;
ordinary formulas continue to use BetterText, and cached diagram SVGs remain usable
without the compiler. Once installed, compilation works offline.

The app validates the archive and each extracted file against its embedded
manifest. A checksum downloaded beside a package is useful for manual verification,
but is not a substitute for the app's pinned trust anchor. Do not replace published
versioned assets; publish a new tag and app manifest when binaries change.

## Sources and licenses

See [third-party notices](THIRD_PARTY_NOTICES.md), [build notes](BUILDING.md),
and `releases/tikz-v1/manifest.json`. The release includes separate license and
source archives. Each third-party component retains its own license; the root
AGPL-3.0 license applies to Neomix-derived wrapper code and packaging changes,
not a relicensing of ICU, fonts, TeX packages or other upstream components.

The original native binaries and TeX data predate this distribution repository.
Source archives and build instructions are provided for inspection and rebuilding;
byte-for-byte reproduction of the original native build is not claimed.
