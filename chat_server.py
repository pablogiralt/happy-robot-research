"""
Chat server: serves MkDocs static site + chat API + research API backed by Claude CLI.
Usage: python chat_server.py [--port 8000]
"""

import asyncio
import hashlib
import json
import os
import re
import secrets
import subprocess
import sys
import uuid
from datetime import datetime
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.base import BaseHTTPMiddleware

DOCS_DIR = Path(__file__).parent / "docs"
SITE_DIR = Path(__file__).parent / "site"
PROJECT_DIR = Path(__file__).parent
CLAUDE_BIN = os.environ.get("CLAUDE_BIN", "/Users/pablo/.nvm/versions/node/v20.19.1/bin/claude")
MODEL = os.environ.get("CLAUDE_MODEL", "claude-opus-4-6")
AUTH_USER = os.environ.get("AUTH_USER", "lola")
AUTH_PASS = os.environ.get("AUTH_PASS", "happyrobot2026")


def load_all_docs() -> str:
    """Load all markdown files from docs/ into a single string."""
    parts = []
    for md_file in sorted(DOCS_DIR.rglob("*.md")):
        if md_file.name.startswith("_"):
            continue
        rel = md_file.relative_to(DOCS_DIR)
        content = md_file.read_text(encoding="utf-8", errors="replace")
        parts.append(f"=== {rel} ===\n{content}")
    return "\n\n".join(parts)


ALL_DOCS = load_all_docs()

CHAT_SYSTEM_PROMPT = f"""Eres un asistente experto sobre la investigación de HappyRobot y la preparación de entrevista para Lola Vilas como General Manager España.

Tienes acceso a toda la documentación del research. Responde en español salvo que te pregunten en otro idioma. Sé conciso y directo. Si citas datos, menciona la fuente si está disponible en los documentos.

Si te preguntan algo que no está en la documentación, dilo claramente.

IMPORTANTE sobre links: Cuando hagas referencia a documentos del research, usa links web con formato Markdown. Las URLs siguen el patrón: /seccion/nombre-archivo/ (sin .md). Ejemplos:
- [Sierra AI](/competidores/sierra-ai/)
- [HappyRobot Overview](/empresa/happyrobot/)
- [Fit Candidata](/entrevista/fit-candidata/)
- [Logistics España](/mercado/logistics-espana/)
NUNCA uses rutas a archivos .md como docs/competidores/sierra-ai.md. Siempre links web.

--- DOCUMENTACIÓN COMPLETA ---

{ALL_DOCS}

--- FIN DOCUMENTACIÓN ---"""

RESEARCH_SYSTEM_PROMPT = """Eres un agente de research experto. Tu trabajo es investigar un tema en profundidad y crear un documento Markdown de alta calidad.

## Metodología

### Niveles de confianza (A/B/C)
| Nivel | Significado | Criterio |
|-------|-------------|----------|
| A | Verificado | Confirmado por 2+ fuentes independientes, o fuente primaria oficial |
| B | Plausible | Una sola fuente creíble sin contrastar, o estimación de analista reputado |
| C | No verificado | Fuente anecdótica, estimación propia, dato antiguo, o fuentes contradictorias |

### Reglas
1. Todo claim cuantitativo lleva fuente y nivel de confianza (A/B/C)
2. Intentar siempre 2+ fuentes para datos clave (funding, revenue, headcount, market size)
3. Datos contradictorios: mostrar el rango, no elegir uno
4. Separar dato de interpretación
5. Cuando no hay dato: decirlo explícitamente con [dato no disponible públicamente]

### Formato tablas de datos
| Metric | Value | Conf | Fuente |
|--------|-------|------|--------|
| Ejemplo | $44M | A | [SOURCE-ID] |

### Formato texto narrativo
Ejemplo: "HappyRobot cerró una Serie B de $44M en septiembre 2025 [A: HR-WEB, TC-SERIEB]."

## Convenciones del documento

Cada archivo DEBE tener frontmatter YAML:
```yaml
---
title: "Nombre del nodo"
type: empresa | persona | competidor | mercado | tecnologia | caso-de-uso | cliente | regulacion
status: completo
tags: [tag1, tag2]
updated: {date}
---
```

## Estructura de carpetas
- docs/competidores/ — Un .md por competidor
- docs/mercado/ — Análisis de mercado
- docs/tecnologia/ — Nodo por tecnología/concepto
- docs/casos-de-uso/ — Un .md por vertical/use case
- docs/clientes/ — Un .md por cliente conocido
- docs/personas/ — Nodo por persona relevante
- docs/empresa/ — HappyRobot en profundidad
- docs/regulacion/ — Marco regulatorio

## Tu tarea

1. Usa WebSearch y WebFetch para investigar el tema en profundidad
2. Busca en fuentes oficiales primero (web empresa, press releases)
3. Contrasta con fuentes secundarias (Tracxn, Crunchbase, prensa)
4. Busca señales cualitativas (Reddit, G2, Twitter, HN)
5. Crea el archivo .md en la carpeta correcta de docs/
6. Clasifica cada dato con nivel A/B/C
7. Escribe en español con términos técnicos en inglés donde sea natural

IMPORTANTE: El archivo debe ser exhaustivo y bien estructurado. Incluir secciones relevantes según el tipo (para competidores: overview, producto, funding, clientes, diferenciadores, fortalezas, debilidades, comparación con HappyRobot).
"""

app = FastAPI()

# --- Auth ---
AUTH_TOKEN = hashlib.sha256(f"{AUTH_USER}:{AUTH_PASS}".encode()).hexdigest()

LOGIN_PAGE = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Login — HappyRobot Research</title>
<style>
  body { font-family: system-ui, sans-serif; display: flex; align-items: center; justify-content: center;
         min-height: 100vh; margin: 0; background: #f5f0ff; }
  .card { background: white; padding: 40px; border-radius: 16px; box-shadow: 0 4px 24px rgba(0,0,0,0.1);
          width: 320px; text-align: center; }
  h2 { color: #7b1fa2; margin: 0 0 8px; }
  p { color: #666; font-size: 0.9rem; margin: 0 0 24px; }
  input { width: 100%; padding: 10px 14px; border: 1px solid #ddd; border-radius: 8px;
          font-size: 0.95rem; margin-bottom: 12px; box-sizing: border-box; }
  input:focus { outline: none; border-color: #7b1fa2; }
  button { width: 100%; padding: 12px; background: #7b1fa2; color: white; border: none;
           border-radius: 8px; font-size: 1rem; font-weight: 600; cursor: pointer; }
  button:hover { background: #6a1b9a; }
  .err { color: #dc2626; font-size: 0.85rem; margin-top: 8px; display: none; }
</style></head><body>
<div class="card">
  <h2>HappyRobot Research</h2>
  <p>Introduce tus credenciales</p>
  <form method="POST" action="/login">
    <input name="user" placeholder="Usuario" required autofocus>
    <input name="pass" type="password" placeholder="Contraseña" required>
    <button type="submit">Entrar</button>
  </form>
  <div class="err" id="err">Usuario o contraseña incorrectos</div>
</div>
<script>if(location.search.includes('err'))document.getElementById('err').style.display='block'</script>
</body></html>"""


@app.post("/login")
async def login(request: Request):
    form = await request.form()
    user = form.get("user", "")
    pw = form.get("pass", "")
    token = hashlib.sha256(f"{user}:{pw}".encode()).hexdigest()
    if secrets.compare_digest(token, AUTH_TOKEN):
        resp = HTMLResponse('<meta http-equiv="refresh" content="0;url=/">', status_code=302)
        resp.headers["location"] = "/"
        resp.set_cookie("auth", token, httponly=True, samesite="lax", max_age=86400 * 30)
        return resp
    return HTMLResponse(status_code=302, headers={"location": "/login?err=1"})


@app.get("/login")
async def login_page():
    return HTMLResponse(LOGIN_PAGE)


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        path = request.url.path
        if path == "/login":
            return await call_next(request)
        token = request.cookies.get("auth", "")
        if not secrets.compare_digest(token, AUTH_TOKEN):
            return HTMLResponse(status_code=302, headers={"location": "/login"})
        return await call_next(request)


app.add_middleware(AuthMiddleware)


# --- Chat API ---

@app.post("/api/chat")
async def chat(request: Request):
    body = await request.json()
    messages = body.get("messages", [])

    if not messages:
        return {"error": "No messages provided"}

    conversation = ""
    for msg in messages[:-1]:
        role = "Usuario" if msg["role"] == "user" else "Asistente"
        conversation += f"{role}: {msg['content']}\n\n"

    last_message = messages[-1]["content"]
    if conversation:
        prompt = f"Historial de conversación:\n{conversation}\nUsuario: {last_message}"
    else:
        prompt = last_message

    async def stream_response():
        proc = await asyncio.create_subprocess_exec(
            CLAUDE_BIN, "-p", prompt,
            "--system-prompt", CHAT_SYSTEM_PROMPT,
            "--model", MODEL,
            "--verbose",
            "--output-format", "stream-json",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        buffer = b""
        async for chunk in proc.stdout:
            buffer += chunk
            while b"\n" in buffer:
                line, buffer = buffer.split(b"\n", 1)
                line = line.strip()
                if not line:
                    continue
                try:
                    data = json.loads(line)
                except json.JSONDecodeError:
                    continue

                if data.get("type") == "assistant":
                    msg = data.get("message", {})
                    for block in msg.get("content", []):
                        if block.get("type") == "text":
                            yield f"data: {json.dumps({'text': block['text']})}\n\n"
                elif data.get("type") == "result":
                    yield f"data: {json.dumps({'done': True})}\n\n"

        await proc.wait()

    return StreamingResponse(
        stream_response(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )


# --- Research API ---

research_jobs: dict = {}
research_lock = asyncio.Lock()


def reload_docs():
    """Reload all docs into memory."""
    global ALL_DOCS, CHAT_SYSTEM_PROMPT
    ALL_DOCS = load_all_docs()
    CHAT_SYSTEM_PROMPT = f"""Eres un asistente experto sobre la investigación de HappyRobot y la preparación de entrevista para Lola Vilas como General Manager España.

Tienes acceso a toda la documentación del research. Responde en español salvo que te pregunten en otro idioma. Sé conciso y directo. Si citas datos, menciona la fuente si está disponible en los documentos.

Si te preguntan algo que no está en la documentación, dilo claramente.

IMPORTANTE sobre links: Cuando hagas referencia a documentos del research, usa links web con formato Markdown. Las URLs siguen el patrón: /seccion/nombre-archivo/ (sin .md). Ejemplos:
- [Sierra AI](/competidores/sierra-ai/)
- [HappyRobot Overview](/empresa/happyrobot/)
- [Fit Candidata](/entrevista/fit-candidata/)
- [Logistics España](/mercado/logistics-espana/)
NUNCA uses rutas a archivos .md como docs/competidores/sierra-ai.md. Siempre links web.

--- DOCUMENTACIÓN COMPLETA ---

{ALL_DOCS}

--- FIN DOCUMENTACIÓN ---"""


MKDOCS_YML = PROJECT_DIR / "mkdocs.yml"

# Map folder names to nav section names
SECTION_MAP = {
    "competidores": "Competidores",
    "mercado": "Mercado",
    "tecnologia": "Tecnología",
    "casos-de-uso": "Casos de Uso",
    "clientes": "Clientes",
    "personas": "Personas",
    "empresa": "Empresa",
    "regulacion": "Regulación",
    "entrevista": "Entrevista",
    "fuentes": "Fuentes",
}


def add_to_nav(md_file: Path):
    """Add a new .md file to mkdocs.yml nav if not already present."""
    rel = md_file.relative_to(DOCS_DIR)
    rel_str = str(rel)
    folder = rel.parts[0] if len(rel.parts) > 1 else None

    if not folder or folder not in SECTION_MAP:
        return

    yml_text = MKDOCS_YML.read_text(encoding="utf-8")

    # Already in nav?
    if rel_str in yml_text:
        return

    # Derive a title from the frontmatter or filename
    title = None
    content = md_file.read_text(encoding="utf-8", errors="replace")
    m = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
    if m:
        title = m.group(1).strip()
    if not title:
        title = md_file.stem.replace("-", " ").title()

    section_name = SECTION_MAP[folder]
    nav_entry = f"    - {title}: {rel_str}"

    # Find the section and insert before the next section
    lines = yml_text.split("\n")
    insert_idx = None
    in_section = False
    for i, line in enumerate(lines):
        if f"- {section_name}:" in line:
            in_section = True
            continue
        if in_section:
            # Still in the section if line starts with enough indent + "-"
            stripped = line.lstrip()
            if stripped.startswith("- ") and line.startswith("    "):
                insert_idx = i + 1
            elif stripped.startswith("- ") and not line.startswith("    "):
                # New top-level section
                break

    if insert_idx:
        lines.insert(insert_idx, nav_entry)
        MKDOCS_YML.write_text("\n".join(lines), encoding="utf-8")


async def run_research(job_id: str, topic: str):
    """Run research in background using claude CLI with tools."""
    today = datetime.now().strftime("%Y-%m-%d")
    prompt = f"""Investiga el siguiente tema y crea un documento de research completo:

TEMA: {topic}

Fecha de hoy: {today}

Instrucciones:
1. Usa WebSearch para buscar información actualizada sobre el tema
2. Usa WebFetch para acceder a páginas específicas cuando necesites más detalle
3. Determina la carpeta correcta en docs/ según el tipo de contenido (competidores/, mercado/, tecnologia/, clientes/, personas/, etc.)
4. Crea el archivo .md con la investigación completa siguiendo la metodología
5. El nombre del archivo debe ser kebab-case (ej: nombre-empresa.md)
6. Asegúrate de incluir frontmatter YAML con updated: {today}
7. Sé exhaustivo: incluye todas las secciones relevantes

Trabaja directamente en el directorio del proyecto: {PROJECT_DIR}
Los documentos van en: {DOCS_DIR}
"""

    try:
        proc = await asyncio.create_subprocess_exec(
            CLAUDE_BIN, "-p", prompt,
            "--system-prompt", RESEARCH_SYSTEM_PROMPT.replace("{date}", today),
            "--model", MODEL,
            "--verbose",
            "--output-format", "stream-json",
            "--allowedTools", "WebSearch,WebFetch,Write,Read,Bash,Edit,Glob,Grep",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            cwd=str(PROJECT_DIR),
        )

        result_text = ""
        doc_path = None
        buffer = b""

        async for chunk in proc.stdout:
            buffer += chunk
            while b"\n" in buffer:
                line, buffer = buffer.split(b"\n", 1)
                line = line.strip()
                if not line:
                    continue
                try:
                    data = json.loads(line)
                except json.JSONDecodeError:
                    continue

                if data.get("type") == "result":
                    result_text = data.get("result", "")

        await proc.wait()

        # Find any new .md files created and add to nav
        for md_file in DOCS_DIR.rglob("*.md"):
            if md_file.name.startswith("_") or md_file.name == "index.md":
                continue
            mtime = md_file.stat().st_mtime
            started = research_jobs[job_id]["started_ts"]
            if mtime >= started:
                rel = md_file.relative_to(DOCS_DIR)
                doc_path = str(rel).replace(".md", "/")
                research_jobs[job_id]["doc_path"] = f"/{doc_path}"
                add_to_nav(md_file)
                break

        # Rebuild mkdocs
        subprocess.run(
            ["/opt/homebrew/bin/mkdocs", "build"],
            cwd=str(PROJECT_DIR),
            capture_output=True,
            timeout=30,
        )

        # Reload docs in memory
        reload_docs()

        research_jobs[job_id]["status"] = "done"
        research_jobs[job_id]["finished"] = datetime.now().strftime("%H:%M")
        research_jobs[job_id]["summary"] = result_text[:500] if result_text else "Research completado"

    except asyncio.TimeoutError:
        research_jobs[job_id]["status"] = "error"
        research_jobs[job_id]["error"] = "Timeout (10 min)"
    except Exception as e:
        research_jobs[job_id]["status"] = "error"
        research_jobs[job_id]["error"] = str(e)[:200]


@app.post("/api/research")
async def start_research(request: Request):
    body = await request.json()
    topic = body.get("topic", "").strip()

    if not topic:
        return JSONResponse({"error": "No topic provided"}, status_code=400)

    # Check if there's already one running
    running = [j for j in research_jobs.values() if j["status"] == "running"]
    if running:
        return JSONResponse(
            {"error": "Ya hay un research en curso. Espera a que termine."},
            status_code=429,
        )

    job_id = uuid.uuid4().hex[:8]
    now = datetime.now()
    research_jobs[job_id] = {
        "id": job_id,
        "topic": topic,
        "status": "running",
        "started": now.strftime("%H:%M"),
        "started_ts": now.timestamp(),
        "finished": None,
        "doc_path": None,
        "summary": None,
        "error": None,
    }

    asyncio.create_task(run_research(job_id, topic))

    return {"job_id": job_id, "status": "started"}


@app.get("/api/research/status")
async def research_status():
    jobs = sorted(research_jobs.values(), key=lambda j: j["started"], reverse=True)
    # Clean up internal fields before sending
    clean = []
    for j in jobs:
        clean.append({
            "id": j["id"],
            "topic": j["topic"],
            "status": j["status"],
            "started": j["started"],
            "finished": j["finished"],
            "doc_path": j["doc_path"],
            "summary": j["summary"],
            "error": j["error"],
        })
    return {"jobs": clean}


# --- Middleware ---

class NoCacheMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        if request.url.path.endswith(".html") or request.url.path == "/" or "." not in request.url.path.split("/")[-1]:
            response.headers["Cache-Control"] = "no-store"
        return response


app.add_middleware(NoCacheMiddleware)

# Serve MkDocs static site (must be last - catches all routes)
if SITE_DIR.exists():
    app.mount("/", StaticFiles(directory=str(SITE_DIR), html=True), name="site")

if __name__ == "__main__":
    import uvicorn

    port = int(sys.argv[sys.argv.index("--port") + 1]) if "--port" in sys.argv else 8000
    print(f"Docs loaded: {len(ALL_DOCS):,} chars from {DOCS_DIR}")
    print(f"Serving site from {SITE_DIR}")
    print(f"Model: {MODEL}")
    print(f"http://localhost:{port}")
    uvicorn.run(app, host="0.0.0.0", port=port)
