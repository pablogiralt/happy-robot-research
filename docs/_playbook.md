# Research Playbook

Estrategia operativa para proyectos de research con Claude Code. Diseñado para maximizar throughput sin saturar el contexto principal.

---

## Fases del proyecto

| # | Fase | Qué se hace | Output |
|---|------|-------------|--------|
| 1 | **Setup** | Crear content graph (mkdocs.yml, skeletons .md con frontmatter), playbook, manifest | Árbol de `docs/` con nodos vacíos |
| 2 | **Research** | Lanzar oleadas de research con `/research-launch` | Archivos raw en `/tmp/research/[proyecto]/` |
| 3 | **Write** | Escribir nodos .md desde research outputs con `/write-wave` | Nodos completos en `docs/` |
| 4 | **QA** | Auditar consistencia, links, números con `/research-qa` | Manifest actualizado, build limpio |
| 5 | **Entrevista** | Preparar Q&A, talking points, plan 90 días | Sección `entrevista/` lista |

---

## Reglas operativas

### Contexto principal
- **Nunca escribir archivos >50 líneas en contexto principal** — delegar a subagentes
- **Nunca leer research outputs completos en contexto principal** — solo rutas y confirmaciones
- El contexto principal es para orquestación: lanzar agentes, verificar status, actualizar manifest
- Late notifications de background agents = dismiss con one-liner si ya integrado

### Agentes
- **Máximo 6 agentes simultáneos** por sesión (evitar throttling)
- Research agents siempre con `run_in_background=true`
- Writers usan Task tool con `subagent_type=general-purpose`
- Cada agente recibe instrucciones completas (no depende del contexto principal)

### Archivos
- Research outputs van a `/tmp/research/[proyecto]/` — son efímeros, no se commitean
- Solo `docs/` contiene contenido final
- `_manifest.md` es la fuente de verdad cross-sesión — leer al inicio, actualizar al final
- `_playbook.md` (este archivo) define las reglas — no cambia entre sesiones

---

## Convenciones de nodos

### Frontmatter YAML

```yaml
---
title: "Nombre del nodo"
type: empresa | persona | competidor | mercado | tecnologia | caso-de-uso | cliente | regulacion | entrevista
status: pendiente | en-progreso | completo
tags: [tag1, tag2]
updated: 2026-04-07
---
```

### Niveles de confianza (A/B/C)

| Nivel | Significado | Criterio |
|-------|-------------|----------|
| **A** | Verificado | 2+ fuentes independientes o fuente primaria oficial |
| **B** | Plausible | 1 fuente creíble sin contrastar |
| **C** | No verificado | Anecdótico, estimación propia, o fuentes contradictorias |

### Formato en texto
```
HappyRobot cerró una Serie B de $44M [A: HR-WEB, TC-SERIEB].
La valoración se estima en ~$200M [C: sin fuente pública].
```

### Formato en tablas
```
| Metric | Value | Conf | Fuente |
|--------|-------|------|--------|
| Funding | $44M | A | [HR-WEB] [TC-SERIEB] |
```

### Links entre nodos
Markdown relativo: `[HappyRobot](../empresa/happyrobot.md)`

### Idioma
Español con términos técnicos en inglés donde sea natural.

---

## Template de oleada

Para cada sección del content graph:

```
1. /research-launch [seccion]
   → Lanza N agentes de research en background
   → Outputs en /tmp/research/[proyecto]/[seccion]-*.md

2. Esperar a que terminen (check /tmp/research/)

3. /write-wave [seccion]
   → Subagentes leen outputs + skeletons
   → Escriben nodos finales en docs/[seccion]/

4. /research-qa
   → Verifica links, números, coverage
   → Actualiza manifest y dashboard
```

---

## Bootstrap de nuevo proyecto

Para iniciar un proyecto de research desde cero:

1. Crear directorio con `mkdocs.yml` (theme: material)
2. Crear `CLAUDE.md` con contexto del proyecto
3. Crear `docs/_playbook.md` (copiar este archivo)
4. Definir el content graph: qué secciones, qué nodos
5. Crear skeletons .md con frontmatter para cada nodo
6. Crear `docs/_manifest.md` con tabla de todos los nodos (status: pendiente)
7. Ejecutar oleadas: research → write → QA

---

## Skills disponibles

| Skill | Invocación | Qué hace |
|-------|-----------|----------|
| `/research-launch` | `/research-launch [seccion]` | Lanza oleada de research (max 6 agentes, background) |
| `/write-wave` | `/write-wave [seccion]` | Escribe nodos desde research outputs |
| `/research-qa` | `/research-qa` | Audita, cross-checks, y finaliza el content graph |
| `/last30days` | `/last30days [tema]` | Research en tiempo real (últimos 30 días, 10+ fuentes) |
