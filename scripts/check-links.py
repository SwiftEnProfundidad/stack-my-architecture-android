#!/usr/bin/env python3
"""
Detecta links markdown rotos e imágenes faltantes en todos los .md del repo.
Solo stdlib Python 3.
Exit 0 si todo OK, exit 1 si hay links rotos.
"""

import re
import sys
from pathlib import Path

COURSE_ROOT = Path(__file__).parent.parent

IGNORED_PREFIXES = ("http://", "https://", "mailto:", "#", "tel:")


def find_md_files():
    return sorted(COURSE_ROOT.rglob("*.md"))


def check_file(md_path):
    content = md_path.read_text(encoding="utf-8", errors="replace")
    issues = []

    # Links: [text](path)
    for match in re.finditer(r"\[([^\]]*)\]\(([^)]+)\)", content):
        text, target = match.group(1), match.group(2)

        # Skip external URLs and anchors
        if any(target.startswith(p) for p in IGNORED_PREFIXES):
            continue

        # Strip anchor from target
        target_clean = target.split("#")[0]
        if not target_clean:
            continue

        # Resolve relative to the md file's directory
        resolved = (md_path.parent / target_clean).resolve()
        if not resolved.exists():
            line_num = content[: match.start()].count("\n") + 1
            issues.append((line_num, "LINK", target, text))

    # Images: ![alt](path)
    for match in re.finditer(r"!\[([^\]]*)\]\(([^)]+)\)", content):
        alt, src = match.group(1), match.group(2)

        if any(src.startswith(p) for p in IGNORED_PREFIXES):
            continue

        resolved = (md_path.parent / src).resolve()
        if not resolved.exists():
            line_num = content[: match.start()].count("\n") + 1
            issues.append((line_num, "IMAGE", src, alt))

    return issues


def main():
    md_files = find_md_files()
    print(f"Escaneando {len(md_files)} archivos .md...")

    total_issues = 0
    for md_path in md_files:
        rel = md_path.relative_to(COURSE_ROOT)
        issues = check_file(md_path)
        if issues:
            for line_num, kind, target, label in issues:
                print(f"  {rel}:{line_num}  [{kind}] {target}")
                total_issues += 1

    print()
    if total_issues:
        print(f"❌ {total_issues} links/imágenes rotos encontrados.")
        sys.exit(1)
    else:
        print("✅ Todos los links e imágenes verificados.")
        sys.exit(0)


if __name__ == "__main__":
    main()
