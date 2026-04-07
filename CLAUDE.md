# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Proyecto

Research y preparación de entrevista para **Lola Vilas** — candidata al puesto de **General Manager España** en **HappyRobot**. No es un proyecto de código; es un proyecto de investigación con documentos Markdown.

## Candidata: Lola Vilas

- **Puesto actual:** Country Manager Spain (Mobility) en Uber (2022–presente)
- **Trayectoria:** 18+ años — KPMG → BNP Paribas → Prophet Brand Strategy (Londres) → Amazon (7 años, Senior Business Manager) → Uber
- **Formación:** MBA London Business School (intercambio Columbia), Doble grado Derecho+ADE en ICADE
- **Idiomas:** Español y Catalán nativos, Inglés bilingüe, Francés avanzado, Alemán intermedio
- **Logros clave en Uber:** Triplicó revenue España, escaló de 7 a 19 ciudades, equipo de 50 personas, lideró electrificación (5%→30% EV), +30 apariciones en medios tier-1
- **Logros clave en Amazon:** Lanzó categoría Apparel desde cero (~50% YoY), 75+ partnerships de marca, creó el Vendor Management Playbook de la empresa
- **Reconocimientos:** Top 150 Líderes en Turismo (Sergestur), Top 15 Mujeres Driving Mobility, Social Impact Award (Fundación Integra)
- **LinkedIn:** https://www.linkedin.com/in/lola-vilas-abadie/
- **CV genérico:** `CV Lola Vilas.pdf`
- **CV enviado a HappyRobot:** `CV Lola Vilas- HappyRobot.pdf` (enfocado en Sales/GTM/Revenue)

## HappyRobot — La empresa

- **Qué hace:** Plataforma de AI enterprise que permite construir, desplegar y gestionar agentes autónomos de IA para operaciones empresariales complejas
- **HQ:** San Francisco, CA
- **Fundadores:** Pablo Palafox y Javier Palafox (hermanos españoles)
- **Funding:** $44M Serie B (septiembre 2025) + rondas anteriores
- **Clientes clave:** DHL Supply Chain, Circle Logistics (300K+ llamadas AI en 2024), Samsara, MODE Global, Syfan Logistics
- **Foco vertical:** Logistics & supply chain (principal), customer service, sales, finance, HR, operations
- **Producto core:** AI Workers — agentes con razonamiento agéntico + lógica determinista + integración nativa de herramientas + ejecución multi-canal (teléfono, email, web chat)
- **Diferenciadores:** Governance & evaluations (AI auditor), shared context & memory, forward-deployed engineers, cloud/model-agnostic, compliance (SOC 2, GDPR, HIPAA, EU AI Act)
- **Métricas publicadas:** 100% response rate, 0min FRT, 50%+ handled autonomously, 119x ROI en collections, 1000x scheduling más rápido
- **Web:** https://www.happyrobot.ai/
- **Careers:** https://jobs.ashbyhq.com/happyrobot.ai
- **Contratando en España:** Enterprise Account Executive, Forward Deployed Engineer (Europe), GTM Operations

## Personas clave

| Persona | Rol | Relevancia |
|---------|-----|------------|
| **Aquilino Peña** | Entrevistador (probablemente inversor/board) | Conduce la entrevista. LinkedIn: https://www.linkedin.com/in/aquilino-pe%C3%B1a/ |
| **Pablo Palafox** | Co-founder | LinkedIn: https://www.linkedin.com/in/pablorpalafox/ |
| **Javier Palafox** | Co-founder | LinkedIn: https://www.linkedin.com/in/javierpalafox/ |

## Estructura del proyecto — Content Graph con MkDocs Material

El research está organizado como un **content graph**: cada entidad (empresa, persona, competidor, tecnología, caso de uso, cliente, regulación) es un nodo .md con frontmatter YAML y links entre nodos. MkDocs Material lo convierte en una web navegable con búsqueda.

### Comandos útiles

```bash
# Preview local (localhost:8000)
/Users/pablo/Library/Python/3.14/bin/mkdocs serve

# Build estático
/Users/pablo/Library/Python/3.14/bin/mkdocs build
```

### Árbol de archivos

```
├── CLAUDE.md                          ← Este archivo
├── mkdocs.yml                         ← Config MkDocs Material
├── CV Lola Vilas.pdf                  ← CV genérico de Lola
├── CV Lola Vilas- HappyRobot.pdf     ← CV adaptado para HappyRobot (GTM/Sales focus)
├── docs/
│   ├── index.md                       ← Dashboard: números clave, links rápidos
│   ├── tags.md                        ← Índice de tags
│   ├── empresa/                       ← HappyRobot en profundidad
│   │   ├── happyrobot.md             ← Overview, historia, funding, métricas
│   │   ├── producto.md               ← AI Workers, Governance, Memory
│   │   ├── cultura.md                ← Cultura, valores, modelo de trabajo
│   │   └── expansion-espana.md       ← Por qué España, posiciones abiertas
│   ├── personas/                      ← Nodo por persona relevante
│   │   ├── lola-vilas.md             ← Perfil, fortalezas, mapeo al puesto
│   │   ├── aquilino-pena.md          ← Entrevistador: perfil, qué busca
│   │   ├── pablo-palafox.md          ← Co-founder
│   │   └── javier-palafox.md         ← Co-founder
│   ├── competidores/                  ← Un .md por competidor
│   │   ├── index.md                  ← Tabla comparativa resumen
│   │   ├── bland-ai.md, synthflow.md, retell-ai.md, air-ai.md
│   │   ├── vapi.md, voiceflow.md, sierra-ai.md, parloa.md, poly-ai.md
│   ├── mercado/                       ← Análisis de mercado
│   │   ├── ai-agents-global.md       ← TAM/SAM/SOM AI agents
│   │   ├── logistics-espana.md       ← Sector logístico español
│   │   ├── enterprise-ai-europa.md   ← AI enterprise en Europa
│   │   └── talento-tech-espana.md    ← Mercado laboral tech España
│   ├── tecnologia/                    ← Nodo por tecnología/concepto
│   │   ├── voice-ai.md, agentic-ai.md, forward-deployed.md, ai-governance.md
│   ├── casos-de-uso/                  ← Un .md por vertical/use case
│   │   ├── logistics-operations.md, customer-service.md, collections.md
│   │   ├── sales-inbound.md, recruiting.md
│   ├── clientes/                      ← Un .md por cliente conocido
│   │   ├── dhl.md, circle-logistics.md, samsara.md, mode-global.md, syfan-logistics.md
│   ├── regulacion/                    ← Marco regulatorio
│   │   ├── eu-ai-act.md, gdpr-lopdgdd.md
│   └── entrevista/                    ← Preparación de entrevista
│       ├── index.md                  ← Overview y checklist
│       ├── fit-candidata.md          ← Mapeo Lola ↔ HappyRobot
│       ├── preguntas-vision.md       ← Q&A: visión estratégica
│       ├── preguntas-gtm.md          ← Q&A: GTM España, ventas
│       ├── preguntas-mercado.md      ← Q&A: mercado, competencia
│       ├── preguntas-liderazgo.md    ← Q&A: equipo, cultura, errores
│       ├── preguntas-para-ellos.md   ← Preguntas de Lola
│       └── primeros-90-dias.md       ← Plan de 90 días
```

### Convenciones de cada nodo .md

Cada archivo usa frontmatter YAML:

```yaml
---
title: "Nombre del nodo"
type: empresa | persona | competidor | mercado | tecnologia | caso-de-uso | cliente | regulacion | entrevista
status: pendiente | en-progreso | completo
tags: [tag1, tag2]
updated: 2026-04-06
---
```

Links entre nodos con Markdown estándar: `[HappyRobot](../empresa/happyrobot.md)`

## Metodología de research

El contenido se distribuye en un **content graph** de nodos .md interconectados bajo `docs/`, servido con MkDocs Material para navegación web.

### Protocolo de fuentes y verificación

**Principio:** Cada dato que escribimos es tan útil como la confianza que Lola puede tener en él. Un número sin fuente es peor que no tener número — genera falsa seguridad.

#### Niveles de confianza (A/B/C)

| Nivel | Significado | Criterio |
|-------|-------------|----------|
| **A** | Verificado | Confirmado por 2+ fuentes independientes, o fuente primaria oficial |
| **B** | Plausible | Una sola fuente creíble sin contrastar, o estimación de analista reputado |
| **C** | No verificado | Fuente anecdótica, estimación propia, dato antiguo, o fuentes contradictorias |

#### Reglas de atribución

1. **Todo claim cuantitativo lleva fuente y nivel de confianza (A/B/C).**
   - En tablas: columnas `Conf` y `Fuente`
   - En texto: sufijo `[A: SOURCE-ID]` o `[C: sin fuente]`

2. **Intentar siempre 2+ fuentes para datos clave** (funding, revenue, headcount, market size). Si solo hay 1 fuente, es B como máximo.

3. **Datos contradictorios: mostrar el rango, no elegir uno.** Usar admonition `!!! warning "Dato en conflicto"` con las fuentes y la explicación de la discrepancia.

4. **Registrar toda fuente** en `docs/fuentes/index.md` con ID, URL, tipo, fecha de acceso y nivel de confianza. Categorizar en: `oficiales.md`, `prensa.md`, `datos.md`, `comunidad.md`, `informes.md`.

5. **Separar dato de interpretación.** El dato lleva fuente; la interpretación o el "so what" de Lola es texto propio claramente separado.

6. **Cuando no hay dato: decirlo explícitamente.** `[dato no disponible públicamente]` es mejor que omitirlo silenciosamente.

#### Formato en tablas de datos

```markdown
| Metric | Value | Conf | Fuente |
|--------|-------|------|--------|
| Funding Serie B | $44M (Sept 2025) | A | [HR-WEB] [TC-SERIEB] |
| Valoración | ~$200M | C | Sin fuente pública confirmada |
| Empleados | 150-200 | B | [TRACXN-HR] — LinkedIn muestra ~180 |
```

#### Formato en texto narrativo

```markdown
HappyRobot cerró una Serie B de $44M en septiembre 2025 [A: HR-WEB, TC-SERIEB].
La valoración post-money se estima en ~$200M [C: sin fuente pública].
```

#### Workflow de research por nodo

Al rellenar un nodo:
1. Buscar datos en fuentes oficiales primero (web empresa, press releases)
2. Contrastar con fuentes secundarias (Tracxn, Crunchbase, prensa)
3. Buscar señales cualitativas (Reddit, G2, Twitter, HN)
4. Clasificar cada dato (A/B/C)
5. Registrar fuentes nuevas en `docs/fuentes/index.md`
6. Actualizar `status:` y `updated:` en frontmatter del nodo

### Principios generales del research

1. **Números concretos** — Tablas con métricas, no vaguedades
2. **Competencia detallada** — Tablas comparativas con pricing, features, market share
3. **Pain points del producto** — Basados en reviews reales (Reddit, Trustpilot, G2, etc.)
4. **Propuestas accionables** — No solo problemas, sino soluciones con talking points
5. **Adaptado al entrevistador** — Entender qué busca cada entrevistador y calibrar respuestas

### Herramienta principal: /last30days

Skill de Claude Code para investigación en tiempo real (últimos 30 días) across 10+ fuentes: Reddit, X/Twitter, YouTube, TikTok, Instagram, Hacker News, Polymarket, Bluesky, web.

Uso: `/last30days [tema]`

Configuración en `.claude/last30days.env` del proyecto.

## Áreas de investigación prioritarias

### 1. HappyRobot — Empresa (`docs/empresa/`)
- Historia, cultura, valores, filosofía de founders → `cultura.md`
- Funding rounds, inversores, valoración → `happyrobot.md`
- Producto en detalle → `producto.md`
- Clientes y casos de uso → `docs/clientes/`, `docs/casos-de-uso/`
- Expansión España → `expansion-espana.md`

### 2. AI Agents Landscape (`docs/competidores/`, `docs/tecnologia/`)
- Competidores directos → un archivo por competidor en `docs/competidores/`
- Tendencias → `docs/tecnologia/voice-ai.md`, `agentic-ai.md`, etc.
- Tamaño de mercado → `docs/mercado/ai-agents-global.md`

### 3. Mercado España (`docs/mercado/`)
- Sector logístico → `logistics-espana.md`
- Enterprise AI Europa → `enterprise-ai-europa.md`
- Talento tech → `talento-tech-espana.md`
- Regulación → `docs/regulacion/eu-ai-act.md`, `gdpr-lopdgdd.md`

### 4. Entrevista (`docs/entrevista/`)
- Perfil entrevistador → `docs/personas/aquilino-pena.md`
- Fit candidata → `fit-candidata.md`
- Preguntas por categoría → `preguntas-vision.md`, `preguntas-gtm.md`, etc.
- Plan 90 días → `primeros-90-dias.md`

## Research Workflow

Este proyecto usa un workflow de research por oleadas. Ver `docs/_playbook.md` para la estrategia completa y `docs/_manifest.md` para el estado actual.

### Skills disponibles
- `/research-launch [seccion]` — Lanza oleada de research (max 6 agentes, background)
- `/write-wave [seccion]` — Lanza escritores para nodos con research completo
- `/research-qa` — Audita, cross-checks, y finaliza el content graph

### Reglas clave
- Máximo 6 agentes por sesión
- Research agents siempre con `run_in_background=true`
- Nunca escribir archivos >50 líneas en contexto principal — delegar a subagentes
- Nunca leer research outputs completos en contexto principal
- Manifest es la fuente de verdad cross-sesión
- Late notifications = dismiss con one-liner si ya integrado

## Idioma

Los documentos de research se escriben en **español**, con términos técnicos en inglés donde sea natural. Las respuestas de entrevista pueden ser en español o inglés según el contexto de la entrevista.
