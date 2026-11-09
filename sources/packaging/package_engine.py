"""Build the pinned TikZ engine pack. No network access or publication.
Run from any directory: python tools/tikz-engine/package_engine.py
"""
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / 'build/tikz-engine/packages'
LIBS = ['libicudata78.so', 'libicuuc78.so', 'libgraphite2.so', 'libtex_poc.so']


def normalize_soname(data):
    # Android resolves DT_NEEDED by SONAME. Termux's versioned SONAMEs differ
    # from the APK-compatible filenames; fix the names in this distributed copy.
    data = bytearray(data)
    for old, new in [(b'libicudata.so.78', b'libicudata78.so'),
                     (b'libicuuc.so.78', b'libicuuc78.so')]:
        old += b'\0'
        new += b'\0'
        data = data.replace(old, new + b'\0' * (len(old) - len(new)))
    return bytes(data)


def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    files = {f'lib/{n}': normalize_soname((ROOT / 'app/src/main/jniLibs/arm64-v8a' / n).read_bytes()) for n in LIBS}
    for n in ['tectonic-bundle-v3.tikzbundle', 'droidsans.ttf']:
        files[f'tex/{n}'] = (ROOT / 'app/src/main/assets/tex' / n).read_bytes()
    pack = OUTPUT / 'tikz-engine-arm64-v8a-v1.zip'
    with zipfile.ZipFile(pack, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(name, (2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, data)
    digest = hashlib.sha256(pack.read_bytes()).hexdigest()
    manifest = dict(id='v1-' + digest[:16], abi='arm64-v8a', archive=pack.name,
                    sha256=digest, size=pack.stat().st_size,
                    files={n: dict(size=len(b), sha256=hashlib.sha256(b).hexdigest()) for n, b in sorted(files.items())})
    target = ROOT / 'app/src/main/assets/tikz-engine.json'
    target.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    print(pack)
    print(f'{manifest["size"]:,} bytes; sha256={digest}')


if __name__ == '__main__':
    main()
