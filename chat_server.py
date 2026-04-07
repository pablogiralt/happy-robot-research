"""
Chat server: serves MkDocs static site + chat API backed by Claude CLI.
Usage: python chat_server.py [--port 8000]
"""

import asyncio
import hashlib
import json
import os
import secrets
import sys
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.base import BaseHTTPMiddleware

DOCS_DIR = Path(__file__).parent / "docs"
SITE_DIR = Path(__file__).parent / "site"
CLAUDE_BIN = os.environ.get("CLAUDE_BIN", "claude")
MODEL = os.environ.get("CLAUDE_MODEL", "claude-sonnet-4-6")
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

SYSTEM_PROMPT = f"""Eres un asistente experto sobre la investigación de HappyRobot y la preparación de entrevista para Lola Vilas como General Manager España.

Tienes acceso a toda la documentación del research. Responde en español salvo que te pregunten en otro idioma. Sé conciso y directo. Si citas datos, menciona la fuente si está disponible en los documentos.

Si te preguntan algo que no está en la documentación, dilo claramente.

--- DOCUMENTACIÓN COMPLETA ---

{ALL_DOCS}

--- FIN DOCUMENTACIÓN ---"""

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


@app.post("/api/chat")
async def chat(request: Request):
    body = await request.json()
    messages = body.get("messages", [])

    if not messages:
        return {"error": "No messages provided"}

    # Build the prompt: last user message + conversation history as context
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
            "--system-prompt", SYSTEM_PROMPT,
            "--model", MODEL,
            "--verbose",
            "--output-format", "stream-json",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        buffer = b""
        async for chunk in proc.stdout:
            buffer += chunk
            # Process complete lines
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
