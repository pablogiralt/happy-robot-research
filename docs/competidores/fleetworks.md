---
title: "FleetWorks"
type: competidor
status: completo
tags: [competidor, logistics-ai, freight-brokers, marketplace, ai-agents, usa, yc, series-a]
updated: 2026-04-07
---

# FleetWorks

Startup YC (S23) que ha construido un **marketplace AI-powered dual-sided** para freight brokerage. A diferencia de [HappyRobot](../empresa/happyrobot.md) (plataforma horizontal de AI agents), FleetWorks se enfoca exclusivamente en el **matching broker-carrier** con un modelo marketplace + AI dispatcher. Fundada por **Paul Singer** (ex-Uber Freight PM) y **Quang Tran** (ex-Airbnb engineer), ha levantado **$17M** y crecido a 10,000+ carriers y 40+ brokerages en ~6 meses. Su inversor lead (Bill Trenchard, First Round Capital) lideró la ronda seed de Uber en 2010 y fue early investor en Flexport.

---

## Ficha rápida

| Dato | Valor | Conf. |
|---|---|---|
| **Web** | [fleetworks.ai](https://www.fleetworks.ai/) | A |
| **HQ** | New York, NY (oficinas también en SF y Chicago) | B |
| **Fundadores** | Paul Singer (CEO, ex-Uber Freight PM, Yale), Quang Tran (CTO, ex-Airbnb engineer, Carleton) | A |
| **Empleados** | ~18-20 (125% YoY growth) | B |
| **Funding total** | $17M ($500K pre-seed YC + ~$15M Serie A) | A |
| **Última ronda** | ~$15M Serie A (oct 2025, First Round Capital lead) | A |
| **Valoración** | No divulgada | C |
| **ARR estimado** | [dato no disponible públicamente] | — |
| **Clientes** | 40+ brokerages (inc. 15+ del top 100 U.S.), 10,000+ carriers; Uber Freight, Sage Freight, Ally Logistics, KCH Transportation | A |

---

## Producto

### Arquitectura: Marketplace Dual-Sided con AI Agents

FleetWorks opera como un marketplace con dos agentes complementarios en ambos lados del mercado:

#### Always-On Dispatcher (lado carrier)

- **Para quién:** Carriers (owner-operators a flotas grandes)
- **Qué hace:** Agente AI que actúa como dispatcher virtual del carrier
- **Canales:** Teléfono (voz), SMS, email
- Aprende preferencias: tipo de equipo, lanes preferidos, disponibilidad, horarios
- Monitoriza marketplace continuamente y alerta cuando aparece un load que encaja
- Negocia tarifas preliminares y gestiona booking completo
- **Onboarding carrier:** Minutos (verificación automática via Highway y Truckstop) [A: FW-FUND]

#### Always-On Carrier Rep (lado broker)

- **Para quién:** Freight brokers
- **Qué hace:** Agente AI que actúa como carrier sales representative
- Se conecta al **TMS** del broker, email, teléfono
- Identifica y contacta al mejor carrier disponible
- Navega phone trees con **96% success rate** [A: FW-FUND]
- Pre-negocia rates, vetting de carriers (crédito, seguro, historial)
- **Fraud prevention** con verificación de foto y voz del driver [B: FW-AWARD]
- **Onboarding broker:** 4 horas a 1 semana [A: FW-FUND]
- **Capacidad:** 75+ loads/día por agente, proyección a 200+ [B: FC-FW]

#### Operaciones automatizadas

| Operación | Descripción |
|-----------|-------------|
| **Load Booking** | Comparte detalles, discute pricing, asegura booking |
| **Load Tracking** | Llamadas al driver para status updates en tiempo real |
| **Appointment Scheduling** | Contacta facilities sin portal de booking, gestiona re-scheduling |
| **Carrier Vetting** | Verificación automática via Highway (seguro) y Truckstop (baseline) |
| **Fraud Prevention** | Verificación de voz y foto del driver |

### Stack tecnológico

- Voice synthesis + generative AI + integración nativa con TMS [A: HIRETOP-FW]
- Multi-canal: teléfono, SMS, email, WhatsApp, Google Chat, Telegram [B: FW-AWARD]
- Compatible desde Gmail/Google Sheets hasta TMS enterprise [A: FW-FUND]

---

## Clientes y métricas

### Clientes confirmados

| Cliente | Tipo | Detalle | Conf. |
|---------|------|---------|-------|
| **Uber Freight** | Broker (mega) | Cliente desde los primeros meses. Ex-employer del CEO | A |
| **Sage Freight** | Broker (top 100) | Partnership oficial. CEO Bob King: "integrating FleetWorks into our operations" | A |
| **Ally Logistics** | Broker (top 100) | Mencionado en múltiples fuentes | A |
| **KCH Transportation** | Broker (top 100) | Mencionado en múltiples fuentes | A |
| *40+ brokerages total* | — | Incluyendo 15+ del top 100 U.S. | A |
| *10,000+ carriers* | — | Red onboarded en primeros 6 meses | A |

### Métricas de performance

| Métrica | Valor | Conf. | Fuente |
|---------|-------|-------|--------|
| Lift en loads/día/persona | ~30% | A | FW-FUND |
| Gross margin expansion | 1-4% por load | A | FW-FUND |
| Loads/día por rep (con FleetWorks) | 50-60 (vs. 20-30 pre-AI) | B | FW-FUND |
| Phone tree navigation success | 96% | A | FW-FUND |
| Cost per call | ~$1 (vs. $5-15 industria) | B | HIRETOP-FW |
| Trucks gestionados | 5,000+ | B | FW-AWARD |
| Crecimiento MoM | 30% | B | FW-AWARD |
| Objetivo carriers | 50% de carriers activos en EE.UU. para agosto 2026 | B | FW-AWARD |

---

## Modelo de negocio

### Pricing (múltiples modelos reportados)

| Modelo | Detalle | Conf. |
|--------|---------|-------|
| Lado carrier | $20/truck/semana, sin contratos, 2 semanas gratis | B |
| Lado broker (per-load) | $6/load después de 1 mes trial | B |
| Alternativa | ~$1/llamada exitosa (vs. $5-15 industria) | B |

!!! warning "Dato en conflicto — Pricing"
    Discrepancias entre fuentes: $20/truck/semana (Futurepedia), $6/load (Amy.vc), $1/llamada (HireTop). Probable que tenga planes diferenciados carrier vs broker, o que haya evolucionado. No hay pricing público en fleetworks.ai.

### Oportunidad de mercado citada

| Dato | Valor | Fuente |
|------|-------|--------|
| Truckloads diarios en EE.UU. | 200,000+ | PULSE2-FW |
| % gestionados manualmente | ~80% | PULSE2-FW |
| Gasto en headcount operacional (top brokers) | $11B anuales | HIRETOP-FW |
| Carriers con <10 trucks | 96% de la industria | PULSE2-FW |

---

## HappyRobot vs FleetWorks

| Dimensión | HappyRobot | FleetWorks |
|---|---|---|
| **Modelo** | Plataforma de AI agents enterprise | Marketplace dual-sided (carrier <-> broker) |
| **Scope** | Multi-vertical: logistics, CS, sales, finance, HR, ops | Solo freight brokerage (U.S. trucking) |
| **Producto core** | AI Workers con razonamiento agéntico + lógica determinista | AI dispatcher que matchea + negocia |
| **Network effect** | No inherente — cada cliente es deployment independiente | **Sí** — más carriers = más valor para brokers y viceversa |
| **Canales** | Teléfono, email, web chat | Teléfono, SMS, email, WhatsApp, Telegram, Google Chat |
| **TMS integration** | Nativa, scope amplio (tracking, scheduling, collections) | Nativa, scoped a matching/booking |
| **Clientes tipo** | Enterprise diverso (DHL, Samsara, etc.) | Freight brokers mid-to-large + carriers |
| **Geografía** | EE.UU. + expansión Europa (España) | Solo EE.UU. |
| **Pricing** | Enterprise SaaS (no público) | Usage-based (per load/per truck/per call) |
| **Funding** | $44M (Serie B, sept 2025) | $17M (Serie A, oct 2025) |
| **Equipo** | 150-200 personas | ~18-20 personas |
| **Governance/Compliance** | SOC 2, GDPR, HIPAA, EU AI Act, AI auditor | No mencionado públicamente |

### Análisis estratégico

1. **Marketplace vs Platform.** FleetWorks construye un marketplace (network effects, winner-takes-most). HappyRobot construye una plataforma de AI agents (stickiness via integración profunda). Modelos distintos que compiten por el mismo presupuesto del broker.

2. **Depth vs Breadth.** FleetWorks va ultra-deep en matching broker-carrier (un solo workflow, excepcionalmente bien). HappyRobot cubre todo el lifecycle (tracking, scheduling, collections, sales, CS).

3. **Network effect es la ventaja defensible de FleetWorks.** Si consolida el marketplace de matching en US, podría expandirse a otros workflows. El network effect es una barrera que HappyRobot no tiene.

4. **Ventaja HappyRobot:** Mayor funding ($44M vs $17M), equipo mucho más grande (150-200 vs ~20), compliance enterprise, multi-vertical, y expansión geográfica (Europa).

---

## Debilidades y críticas

| Debilidad | Detalle | Conf. |
|-----------|---------|-------|
| **Scope limitado** | Solo freight matching/booking. No cubre tracking, collections, scheduling, CS | B |
| **Solo U.S.** | Sin presencia internacional ni planes de expansión geográfica | A |
| **Equipo muy pequeño** | ~18-20 personas para marketplace dual-sided es lean en exceso | B |
| **Dependencia de network effects** | Si no alcanza masa crítica de carriers, el valor se erosiona | B |
| **Sin compliance enterprise** | No menciona SOC 2, GDPR, HIPAA ni certificaciones | C |
| **Pricing confuso** | Múltiples modelos en fuentes diferentes — pricing inmaduro | B |
| **"Personal touch"** | Algunos clientes prefieren interacción humana que AI no replica | B |
| **Carrier-first puede alienar brokers** | Filosofía "carrier first and carrier centric" puede crear tensión con brokers que pagan | B |

### Señales de riesgo

- **Uber Freight como cliente y riesgo:** Si Uber Freight builds in-house, FleetWorks pierde su referencia más importante [C: análisis]
- **Recepción dividida:** "Reactions remain divided — skeptics question efficacy of AI in nuanced negotiations" [A: FreightCaviar]

---

## Noticias recientes

| Fecha | Noticia | Fuente |
|-------|---------|--------|
| **Oct 2025** | Cierre **Serie A $17M** liderada por First Round Capital | TechCrunch [A] |
| **Oct 2025** | Lanzamiento "always-on dispatcher" para carriers | FW-FUND [A] |
| **Oct 2025** | Partnership con **Sage Freight** anunciada | SAGE-FW [A] |
| **2025** | Premio **FreightWaves AI Excellence in Supply Chain** (inaugural) | FW-AWARD [A] |
| **2025-2026** | Expansión a 40+ brokerages, 5,000+ trucks, 30% MoM growth | FW-AWARD [B] |

---

## Equipo fundador

### Paul Singer — CEO & Co-founder

- **Background:** Product Manager en **Uber Freight**, lideró equipo de Carrier Quality
- **Formación:** Economics, Yale University
- **Filosofía:** "Carrier first and carrier centric" — todo prioriza la relación con el carrier
- **Cita clave:** "Covering a load in 2025 looks way too similar to covering a load in 1980"

### Quang Tran — CTO & Co-founder

- **Background:** Ingeniero en **Airbnb**, reconstruyó arquitectura para estancias largas/flexibles
- **Formación:** Computer Science, Carleton College
- **Pre-Airbnb:** Fundó empresa de AI NFTs

### Relación con Uber Freight

Singer conoce íntimamente los pain points de Uber Freight y construyó FleetWorks para resolverlos. Que Uber Freight sea cliente valida el producto. Bill Trenchard (lead investor) lideró la seed de Uber en 2010, cerrando el círculo.

**Relevancia para Lola:** Lola también viene de Uber (Mobility, no Freight). Puede hablar del "estilo Uber" de product-market fit obsession.

---

## Contexto competitivo — Los "Tres" de FreightCaviar

FreightCaviar identificó tres empresas creando AI agents para freight brokers [A: FC-3CO]:

| Empresa | Enfoque |
|---------|---------|
| **[HappyRobot](../empresa/happyrobot.md)** | Voice AI para operaciones completas: load updates, capacity, check calls, scheduling + negociación |
| **FleetWorks** | Marketplace dual-sided AI: matching carriers con loads |
| **LoadPartner** | AI load coordination: check calls via voz, SMS, email, WhatsApp |

Los tres son YC-backed. Mercado naciente en rápido crecimiento.

---

## Relevancia para la entrevista

### Talking points concretos para Lola

1. **"FleetWorks valida el mercado de AI en freight, pero su modelo marketplace tiene un techo: solo cubre matching."** — Los brokers necesitan automatizar TODO el workflow operativo. HappyRobot es la plataforma completa.

2. **"FleetWorks no tiene presencia en Europa — es 100% U.S."** — Para la expansión española de HappyRobot, FleetWorks no es competidor.

3. **"El network effect del marketplace es su principal ventaja defensible."** — Si consolidan el matching en US, sería difícil desplazarlos en ese workflow específico. Pero el matching es un solo eslabón de la cadena.

4. **"El riesgo para HappyRobot es en el middle market americano."** — FleetWorks puede capturar brokers mid-size antes de que HappyRobot baje a ese segmento. Pero para enterprise y Europa, HappyRobot tiene ventaja clara.

5. **(Conexión Uber)** **"Conozco el ADN de Uber — product-market fit obsession, velocidad de ejecución. FleetWorks hereda esa mentalidad, pero HappyRobot tiene una visión más amplia y enterprise."**

---

## Fuentes

| Código | URL | Tipo | Conf. |
|--------|-----|------|-------|
| TC-FW | https://techcrunch.com/2025/10/14/fleetworks-raises-17m-to-match-truckers-with-cargo-faster/ | TechCrunch | A |
| FW-FUND | https://www.freightwaves.com/news/how-fleetworks-17m-funding-fuels-ai-dispatcher-innovation | FreightWaves | A |
| FC-FW | https://www.freightcaviar.com/fleetworks-raises-17m-for-an-ai-dispatcher-that-never-sleeps/ | FreightCaviar | A |
| AMY-FW | https://blog.amy.vc/fleetworks-17m-series-a-funding-round/ | Amy.vc análisis | B |
| YC-FW | https://www.ycombinator.com/companies/fleetworks | YC profile | A |
| FW-ABOUT | https://www.fleetworks.ai/about | Oficial | A |
| PULSE2-FW | https://pulse2.com/fleetworks-17-million-closed... | Pulse2 | B |
| HIRETOP-FW | https://hiretop.com/blog2/fleetworks-automating-manual-freight-brokerage-operations/ | HireTop | B |
| FW-AWARD | https://www.freightwaves.com/news/fleetworks-ai-powered-carrier-rep-stands-out-from-the-pack | FreightWaves award | A |
| SAGE-FW | https://www.sagefreight.com/news/sage-freight-partners-with-fleetworks... | Sage Freight oficial | A |
| FC-3CO | https://www.freightcaviar.com/these-three-companies-are-creating-freight-broker-ai-agents/ | FreightCaviar | A |
| CRUNCHBASE-FW | https://www.crunchbase.com/organization/fleetworks-cd1a | Crunchbase | A |

---

*Ver también: [HappyRobot](../empresa/happyrobot.md), [Lanesurf](lanesurf.md), [Pallet](pallet.md), [Logistics Operations](../casos-de-uso/logistics-operations.md), [Tabla comparativa competidores](index.md)*
