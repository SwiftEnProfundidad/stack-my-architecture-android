#!/usr/bin/env python3
"""
Convierte el curso Android (Markdown) a un HTML único autocontenido.
Sin dependencias externas de Python.
"""

import re
from pathlib import Path

COURSE_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = COURSE_ROOT / "dist"
OUTPUT_FILE = OUTPUT_DIR / "curso-stack-my-architecture-android.html"

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


def inline_format(text: str) -> str:
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    return text


def render_table(rows):
    if len(rows) < 2:
        return ""
    html = "<table>\n<thead>\n<tr>\n"
    headers = [c.strip() for c in rows[0].strip().strip("|").split("|")]
    for h in headers:
        html += f"  <th>{inline_format(h)}</th>\n"
    html += "</tr>\n</thead>\n<tbody>\n"
    for row in rows[2:]:
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        html += "<tr>\n"
        for c in cells:
            html += f"  <td>{inline_format(c)}</td>\n"
        html += "</tr>\n"
    html += "</tbody>\n</table>\n"
    return html


def md_to_html(md_text, file_id):
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
            raw = "\n".join(code_buffer)
            if code_lang.lower() == "mermaid":
                html += f'<pre class="mermaid">{raw}</pre>\n'
            else:
                code = raw.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                cls = f' class="language-{code_lang}"' if code_lang else ""
                html += f"<pre><code{cls}>{code}</code></pre>\n"
            in_code = False
            code_lang = ""
            i += 1
            continue

        if in_code:
            code_buffer.append(line)
            i += 1
            continue

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

        header_match = re.match(r"^(#{1,6})\s+(.+)$", line)
        if header_match:
            if in_list:
                html += "</ul>\n"
                in_list = False
            level = len(header_match.group(1))
            text = inline_format(header_match.group(2))
            anchor = re.sub(r"[^a-z0-9]+", "-", re.sub("<[^>]+>", "", text).lower().strip())
            html += f'<h{level} id="{file_id}-{anchor}">{text}</h{level}>\n'
            i += 1
            continue

        if re.match(r"^---+\s*$", line):
            html += "<hr>\n"
            i += 1
            continue

        if re.match(r"^\s*[-*]\s+", line):
            if not in_list:
                html += "<ul>\n"
                in_list = True
            content = re.sub(r"^\s*[-*]\s+", "", line)
            content = content.replace("[ ]", "&#9744;").replace("[x]", "&#9745;")
            html += f"  <li>{inline_format(content)}</li>\n"
            i += 1
            continue

        if in_list and line.strip():
            html += "</ul>\n"
            in_list = False

        if not line.strip():
            i += 1
            continue

        html += f"<p>{inline_format(line)}</p>\n"
        i += 1

    if in_list:
        html += "</ul>\n"
    if in_table:
        html += render_table(table_buffer)
    return html


def build_index(entries):
    index = ["<ul class='toc'>"]
    for title, anchor in entries:
        index.append(f"<li><a href='#{anchor}'>{title}</a></li>")
    index.append("</ul>")
    return "\n".join(index)


def extract_title(md_text, fallback):
    for line in md_text.split("\n"):
        m = re.match(r"^#\s+(.+)$", line)
        if m:
            return m.group(1).strip()
    return fallback


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    sections = []
    toc_entries = []

    for idx, rel_path in enumerate(FILE_ORDER):
        file_path = COURSE_ROOT / rel_path
        if not file_path.exists():
            continue
        md_text = file_path.read_text(encoding="utf-8")
        file_id = f"s{idx:03d}"
        title = extract_title(md_text, rel_path)
        anchor = f"{file_id}-{re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')}"
        toc_entries.append((title, anchor))

        html_body = md_to_html(md_text, file_id)
        sections.append(
            f"<section><div class='file-meta'>{rel_path}</div>{html_body}</section>"
        )

    html_doc = f"""<!doctype html>
<html lang=\"es\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>Stack My Architecture Android</title>
  <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css\">
  <script src=\"https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js\"></script>
  <script src=\"https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js\"></script>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 0; background: #0b1220; color: #e5e7eb; }}
    .layout {{ display: grid; grid-template-columns: 320px 1fr; min-height: 100vh; }}
    nav {{ position: sticky; top: 0; height: 100vh; overflow: auto; background: #111827; border-right: 1px solid #1f2937; padding: 16px; }}
    main {{ padding: 28px; max-width: 1100px; }}
    h1,h2,h3,h4 {{ color: #f9fafb; }}
    a {{ color: #60a5fa; text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    .toc {{ list-style: none; padding: 0; margin: 0; }}
    .toc li {{ margin: 0 0 8px 0; line-height: 1.25; }}
    section {{ background: #111827; border: 1px solid #1f2937; border-radius: 12px; padding: 20px; margin-bottom: 18px; }}
    .file-meta {{ font-size: 12px; color: #9ca3af; margin-bottom: 10px; }}
    pre {{ overflow: auto; border-radius: 8px; padding: 12px; background: #0f172a; }}
    code {{ font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }}
    table {{ width: 100%; border-collapse: collapse; margin: 12px 0; }}
    th, td {{ border: 1px solid #334155; padding: 8px; text-align: left; }}
    hr {{ border: none; border-top: 1px solid #334155; margin: 16px 0; }}
    @media (max-width: 980px) {{ .layout {{ grid-template-columns: 1fr; }} nav {{ position: relative; height: auto; }} }}
  </style>
</head>
<body>
  <div class=\"layout\">
    <nav>
      <h2>Índice del curso</h2>
      {build_index(toc_entries)}
    </nav>
    <main>
      <h1>Stack My Architecture Android</h1>
      {''.join(sections)}
    </main>
  </div>
  <script>
    hljs.highlightAll();
    mermaid.initialize({{ startOnLoad: true, theme: 'dark' }});
  </script>
</body>
</html>"""

    OUTPUT_FILE.write_text(html_doc, encoding="utf-8")
    print(f"HTML generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()

