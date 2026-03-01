#!/usr/bin/env python3
"""
Convierte todos los .md del curso a un unico HTML autocontenido.
No requiere dependencias externas (solo Python 3 estandar).
Mermaid.js y highlight.js se cargan desde CDN.
"""

import os
import re
import sys
import shutil
import html
import time
import hashlib
from pathlib import Path

COURSE_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = COURSE_ROOT / "dist"
OUTPUT_FILE = OUTPUT_DIR / "curso-stack-my-architecture-android.html"
OUTPUT_INDEX_FILE = OUTPUT_DIR / "index.html"
ASSETS_SRC_DIR = COURSE_ROOT / "assets"
ASSETS_DIST_DIR = OUTPUT_DIR / "assets"
VERCEL_CONFIG_SRC = COURSE_ROOT / "vercel.json"

# Orden de los archivos (segun README)
FILE_ORDER = [
    "00-informe/INFORME-CURSO.md",
    "00-informe/AUDITORIA-EQUIVALENCIA-IOS-ANDROID.md",
    "00-informe/PLAN-REFUERZO-CURSO-ANDROID.md",
    "00-informe/MEJORAS-POR-MODULO-Y-EVIDENCIAS.md",
    "00-nivel-cero/00-introduccion.md",
    "00-nivel-cero/00-setup.md",
    "00-nivel-cero/01-que-es-software.md",
    "00-nivel-cero/02-logica-basica.md",
    "00-nivel-cero/03-primer-kotlin.md",
    "00-nivel-cero/04-variables-y-tipos.md",
    "00-nivel-cero/05-condicionales-y-bucles.md",
    "00-nivel-cero/06-funciones.md",
    "00-nivel-cero/07-errores-frecuentes.md",
    "00-nivel-cero/08-android-studio-desde-cero.md",
    "00-nivel-cero/09-primera-app-compose.md",
    "00-nivel-cero/10-inputs-y-validacion.md",
    "00-nivel-cero/11-navegacion-simple.md",
    "00-nivel-cero/12-proyecto-rutina-diaria.md",
    "00-nivel-cero/entregables-nivel-cero.md",
    "01-junior/00-introduccion.md",
    "01-junior/00-setup-junior.md",
    "01-junior/01-arquitectura-android-recomendada.md",
    "01-junior/02-feature-base-practica.md",
    "01-junior/03-navegacion-moderna-navigation-compose.md",
    "01-junior/04-hilt-integracion-inicial.md",
    "01-junior/05-room-offline-first.md",
    "01-junior/06-datastore-estado-ligero.md",
    "01-junior/07-workmanager-tareas-persistentes.md",
    "01-junior/08-compose-ui-testing.md",
    "01-junior/09-pruebas-unitarias-viewmodel-repositorio.md",
    "01-junior/entregables-nivel-junior.md",
    "02-midlevel/00-introduccion.md",
    "02-midlevel/01-red-robusta-retrofit-okhttp.md",
    "02-midlevel/02-offline-first-sincronizacion.md",
    "02-midlevel/03-consistencia-y-resolucion-de-conflictos.md",
    "02-midlevel/04-observabilidad-y-diagnostico.md",
    "02-midlevel/05-pruebas-de-integracion-offline-sync.md",
    "02-midlevel/06-quality-gates-ci-offline-sync.md",
    "02-midlevel/07-performance-ci-macrobenchmark-baselineprofiles.md",
    "02-midlevel/08-observabilidad-produccion-metricas-alertas.md",
    "02-midlevel/09-decisiones-evolutivas-con-metricas.md",
    "02-midlevel/10-gobernanza-dependencias-entre-features.md",
    "02-midlevel/11-versionado-contratos-internos.md",
    "02-midlevel/12-evolucion-navegacion-y-deeplinks-compatibles.md",
    "02-midlevel/entregables-nivel-midlevel.md",
    "03-senior/00-introduccion.md",
    "03-senior/01-release-strategy-y-rollback-seguro.md",
    "03-senior/02-incident-response-y-runbooks-operativos.md",
    "03-senior/03-slos-error-budgets-priorizacion-fiabilidad.md",
    "03-senior/04-tablero-operativo-fiabilidad-y-alertas-accionables.md",
    "03-senior/05-gobernanza-tecnica-de-sprint-fiabilidad-vs-roadmap.md",
    "03-senior/06-simulacion-sprint-bajo-presion-roadmap-y-fiabilidad.md",
    "03-senior/07-cierre-del-bloque-senior-y-transicion-a-maestria.md",
    "04-maestria/00-introduccion.md",
    "04-maestria/01-contratos-evolutivos-entre-dominios.md",
    "04-maestria/02-bounded-contexts-y-ownership-tecnico.md",
    "04-maestria/03-mapa-de-dependencias-y-acoplamiento-circular.md",
    "04-maestria/04-migraciones-transversales-sin-bloqueo.md",
    "04-maestria/05-coordinacion-release-rollback-y-comunicacion-tecnica.md",
    "04-maestria/06-evolucion-multi-equipo-y-gobernanza-trimestral.md",
    "04-maestria/07-defensa-tecnica-del-proyecto-android.md",
    "04-maestria/08-cierre-proyecto-final-y-publicacion-play-store.md",
    "04-maestria/09-rubrica-final-y-entrevista-tecnica-android.md",
    "04-maestria/10-plan-de-90-dias-despues-del-curso.md",
    "04-maestria/11-epilogo-profesional-y-siguientes-retos.md",
    "04-maestria/12-casos-reales-y-antipatrones-de-equipos-android.md",
    "04-maestria/13-operacion-largo-plazo-y-deuda-tecnica.md",
    "04-maestria/14-primer-ano-en-equipo-android-real.md",
    "04-maestria/15-mapa-de-carrera-android-de-junior-a-senior.md",
    "04-maestria/16-cierre-definitivo-del-recorrido-android.md",
    "05-proyecto-final/00-brief.md",
    "05-proyecto-final/00-brief-ruralgo-fieldops.md",
    "05-proyecto-final/01-rubrica-empleabilidad.md",
    "05-proyecto-final/02-evidencias-obligatorias.md",
    "05-proyecto-final/03-operacion-senior.md",
    "05-proyecto-final/04-gobernanza-maestria.md",
    "anexos/glosario.md",
    "anexos/guia-publicacion-playstore-real.md",
    "anexos/preguntas-entrevista-android.md",
    "anexos/proyecto-final-android.md",
]


MERMAID_ARROW_LEGEND_KEYWORDS = (
    "module",
    "modulo",
    "feature",
    "context",
    "bounded",
    "boundary",
    "dependency",
    "dependenc",
    "protocol",
    "interface",
    "inherit",
    "extension",
    "router",
    "coordinator",
    "viewmodel",
    "repository",
    "adapter",
    "domain",
    "application",
    "infrastructure",
    "wiring",
    "usecase",
    "actor",
    "aggregate",
    "service",
)


def mermaid_needs_arrow_legend(raw_code_content: str, file_path: str) -> bool:
    source = f"{file_path}\n{raw_code_content}".lower()
    relation_tokens = ("-->", "-.->", "==>", "--o", "<|--", "--|>", "..|>", "..>", "o--", "*--")
    has_relations = any(token in raw_code_content for token in relation_tokens)
    if not has_relations:
        return False
    return any(keyword in source for keyword in MERMAID_ARROW_LEGEND_KEYWORDS)


def normalize_mermaid_source(raw_code_content: str) -> str:
    normalized = raw_code_content
    lines = [line.strip() for line in raw_code_content.splitlines() if line.strip()]
    if not lines:
        return normalized
    is_flowchart = lines[0].startswith("flowchart") or lines[0].startswith("graph")
    is_state_diagram = lines[0].startswith("stateDiagram")
    if is_flowchart:
        normalized = re.sub(r"\.\.\>\|", "-.->|", normalized)
        normalized = re.sub(r"\.\.\>", "-.->", normalized)
        normalized = normalized.replace("-.o", "-.->")
    if is_state_diagram:
        normalized = re.sub(r"-\.\->", "-->", normalized)
    return normalized


def _clean_mermaid_label(raw_label: str) -> str:
    label = raw_label.strip()
    if len(label) >= 2 and ((label[0] == '"' and label[-1] == '"') or (label[0] == "'" and label[-1] == "'")):
        label = label[1:-1]
    label = label.replace("<br/>", "\n").replace("<br>", "\n").replace("\\n", "\n")
    label = re.sub(r"\s*\n\s*", "\n", label)
    return label.strip()


def _extract_mermaid_label(raw_code_content: str, node_id: str, default: str) -> str:
    pattern = rf"^\s*{re.escape(node_id)}\s*\[(.+?)\]\s*$"
    match = re.search(pattern, raw_code_content, flags=re.MULTILINE)
    if not match:
        return default
    parsed = _clean_mermaid_label(match.group(1))
    return parsed if parsed else default


def _extract_mermaid_subgraph_title(raw_code_content: str, subgraph_id: str, default: str) -> str:
    pattern = rf"subgraph\s+{re.escape(subgraph_id)}\s*\[(.+?)\]"
    match = re.search(pattern, raw_code_content)
    if not match:
        return default
    parsed = _clean_mermaid_label(match.group(1))
    return parsed if parsed else default


def _split_svg_lines(label: str, max_chars: int = 20) -> list[str]:
    lines = []
    for raw_line in label.split("\n"):
        normalized = re.sub(r"\s+", " ", raw_line).strip()
        if not normalized:
            continue
        words = normalized.split(" ")
        current = ""
        for word in words:
            candidate = word if not current else f"{current} {word}"
            if len(candidate) <= max_chars:
                current = candidate
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
    return lines if lines else [label.strip() or "-"]


def _svg_text(x: float, y: float, label: str, css_class: str, max_chars: int = 20) -> str:
    lines = _split_svg_lines(label, max_chars=max_chars)
    base_y = y - (len(lines) - 1) * 8
    tspans = []
    for index, line in enumerate(lines):
        dy = "0" if index == 0 else "1.3em"
        tspans.append(f'<tspan x="{x}" dy="{dy}">{html.escape(line)}</tspan>')
    return f'<text x="{x}" y="{base_y}" class="{css_class}" text-anchor="middle">{"".join(tspans)}</text>'


def is_layered_architecture_mermaid(raw_code_content: str) -> bool:
    normalized = raw_code_content.lower()
    required_tokens = (
        "flowchart",
        "subgraph core",
        "subgraph app",
        "subgraph ui",
        "subgraph infra",
        "vm --> uc",
        "uc --> ent",
        "uc ==> port",
        "boot -.->",
        "port --o",
    )
    return all(token in normalized for token in required_tokens)


def render_mermaid_arrow_legend() -> str:
    return (
        '<div class="sma-mermaid-legend" role="note" aria-label="Leyenda de flechas para diagramas de arquitectura">'
        '<p class="sma-mermaid-legend-title">Leyenda de flechas</p>'
        '<div class="sma-mermaid-legend-grid">'
        '<span class="sma-mermaid-legend-item">'
        '<svg class="sma-legend-arrow direct-closed" viewBox="0 0 40 12" aria-hidden="true">'
        '<line x1="2" y1="6" x2="30" y2="6"></line><polygon points="30,2 38,6 30,10"></polygon>'
        "</svg>Dependencia directa (runtime)</span>"
        '<span class="sma-mermaid-legend-item">'
        '<svg class="sma-legend-arrow dashed-closed" viewBox="0 0 40 12" aria-hidden="true">'
        '<line x1="2" y1="6" x2="30" y2="6"></line><polygon points="30,2 38,6 30,10"></polygon>'
        "</svg>Wiring / configuracion</span>"
        '<span class="sma-mermaid-legend-item">'
        '<svg class="sma-legend-arrow contract-open" viewBox="0 0 40 12" aria-hidden="true">'
        '<line x1="2" y1="6" x2="30" y2="6"></line><polyline points="30,2 38,6 30,10"></polyline>'
        "</svg>Contrato / abstraccion</span>"
        '<span class="sma-mermaid-legend-item">'
        '<svg class="sma-legend-arrow solid-open" viewBox="0 0 40 12" aria-hidden="true">'
        '<line x1="2" y1="6" x2="30" y2="6"></line><polyline points="30,2 38,6 30,10"></polyline>'
        "</svg>Salida / propagacion</span>"
        "</div>"
        "</div>\n"
    )


def render_layered_architecture_svg(raw_code_content: str) -> str:
    titles = {
        "CORE": _extract_mermaid_subgraph_title(raw_code_content, "CORE", "Core / Domain"),
        "APP": _extract_mermaid_subgraph_title(raw_code_content, "APP", "Application"),
        "UI": _extract_mermaid_subgraph_title(raw_code_content, "UI", "Interface"),
        "INFRA": _extract_mermaid_subgraph_title(raw_code_content, "INFRA", "Infrastructure"),
    }

    labels = {
        "VM": _extract_mermaid_label(raw_code_content, "VM", "ViewModel"),
        "VIEW": _extract_mermaid_label(raw_code_content, "VIEW", "View"),
        "ENT": _extract_mermaid_label(raw_code_content, "ENT", "Entity"),
        "POL": _extract_mermaid_label(raw_code_content, "POL", "Policy"),
        "BOOT": _extract_mermaid_label(raw_code_content, "BOOT", "Composition Root"),
        "UC": _extract_mermaid_label(raw_code_content, "UC", "UseCase"),
        "PORT": _extract_mermaid_label(raw_code_content, "PORT", "FeaturePort"),
        "API": _extract_mermaid_label(raw_code_content, "API", "API Client"),
        "STORE": _extract_mermaid_label(raw_code_content, "STORE", "Persistence Adapter"),
    }

    layer_boxes = {
        "UI": (100, 80, 300, 240),
        "CORE": (100, 350, 300, 220),
        "APP": (420, 520, 380, 190),
        "INFRA": (830, 80, 350, 630),
    }
    nodes = {
        "VM": (145, 140, 170, 58, "UI"),
        "VIEW": (165, 235, 130, 58, "UI"),
        "ENT": (170, 395, 130, 58, "CORE"),
        "POL": (175, 480, 120, 58, "CORE"),
        "BOOT": (470, 550, 280, 54, "APP"),
        "UC": (470, 625, 120, 58, "APP"),
        "PORT": (620, 625, 170, 58, "APP"),
        "API": (900, 220, 200, 70, "INFRA"),
        "STORE": (880, 520, 240, 74, "INFRA"),
    }

    node_markup = []
    for node_id, (x, y, width, height, layer_id) in nodes.items():
        node_markup.append(
            f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="8" class="sma-arch-node sma-arch-node-{layer_id.lower()}"></rect>'
        )
        node_markup.append(_svg_text(x + width / 2, y + height / 2 + 5, labels[node_id], "sma-arch-node-label", max_chars=22))

    layer_markup = []
    for layer_id, (x, y, width, height) in layer_boxes.items():
        layer_markup.append(
            f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="16" class="sma-arch-layer sma-arch-layer-{layer_id.lower()}"></rect>'
        )
        layer_markup.append(_svg_text(x + width / 2, y + 26, titles[layer_id], "sma-arch-layer-label", max_chars=28))

    marker_seed = hashlib.md5(raw_code_content.encode("utf-8")).hexdigest()[:10]
    marker_direct = f"sma-head-direct-{marker_seed}"
    marker_wiring = f"sma-head-wiring-{marker_seed}"
    marker_contract = f"sma-head-contract-{marker_seed}"
    marker_open = f"sma-head-open-{marker_seed}"

    legend_html = render_mermaid_arrow_legend()
    return (
        '<div class="sma-mermaid-block sma-architecture-block">\n'
        f"{legend_html}"
        '<div class="sma-architecture-svg-wrap" role="img" aria-label="Diagrama de arquitectura por capas del curso">'
        '<svg class="sma-architecture-svg" viewBox="0 0 1280 780" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">'
        "<defs>"
        f'<marker id="{marker_direct}" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto" markerUnits="strokeWidth">'
        '<path d="M0,0 L10,5 L0,10 z" class="sma-arch-head-direct"></path></marker>'
        f'<marker id="{marker_wiring}" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto" markerUnits="strokeWidth">'
        '<path d="M0,0 L10,5 L0,10 z" class="sma-arch-head-wiring"></path></marker>'
        f'<marker id="{marker_contract}" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto" markerUnits="strokeWidth">'
        '<path d="M0,0 L10,5 L0,10 z" class="sma-arch-head-contract"></path></marker>'
        f'<marker id="{marker_open}" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto" markerUnits="strokeWidth">'
        '<path d="M0,0 L10,5 L0,10" class="sma-arch-head-open"></path></marker>'
        "</defs>"
        '<rect x="8" y="8" width="1264" height="764" rx="20" class="sma-arch-board"></rect>'
        f'{"".join(layer_markup)}'
        f'{"".join(node_markup)}'
        f'<path d="M315 169 C380 250 410 470 470 654" class="sma-arch-edge sma-arch-edge-direct" marker-end="url(#{marker_direct})"></path>'
        f'<path d="M470 654 C400 620 300 540 235 424" class="sma-arch-edge sma-arch-edge-direct" marker-end="url(#{marker_direct})"></path>'
        f'<path d="M590 654 L620 654" class="sma-arch-edge sma-arch-edge-contract" marker-end="url(#{marker_contract})"></path>'
        f'<path d="M610 604 L705 625" class="sma-arch-edge sma-arch-edge-wiring" marker-end="url(#{marker_wiring})"></path>'
        f'<path d="M750 577 C810 510 850 360 900 255" class="sma-arch-edge sma-arch-edge-wiring" marker-end="url(#{marker_wiring})"></path>'
        f'<path d="M750 594 L880 557" class="sma-arch-edge sma-arch-edge-wiring" marker-end="url(#{marker_wiring})"></path>'
        f'<path d="M790 654 C860 600 890 410 900 255" class="sma-arch-edge sma-arch-edge-open" marker-end="url(#{marker_open})"></path>'
        f'<path d="M790 654 L880 557" class="sma-arch-edge sma-arch-edge-open" marker-end="url(#{marker_open})"></path>'
        f'<path d="M470 654 C400 520 345 330 315 169" class="sma-arch-edge sma-arch-edge-open" marker-end="url(#{marker_open})"></path>'
        "</svg>"
        "</div>\n"
        "</div>\n"
    )


def render_mermaid_block(raw_code_content: str, file_path: str) -> str:
    normalized_code_content = normalize_mermaid_source(raw_code_content)
    if is_layered_architecture_mermaid(normalized_code_content):
        return render_layered_architecture_svg(normalized_code_content)
    escaped_mermaid_code = html.escape(normalized_code_content)
    legend_html = ""
    if mermaid_needs_arrow_legend(normalized_code_content, file_path):
        legend_html = render_mermaid_arrow_legend()
    return f'<div class="sma-mermaid-block">\n{legend_html}<pre class="mermaid">{escaped_mermaid_code}</pre>\n</div>\n'


def md_to_html(md_text, file_id, file_path):
    """Convierte markdown a HTML basico con soporte para Mermaid."""
    html = ""
    lines = md_text.split("\n")
    i = 0
    in_code = False
    in_list = False
    in_table = False
    code_lang = ""
    code_buffer = []
    table_buffer = []

    while i < len(lines):
        line = lines[i]

        # Code blocks
        if line.strip().startswith("```") and not in_code:
            if in_list:
                html += "</ul>\n"
                in_list = False
            code_lang = line.strip()[3:].strip()
            in_code = True
            code_buffer = []
            i += 1
            continue

        if line.strip().startswith("```") and in_code:
            raw_code_content = "\n".join(code_buffer)
            if code_lang.lower() == "mermaid":
                html += render_mermaid_block(raw_code_content, file_path)
            else:
                code_content = (
                    raw_code_content.replace("&", "&amp;")
                    .replace("<", "&lt;")
                    .replace(">", "&gt;")
                )
                if code_lang:
                    html += f'<pre><code class="language-{code_lang}">{code_content}</code></pre>\n'
                else:
                    html += f"<pre><code>{code_content}</code></pre>\n"
            in_code = False
            code_lang = ""
            i += 1
            continue

        if in_code:
            code_buffer.append(line)
            i += 1
            continue

        # Tables
        if "|" in line and line.strip().startswith("|"):
            if not in_table:
                if in_list:
                    html += "</ul>\n"
                    in_list = False
                in_table = True
                table_buffer = []
            table_buffer.append(line)
            i += 1
            continue
        elif in_table:
            html += render_table(table_buffer)
            in_table = False
            table_buffer = []
            # Don't increment, process current line

        # Headers
        header_match = re.match(r"^(#{1,6})\s+(.+)$", line)
        if header_match:
            if in_list:
                html += "</ul>\n"
                in_list = False
            level = len(header_match.group(1))
            text = inline_format(header_match.group(2))
            anchor = re.sub(r"[^a-z0-9]+", "-", text.lower().strip())
            anchor = f"{file_id}-{anchor}"
            html += f'<h{level} id="{anchor}">{text}</h{level}>\n'
            i += 1
            continue

        # Horizontal rule
        if re.match(r"^---+\s*$", line):
            if in_list:
                html += "</ul>\n"
                in_list = False
            html += "<hr>\n"
            i += 1
            continue

        # List items
        if re.match(r"^\s*[-*]\s+", line):
            if not in_list:
                html += "<ul>\n"
                in_list = True
            content = re.sub(r"^\s*[-*]\s+", "", line)
            # Handle checkbox
            content = content.replace("[ ]", "&#9744;").replace("[x]", "&#9745;")
            html += f"  <li>{inline_format(content)}</li>\n"
            i += 1
            continue

        # Numbered list
        if re.match(r"^\s*\d+[.)]\s+", line):
            if not in_list:
                html += "<ol>\n"
                in_list = True
            content = re.sub(r"^\s*\d+[.)]\s+", "", line)
            html += f"  <li>{inline_format(content)}</li>\n"
            i += 1
            continue

        # Close list if we hit non-list content
        if in_list and line.strip():
            if html.rstrip().endswith("</ol>") or "<ol>" in html[-200:]:
                html += "</ol>\n"
            else:
                html += "</ul>\n"
            in_list = False

        # Empty lines
        if not line.strip():
            i += 1
            continue

        # Paragraphs
        html += f"<p>{inline_format(line)}</p>\n"
        i += 1

    if in_list:
        html += "</ul>\n"
    if in_table:
        html += render_table(table_buffer)

    return html


def render_table(rows):
    """Renderiza una tabla markdown a HTML."""
    if len(rows) < 2:
        return ""
    html = '<table>\n<thead>\n<tr>\n'
    headers = [c.strip() for c in rows[0].strip().strip("|").split("|")]
    for h in headers:
        html += f"  <th>{inline_format(h)}</th>\n"
    html += "</tr>\n</thead>\n<tbody>\n"

    for row in rows[2:]:  # Skip header separator
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        html += "<tr>\n"
        for c in cells:
            html += f"  <td>{inline_format(c)}</td>\n"
        html += "</tr>\n"

    html += "</tbody>\n</table>\n"
    return html


def inline_format(text):
    """Aplica formato inline: bold, italic, code, links."""
    # Inline code (before other formatting to avoid conflicts)
    text = re.sub(r"`([^`]+)`", lambda m: "<code>" + m.group(1).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;") + "</code>", text)
    # Bold + italic
    text = re.sub(r"\*\*\*(.+?)\*\*\*", r"<strong><em>\1</em></strong>", text)
    # Bold
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    # Italic
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    # Links
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    # Images
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r'<img alt="\1" src="\2">', text)
    return text


def build_nav(files_content):
    """Construye la barra de navegacion con anchors."""
    nav = (
        '<nav id="sidebar">\n'
        '<div class="sidebar-top">\n'
        '<h2>Indice</h2>\n'
        '<div class="sidebar-search-wrap">\n'
        '  <input id="sidebar-search" type="search" placeholder="Buscar leccion..." '
        'aria-label="Buscar leccion en el curso" autocomplete="off">\n'
        '  <div id="sidebar-search-count" aria-live="polite"></div>\n'
        '</div>\n'
        '</div>\n'
        '<ul>\n'
    )

    sections = {
        "00-informe": "Informe fundacional",
        "00-nivel-cero": "Nivel Cero: Fundamentos",
        "01-junior": "Nivel Junior",
        "02-midlevel": "Nivel Midlevel",
        "03-senior": "Nivel Senior",
        "04-maestria": "Nivel Maestria",
        "05-proyecto-final": "Proyecto Final",
        "anexos": "Anexos",
    }

    current_section = ""
    for filepath, content in files_content:
        section_key = filepath.split("/")[0]
        section_name = sections.get(section_key, section_key)

        if section_name != current_section:
            if current_section:
                nav += "</ul></li>\n"
            current_section = section_name
            nav += f'<li class="nav-section"><strong>{section_name}</strong>\n<ul>\n'

        # Extract first h1 or filename
        h1_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        title = h1_match.group(1) if h1_match else Path(filepath).stem
        file_id = filepath.replace("/", "-").replace(".md", "")
        nav += f'  <li><a class="doc-nav-link" data-lesson-path="{filepath}" href="#{file_id}">{title}</a></li>\n'

    nav += "</ul></li>\n</ul>\n</nav>\n"
    return nav


def build_html():
    """Construye el HTML completo."""
    files_content = []
    for rel_path in FILE_ORDER:
        full_path = COURSE_ROOT / rel_path
        if full_path.exists():
            content = full_path.read_text(encoding="utf-8")
            files_content.append((rel_path, content))
        else:
            print(f"  [SKIP] {rel_path} (no encontrado)")

    print(f"  Procesando {len(files_content)} archivos...")

    nav = build_nav(files_content)

    version_sources = [
        "study-ux.js",
        "study-ux.css",
        "course-switcher.js",
        "course-switcher.css",
        "theme-controls.js",
        "assistant-panel.js",
        "assistant-panel.css",
        "assistant-bridge.js",
    ]
    version_marks = [
        int((ASSETS_SRC_DIR / name).stat().st_mtime)
        for name in version_sources
        if (ASSETS_SRC_DIR / name).exists()
    ]
    asset_version = str(max(version_marks + [int(time.time())]))

    body_html = ""
    for filepath, content in files_content:
        file_id = filepath.replace("/", "-").replace(".md", "")
        body_html += f'<section id="{file_id}" class="lesson" data-topic-id="{file_id}" data-lesson-path="{filepath}">\n'
        body_html += f'<div class="lesson-path">{filepath}</div>\n'
        body_html += md_to_html(content, file_id, filepath)
        body_html += "</section>\n"

    html_template = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="darkreader-lock">
<meta name="course-id" content="stack-my-architecture-android">
<title>Stack: My Architecture Android</title>
<link rel="stylesheet" href="assets/study-ux.css?v=__ASSET_VERSION__">
<link rel="stylesheet" href="assets/course-switcher.css?v=__ASSET_VERSION__">
<link rel="stylesheet" href="assets/assistant-panel.css?v=__ASSET_VERSION__">
<script defer src="assets/study-ux.js?v=__ASSET_VERSION__"></script>
<script defer src="assets/course-switcher.js?v=__ASSET_VERSION__"></script>
<script defer src="assets/theme-controls.js?v=__ASSET_VERSION__"></script>
<script defer src="assets/assistant-panel.js?v=__ASSET_VERSION__"></script>
<script defer src="assets/assistant-bridge.js?v=__ASSET_VERSION__"></script>

<!-- Google Fonts - Inter -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;450;500;600;700&display=swap" rel="stylesheet">

<!-- Mermaid.js para diagramas -->
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>

<!-- Highlight.js para syntax highlighting -->
<link id="hljs-theme" rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/monokai.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/kotlin.min.js"></script>

<style>
/* ============================================
   SISTEMA DE DISEÑO: Stack My Architecture iOS
   ============================================ */

:root {{
    /* ============================================
       VISUAL STYLES: enterprise, bold, paper
       ============================================ */
    --visual-style: 'enterprise';
}}

/* ============================================
   STYLE: ENTERPRISE (Default)
   Profesional, limpio, corporativo
   ============================================ */
[data-style="enterprise"] {{
    /* Paleta de colores */
    --bg: #ffffff;
    --bg-elevated: #fafbfc;
    --bg-surface: #f6f8fa;
    
    --text: #1a1a2e;
    --text-secondary: #4a4a5a;
    --text-muted: #6a6a7a;
    
    --accent: #2563eb;
    --accent-light: #3b82f6;
    --accent-dark: #1d4ed8;
    --accent-soft: rgba(37, 99, 235, 0.1);
    
    --success: #10b981;
    --success-soft: rgba(16, 185, 129, 0.1);
    --warning: #f59e0b;
    --warning-soft: rgba(245, 158, 11, 0.1);
    --danger: #ef4444;
    --danger-soft: rgba(239, 68, 68, 0.1);
    --info: #06b6d4;
    --info-soft: rgba(6, 182, 212, 0.1);
    
    --sidebar-bg: #f8fafc;
    --code-bg: #f1f5f9;
    --border: #e2e8f0;
    --border-light: #f1f5f9;
    
    --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
    --shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
    --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.1);
    
    --font-weight-body: 500;
    --font-weight-heading: 700;
    --heading-letter-spacing: -0.02em;
    --border-radius: 8px;
}}

/* ============================================
   STYLE: ENTERPRISE - Dark Mode overrides
   Profesional, azul corporativo
   ============================================ */
[data-theme="dark"][data-style="enterprise"] {{
    --bg: #0c1821;
    --bg-elevated: #152a3d;
    --bg-surface: #1e3a5f;
    
    --text: #e8f4ff;
    --text-secondary: #a8c5e0;
    --text-muted: #6b8fb0;
    
    --accent: #60a5fa;
    --accent-light: #93c5fd;
    --accent-dark: #3b82f6;
    --accent-soft: rgba(96, 165, 250, 0.15);
    
    --sidebar-bg: #0f2335;
    --code-bg: #152a3d;
    --border: #2a4a6d;
    --border-light: #1e3a5f;
}}

/* ============================================
   STYLE: BOLD
   Alto contraste, impactante, moderno
   ============================================ */
[data-style="bold"] {{
    --bg: #0a0a0f;
    --bg-elevated: #141419;
    --bg-surface: #1e1e24;
    
    --text: #ffffff;
    --text-secondary: #d0d0e0;
    --text-muted: #a0a0b0;
    
    --accent: #ff6b35;
    --accent-light: #ff8c5a;
    --accent-dark: #e55a2b;
    --accent-soft: rgba(255, 107, 53, 0.15);
    
    --success: #00d9a3;
    --success-soft: rgba(0, 217, 163, 0.15);
    --warning: #ffc107;
    --warning-soft: rgba(255, 193, 7, 0.15);
    --danger: #ff4757;
    --danger-soft: rgba(255, 71, 87, 0.15);
    --info: #00d4ff;
    --info-soft: rgba(0, 212, 255, 0.15);
    
    --sidebar-bg: #0f0f14;
    --code-bg: #1a1a22;
    --border: #3a3a45;
    --border-light: #2a2a35;
    
    --shadow-sm: 0 1px 2px rgba(0,0,0,0.3);
    --shadow: 0 4px 6px -1px rgba(0,0,0,0.4);
    --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.5);
    
    --font-weight-body: 500;
    --font-weight-heading: 800;
    --heading-letter-spacing: -0.03em;
    --border-radius: 12px;
}}

/* ============================================
   STYLE: BOLD - Dark Mode overrides
   Alto contraste, manteniendo la identidad naranja
   ============================================ */
[data-theme="dark"][data-style="bold"] {{
    --bg: #0a0a0f;
    --bg-elevated: #141419;
    --bg-surface: #1e1e24;
    
    --text: #ffffff;
    --text-secondary: #d0d0e0;
    --text-muted: #a0a0b0;
    
    --accent: #ff6b35;
    --accent-light: #ff8c5a;
    --accent-dark: #e55a2b;
    --accent-soft: rgba(255, 107, 53, 0.15);
    
    --sidebar-bg: #0f0f14;
    --code-bg: #1a1a22;
    --border: #3a3a45;
    --border-light: #2a2a35;
}}

/* ============================================
   STYLE: PAPER
   Cálido, orgánico, académico
   ============================================ */
[data-style="paper"] {{
    --bg: #fdfbf7;
    --bg-elevated: #f5f1e8;
    --bg-surface: #f0ebe0;
    
    --text: #2c241b;
    --text-secondary: #5a5045;
    --text-muted: #8a8075;
    
    --accent: #8b4513;
    --accent-light: #a0522d;
    --accent-dark: #654321;
    --accent-soft: rgba(139, 69, 19, 0.08);
    
    --success: #2e7d32;
    --success-soft: rgba(46, 125, 50, 0.1);
    --warning: #ed6c02;
    --warning-soft: rgba(237, 108, 2, 0.1);
    --danger: #c62828;
    --danger-soft: rgba(198, 40, 40, 0.1);
    --info: #1565c0;
    --info-soft: rgba(21, 101, 192, 0.1);
    
    --sidebar-bg: #f7f3ec;
    --code-bg: #f5f0e6;
    --border: #e0d5c5;
    --border-light: #ebe5d8;
    
    --shadow-sm: 0 1px 3px rgba(44, 36, 27, 0.08);
    --shadow: 0 4px 8px rgba(44, 36, 27, 0.12);
    --shadow-lg: 0 8px 16px rgba(44, 36, 27, 0.15);
    
    --font-weight-body: 400;
    --font-weight-heading: 600;
    --heading-letter-spacing: -0.01em;
    --border-radius: 4px;
}}

/* ============================================
   STYLE: PAPER - Dark Mode overrides
   Marrón cálido, estilo parchment
   ============================================ */
[data-theme="dark"][data-style="paper"] {{
    --bg: #2d2419;
    --bg-elevated: #3d3124;
    --bg-surface: #4a3d2e;
    
    --text: #f5e6d3;
    --text-secondary: #d4c4b0;
    --text-muted: #a89080;
    
    --accent: #c4956a;
    --accent-light: #d4a87a;
    --accent-dark: #a87b5a;
    --accent-soft: rgba(196, 149, 106, 0.15);
    
    --sidebar-bg: #3d3124;
    --code-bg: #4a3d2e;
    --border: #5a4d3e;
    --border-light: #4a3d2e;
}}

/* ============================================
   COMMON VARIABLES (No cambian entre estilos)
   ============================================ */
:root {{
    --sidebar-width: 300px;
    
    /* Tipografía */
    --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    --font-mono: 'SF Mono', 'Fira Code', 'JetBrains Mono', Menlo, Consolas, monospace;
    
    /* Espaciado */
    --space-xs: 0.25rem;
    --space-sm: 0.5rem;
    --space-md: 1rem;
    --space-lg: 1.5rem;
    --space-xl: 2rem;
    --space-2xl: 3rem;
    --space-3xl: 4rem;
    
    /* Radios */
    --radius-sm: calc(var(--border-radius) / 2);
    --radius-md: var(--border-radius);
    --radius-lg: calc(var(--border-radius) * 1.5);
    --radius-xl: calc(var(--border-radius) * 2);
}}

* {{ margin: 0; padding: 0; box-sizing: border-box; }}

html {{ scroll-behavior: smooth; }}

body {{
    font-family: var(--font-sans);
    color: var(--text);
    background: var(--bg);
    line-height: 1.75;
    font-size: 16px;
    font-weight: var(--font-weight-body);
    display: flex;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}}

/* ============================================
   SIDEBAR NAVEGACIÓN
   ============================================ */
#sidebar {{
    position: fixed;
    top: 0;
    left: 0;
    width: var(--sidebar-width);
    height: 100vh;
    overflow-y: auto;
    background: var(--sidebar-bg);
    border-right: 1px solid var(--border);
    padding: calc(var(--space-lg) + 8px) var(--space-md) var(--space-lg);
    font-size: 0.875rem;
    z-index: 100;
    scrollbar-width: thin;
}}

#sidebar::-webkit-scrollbar {{
    width: 6px;
}}

#sidebar::-webkit-scrollbar-thumb {{
    background: var(--border);
    border-radius: 3px;
}}

#sidebar .sidebar-top {{
    position: sticky;
    top: 0;
    z-index: 5;
    background: var(--sidebar-bg);
    padding-top: var(--space-xs);
}}

#sidebar h2 {{
    font-size: 1rem;
    font-weight: 700;
    margin-bottom: var(--space-sm);
    color: var(--accent);
    letter-spacing: -0.02em;
    text-transform: uppercase;
    font-size: 0.75rem;
    line-height: 1.25;
}}

#sidebar .sidebar-search-wrap {{
    margin-bottom: var(--space-sm);
    padding-bottom: var(--space-sm);
    border-bottom: 1px solid color-mix(in srgb, var(--border) 80%, transparent);
}}

#sidebar #sidebar-search {{
    width: 100%;
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    background: var(--bg-surface);
    color: var(--text);
    padding: 8px 10px;
    font-size: 0.82rem;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}}

#sidebar #sidebar-search::placeholder {{
    color: var(--text-muted);
}}

#sidebar #sidebar-search:focus {{
    outline: none;
    border-color: var(--accent);
    box-shadow: 0 0 0 3px color-mix(in srgb, var(--accent) 20%, transparent);
}}

#sidebar #sidebar-search-count {{
    margin-top: 6px;
    min-height: 1em;
    font-size: 0.72rem;
    color: var(--text-muted);
}}

#sidebar ul {{ list-style: none; padding-left: 0; }}

#sidebar li {{ margin-bottom: 2px; }}

#sidebar li.nav-section {{
    margin-top: var(--space-lg);
}}

#sidebar li.nav-section:first-child {{
    margin-top: 0;
}}

#sidebar li.nav-section > strong {{
    color: var(--text);
    font-size: 0.8rem;
    font-weight: 600;
    display: block;
    padding: var(--space-xs) var(--space-sm);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--text-muted);
}}

#sidebar a {{
    color: var(--text-secondary);
    text-decoration: none;
    display: block;
    padding: 6px 10px;
    border-radius: var(--radius-sm);
    transition: all 0.2s ease;
    font-weight: 450;
    border-left: 2px solid transparent;
}}

#sidebar a:hover {{
    background: var(--accent-soft);
    color: var(--accent);
    border-left-color: var(--accent);
}}

/* ============================================
   CONTENIDO PRINCIPAL
   ============================================ */
#content {{
    margin-left: var(--sidebar-width);
    max-width: none;
    padding: var(--space-3xl) var(--space-2xl);
    width: calc(100% - var(--sidebar-width));
    min-height: 100vh;
}}

/* ============================================
   TIPOGRAFÍA - JERARQUÍA VISUAL
   ============================================ */
h1, h2, h3, h4 {{
    font-weight: var(--font-weight-heading);
    line-height: 1.3;
    letter-spacing: var(--heading-letter-spacing);
    color: var(--text);
}}

h1 {{
    font-size: 2.5em;
    margin: 0 0 var(--space-lg);
    padding-bottom: var(--space-md);
    border-bottom: 3px solid var(--accent);
    color: var(--text);
    position: relative;
}}

h1::after {{
    content: '';
    position: absolute;
    bottom: -3px;
    left: 0;
    width: 120px;
    height: 3px;
    background: linear-gradient(90deg, var(--accent) 0%, var(--accent-light) 100%);
}}

h2 {{
    font-size: 1.75em;
    margin: var(--space-2xl) 0 var(--space-md);
    color: var(--text);
    display: flex;
    align-items: center;
    gap: var(--space-sm);
}}

h2::before {{
    content: '';
    width: 4px;
    height: 28px;
    background: var(--accent);
    border-radius: 2px;
}}

h3 {{
    font-size: 1.375em;
    margin: var(--space-xl) 0 var(--space-sm);
    color: var(--text);
    font-weight: 600;
}}

h4 {{
    font-size: 1.125em;
    margin: var(--space-lg) 0 var(--space-sm);
    color: var(--text-secondary);
    font-weight: 600;
}}

p {{
    margin: var(--space-md) 0;
    color: var(--text-secondary);
    line-height: 1.8;
    font-weight: var(--font-weight-body);
}}

/* ============================================
   SEPARADORES Y SECCIONES
   ============================================ */
hr {{
    border: none;
    border-top: 1px solid var(--border);
    margin: var(--space-2xl) 0;
}}

hr.lesson-separator {{
    border: none;
    height: 4px;
    background: linear-gradient(90deg, var(--accent) 0%, var(--info) 50%, var(--success) 100%);
    margin: var(--space-3xl) 0;
    border-radius: 2px;
}}

/* ============================================
   BLOQUES DE CÓDIGO
   ============================================ */
pre {{
    background: transparent;
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    padding: 0;
    overflow-x: auto;
    margin: var(--space-lg) 0;
    font-size: 0.875em;
    line-height: 1.6;
    box-shadow: var(--shadow-sm);
}}

pre > code {{
    display: block;
    padding: var(--space-lg);
    border-radius: var(--radius-md);
    background: var(--code-bg);
}}

pre.sma-code-enhanced {{
    position: relative;
}}

pre.sma-code-enhanced > code {{
    padding-top: calc(var(--space-lg) + 1.2rem);
}}

.sma-code-tools {{
    position: absolute;
    top: 8px;
    right: 10px;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    z-index: 2;
}}

.sma-code-lang {{
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    color: var(--text-muted);
    background: var(--bg-elevated);
    border: 1px solid var(--border);
    border-radius: 999px;
    padding: 2px 8px;
}}

.sma-code-copy-btn {{
    font-size: 0.72rem;
    font-weight: 600;
    color: var(--text);
    background: var(--bg-elevated);
    border: 1px solid var(--border);
    border-radius: 999px;
    padding: 3px 10px;
    cursor: pointer;
}}

.sma-code-copy-btn:hover {{
    border-color: var(--accent);
    color: var(--accent);
}}

code {{
    font-family: var(--font-mono);
    font-size: 0.9em;
}}

p code, li code, td code {{
    background: var(--code-bg);
    padding: 3px 8px;
    border-radius: var(--radius-sm);
    border: 1px solid var(--border-light);
    color: var(--danger);
    font-weight: 500;
    font-size: 0.85em;
}}

/* Mermaid diagrams */
:root {{
    --mermaid-bg: #ffffff;
    --mermaid-text: #0f172a;
    --mermaid-node-bg: #f8fafc;
    --mermaid-node-border: #1d4ed8;
    --mermaid-line: #1e40af;
    --mermaid-label-bg: #eef2ff;
    --mermaid-legend-direct: #cbd5e1;
    --mermaid-legend-dashed-closed: #cbd5e1;
    --mermaid-legend-contract: #cbd5e1;
    --mermaid-legend-solid-open: #cbd5e1;
}}

.sma-mermaid-block {{
    margin: var(--space-lg) 0;
}}

.sma-mermaid-legend {{
    border: 1px solid var(--border);
    background: var(--bg-surface);
    border-radius: var(--radius-md);
    padding: 10px 12px;
    margin: 0 0 var(--space-sm);
}}

.sma-mermaid-legend-title {{
    margin: 0 0 8px;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.03em;
    text-transform: uppercase;
    color: var(--text-secondary);
}}

.sma-mermaid-legend-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 6px 12px;
}}

.sma-mermaid-legend-item {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-size: 0.78rem;
    color: var(--text);
}}

.sma-legend-arrow {{
    width: 40px;
    height: 12px;
    flex: 0 0 40px;
    overflow: visible;
}}

.sma-legend-arrow line,
.sma-legend-arrow polygon,
.sma-legend-arrow polyline {{
    stroke: currentColor;
    fill: currentColor;
    stroke-width: 2.3;
    stroke-linecap: round;
    stroke-linejoin: round;
}}

.sma-legend-arrow polyline {{
    fill: none;
}}

.sma-legend-arrow.dashed-closed line,
.sma-legend-arrow.contract-open line {{
    stroke-dasharray: 6 4;
}}

.sma-legend-arrow.direct-closed {{ color: var(--mermaid-legend-direct); }}
.sma-legend-arrow.dashed-closed {{ color: var(--mermaid-legend-dashed-closed); }}
.sma-legend-arrow.contract-open {{ color: var(--mermaid-legend-contract); }}
.sma-legend-arrow.solid-open {{ color: var(--mermaid-legend-solid-open); }}

.sma-architecture-block {{
    margin-top: var(--space-md);
}}

.sma-architecture-svg-wrap {{
    border: 1px solid rgba(148, 163, 184, 0.4);
    border-radius: 16px;
    background: radial-gradient(circle at 20% 10%, rgba(59, 130, 246, 0.16), transparent 42%), #0b1220;
    box-shadow: inset 0 1px 0 rgba(148, 163, 184, 0.25), 0 8px 28px rgba(15, 23, 42, 0.32);
    padding: 12px;
    overflow-x: auto;
}}

.sma-architecture-svg {{
    display: block;
    width: 100%;
    min-width: 960px;
    height: auto;
}}

.sma-arch-board {{
    fill: rgba(15, 23, 42, 0.92);
    stroke: rgba(148, 163, 184, 0.32);
    stroke-width: 1.5;
}}

.sma-arch-layer {{
    stroke-width: 2;
}}

.sma-arch-layer-ui {{
    fill: rgba(29, 78, 216, 0.14);
    stroke: #7dd3fc;
}}

.sma-arch-layer-core {{
    fill: rgba(14, 116, 144, 0.12);
    stroke: #67e8f9;
}}

.sma-arch-layer-app {{
    fill: rgba(124, 58, 237, 0.1);
    stroke: #f97316;
}}

.sma-arch-layer-infra {{
    fill: rgba(168, 85, 247, 0.11);
    stroke: #d8b4fe;
}}

.sma-arch-layer-label {{
    font-family: var(--font-display);
    font-size: 21px;
    font-weight: 700;
    letter-spacing: 0.02em;
    fill: #e2e8f0;
}}

.sma-arch-node {{
    stroke-width: 1.6;
    fill: rgba(15, 23, 42, 0.72);
}}

.sma-arch-node-ui {{ stroke: #93c5fd; }}
.sma-arch-node-core {{ stroke: #67e8f9; }}
.sma-arch-node-app {{ stroke: #fb923c; }}
.sma-arch-node-infra {{ stroke: #d8b4fe; }}

.sma-arch-node-label {{
    font-family: var(--font-body);
    font-size: 17px;
    font-weight: 600;
    fill: #f8fafc;
}}

.sma-arch-edge {{
    fill: none;
    stroke-width: 3;
    stroke-linecap: round;
}}

.sma-arch-edge-direct {{ stroke: #f472b6; }}

.sma-arch-edge-wiring {{
    stroke: #94a3b8;
    stroke-dasharray: 8 6;
}}

.sma-arch-edge-contract {{
    stroke: #60a5fa;
    stroke-dasharray: 8 5;
}}

.sma-arch-edge-open {{ stroke: #86efac; }}

.sma-arch-head-direct {{ fill: #f472b6; stroke: #f472b6; }}
.sma-arch-head-wiring {{ fill: #94a3b8; stroke: #94a3b8; }}
.sma-arch-head-contract {{ fill: #60a5fa; stroke: #60a5fa; }}
.sma-arch-head-open {{
    fill: none;
    stroke: #86efac;
    stroke-width: 2.2;
    stroke-linecap: round;
    stroke-linejoin: round;
}}

pre.mermaid {{
    background: var(--mermaid-bg);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    text-align: center;
    padding: var(--space-xl);
    box-shadow: var(--shadow);
    overflow-x: auto;
    overflow-y: hidden;
}}

pre.mermaid svg {{
    max-width: 100%;
    height: auto;
}}

html[data-theme][data-style] pre.mermaid .label,
html[data-theme][data-style] pre.mermaid .nodeLabel,
html[data-theme][data-style] pre.mermaid .edgeLabel,
html[data-theme][data-style] pre.mermaid .cluster-label,
html[data-theme][data-style] pre.mermaid text,
html[data-theme][data-style] pre.mermaid tspan {{
    fill: var(--mermaid-text) !important;
    color: var(--mermaid-text) !important;
}}

html[data-theme][data-style] pre.mermaid .node rect,
html[data-theme][data-style] pre.mermaid .node polygon,
html[data-theme][data-style] pre.mermaid .node circle,
html[data-theme][data-style] pre.mermaid .node ellipse,
html[data-theme][data-style] pre.mermaid .cluster rect,
html[data-theme][data-style] pre.mermaid .actor,
html[data-theme][data-style] pre.mermaid .labelBox {{
    fill: var(--mermaid-node-bg) !important;
    stroke: var(--mermaid-node-border) !important;
}}

html[data-theme][data-style] pre.mermaid .edgePath .path,
html[data-theme][data-style] pre.mermaid path.relation,
html[data-theme][data-style] pre.mermaid line {{
    stroke: var(--mermaid-line) !important;
}}

html[data-theme][data-style] pre.mermaid .messageLine0,
html[data-theme][data-style] pre.mermaid .messageLine1,
html[data-theme][data-style] pre.mermaid .messageLine2 {{
    stroke: var(--mermaid-line) !important;
    stroke-width: 2px !important;
    opacity: 1 !important;
}}

html[data-theme][data-style] pre.mermaid .arrowheadPath,
html[data-theme][data-style] pre.mermaid marker path,
html[data-theme][data-style] pre.mermaid marker polygon,
html[data-theme][data-style] pre.mermaid marker polyline {{
    fill: var(--mermaid-line) !important;
    stroke: var(--mermaid-line) !important;
    opacity: 1 !important;
}}

html[data-theme][data-style] pre.mermaid .edgeLabel rect,
html[data-theme][data-style] pre.mermaid .labelBkg {{
    fill: var(--mermaid-label-bg) !important;
    opacity: 1 !important;
}}

/* ============================================
   TABLAS MODERNAS
   ============================================ */
table {{
    border-collapse: separate;
    border-spacing: 0;
    width: 100%;
    margin: var(--space-lg) 0;
    font-size: 0.9rem;
    border-radius: var(--radius-md);
    overflow: hidden;
    box-shadow: var(--shadow-sm);
}}

th, td {{
    border-bottom: 1px solid var(--border);
    padding: 12px 16px;
    text-align: left;
}}

th {{
    background: linear-gradient(180deg, var(--bg-surface) 0%, var(--sidebar-bg) 100%);
    font-weight: 600;
    color: var(--text);
    text-transform: uppercase;
    font-size: 0.75rem;
    letter-spacing: 0.05em;
    border-bottom: 2px solid var(--accent);
}}

tr:hover {{
    background: var(--bg-surface);
}}

tr:last-child td {{
    border-bottom: none;
}}

/* ============================================
   LISTAS
   ============================================ */
ul, ol {{
    margin: var(--space-md) 0;
    padding-left: var(--space-xl);
}}

li {{
    margin: var(--space-sm) 0;
    color: var(--text-secondary);
}}

li strong {{
    color: var(--text);
    font-weight: 600;
}}

/* Checkboxes en listas */
li:has(> input[type="checkbox"]) {{
    list-style: none;
    margin-left: -1.5em;
}}

/* ============================================
   LINKS
   ============================================ */
a {{
    color: var(--accent);
    text-decoration: none;
    font-weight: 500;
    transition: color 0.15s ease;
}}

a:hover {{
    color: var(--accent-dark);
    text-decoration: underline;
    text-underline-offset: 2px;
}}

/* ============================================
   BADGE DE RUTA DE LECCIÓN
   ============================================ */
.lesson-path {{
    font-size: 0.75rem;
    color: var(--text-muted);
    background: var(--bg-surface);
    padding: 6px 14px;
    border-radius: 999px;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    margin-bottom: var(--space-md);
    font-family: var(--font-mono);
    border: 1px solid var(--border-light);
    font-weight: 500;
}}

.lesson-path::before {{
    content: '📁';
    font-size: 0.9em;
}}

/* ============================================
   CALLOUTS / BLOQUES DESTACADOS
   ============================================ */
/* Notas con > blockquote */
blockquote {{
    margin: var(--space-lg) 0;
    padding: var(--space-md) var(--space-lg);
    border-left: 4px solid var(--accent);
    background: var(--accent-soft);
    border-radius: 0 var(--radius-md) var(--radius-md) 0;
    font-style: italic;
    color: var(--text-secondary);
}}

blockquote p {{
    margin: 0;
}}

/* ============================================
   Responsive - MOBILE FIRST
   ============================================ */
@media (max-width: 1024px) {{
    :root {{ --sidebar-width: 260px; }}
    #content {{ padding: 32px 28px; }}
}}

@media (max-width: 768px) {{
    :root {{ --sidebar-width: 0; }}
    #sidebar {{ display: none; }}
    #content {{ 
        margin-left: 0; 
        padding: 20px 16px;
        width: 100%;
    }}
    h1 {{ font-size: 1.6em; margin: 32px 0 12px; }}
    h2 {{ font-size: 1.3em; margin: 28px 0 10px; }}
    h3 {{ font-size: 1.1em; margin: 20px 0 8px; }}
    h4 {{ font-size: 1em; margin: 16px 0 6px; }}
    pre {{ padding: 0; font-size: 0.82em; }}
    th, td {{ padding: 8px 10px; font-size: 0.85rem; }}
}}

@media (max-width: 480px) {{
    #content {{ padding: 16px 12px; }}
    h1 {{ font-size: 1.4em; }}
    h2 {{ font-size: 1.2em; }}
    pre {{ padding: 0; font-size: 0.78em; overflow-x: scroll; }}
}}

/* Dark theme */
[data-theme="dark"] {{
    --bg: #0d1117;
    --text: #c9d1d9;
    --sidebar-bg: #161b22;
    --accent: #58a6ff;
    --code-bg: #161b22;
    --border: #30363d;
}}

[data-theme="dark"] h1 {{ color: #f0f6fc; }}
[data-theme="dark"] h2 {{ color: #c9d1d9; }}
[data-theme="dark"] h3 {{ color: #c9d1d9; }}
[data-theme="dark"] th {{ background: #21262d; }}
[data-theme="dark"] tr:nth-child(even) {{ background: #161b22; }}
[data-theme="dark"] li strong {{ color: #f0f6fc; }}
[data-theme="dark"] #sidebar a {{ color: #8b949e; }}
[data-theme="dark"] #sidebar a:hover {{ background: #21262d; color: var(--accent); }}
[data-theme="dark"] #sidebar li.nav-section > strong {{ color: #f0f6fc; }}
[data-theme="dark"] .lesson-path {{ color: #8b949e; }}

/* Back to top */
#back-to-top {{
    position: fixed;
    bottom: 24px;
    right: 24px;
    background: var(--accent);
    color: white;
    border: none;
    border-radius: 50%;
    width: 44px;
    height: 44px;
    font-size: 1.2rem;
    cursor: pointer;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    display: none;
    z-index: 200;
}}

/* Theme controls container */
#theme-controls {{
    position: fixed;
    top: 16px;
    right: 16px;
    z-index: 9999;
    display: flex;
    gap: 12px;
    align-items: center;
}}

#theme-controls button {{
    border-radius: 8px;
    padding: 10px 16px;
    font-size: 0.85rem;
    font-weight: 600;
    cursor: pointer;
    box-shadow: 0 2px 8px rgba(0,0,0,0.3);
    transition: all 0.2s ease;
    white-space: nowrap;
    border: 2px solid transparent;
}}

#theme-controls button:hover {{
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.4);
}}

/* Style cycle button - dynamic colors set by JS */
#style-cycle-btn {{
    background: #2563eb;
    color: white;
    border-color: #3b82f6;
}}

/* Code theme button */
#code-theme-cycle-btn {{
    background: var(--bg-elevated);
    color: var(--text);
    border-color: var(--border);
}}

/* Theme toggle button */
#theme-toggle {{
    background: var(--accent);
    color: white;
    border-color: var(--accent-light);
}}

/* Mobile responsive */
@media (max-width: 768px) {{
    #theme-controls {{
        top: 12px;
        right: 12px;
        gap: 8px;
    }}
    
    #theme-controls button {{
        padding: 8px 12px;
        font-size: 0.75rem;
    }}
}}

@media (max-width: 600px) {{
    #theme-controls {{
        flex-direction: column;
        align-items: flex-end;
        gap: 6px;
    }}
    
    #theme-controls button {{
        width: 120px;
        padding: 6px 10px;
        font-size: 0.7rem;
    }}
}}

/* Style selector dropdowns - ensure they inherit theme colors */
#style-selector select {{
    background-color: var(--bg-elevated) !important;
    color: var(--text) !important;
    border-color: var(--border) !important;
}}

#style-selector select option {{
    background-color: var(--bg-elevated);
    color: var(--text);
}}
#menu-toggle {{
    display: none;
    position: fixed;
    top: 12px;
    left: 12px;
    background: var(--sidebar-bg);
    color: var(--text);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 8px 12px;
    font-size: 1.1rem;
    cursor: pointer;
    z-index: 250;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}}

@media (max-width: 768px) {{
    #menu-toggle {{ display: block; }}
}}
</style>
</head>
<body>

<button id="menu-toggle" onclick="toggleSidebar()" title="Abrir menú">&#9776;</button>

<div id="study-ux-controls" class="study-ux-controls" aria-label="Controles de estudio">
    <button id="study-completion-toggle" type="button">✅ Marcar completado</button>
    <button id="study-zen-toggle" type="button">🧘 Enfoque</button>
    <span id="study-progress" class="study-progress">Progreso: 0/0 (0%)</span>
</div>

<div id="course-switcher" class="course-switcher" aria-label="Selector de cursos">
    <button id="course-switcher-toggle" type="button">&#9776; Cursos</button>
    <div id="course-switcher-menu" class="course-switcher-menu">
        <a id="course-switcher-home" href="#">Cursos</a>
        <a id="course-switcher-ios" href="#">Curso iOS</a>
        <a id="course-switcher-android" href="#">Curso Android</a>
        <a id="course-switcher-sdd" href="#">Curso IA + SDD</a>
    </div>
</div>

<div id="theme-controls">
    <button id="style-cycle-btn" onclick="cycleStyle()">Estilo: Enterprise</button>
    <button id="code-theme-cycle-btn" onclick="cycleCodeTheme()">Codigo: Monokai</button>
    <button id="theme-toggle" onclick="toggleTheme()" title="Cambiar tema claro/oscuro">Tema: Claro</button>
</div>

{nav}

<main id="content">
<section id="study-ux-index-actions" class="study-ux-index-actions" aria-label="Study UX index actions"></section>
{body_html}
</main>

<button id="back-to-top" onclick="window.scrollTo({{top:0, behavior:'smooth'}})">&#8593;</button>

<script>
// Theme management
function getPreferredTheme() {{
    const saved = localStorage.getItem('course-theme');
    if (saved) return saved;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
}}

function getPreferredStyle() {{
    return localStorage.getItem('course-style') || 'enterprise';
}}

function getPreferredCodeTheme() {{
    return localStorage.getItem('course-code-theme') || 'monokai';
}}

function applyStyle(style) {{
    document.documentElement.setAttribute('data-style', style);
    localStorage.setItem('course-style', style);
    
    const btn = document.getElementById('style-cycle-btn');
    if (btn) {{
        btn.textContent = 'Estilo: ' + style.charAt(0).toUpperCase() + style.slice(1);
        
        // Set button colors based on style
        const styleColors = {{
            'enterprise': {{ bg: '#2563eb', border: '#3b82f6', text: '#ffffff' }},
            'bold': {{ bg: '#ff6b35', border: '#ff8c5a', text: '#ffffff' }},
            'paper': {{ bg: '#c4956a', border: '#d4a87a', text: '#2d2419' }}
        }};
        
        const colors = styleColors[style] || styleColors['enterprise'];
        btn.style.backgroundColor = colors.bg;
        btn.style.borderColor = colors.border;
        btn.style.color = colors.text;
    }}
}}

function cycleStyle() {{
    const styles = ['enterprise', 'bold', 'paper'];
    const current = document.documentElement.getAttribute('data-style') || 'enterprise';
    const currentIndex = styles.indexOf(current);
    const nextIndex = (currentIndex + 1) % styles.length;
    const nextStyle = styles[nextIndex];
    applyStyle(nextStyle);
    renderMermaid();
}}

function applyCodeTheme(theme) {{
    localStorage.setItem('course-code-theme', theme);
    const btn = document.getElementById('code-theme-cycle-btn');
    if (btn) {{
        btn.textContent = 'Codigo: ' + theme.charAt(0).toUpperCase() + theme.slice(1).replace(/-/g, ' ');
    }}
    
    const hljsLink = document.getElementById('hljs-theme');
    const themeMap = {{
        'monokai': 'monokai.min.css',
        'github': 'github.min.css',
        'github-dark': 'github-dark.min.css',
        'atom-one-dark': 'atom-one-dark.min.css'
    }};
    hljsLink.href = `https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/${{themeMap[theme] || 'monokai.min.css'}}`;
    
    // Re-highlight all code blocks
    document.querySelectorAll('pre code').forEach(block => {{
        hljs.highlightElement(block);
    }});
    enhanceCodeBlocks();
}}

function detectSnippetLang(codeEl) {{
    const className = (codeEl.className || '').toLowerCase();
    if (className.includes('language-kotlin') || className.includes('language-kt')) return 'KT';
    if (className.includes('language-swift')) return 'Swift';
    if (className.includes('language-js') || className.includes('language-javascript')) return 'JS';
    if (className.includes('language-ts') || className.includes('language-typescript')) return 'TS';
    if (className.includes('language-json')) return 'JSON';
    if (className.includes('language-bash') || className.includes('language-shell')) return 'SH';
    if (className.includes('language-yaml') || className.includes('language-yml')) return 'YAML';
    if (className.includes('language-python') || className.includes('language-py')) return 'PY';
    if (className.includes('language-mermaid')) return 'Mermaid';
    if (className.includes('language-xml') || className.includes('language-html')) return 'XML';
    if (className.includes('language-sql')) return 'SQL';
    if (className.includes('language-markdown') || className.includes('language-md')) return 'MD';
    if (className.includes('language-gherkin') || className.includes('language-feature')) return 'Gherkin';

    const content = (codeEl.textContent || '').trim();
    if (!content) return 'TXT';

    if (
        content.startsWith('flowchart') ||
        content.startsWith('sequenceDiagram') ||
        content.startsWith('classDiagram') ||
        content.startsWith('stateDiagram') ||
        content.startsWith('erDiagram')
    ) return 'Mermaid';

    if (/^(\\$\\s*)?(gradlew|adb|emulator|kotlin|ktlint|detekt|git|npm|node|python3|bash|sh)\\b/m.test(content)) return 'SH';
    if (/^\\s*(package\\s+[a-zA-Z0-9_.]+|import\\s+[a-zA-Z0-9_.]+|data\\s+class\\s+\\w+|sealed\\s+(class|interface)\\s+\\w+|@Composable|class\\s+\\w+)/m.test(content)) return 'KT';
    if (/^\\s*(\\{{|\\[\\s*\\{{|\"[^\"]+\"\\s*:)/m.test(content)) return 'JSON';
    if (/^\\s*[a-zA-Z0-9_-]+\\s*:\\s*.+$/m.test(content) && !/;\\s*$/m.test(content)) return 'YAML';
    if (/^\\s*SELECT\\b|^\\s*INSERT\\b|^\\s*UPDATE\\b|^\\s*DELETE\\b|^\\s*CREATE\\s+TABLE\\b/im.test(content)) return 'SQL';
    if (/^\\s*<[^>]+>/m.test(content)) return 'XML';

    return 'TXT';
}}

function copyCodeToClipboard(text) {{
    if (navigator.clipboard && navigator.clipboard.writeText) {{
        return navigator.clipboard.writeText(text);
    }}
    return new Promise((resolve, reject) => {{
        try {{
            const ta = document.createElement('textarea');
            ta.value = text;
            ta.setAttribute('readonly', 'readonly');
            ta.style.position = 'fixed';
            ta.style.left = '-9999px';
            document.body.appendChild(ta);
            ta.select();
            const ok = document.execCommand('copy');
            document.body.removeChild(ta);
            if (ok) resolve();
            else reject(new Error('copy-failed'));
        }} catch (err) {{
            reject(err);
        }}
    }});
}}

function enhanceCodeBlocks() {{
    document.querySelectorAll('pre code').forEach(code => {{
        const pre = code.closest('pre');
        if (!pre || pre.classList.contains('mermaid')) return;
        if (pre.dataset.codeEnhanced === '1') return;
        pre.dataset.codeEnhanced = '1';
        pre.classList.add('sma-code-enhanced');

        const tools = document.createElement('div');
        tools.className = 'sma-code-tools';

        const lang = document.createElement('span');
        lang.className = 'sma-code-lang';
        lang.textContent = detectSnippetLang(code);

        const copyBtn = document.createElement('button');
        copyBtn.type = 'button';
        copyBtn.className = 'sma-code-copy-btn';
        copyBtn.textContent = 'Copiar';
        copyBtn.setAttribute('aria-label', `Copiar snippet ${lang.textContent}`);
        copyBtn.addEventListener('click', () => {{
            const originalText = copyBtn.textContent;
            copyCodeToClipboard(code.textContent || '')
                .then(() => {{
                    copyBtn.textContent = 'Copiado';
                    setTimeout(() => {{ copyBtn.textContent = originalText; }}, 1200);
                }})
                .catch(() => {{
                    copyBtn.textContent = 'Error';
                    setTimeout(() => {{ copyBtn.textContent = originalText; }}, 1200);
                }});
        }});

        tools.appendChild(lang);
        tools.appendChild(copyBtn);
        pre.appendChild(tools);
    }});
}}

function cycleCodeTheme() {{
    const themes = ['monokai', 'github', 'github-dark', 'atom-one-dark'];
    const current = localStorage.getItem('course-code-theme') || 'monokai';
    const currentIndex = themes.indexOf(current);
    const nextIndex = (currentIndex + 1) % themes.length;
    const nextTheme = themes[nextIndex];
    applyCodeTheme(nextTheme);
}}

function applyTheme(theme) {{
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('course-theme', theme);
    const btn = document.getElementById('theme-toggle');
    btn.textContent = theme === 'dark' ? 'Tema: Oscuro' : 'Tema: Claro';
    btn.title = theme === 'dark' ? 'Cambiar a tema claro' : 'Cambiar a tema oscuro';
    // Keep code theme as selected, don't override
}}

function toggleTheme() {{
    const current = document.documentElement.getAttribute('data-theme') || 'light';
    applyTheme(current === 'dark' ? 'light' : 'dark');
    renderMermaid();
}}

// Apply saved preferences immediately
applyStyle(getPreferredStyle());
applyCodeTheme(getPreferredCodeTheme());
applyTheme(getPreferredTheme());

function currentMermaidTheme() {{
    const theme = document.documentElement.getAttribute('data-theme') || 'light';
    return theme === 'dark' ? 'dark' : 'default';
}}

function renderMermaid() {{
    if (typeof mermaid === 'undefined') {{
        console.warn('Mermaid no cargado. Revisa conexión a internet/CDN.');
        return;
    }}

    document.querySelectorAll('pre.mermaid').forEach(function(el) {{
        if (!el.dataset.originalMermaid) {{
            el.dataset.originalMermaid = (el.textContent || '').trimEnd();
        }}
        if (el.dataset.originalMermaid) {{
            el.innerHTML = '';
            el.textContent = el.dataset.originalMermaid;
        }}
        el.removeAttribute('data-processed');
    }});

    mermaid.initialize({{
        startOnLoad: false,
        theme: currentMermaidTheme(),
        securityLevel: 'loose'
    }});

    mermaid.run({{ querySelector: 'pre.mermaid' }});
}}

// Init Mermaid
renderMermaid();

// Init Highlight.js
document.querySelectorAll('pre code').forEach(block => {{
    hljs.highlightElement(block);
}});
enhanceCodeBlocks();

// Back to top button
window.addEventListener('scroll', () => {{
    const btn = document.getElementById('back-to-top');
    btn.style.display = window.scrollY > 400 ? 'block' : 'none';
}});

// Active nav highlight
const sections = document.querySelectorAll('section.lesson');
const navLinks = document.querySelectorAll('#sidebar a');

const observer = new IntersectionObserver(entries => {{
    entries.forEach(entry => {{
        if (entry.isIntersecting) {{
            navLinks.forEach(link => link.style.fontWeight = 'normal');
            const active = document.querySelector(`#sidebar a[href="#${{entry.target.id}}"]`);
            if (active) active.style.fontWeight = '700';
        }}
    }});
}}, {{ rootMargin: '-20% 0px -70% 0px' }});

sections.forEach(s => observer.observe(s));

// Mobile sidebar toggle
function toggleSidebar() {{
    const sidebar = document.getElementById('sidebar');
    const current = sidebar.style.display;
    sidebar.style.display = current === 'block' ? 'none' : 'block';
}}

// Close sidebar when clicking a link on mobile
document.querySelectorAll('#sidebar a').forEach(link => {{
    link.addEventListener('click', () => {{
        if (window.innerWidth <= 768) {{
            document.getElementById('sidebar').style.display = 'none';
        }}
    }});
}});

// Sidebar search/filter
const sidebarSearchInput = document.getElementById('sidebar-search');
const sidebarSearchCount = document.getElementById('sidebar-search-count');

function normalizeSearchText(value) {{
    return (value || '')
        .toLowerCase()
        .normalize('NFD')
        .replace(/[\u0300-\u036f]/g, '');
}}

function applySidebarSearch() {{
    if (!sidebarSearchInput) return;
    const query = normalizeSearchText(sidebarSearchInput.value.trim());
    const sections = document.querySelectorAll('#sidebar li.nav-section');
    let visibleLessons = 0;

    sections.forEach(section => {{
        const sectionTitle = section.querySelector(':scope > strong');
        const sectionLabel = normalizeSearchText(sectionTitle ? sectionTitle.textContent : '');
        const links = section.querySelectorAll('a.doc-nav-link');
        let sectionHasVisible = false;

        links.forEach(link => {{
            const item = link.closest('li');
            if (!item) return;
            const lessonPath = normalizeSearchText(link.dataset.lessonPath || '');
            const lessonTitle = normalizeSearchText(link.textContent || '');
            const match = !query || lessonTitle.includes(query) || lessonPath.includes(query) || sectionLabel.includes(query);
            item.style.display = match ? '' : 'none';
            if (match) {{
                sectionHasVisible = true;
                visibleLessons += 1;
            }}
        }});

        section.style.display = sectionHasVisible ? '' : 'none';
    }});

    if (sidebarSearchCount) {{
        if (!query) {{
            sidebarSearchCount.textContent = '';
        }} else if (visibleLessons === 1) {{
            sidebarSearchCount.textContent = '1 resultado';
        }} else {{
            sidebarSearchCount.textContent = `${{visibleLessons}} resultados`;
        }}
    }}
}}

if (sidebarSearchInput) {{
    sidebarSearchInput.addEventListener('input', applySidebarSearch);
    sidebarSearchInput.addEventListener('keydown', event => {{
        if (event.key === 'Escape') {{
            sidebarSearchInput.value = '';
            applySidebarSearch();
            sidebarSearchInput.blur();
        }}
    }});
    applySidebarSearch();
}}
</script>

</body>
</html>"""

    # This template includes lots of CSS/JS braces. We keep the template as a
    # plain string, unescape doubled braces from previous formatting, then inject
    # dynamic sections explicitly.
    html = html_template.replace("{{", "{").replace("}}", "}")
    html = html.replace("__ASSET_VERSION__", asset_version)
    html = html.replace("{nav}", nav).replace("{body_html}", body_html)

    OUTPUT_DIR.mkdir(exist_ok=True)
    OUTPUT_FILE.write_text(html, encoding="utf-8")
    OUTPUT_INDEX_FILE.write_text(html, encoding="utf-8")

    ASSETS_DIST_DIR.mkdir(parents=True, exist_ok=True)
    for asset_name in [
        "study-ux.js",
        "study-ux.css",
        "course-switcher.js",
        "course-switcher.css",
        "theme-controls.js",
        "assistant-panel.js",
        "assistant-panel.css",
        "assistant-bridge.js",
    ]:
        src = ASSETS_SRC_DIR / asset_name
        if src.exists():
            shutil.copy2(src, ASSETS_DIST_DIR / asset_name)

    if VERCEL_CONFIG_SRC.exists():
        shutil.copy2(VERCEL_CONFIG_SRC, OUTPUT_DIR / "vercel.json")

    print(f"  HTML generado: {OUTPUT_FILE}")
    print(f"  HTML index generado: {OUTPUT_INDEX_FILE}")
    print(f"  Tamano: {OUTPUT_FILE.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    print("Construyendo HTML del curso...")
    build_html()
    print("Listo.")
