#!/usr/bin/env python3
"""
standardize_readmes.py
Unifica y estandariza el menú superior y footer de navegación lineal
en todos los READMEs de casos de uso de CTS Academy RUP.
"""

import glob
import os
import re

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "RUP", "01-requisitos", "03-detalle-casos-uso")
)

HEADER_TEMPLATE = """<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

<sub>**Fase 01 Requisitos** › **Detalle de Caso de Uso** › `{cu_name}()`</sub>

</div>

"""

FOOTER_TEMPLATE = """
---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
"""

def standardize():
    pattern = os.path.join(BASE_DIR, "*", "README.md")
    files = sorted(glob.glob(pattern))
    print(f"Procesando {len(files)} casos de uso...")

    for path in files:
        cu_name = os.path.basename(os.path.dirname(path))
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # Encontrar '# Caso de Uso:'
        heading_match = re.search(r"(# Caso de Uso:[^\n]+)", content)
        if not heading_match:
            print(f"⚠️  No se encontró encabezado en {cu_name}")
            continue

        start_idx = heading_match.start()
        body = content[start_idx:]

        # Limpiar posible tabla obsoleta '> | [Inicio]...' justo debajo del título
        body_clean = re.sub(
            r"^(# Caso de Uso:[^\n]+\n+)(?:>\s*\|[^\n]+\n+>\s*\|[^\n]+\n+)?",
            r"\1\n",
            body,
        )

        # Limpiar pie de página previo si ya tuviera algún enlace similar
        body_clean = re.sub(r"\n+---\s*\n+<div align=[\"']?center[\"']?>\s*\n+\[⬅️[^\n]+\n+</div>\s*$", "", body_clean.strip())

        # Ensamblar nuevo contenido
        final_content = HEADER_TEMPLATE.format(cu_name=cu_name) + body_clean.strip() + FOOTER_TEMPLATE

        with open(path, "w", encoding="utf-8") as f:
            f.write(final_content)

        print(f"✓ Actualizado: {cu_name}")

    print("✨ Todos los README de casos de uso han sido estandarizados con navegación lineal.")

if __name__ == "__main__":
    standardize()
