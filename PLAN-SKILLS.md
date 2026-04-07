# Plan: Research Skills + Playbook

## Qué crear

### 1. Playbook (`docs/_playbook.md`)
Documento con la estrategia completa de research. Incluye:
- Fases (setup → research → write → entrevista → QA)
- Reglas operativas (max 6 agentes, background mode, nunca escribir en contexto principal, etc.)
- Convenciones de nodos (frontmatter, confidence levels, idioma, fuentes)
- Template de oleadas por tema

### 2. Manifest (`docs/_manifest.md`)
Tabla de estado de todos los nodos del content graph:
```
| Nodo | Sección | Research | Escrito | QA | Sesión |
|------|---------|----------|---------|-----|--------|
| happyrobot.md | empresa | done | done | done | 1A/2A |
```
- Fuente de verdad cross-sesión
- Claude lo lee al inicio de cada sesión y lo actualiza al final
- Permite retomar desde cualquier punto si se pierde contexto

### 3. Skill: `/research-launch`
Ubicación: `.claude/skills/research-launch/`

Comportamiento:
1. Lee `_manifest.md`, identifica nodos con research pendiente para el tema dado
2. Lanza 5-6 agentes de research con `run_in_background=true` y `--save-dir`
3. Cada agente escribe su output a un archivo en `/tmp/research/[proyecto]/[tema]-[nodo].md`
4. NO lee outputs en contexto principal
5. Actualiza manifest: status research → "done"
6. Reporta: "X agentes lanzados, outputs en /tmp/research/..."

Invocación: `/research-launch empresa` o `/research-launch competidores`

### 4. Skill: `/write-wave`
Ubicación: `.claude/skills/write-wave/`

Comportamiento:
1. Lee `_manifest.md`, identifica nodos con research done pero sin escribir
2. Lanza 1-2 subagentes escritores (Task tool, tipo general-purpose)
   - El subagente recibe: rutas de research outputs, rutas de skeletons, convenciones, 1-2 nodos de referencia
   - El subagente lee los research outputs y escribe los .md con Write tool
3. Contexto principal solo recibe confirmación
4. Verifica `mkdocs build`
5. Actualiza manifest: status escrito → "done"

Invocación: `/write-wave empresa` o `/write-wave competidores`

### 5. Skill: `/research-qa`
Ubicación: `.claude/skills/research-qa/`

Comportamiento:
1. Grep todos los nodos por status en frontmatter
2. Cuenta líneas de cada archivo, flag los que tengan <50 líneas
3. Verifica links internos entre nodos (grep por links rotos)
4. Cross-check números clave (funding, clientes, métricas) entre nodos
5. Actualiza todos los status a `completo`
6. Actualiza dashboard (index.md)
7. Ejecuta `mkdocs build` final

Invocación: `/research-qa`

## Referencia: CLAUDE.md addition

Añadir al CLAUDE.md del proyecto:
```markdown
## Research Workflow

Este proyecto usa un workflow de research por oleadas. Ver `docs/_playbook.md` para la estrategia completa y `docs/_manifest.md` para el estado actual.

### Skills disponibles
- `/research-launch [tema]` — Lanza oleada de research (max 6 agentes, background)
- `/write-wave [seccion]` — Lanza escritores para nodos con research completo
- `/research-qa` — Audita, cross-checks, y finaliza el content graph

### Reglas clave
- Máximo 6 agentes por sesión
- Research agents siempre con `run_in_background=true`
- Nunca escribir archivos >50 líneas en contexto principal — delegar a subagentes
- Nunca leer research outputs completos en contexto principal
- Manifest es la fuente de verdad cross-sesión
- Late notifications = dismiss con one-liner si ya integrado
```

## Orden de ejecución

1. Crear `docs/_playbook.md` con la estrategia completa
2. Crear `docs/_manifest.md` con la tabla de nodos (para este proyecto: ya todo está done, pero sirve como template)
3. Crear los 3 skills en `.claude/skills/`
4. Actualizar CLAUDE.md con la sección de workflow
5. Test: ejecutar `/research-qa` en este proyecto como smoke test

## Notas

- Los skills deben ser genéricos — reutilizables para futuros proyectos de research (no hardcoded a HappyRobot)
- El playbook puede tener una sección "template" para bootstrappear nuevos proyectos
- El manifest se genera automáticamente a partir del árbol de `docs/` y el frontmatter YAML
- Considerar que `/last30days` se integre como fuente de research en `/research-launch`
