---
title: "Synthflow"
type: competidor
status: completo
tags: [competidor, voice-ai, no-code, alemania, series-a, bpo]
updated: 2026-04-07
---

# Synthflow

Plataforma de voice AI no-code con sede en **Berlin, Alemania**, que permite crear y desplegar agentes de voz para automatización de llamadas telefónicas. Fundada en 2023 por los hermanos Astabatsyan (ex-BCG, Rocket Internet) y Sassun Mirzakhan-Saky, ha levantado **$30M** (Serie A liderada por Accel, junio 2025). Gestiona **45M+ llamadas** con **1,000+ clientes**. Compite con [HappyRobot](../empresa/happyrobot.md) en voice AI pero en **segmentos diferentes**: Synthflow es *voice-first, no-code* (SMB/mid-market, BPO/call centers); HappyRobot es *enterprise agentic AI, multi-canal* con foco vertical en logistics.

---

## Ficha rápida

| Dato | Valor | Conf. |
|---|---|---|
| **Web** | [synthflow.ai](https://synthflow.ai/) | A |
| **HQ** | Berlin, Alemania (Kurfürstendamm 15) | A |
| **Fundadores** | Hakob Astabatsyan (CEO, ex-BCG/Rocket Internet), Albert Astabatsyan (CPO, hermano, ex-BCG/Rocket Internet), Sassun Mirzakhan-Saky (CTO) | A |
| **Empleados** | ~72 (feb 2026) | B |
| **Funding total** | $30M (3 rondas) | A |
| **Última ronda** | $20M Serie A (jun 2025, Accel lead) | A |
| **Valoración** | No publicada; estimación $80–150M post-money Serie A | C |
| **ARR estimado** | $1.1M (sept 2025) | B |
| **Clientes** | 1,000+ de pago (30,000+ cuentas registradas); BPO multinacional, Smartcat, Freshworks (partnership) | A/B |

!!! warning "Dato en conflicto: Cuentas vs Clientes"
    Synthflow reporta "30,000+ accounts" en su web pero "1,000+ customers" en PR de Serie A. La diferencia sugiere que ~29,000 son cuentas free/trial y ~1,000 son clientes de pago.

---

## Producto

### Plataforma core

- **Visual Flow Designer:** Constructor drag-and-drop node-based para diseñar flujos de llamada sin código. Cada nodo maneja una tarea específica.
- **BELL Framework:** Metodología enterprise para deployment — Build, Evaluate, Launch, Learn. Lanzado en 2026 [B: SYNTH-BLOG].
- **Test Center:** Testing automatizado de agentes a escala — señala ambición enterprise [B: SOFTAILED-REVIEW].

### Voice & Language

| Capacidad | Detalle | Conf. |
|-----------|---------|-------|
| **Latencia** | <100ms con infraestructura de telefonía propietaria | B |
| **Multi-idioma** | 30-50+ idiomas con acentos regionales via **ElevenLabs** | A |
| **Modelo BYOK** | Bring Your Own Keys — usuario paga separadamente por ElevenLabs, LLM, transcriber | A |

### Integraciones

- **200+ integraciones:** Salesforce (AppExchange listing), HubSpot, Freshworks (partnership estratégica), GoHighLevel, Zapier, Make
- **CCaaS:** Five9, Genesys, RingCentral, Cisco, Avaya
- **Calendarios:** Google Calendar, herramientas de datos

### White-label capabilities

- Branding custom, dominios custom, subaccounts, Stripe rebilling integrado
- Coste: $2,000/mes como add-on [A: SYNTH-PRICING]
- **Calidad reportada:** Reviews mixtas — usuarios reportan que branding de Synthflow persiste a pesar de promesas [B: Trustpilot]

### Compliance

| Certificación | Estado | Conf. |
|---------------|--------|-------|
| SOC 2 | Sí | A |
| HIPAA | Sí | A |
| PCI DSS | Sí | B |
| GDPR | Sí | A |
| ISO 27001 | Sí | A |
| EU AI Act | **No mencionado** | B |

---

## Clientes y métricas

### Métricas agregadas

| Métrica | Valor | Conf. | Fuente |
|---------|-------|-------|--------|
| Clientes de pago | 1,000+ | A | [SYNTH-SERIES-A] |
| Llamadas acumuladas | 45M+ | A | [TECHCRUNCH] |
| Llamadas mensuales | 5M/mes | B | [SYNTH-SERIES-A] |
| Crecimiento YoY | 15x | B | [SYNTH-SERIES-A] |
| Retención enterprise | 90%+ | B | [SYNTH-SERIES-A] |
| Revenue | $1.1M (sept 2025) | B | [GETLATKA] |
| G2 rating | 4.9/5 (999 reviews) | A | [G2] |

### Case studies conocidos

| Cliente/Caso | Sector | Métricas | Conf. |
|-------------|--------|----------|-------|
| BPO multinacional ($230M revenue) | BPO | 600K+ llamadas/mes, 40+ agentes, 15+ idiomas, deployment en 60 días | A |
| Top U.S. CRM platform (anónimo) | SaaS | 500K+ llamadas/mes, voice AI white-labeled embebido | B |
| Smartcat | Language AI | -70% coste booking, +24% llamadas contestadas | A |
| **Freshworks** (partnership) | CRM/CCaaS | 65% rutina automatizada, -75% wait times | A |
| Medbelle | Healthcare | +60% eficiencia scheduling, 2.5x citas cualificadas | A |

**Dato clave para Lola:** Synthflow tiene **cero clientes logísticos/supply chain**. Ninguna mención de logistics como vertical.

---

## Modelo de negocio

### Pricing (abril 2026)

| Tier | Coste base | Features clave | Conf. |
|------|-----------|----------------|-------|
| **Pay-as-you-go** | $0.09/min (voice engine) | 5 concurrent calls, unlimited agents, API & integraciones | A |
| **Enterprise** | Custom ($0.07-0.08/min) | 10,000+ min/mes, SLA 99.99%, SIP Trunking, solution architect dedicado | A |

### Costes adicionales (BYOK)

| Componente | Coste | Conf. |
|------------|-------|-------|
| Voice engine (Synthflow) | $0.09/min | A |
| LLM (GPT-4.1 mini) | $0.02/min | A |
| LLM (GPT-4.1) | $0.05/min | A |
| Telephony (Synthflow-managed Twilio) | $0.02/min | A |
| **Total all-in típico** | **$0.11–$0.24/min** | B |

### Add-ons

| Add-On | Coste | Conf. |
|--------|-------|-------|
| Performance Routing | $0.04/min | A |
| Global Low Latency Edge | $0.04/min | A |
| **White-Label & Reseller** | **$2,000/mes** | A |
| Concurrent call adicional | $20/call/mes (max 50) | A |

### Modelo de negocio

- **Product-led growth (PLG):** Free builder + PAYG convierte SMBs sin fricción
- **White-label/agency:** Revenue stream adicional para resellers y BPOs
- **Partnership CRM:** Integración embebida en Freshworks (distribución a escala)

---

## HappyRobot vs Synthflow

| Dimensión | HappyRobot | Synthflow |
|---|---|---|
| **Segmento target** | Enterprise-first | SMB → mid-market → enterprise (PLG) |
| **Vertical foco** | Multi-vertical (logistics beachhead) | BPO/call centers, healthcare, real estate |
| **Modelo lógica** | **Agentic AI + determinista (híbrido)** | Flow-based determinista only |
| **Canales** | Teléfono, email, web chat (peso igual) | Voz (principal), chat, SMS, WhatsApp |
| **No-code** | Forward-deployed engineers | Muy maduro (visual builder) |
| **Latencia voz** | No benchmarkeado públicamente | <100ms (telefonía propietaria) |
| **Governance** | **AI Auditor + evaluations framework** | No tiene AI auditor |
| **Shared context** | **Shared context & memory entre agentes** | No mencionado |
| **Compliance** | SOC 2, HIPAA, GDPR, **EU AI Act** | SOC 2, HIPAA, PCI DSS, GDPR, ISO 27001 |
| **Outbound UE** | Approach compliant | **Restricción legal** marketing calls |
| **Clientes logística** | DHL, Circle, Samsara, MODE, Syfan | **Cero** |
| **Europa** | Hiring en España, founders españoles | HQ Berlin |
| **Funding** | $44M+ (Serie B) | $30M (Serie A) |
| **Empleados** | 150-200 (est.) | ~72 |

**Sin solapamiento significativo.** Synthflow es voice-first, no-code para BPOs/SMBs. HappyRobot es enterprise agentic AI multi-canal con expertise vertical en logistics.

---

## Debilidades y críticas

### Problemas reportados (G2, Reddit, Trustpilot)

| Problema | Detalle | Frecuencia |
|----------|---------|------------|
| **Soporte lento** | Respuestas 24+ horas, "more questions than solutions" | Frecuente |
| **Testing limitado** | Probar llamadas reales consume minutos pagados | Frecuente |
| **Plataforma capada en tiers bajos** | "Half the platform crippled unless on enterprise" | Frecuente |
| **Billing problemático** | Cargos tras cancelación, "bait and switch" pricing | Moderado |
| **Performance inconsistente** | Latency spikes, agentes pierden hilo fuera de script | Moderado |
| **White-label incompleto** | Branding Synthflow persiste a pesar de promesas | Moderado |
| **Workflows complejos limitados** | "Rigid when setting up advanced branching or passing dynamic variables" | Moderado |
| **Límite llamadas diarias** | ~1,000 calls/día en planes standard | Importante |

### Debilidades estructurales

1. **Revenue muy bajo vs funding:** $1.1M revenue con $30M levantados sugiere burn rate elevado [B: GETLATKA]
2. **Dependencia BYOK:** No controla componentes core de su stack (ElevenLabs + OpenAI)
3. **Restricción outbound UE:** Marketing calls automatizadas ilegales sin consentimiento explícito previo
4. **No-code ceiling:** Ventaja para simplicidad pero limitación para complejidad enterprise
5. **Sin vertical depth:** Horizontal play sin expertise profundo en ningún vertical

---

## Noticias recientes

| Fecha | Evento | Fuente |
|-------|--------|--------|
| **Q1 2026** | Lanzamiento **BELL Framework** + Test Center | SYNTH-BLOG [A] |
| **Q1 2026** | Partnership **Freshworks** — voice AI embebido en Freshcaller/Freshdesk | SYNTH-FRESHWORKS [A] |
| **Nov 2025** | Contratación **Joe Havlik** como VP Global Revenue (ex-Nokia, RingCentral, Cognigy) | BusinessWire [A] |
| **Jun 2025** | **Serie A $20M** liderada por Accel | BusinessWire, TechCrunch [A] |
| **2026** | Expansión a EE.UU. con oficina en Dallas | BusinessWire [B] |

### Presencia en Europa

| Aspecto | Detalle | Conf. |
|---------|---------|-------|
| **HQ** | Berlin, Alemania | A |
| **Entidad legal** | AgentFlow AI GmbH | A |
| **Idioma español** | Soportado (50+ idiomas) | A |
| **Oficina en España** | No | B |
| **GDPR** | Compliant | A |
| **EU AI Act** | No mencionado | B |
| **Restricción outbound UE** | Marketing calls automatizadas ilegales sin consentimiento explícito | A |

---

## Relevancia para la entrevista

### Talking points concretos para Lola

1. **"Categoría diferente, no competidor directo"** — Synthflow es voice-first, no-code, enfocado en BPOs y SMBs. HappyRobot es enterprise agentic AI multi-canal con expertise vertical en logistics.

2. **"Zero amenaza en logistics"** — Synthflow tiene cero clientes logísticos. Ni una mención de logistics como vertical. HappyRobot posee el vertical con DHL, Circle, Samsara, MODE, Syfan.

3. **"Ventaja regulatoria de HappyRobot en UE"** — Synthflow enfrenta restricciones legales para outbound calls en UE. HappyRobot cumple EU AI Act y tiene approach compliance-first.

4. **"No-code vs agentic = complejidad diferente"** — El no-code de Synthflow es perfecto para flujos simples. Pero para operaciones enterprise multi-step (tracking de envíos, collections, scheduling logístico), el agentic reasoning de HappyRobot es necesario.

5. **"Base Berlin valida el mercado europeo"** — Synthflow con funding europeo (Atlantic Labs, Accel) demuestra demanda real de voice AI enterprise en Europa. Buena señal para la expansión de HappyRobot en España.

6. **"Revenue gap sugiere oportunidad"** — Synthflow tiene $1.1M revenue con $30M levantados — todavía buscando PMF enterprise. HappyRobot con $44M+ y DHL ya tiene tracción enterprise demostrada.

---

## Fuentes

| Código | URL | Tipo | Conf. |
|--------|-----|------|-------|
| BUSINESSWIRE | https://www.businesswire.com/news/home/20250624442670/en/ | PR Serie A | A |
| TECHCRUNCH | https://techcrunch.com/2025/06/24/how-synthflow-ai-is-cutting-through-the-noise-in-a-loud-ai-voice-category/ | TechCrunch | A |
| SYNTH-SERIES-A | https://synthflow.ai/news/synthflow-raises-20m-series-a | PR oficial | A |
| CRUNCHBASE | https://www.crunchbase.com/organization/synthflow-ai | Crunchbase | A |
| SYNTH-WEB | https://synthflow.ai/ | Web principal | A |
| SYNTH-PRICING | https://synthflow.ai/pricing | Pricing | A |
| G2 | https://www.g2.com/products/synthflow/reviews | Reviews | A |
| GETLATKA | https://getlatka.com/companies/synthflow-ai | Revenue data | B |
| UNITE-AI | https://www.unite.ai/hakob-astabatsyan-co-founder-ceo-of-synthflow-interview-series/ | Entrevista CEO | A |
| BUSINESSWIRE-VP | https://www.businesswire.com/news/home/20251103012543/en/ | VP Revenue hire | A |
| ACCEL-INVESTMENT | https://www.accel.com/noteworthies/our-investment-in-synthflow... | Accel note | A |
| SYNTH-FRESHWORKS | https://synthflow.ai/success-stories/ | Partnership Freshworks | A |
| TRUSTPILOT | https://www.trustpilot.com/review/synthflow.ai | Trustpilot reviews | B |
| RINGLY-PRICING | https://www.ringly.io/blog/synthflow-pricing | Análisis pricing | B |
| RETELL-REVIEW | https://www.retellai.com/blog/synhtflow-ai-review | Review competidor | B |

---

*Ver también: [HappyRobot](../empresa/happyrobot.md), [Bland AI](bland-ai.md), [Retell AI](retell-ai.md), [Tabla comparativa competidores](index.md)*
