# Plan: Primer Research Masivo de HappyRobot

## Estado actual
- 61 nodos .md, ~80% vacíos (43 pendiente, 15 en-progreso, 1 completo)
- Solo `lola-vilas.md` está completo. Todo lo demás necesita research.
- Estructura de esqueleto excelente — falta contenido con fuentes.

---

## Estrategia de canales de búsqueda

Cada tema tiene canales óptimos distintos. Definimos qué herramienta y qué fuentes usa cada subagente:

| Canal | Herramienta | Mejor para |
|-------|-------------|------------|
| **Web oficial** (happyrobot.ai, blog) | WebFetch | Datos de producto, métricas, careers, pricing |
| **Crunchbase / Tracxn / PitchBook** | WebSearch + WebFetch | Funding, valoración, inversores, headcount |
| **Press releases / prensa tech** | WebSearch | Rondas, partnerships, expansiones, quotes founders |
| **LinkedIn** | WebSearch (perfil público) | Trayectoria personas, headcount empresa, hiring |
| **G2 / Capterra** | WebSearch + WebFetch | Reviews producto, satisfaction scores, comparativas |
| **Reddit** | /last30days + WebSearch | Sentiment real, pain points, experiencias usuarios |
| **X/Twitter** | /last30days | Buzz reciente, opiniones industria, threads founders |
| **YouTube** | /last30days + WebSearch | Demos producto, entrevistas founders, conferencias |
| **Hacker News** | /last30days + WebSearch | Opiniones técnicas, discusiones sobre AI agents |
| **GitHub** | WebSearch | Repos públicos, actividad técnica founders |
| **Informes industria** | WebSearch | TAM/SAM/SOM, proyecciones mercado, adoption rates |
| **Glassdoor** | WebSearch | Cultura empresa, salarios, reviews empleados |
| **Gobierno/EU** | WebSearch + WebFetch | EU AI Act, GDPR, datos sector logístico España |

---

## Protocolo de fuentes (aplicado por cada subagente)

Cada subagente DEBE devolver sus hallazgos con:

1. **Source ID** para cada fuente (formato: `[SIGLA-TEMA]`, ej: `[HR-WEB]`, `[TC-SERIEB]`, `[G2-BLAND]`)
2. **URL completa**
3. **Tipo**: oficial / prensa / datos / comunidad / informe
4. **Fecha de acceso**: 2026-04-07
5. **Nivel de confianza**: A / B / C
6. **Categoría** para `docs/fuentes/`: oficiales / prensa / datos / comunidad / informes

Al escribir los nodos .md, se aplica:
- Tablas con columnas `Conf` y `Fuente`
- Texto narrativo con sufijo `[A: SOURCE-ID]` o `[C: sin fuente]`
- Datos contradictorios: admonition `!!! warning` con rango
- Dato no disponible: `[dato no disponible públicamente]`

Al final del research, todas las fuentes se registran en `docs/fuentes/index.md` y su subcategoría correspondiente.

---

## OLEADA 1 — Research paralelo masivo

### Grupo A: HappyRobot Core (3 subagentes)

**A1 — Company & Funding**
- Canales: WebFetch (happyrobot.ai, blog), WebSearch (Crunchbase, Tracxn, prensa), /last30days "HappyRobot AI funding"
- Busca: año fundación, historia, todas las rondas (seed, A, B), lead investors por ronda, valoración, headcount (LinkedIn vs Tracxn), revenue signals, métricas de crecimiento
- Output: datos con source IDs para happyrobot.md

**A2 — Producto**
- Canales: WebFetch (happyrobot.ai/product, blog posts técnicos), WebSearch (G2 reviews, Capterra), YouTube (demos)
- Busca: AI Workers features detalladas, Governance & Evaluations, Shared Context & Memory, pricing model, integraciones, stack técnico, reviews reales de usuarios
- Output: datos con source IDs para producto.md

**A3 — Cultura & Founders Philosophy**
- Canales: WebSearch (entrevistas founders, podcasts, conferencias), WebFetch (blog.happyrobot.ai), Glassdoor, LinkedIn posts
- Busca: valores, modelo de trabajo (remote/hybrid/office), filosofía de los Palafox, cómo contratan, cómo escalan, por qué fundaron HR
- Output: datos con source IDs para cultura.md

### Grupo B: Personas Clave (3 subagentes)

**B1 — Aquilino Peña** (CRÍTICO para entrevista)
- Canales: WebSearch (nombre + VC + inversor + fondo), LinkedIn público, Crunchbase (inversor), YouTube/podcasts (entrevistas)
- Busca: fondo VC (¿Kibo Ventures? ¿otro?), portfolio de inversiones, tesis de inversión, rol en HappyRobot (board?), background profesional, estilo como entrevistador/inversor, qué valora en equipos de gestión, apariciones en conferencias
- Output: datos con source IDs para aquilino-pena.md

**B2 — Pablo Palafox** (Co-founder)
- Canales: WebSearch, LinkedIn, GitHub (pablorpalafox), YouTube/podcasts, conferencias tech
- Busca: formación, experiencia pre-HappyRobot, visión técnica, publicaciones, patentes, rol actual (CEO? CTO?), estilo de liderazgo, interviews
- Output: datos con source IDs para pablo-palafox.md

**B3 — Javier Palafox** (Co-founder)
- Canales: igual que B2
- Busca: formación, experiencia pre-HappyRobot, rol actual, área de responsabilidad (sales? ops? product?), publicaciones, entrevistas
- Output: datos con source IDs para javier-palafox.md

### Grupo C: Competidores (9 subagentes — uno por competidor)

Cada subagente sigue el mismo protocolo de búsqueda:

**Canales por competidor:**
1. WebFetch → web oficial (producto, pricing)
2. WebSearch → Crunchbase/Tracxn (funding, HQ, headcount)
3. WebSearch → G2/Capterra (reviews, scores, comparativas)
4. WebSearch → Reddit "nombre_competidor review" / "nombre_competidor vs"
5. WebSearch → prensa tech (TechCrunch, VentureBeat, etc.)

**Datos a recoger por competidor:**
- Ficha: tipo, funding total + última ronda, HQ, foco vertical, pricing, presencia Europa/España
- Producto: features principales, modelo de deployment, integraciones
- Clientes conocidos
- Fortalezas vs HappyRobot (ser honesto)
- Debilidades vs HappyRobot (oportunidades para Lola)
- Sentiment: score G2, themes de reviews positivos/negativos, quejas en Reddit
- Source IDs para cada dato

| # | Competidor | Web a buscar |
|---|------------|-------------|
| C1 | **Bland AI** | bland.ai |
| C2 | **Synthflow** | synthflow.ai |
| C3 | **Retell AI** | retellai.com |
| C4 | **Air AI** | air.ai |
| C5 | **Vapi** | vapi.ai |
| C6 | **Voiceflow** | voiceflow.com |
| C7 | **Sierra AI** | sierra.ai |
| C8 | **Parloa** | parloa.com |
| C9 | **PolyAI** | poly.ai |

### Grupo D: Mercado & Regulación (4 subagentes)

**D1 — AI Agents Global Market**
- Canales: WebSearch (Grand View Research, Gartner, Markets&Markets, CB Insights, McKinsey), informes de industria
- Busca: TAM/SAM/SOM AI agents 2025-2030, CAGR, segmentación por vertical (logistics, customer service, sales), top players por cuota, tendencias (agentic AI, voice AI)
- Output: datos con source IDs para ai-agents-global.md

**D2 — Logistics España**
- Canales: WebSearch (INE, Ministerio Transportes, informes DBK/Alimarket, AECOC), prensa sectorial (El Vigía, Cadena de Suministro)
- Busca: tamaño sector logístico España, top operadores, grado de digitalización, adopción AI, pain points operacionales, nº empresas, empleo en el sector
- Output: datos con source IDs para logistics-espana.md

**D3 — Enterprise AI Europa + Talento Tech España**
- Canales: WebSearch (IDC Europe, Eurostat, McKinsey, Glassdoor, LinkedIn Salary Insights, Levels.fyi)
- Busca: adoption rates AI enterprise por país EU, inversión AI Europa, salarios ML/AI/dev en España (Madrid, Barcelona, remoto), disponibilidad talento, competencia por talento (vs fintechs, big tech offices)
- Output: datos para enterprise-ai-europa.md + talento-tech-espana.md

**D4 — Regulación (EU AI Act + GDPR/LOPDGDD)**
- Canales: WebFetch (eur-lex.europa.eu, aepd.es), WebSearch (análisis legal EU AI Act, implicaciones voice AI)
- Busca: clasificación riesgo AI agents en EU AI Act, requisitos de compliance, timeline implementación, GDPR implicaciones para grabación de voz/llamadas, LOPDGDD específicas España, qué necesita HappyRobot para operar en EU
- Output: datos para eu-ai-act.md + gdpr-lopdgdd.md

### Grupo E: Clientes (1 subagente consolidado)

**E1 — 5 Clientes de HappyRobot**
- Canales: WebSearch (nombre_cliente + "HappyRobot"), WebFetch (case studies en blog HR), prensa
- Busca por cada uno (DHL, Circle Logistics, Samsara, MODE Global, Syfan):
  - Tamaño empresa, vertical, presencia global
  - Caso de uso con HappyRobot
  - Métricas publicadas (ROI, volumen llamadas, ahorro)
  - Quotes o testimonials
  - Desde cuándo son clientes
- Output: datos para los 5 nodos en clientes/

### Grupo F: Señales recientes (/last30days)

**F1-F3 — Tres búsquedas /last30days en paralelo:**

| # | Query | Cubre |
|---|-------|-------|
| F1 | `HappyRobot AI` | Buzz general: noticias, menciones, sentiment sobre la empresa |
| F2 | `AI voice agents logistics 2026` | Tendencias del sector: quién habla de AI agents en logistics |
| F3 | `Bland AI OR Synthflow OR Retell AI OR Sierra AI voice agents` | Competitive intelligence reciente: qué dicen de los competidores |

---

## OLEADA 2 — Escritura de nodos .md

Con los datos de Oleada 1, escribo cada nodo siguiendo:

1. **Protocolo A/B/C** en todo dato cuantitativo
2. **Cross-linking** entre nodos relacionados
3. **Frontmatter** actualizado (status, updated)
4. **Admonitions** para datos en conflicto o gaps

### Orden de escritura (prioridad entrevista):

| Prioridad | Nodos | Por qué primero |
|-----------|-------|----------------|
| 1 | `personas/aquilino-pena.md` | Conocer al entrevistador es lo más urgente |
| 2 | `empresa/happyrobot.md` | Base de todo — Lola debe dominar estos datos |
| 3 | `empresa/producto.md` | Saber qué vende es fundamental |
| 4 | `personas/pablo-palafox.md` + `javier-palafox.md` | Entender a los founders |
| 5 | `empresa/cultura.md` | Para cultural fit en entrevista |
| 6 | `competidores/index.md` + 9 nodos | Tabla comparativa para preguntas de mercado |
| 7 | `mercado/*.md` (4 nodos) | TAM, logistics España, talento — para GTM narrative |
| 8 | `clientes/*.md` (5 nodos) | Casos de éxito para referenciar |
| 9 | `regulacion/*.md` (2 nodos) | Compliance angle para Europa |
| 10 | `empresa/expansion-espana.md` | Enriquecer con todo lo anterior |
| 11 | `fuentes/*.md` | Registro completo de todas las fuentes usadas |

### Al escribir cada nodo se registran las fuentes nuevas en:
- `docs/fuentes/index.md` — Tabla maestra
- `docs/fuentes/oficiales.md` — Webs corporativas, blogs, docs
- `docs/fuentes/prensa.md` — Press releases, artículos
- `docs/fuentes/datos.md` — Crunchbase, Tracxn, PitchBook
- `docs/fuentes/comunidad.md` — Reddit, G2, X, HN
- `docs/fuentes/informes.md` — Gartner, McKinsey, Grand View

---

## Qué NO se hace en este primer research

- **Entrevista Q&A** (`entrevista/preguntas-*.md`) — Requiere todo lo anterior completo
- **Plan 90 días** (`entrevista/primeros-90-dias.md`) — Depende de datos de mercado + competencia
- **Fit candidata update** — Se enriquece después con datos nuevos
- Estos se hacen en una sesión posterior dedicada a prep de entrevista.

---

## Resultado esperado

- ~35 nodos pasan de `pendiente` a `en-progreso` o `completo`
- Tabla comparativa de 9 competidores funcional con datos reales
- Perfil completo de Aquilino Peña (qué busca, cómo entrevista)
- Datos de mercado con fuentes clasificadas A/B/C
- Registro de fuentes poblado en `docs/fuentes/`
- Base sólida para fase 2 (Q&A de entrevista)
