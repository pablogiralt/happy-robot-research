---
name: write-wave
description: "Escribe nodos del content graph desde research outputs usando subagentes escritores"
argument-hint: "[seccion] — e.g. empresa, competidores, entrevista"
user-invocable: true
allowed-tools: Read, Grep, Glob, Bash, Write, Task
---

# /write-wave $ARGUMENTS

Escribe los nodos .md de la sección `$0` a partir de los research outputs en `/tmp/research/`.

## Proceso

### 1. Leer estado actual

Lee `docs/_manifest.md` para identificar nodos de la sección `$0` que tienen:
- Research = "done" (o "launched" si los outputs ya existen)
- Escrito != "done"

Si no hay nodos pendientes de escritura, reporta "Nada pendiente en $0" y termina.

### 2. Verificar que existen research outputs

Comprueba que existen archivos en `/tmp/research/[proyecto]/$0-*.md` para los nodos pendientes.
Si faltan outputs, lista cuáles faltan y sugiere ejecutar `/research-launch $0` primero.

### 3. Leer nodos de referencia

Lee 1-2 nodos completos de la misma sección que ya estén escritos (status "done") para usar como referencia de estilo, estructura y profundidad.

### 4. Lanzar subagentes escritores

Lanza 1-2 agentes con Task tool (`subagent_type: general-purpose`) asignando 2-4 nodos a cada uno.

Cada agente recibe:
- Las rutas de los research outputs a procesar
- Las rutas de los .md destino en `docs/[seccion]/`
- El frontmatter YAML esperado (de los skeletons existentes)
- 1-2 nodos de referencia completos (para calibrar estilo)
- Las convenciones del playbook (confianza A/B/C, formato, idioma)
- Instrucción de usar Write tool para escribir cada nodo final

### 5. Prompt template para cada agente escritor

```
Escribe los siguientes nodos del content graph a partir de los research outputs proporcionados.

## Nodos a escribir
[Lista de nodos con rutas de research output y destino .md]

## Referencia de estilo
[Contenido de 1-2 nodos de referencia de la misma sección]

## Convenciones
- Frontmatter YAML: title, type, status: completo, tags, updated: [HOY]
- Niveles de confianza (A/B/C) en claims cuantitativos
- Links entre nodos con Markdown relativo
- Idioma: español, términos técnicos en inglés
- Dato sin fuente → marcar explícitamente [dato no disponible públicamente]

Lee cada research output, sintetiza la información, y escribe el nodo final con Write tool.
No resumas en exceso — mantén el detalle relevante para preparación de entrevista.
```

### 6. Verificar build

Después de que los agentes terminen, ejecuta:
```bash
/Users/pablo/Library/Python/3.14/bin/mkdocs build 2>&1 | tail -5
```

Si hay errores de build, reportarlos al usuario.

### 7. Actualizar manifest

Actualiza `docs/_manifest.md`:
- Marca los nodos escritos como Escrito = "done"
- Actualiza conteo de líneas
- Actualiza la tabla resumen

### 8. Reportar

```
Write wave: [seccion]
- X nodos escritos
- Build: OK / errores
- Nodos: [lista con líneas]
- Siguiente paso: /research-qa para verificar
```

## Reglas

- Máximo 2 subagentes escritores simultáneos (escritura requiere más cuidado)
- Cada agente recibe contexto completo — no depende del contexto principal
- Nunca leer research outputs completos en contexto principal
- Verificar mkdocs build al final
