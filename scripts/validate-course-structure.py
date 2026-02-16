#!/usr/bin/env python3
"""
Verifica existencia de carpetas base y archivos criticos del curso.
Solo stdlib Python 3.
Exit 0 si todo OK, exit 1 si falta algo critico.
"""

import sys
from pathlib import Path

COURSE_ROOT = Path(__file__).parent.parent

REQUIRED_DIRS = [
    "00-informe",
    "00-nivel-cero",
    "01-junior",
    "02-midlevel",
    "03-senior",
    "04-maestria",
    "05-proyecto-final",
    "anexos",
    "scripts",
]

REQUIRED_FILES = [
    "README.md",
    "00-informe/INFORME-CURSO.md",
    "00-informe/AUDITORIA-EQUIVALENCIA-IOS-ANDROID.md",
    "00-informe/PLAN-REFUERZO-CURSO-ANDROID.md",
    "00-informe/MEJORAS-POR-MODULO-Y-EVIDENCIAS.md",
    "scripts/build-html.py",
    "05-proyecto-final/00-brief-ruralgo-fieldops.md",
    "05-proyecto-final/01-rubrica-empleabilidad.md",
    "05-proyecto-final/02-evidencias-obligatorias.md",
]


def main():
    issues = []

    print("Verificando carpetas base...")
    for d in REQUIRED_DIRS:
        full = COURSE_ROOT / d
        if not full.is_dir():
            issues.append(f"  MISSING DIR:  {d}/")
            print(f"  ❌ {d}/")
        else:
            print(f"  ✅ {d}/")

    print("\nVerificando archivos criticos...")
    for f in REQUIRED_FILES:
        full = COURSE_ROOT / f
        if not full.is_file():
            issues.append(f"  MISSING FILE: {f}")
            print(f"  ❌ {f}")
        else:
            print(f"  ✅ {f}")

    print()
    if issues:
        print(f"❌ {len(issues)} elementos críticos faltantes (P0):")
        for i in issues:
            print(i)
        sys.exit(1)
    else:
        print("✅ Estructura del curso verificada.")
        sys.exit(0)


if __name__ == "__main__":
    main()
