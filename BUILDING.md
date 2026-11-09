# Build and packaging notes

The JNI interface is bound to `app.androidrik.rikkahub.tikz.TectonicNative`.
The application ID may differ without changing this Java namespace.

`sources/tex-poc` contains the local Rust JNI wrapper, dependency lock file and
Android build script. Source crates are included in the release source archive;
each `.crate` hash is checked against `Cargo.lock` before publication. The Tectonic
source archive also supplies the native engine sources and their notices.

Native rebuild prerequisites: Rust with the aarch64-linux-android target, Android
NDK r27c, pkg-config metadata and cross-compiled FreeType/libpng/Graphite2,
ICU 78.3, and the fontconfig stub used by this build. See the wrapper README.
The historical external native build environment is not a turn-key container.

The packaging script is a snapshot of the app integration's
`tools/tikz-engine/package_engine.py`. It expects the Neomix source layout:
`app/src/main/jniLibs/arm64-v8a/` for binaries and `app/src/main/assets/tex/` for data.
It is a repackager, not a compiler. It fixes the ICU SONAME strings in distributed
copies to match `libicudata78.so` / `libicuuc78.so`, without changing the source
binaries. Native sources otherwise have no new changes in this packaging step.

The ZIP uses fixed entry timestamps and includes only the four engine libraries,
TeX bundle and Noto font. Its pinned manifest records archive and per-file hashes.
Repacking with another Python/zlib version may yield different ZIP bytes, requiring
a new manifest even if the extracted files have the same hashes.

Release source archives contain the exact runtime TeX bundle as well as upstream
source distributions. Copyright/license headers in runtime files are preserved.
Upstream download URLs and source archive SHA-256 values are recorded in
`sources/upstream.json`; package content hashes are in the release manifest.

Verification performed before publication: synthetic-app arm64/Android 15 smoke
checks for missing engine, cache access without installation, corrupt ZIP rejection,
local import, isolated compilation of Chinese/math labels, SVG conversion and
preservation after a corrupt replacement. The UI process did not map libtex_poc.so.
