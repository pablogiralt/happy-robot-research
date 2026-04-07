# Plan: Research desde el chat

## Concepto

El chat tiene **dos pestañas**:

1. **Chat** — Modo actual. Pregunta/respuesta sobre la documentación existente.
2. **Research** — Lola describe qué quiere investigar. El sistema lanza un proceso de research en background, crea el documento y lo integra en el site.

## Arquitectura

```
┌─────────────────────────────────────────────────┐
│  Chat widget (2 tabs)                           │
│  ┌──────────┬──────────┐                        │
│  │  💬 Chat │ 🔍 Research │                     │
│  └──────────┴──────────┘                        │
│                                                 │
│  Tab Chat:    como ahora, Q&A sobre docs        │
│  Tab Research: input + lista de research jobs   │
└───────────────┬─────────────────────────────────┘
                │
    POST /api/chat     POST /api/research
         │                    │
    claude -p              claude -p
    (sin tools,            (con tools: WebSearch,
     solo docs)             WebFetch, Write, Read, Bash)
                              │
                         1. Busca en web
                         2. Crea .md en docs/
                         3. Actualiza mkdocs.yml
                         4. mkdocs build
                         5. Recarga ALL_DOCS
                              │
                    GET /api/research/status
                         (polling cada 15s)
```

## UI de la pestaña Research

### Formulario
- Textarea: "¿Qué quieres investigar?" con placeholder examples:
  - "Competidor: Cognigy"
  - "Mercado de AI en healthcare en España"
  - "Cliente potencial: Maersk"
- Botón "Lanzar Research"

### Lista de jobs
- Debajo del formulario, lista de research en curso y completados
- Cada job muestra:
  - Tema solicitado
  - Estado: 🔄 En curso | ✅ Completado | ❌ Error
  - Hora de inicio
  - Cuando completa: link al nuevo doc en el site

## Backend

### Nuevo endpoint: `POST /api/research`

```
Request:  { "topic": "Competidor: Cognigy" }
Response: { "job_id": "abc123", "status": "started" }
```

Lanza `claude -p` en background con:
- System prompt con la metodología de research (niveles A/B/C, fuentes, convenciones frontmatter)
- Herramientas habilitadas: `--allowedTools WebSearch,WebFetch,Write,Read,Bash`
- Instrucciones para:
  1. Investigar el tema en profundidad
  2. Crear el .md en la carpeta correcta de `docs/`
  3. Registrar fuentes en `docs/fuentes/`
  4. Actualizar `mkdocs.yml` nav si es un nuevo archivo
  5. Ejecutar `mkdocs build`

### Nuevo endpoint: `GET /api/research/status`

```
Response: {
  "jobs": [
    { "id": "abc123", "topic": "Competidor: Cognigy", "status": "running", "started": "10:30" },
    { "id": "def456", "topic": "Cliente: Maersk", "status": "done", "doc_url": "/competidores/cognigy/", "finished": "10:42" }
  ]
}
```

Frontend hace polling cada 15 segundos.

### Recarga de docs

Después de cada research completado:
- Rebuild `mkdocs build`
- Recargar `ALL_DOCS` en memoria (para que el tab Chat tenga los nuevos datos)
- Exponer función `reload_docs()` en el server

## System prompt del agente research

Incluye:
- La metodología completa del CLAUDE.md (niveles A/B/C, atribución, fuentes)
- Las convenciones de frontmatter YAML
- La estructura de carpetas del proyecto
- Instrucciones para registrar fuentes
- Instrucciones para actualizar nav en mkdocs.yml

## Jobs en memoria

Los jobs se guardan en un dict en memoria del server (no necesitamos persistencia):

```python
research_jobs = {
    "abc123": {
        "topic": "Competidor: Cognigy",
        "status": "running",  # running | done | error
        "started": datetime,
        "finished": datetime | None,
        "doc_path": str | None,
        "error": str | None,
    }
}
```

## Límites y seguridad

- Máximo 1 research concurrente (cola si hay otro en curso)
- Timeout de 10 minutos por job
- Solo usuarios autenticados (misma cookie auth)

## Pasos de implementación

1. **Backend**: Añadir `/api/research` y `/api/research/status` a `chat_server.py`
2. **Frontend**: Rediseñar chat widget con dos tabs, añadir UI de research
3. **System prompt research**: Escribir el prompt con la metodología
4. **Recarga docs**: Implementar `reload_docs()` post-research
5. **Test**: Probar con un research real de competidor
