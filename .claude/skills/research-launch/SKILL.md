---
name: research-launch
description: "Lanza oleada de research para una sección del content graph (max 6 agentes en background)"
argument-hint: "[seccion] — e.g. empresa, competidores, mercado"
user-invocable: true
allowed-tools: Read, Grep, Glob, Bash, Write, Task
---

# /research-launch $ARGUMENTS

Lanza una oleada de research para la sección `$0` del content graph.

## Proceso

### 1. Leer estado actual

Lee `docs/_manifest.md` para identificar qué nodos de la sección `$0` tienen research pendiente (columna Research != "done").

Si todos los nodos ya tienen research "done", reporta "Nada pendiente en $0" y termina.

### 2. Preparar directorio de outputs

```bash
mkdir -p /tmp/research/$(basename $(pwd))
```

### 3. Lanzar agentes de research

Para cada nodo pendiente (máximo 6), lanza un agente con Task tool:
- `subagent_type: general-purpose`
- `run_in_background: true`
- Cada agente recibe:
  - El tema/entidad a investigar
  - Las convenciones del proyecto (de `docs/_playbook.md`)
  - La ruta donde escribir su output: `/tmp/research/[proyecto]/$0-[nodo].md`
  - Instrucción de usar WebSearch y `/last30days` si disponible
  - Instrucción de clasificar cada dato con nivel de confianza (A/B/C) y fuente

### 4. Prompt template para cada agente

```
Investiga [ENTIDAD] para un proyecto de research.

Escribe los resultados en el archivo: /tmp/research/[PROJECT]/[SECCION]-[NODO].md

Usa WebSearch para buscar información actualizada. Incluye:
- Datos cuantitativos con fuentes
- Nivel de confianza (A/B/C) para cada dato
- Links a fuentes originales
- Señales cualitativas (reviews, opiniones, tendencias)

Formato: Markdown con headers claros. Idioma: español (términos técnicos en inglés).

No resumas — incluye todo el detalle relevante. Este output será procesado por otro agente para escribir el nodo final.
```

### 5. Actualizar manifest

Después de lanzar los agentes, actualiza `docs/_manifest.md`:
- Marca los nodos lanzados como Research = "launched"
- NO esperes a que terminen — son background agents

### 6. Reportar

Output final al usuario:
```
Research launch: [seccion]
- X agentes lanzados en background
- Outputs en /tmp/research/[proyecto]/
- Nodos: [lista]
- Siguiente paso: esperar y luego /write-wave [seccion]
```

## Reglas

- Máximo 6 agentes simultáneos
- Siempre `run_in_background=true`
- No leer outputs en contexto principal
- Si hay más de 6 nodos pendientes, dividir en lotes y avisar al usuario
- Integrar `/last30days` como fuente de research cuando esté disponible
