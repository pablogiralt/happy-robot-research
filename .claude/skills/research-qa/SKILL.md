---
name: research-qa
description: "Audita el content graph: verifica links, números, coverage, y actualiza manifest y dashboard"
user-invocable: true
allowed-tools: Read, Grep, Glob, Bash, Write, Edit
---

# /research-qa

Auditoría completa del content graph. Verifica consistencia, coverage, y calidad.

## Proceso

### 1. Inventory de nodos

Usa Glob para listar todos los .md bajo `docs/` (excluyendo `_playbook.md`, `_manifest.md`, `tags.md`).
Para cada nodo, extrae:
- Frontmatter: title, type, status
- Líneas totales (con `wc -l` o conteo)

### 2. Coverage check

Flag nodos con problemas:
- **Thin nodes:** < 50 líneas de contenido (excluyendo index/nav files)
- **Status incorrecto:** `status: pendiente` o `en-progreso` pero con contenido sustancial
- **Sin frontmatter:** archivos que no tengan YAML frontmatter válido

### 3. Link check

Grep todos los nodos por links Markdown internos (`](../` pattern).
Para cada link, verifica que el archivo destino existe.
Reporta links rotos.

### 4. Cross-check de números clave

Buscar datos clave que aparecen en múltiples nodos y verificar consistencia:
- Funding de HappyRobot ($44M Serie B)
- Número de empleados
- Métricas de clientes (300K+ llamadas Circle Logistics, etc.)
- TAM/SAM/SOM
- Fechas de funding rounds

Si hay inconsistencias, listarlas con los nodos afectados.

### 5. Actualizar status de nodos

Para nodos que tienen contenido sustancial (>50 líneas) pero status != "completo":
- Actualizar frontmatter a `status: completo`
- Actualizar `updated:` a la fecha de hoy

### 6. Regenerar manifest

Reescribir `docs/_manifest.md` con datos frescos:
- Tabla resumen actualizada
- Detalle por nodo con líneas reales
- Timestamp de actualización

### 7. Actualizar dashboard

Revisar `docs/index.md`:
- Verificar que los números del cheat sheet son consistentes con los nodos
- Actualizar links si hay nodos nuevos

### 8. Build final

```bash
/Users/pablo/Library/Python/3.14/bin/mkdocs build 2>&1
```

Reportar si hay warnings o errores.

### 9. Reporte final

```
=== Research QA Report ===

Nodos totales: X
Completos: X
Pendientes: X

Thin nodes (<50 líneas): [lista o "ninguno"]
Links rotos: [lista o "ninguno"]
Inconsistencias de datos: [lista o "ninguno"]
Status corregidos: [lista o "ninguno"]

Manifest: actualizado
Dashboard: actualizado
Build: OK / X warnings

Siguiente paso: [recomendación]
```

## Reglas

- Este skill corre en el contexto principal (no background) — es el paso final de verificación
- Leer archivos directamente con Read tool (son archivos propios del proyecto)
- Usar Edit tool para correcciones menores (status, updated)
- Usar Write tool solo para regenerar manifest
- No modificar contenido narrativo de los nodos — solo metadata y manifest
