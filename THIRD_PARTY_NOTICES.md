# Third-party notices for TikZ v1

The root AGPL-3.0 license is not a blanket license for the engine package. All
upstream copyrights and license choices remain with the respective authors.

| Component | Distribution / notice |
| --- | --- |
| Neomix JNI wrapper and packaging changes | AGPL-3.0; source snapshot and root LICENSE supplied |
| Tectonic 0.17.0 | MIT for Tectonic-specific code; upstream engines have their original terms in source headers |
| ICU 78.3 (libicuuc / libicudata) | Unicode License V3 and additional data notices; see ICU-78.3.txt and ICU source archive |
| Graphite2 1.3.15 | SIL's multi-license terms; full LICENSE and COPYING and upstream source supplied |
| FreeType integration | FreeType Project License; FTL notice supplied, see source headers for contributors |
| libpng integration | libpng license; full notice supplied |
| HarfBuzz-related integration | Upstream notice supplied; Rust-side dependencies are listed separately |
| Noto Sans SC Regular 2.004 | Copyright 2014-2021 Adobe; SIL Open Font License 1.1. The installed name droidsans.ttf is a compatibility filename, not Droid Sans |
| LaTeX2e 2026-06-01 and required packages | LPPL 1.3c or later; full LaTeX base/required source distribution and legal notice supplied |
| PGF/TikZ 3.1.12 | LPPL / GPL terms specified by upstream; full notices and source supplied |
| PGFPlots 1.18.3 | GPL-3.0-or-later; full license and source supplied |
| tikz-cd 1.0 | LPPL 1.3 or later; full source distribution supplied |
| preview-latex 13.2 | Included with AUCTeX; full AUCTeX source, preview.dtx and COPYING supplied |
| Latin Modern fonts | GUST Font License, derived from LPPL; upstream distribution and notice supplied |
| Computer Modern / AMS fonts | Individual font/source terms in the AMSFonts distribution; upstream distribution supplied |

The source archive contains the exact runtime TeX bundle, preserving file headers,
plus the full upstream source distributions described above. Source distributions
may include documentation/tests that are not part of the installed engine.

`sources/rust-dependencies.csv` lists all 382 registry packages from the wrapper's
Cargo.lock, including optional/platform-specific dependencies that may not be linked
into the Android binary. Their original source `.crate` archives accompany the
release and were verified against the lockfile checksums. Extracted license files
are in `licenses/rust/`; additional file-level notices remain in the source archives.

MuPDF, AndroidSVG and libc++ are not shipped in this engine ZIP. They remain app
components and are covered by the app distribution's own notices.

No runtime files have been stripped of copyright headers. ICU SONAME strings are
normalized by the supplied packaging script to the Android filenames used by the
application. The Noto font is not renamed internally or modified by this step.
