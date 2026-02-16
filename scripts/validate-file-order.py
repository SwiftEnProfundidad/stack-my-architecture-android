#!/usr/bin/env python3
"""
Valida que todo path en FILE_ORDER de build-html.py existe en disco.
Exit 0 si todo OK, exit 1 si falta alguno (P0).
Solo stdlib Python 3.
"""

import re
import sys
from pathlib import Path

COURSE_ROOT = Path(__file__).parent.parent
BUILD_SCRIPT = COURSE_ROOT / "scripts" / "build-html.py"


def extract_file_order():
    content = BUILD_SCRIPT.read_text(encoding="utf-8")
    match = re.search(r"FILE_ORDER\s*=\s*\[(.*?)\]", content, re.DOTALL)
    if not match:
        print("ERROR: No se encontró FILE_ORDER en build-html.py")
        sys.exit(1)
    raw = match.group(1)
    paths = re.findall(r'"([^"]+)"', raw)
    return paths


def main():
    paths = extract_file_order()
    print(f"FILE_ORDER: {len(paths)} entradas")

    missing = []
    for p in paths:
        full = COURSE_ROOT / p
        if not full.exists():
            missing.append(p)

    if missing:
        print(f"\n❌ {len(missing)} archivos NO encontrados (P0):\n")
        for m in missing:
            print(f"  MISSING: {m}")
        sys.exit(1)
    else:
        print("✅ Todos los archivos de FILE_ORDER existen.")
        sys.exit(0)


if __name__ == "__main__":
    main()
