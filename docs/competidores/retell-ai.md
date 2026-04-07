---
title: "Retell AI"
type: competidor
status: completo
tags: [competidor, voice-ai, usa, yc, developer-first]
updated: 2026-04-07
---

# Retell AI

## Resumen ejecutivo

**Retell AI** es una plataforma developer-first de voice AI para automatización de llamadas telefónicas, fundada en 2023 por un equipo ex-ByteDance/Google/Meta (YC W24). Con $4.6M en seed funding, ha escalado a 1,000+ clientes, 30M+ llamadas/mes y revenue de ~$7.2M (2025). Destaca por su **latencia líder (~600ms)**, calidad de voice turn-taking y herramientas API-first. Compite con [HappyRobot](../empresa/happyrobot.md) en voz telefónica pero con enfoque radicalmente distinto: Retell = self-serve developer tools para voz; HappyRobot = AI Workers multi-canal con forward-deployed engineers para enterprise logistics.

**Takeaway para Lola:** Retell valida la demanda de voice AI pero su modelo developer-first y single-channel lo posiciona lejos del enterprise ops buyer que HappyRobot busca. En España, Retell opera vía partners (Telvia); HappyRobot tendrá presencia directa.

## Ficha de empresa

| Campo | Dato | Confianza | Fuente |
|-------|------|-----------|--------|
| **Nombre** | Retell AI | A | [RETELL-WEB] |
| **Fundación** | 2023 | A | [RETELL-CB] |
| **Founders** | Bing Wu (CEO, ex-ByteDance), Evie Wang (CMO, ex-ByteDance), Zexia Zhang (CTO, ex-Google), Weijia Yu (ex-Meta), Todd Li | A | [RETELL-LI] |
| **HQ** | Saratoga/San Carlos, California | A | [RETELL-CB] |
| **Empleados** | ~94 (ene 2026); 41 en 2025 — crecimiento rápido | B | [RETELL-LATKA] |
| **Y Combinator** | Winter 2024 (W24) | A | [RETELL-CB] |
| **Producto** | Voice AI platform developer-focused para llamadas | A | [RETELL-WEB] |
| **Canales** | Voz (principal), chat, SMS, API | A | [RETELL-WEB] |
| **Foco vertical** | Healthcare, financial services, insurance, logistics (secundario) | A | [RETELL-WEB] |
| **Pricing** | PAYG $0.13–$0.31/min all-in; enterprise desde $0.05/min | A | [RETELL-PRICING] |
| **España/Europa** | Sin oficina directa; partner Telvia en España | B | [RETELL-INTL] |

---

## Funding y performance financiera

| Ronda | Importe | Fecha | Lead / Inversores | Fuente |
|-------|---------|-------|-------------------|--------|
| **Seed** | $4.6M | 2024 | Alt Capital (lead) | [RETELL-CB] |
| **Total** | **$4.6M** | — | Y Combinator, Carya Venture + 20 founders/execs | [RETELL-CB] |

**Inversores notables:** Rajat Suri (co-founder Lyft/Presto), Aaron Levie (CEO Box), Siqi Chen (CEO Runway), Michael Seibel (co-founder Twitch, partner YC), Tyler Bosmeny (co-founder Clever, partner YC).

**Trayectoria de revenue:**

| Período | Revenue | Notas | Confianza |
|---------|---------|-------|-----------|
| Jun 2024 | $3M | — | B |
| 2025 | $7.2M | — | B |
| Annualized | $40M | Con equipo de 25 personas [unverified - fechas conflictivas] | C |

**Escala:** 30M+ llamadas/mes, 10M+ minutos de llamada/mes, 1,000+ clientes business.

---

## Producto y tecnología

### Plataforma core

- **Posicionamiento:** "3rd generation Voice AI" (LLM-powered vs. 1st gen IVR, 2nd gen NLP)
- **Latencia:** ~600ms response time (claim líder en industria)
- **Calidad de voz:** "Ultra realistic voice" con natural turn-taking, interrupciones humanas, filler words

### Funcionalidades clave

| Feature | Descripción |
|---------|-------------|
| **Agentic Framework** | Designer drag-and-drop de flujos de llamada con guardrails |
| **Real-Time Function Calling** | Booking, pagos, actualización de registros, live transfers |
| **Knowledge Base** | Streaming RAG con auto-sync |
| **Multi-Channel** | Voz, chat, SMS, API |
| **QA & Testing** | Simulación de llamadas, monitoreo continuo, analytics de performance |
| **Telephony** | SIP trunking, caller ID branded, números verificados, batch calling |

### Diferenciadores técnicos vs HappyRobot

- **Voice-first focus:** Retell es phone-native (vs. plataforma AI agent más amplia de HR)
- **Developer experience:** API-first, altamente programable (vs. modelo forward-deployed de HR)
- **Turn-taking tech:** Años invertidos en dinámica de conversación natural, manejo de interrupciones
- **Voice models:** Soporta ElevenLabs, OpenAI, otros (vs. approach model-agnostic más amplio de HR)

---

## Pricing

### Estructura Pay-As-You-Go

| Componente | Coste | Notas |
|-----------|-------|-------|
| **Voice Engine base** | $0.07–$0.08/min | ElevenLabs, OpenAI |
| **LLM Agent** | $0.006–$0.06/min | Básico a Claude 3.5 |
| **Telephony (Retell Twilio)** | $0.015/min | Gratis con BYOT |
| **Total real** | **$0.13–$0.31/min** | All-in con features apilados |
| **Concurrencia** | 20 llamadas gratis, luego $8/concurrent call/mes | — |

### Enterprise Plan

- **Umbral:** $3K+/mes de gasto
- **Tarifa:** Desde $0.05/min
- **Incluye:** Descuentos, setup gestionado, mayor concurrencia, soporte premium

### Trial

$10 de crédito gratuito al registrarse.

**vs HappyRobot:** Pricing per-minute de Retell es transparente pero los costes se apilan (voice + LLM + telephony). HappyRobot no publica precios, probablemente contratos enterprise con AI Worker seats bundled vs. usage-based. Retell optimiza para self-serve developers; HappyRobot para deployments enterprise full-stack.

---

## Compliance y seguridad

| Certificación | Estado | Fuente |
|---------------|--------|--------|
| SOC 2 Type II | Sí | [RETELL-DOCS-COMP] |
| HIPAA | Sí | [RETELL-DOCS-COMP] |
| PCI-DSS | Sí | [RETELL-DOCS-COMP] |
| GDPR | Sí | [RETELL-DOCS-COMP] |
| EU AI Act | No mencionado | — |

**Seguridad:** Encriptación end-to-end, datos encriptados at rest/in transit, aislamiento multi-tenant, 99.99% uptime.

**Opciones deployment:** Cloud, VPC, **on-premises** (similar a flexibilidad enterprise de HappyRobot).

**Features enterprise:** SSO, PII redaction, role-based access control, data masking.

---

## Verticales y casos de uso

### Verticales principales

| Vertical | Cliente destacado | Métricas |
|----------|------------------|----------|
| **Healthcare** | Pine Park Health | +38% scheduling NPS |
| **Financial Services** | — | Loan applications, collections |
| **Insurance** | Matic | 8,000+ llamadas Q1 2025 |
| **Logistics** | — | Dispatch services, customer support (secundario) |
| **Home Services** | — | — |
| **Debt Collection** | Medical Data Systems | ~$280K/mes collections, 100% inbound handling |
| **Education** | TripleTen | 3,000+ horas ahorradas, 200 hrs/mes outbound |
| **Lead Gen** | ISpeedToLead | 24/7 outbound, 17K llamadas/mes |

**vs HappyRobot:** Retell indexa fuerte en **healthcare, finserv, insurance** (verticales regulados voice-heavy). HappyRobot se centra en **logistics & supply chain** como vertical core. Solapamiento en logistics/customer service, pero diferente énfasis.

---

## Clientes conocidos

| Cliente | Sector | Detalle |
|---------|--------|---------|
| **PWC** | Consultoría | Enterprise |
| **Twilio** | Telecom/Platform | Enterprise |
| Capsule.com | — | Enterprise |
| GiftHealth | Healthcare | 45–50% llamadas fully automated |
| Pine Park Health | Healthcare | +38% scheduling NPS |
| Everise | Servicios | 65% ticket containment, 600 man-hours saved |
| Inbounds.com | Lead gen | High-ticket campaigns |
| TripleTen | Educación | 17K llamadas/mes |
| Matic | Insurance | 8,000+ llamadas Q1 2025 |
| AccioJob | Talent | -70% false positives |
| ISpeedToLead | Real estate | 24/7 outbound |
| SWTCH | — | -50%+ coste |

**Total:** 1,000+ businesses.

**vs HappyRobot:** Retell sirve SMB-to-mid-market con self-serve + enterprise tier. HappyRobot muestra **DHL Supply Chain, Samsara, Circle Logistics** (300K+ llamadas) — enterprises logísticas más grandes con workflows multi-agent complejos.

---

## Presencia Europa / España

### Operaciones europeas

- **Sin oficina directa** en Europa/España
- **Partners certificados en Europa:**
  - **Telvia** (España, Latam, equipo europeo)
  - **Sentrovo** (Alemania)
  - **SmartVerse Group** (Europa)
- **Multi-idioma:** 31+ idiomas incluyendo español (España + LatAm), francés, alemán, portugués, italiano, holandés
- **Compliance:** GDPR-ready, infraestructura fiscal en 100+ países

**vs HappyRobot:** Retell opera vía **partner network** en Europa. HappyRobot está activamente **hiring en España** (Enterprise AE, Forward Deployed Engineer Europe, GTM Ops) y planificando **expansión directa** con el rol de GM España. Retell = indirecto; HappyRobot = boots-on-ground directo.

---

## Reviews y sentimiento

### G2

**Score:** 4.8/5 (1,414 reviews verificados) [RETELL-G2]

**Fortalezas (usuarios):**

- 85% valoró reconocimiento de voz alto — "faster than human response"
- Respuesta near-instant, lag mínimo
- Integración fluida con campañas de marketing
- Manejo de alto volumen con conversaciones naturales

**Debilidades (usuarios):**

- Naturalidad requiere heavy prompt tuning (filler words, tono robótico sin refinamiento)
- Gaps de debugging/observabilidad (difícil trazar problemas de flujo conversacional)

### Sentimiento Reddit/comunidad

- **Developer love:** "Most realistic sounding agents", "extremely simple to use", "true real-time performance"
- **Frustración non-technical:** "Way too complicated" para non-developers, "gave up after being asked for passport just to test call"
- **Quejas billing:** Cargos sin consentimiento tras trial, "ridiculously complicated" cancelar
- **Preocupaciones GDPR:** "Unclear GDPR compliance", soporte lento en preguntas de data privacy
- **Issues UK/Europa:** Gaps de disponibilidad, respuesta de soporte lenta

**vs HappyRobot:** Retell tiene **alto developer NPS** pero **baja satisfacción de usuarios no-técnicos**. El modelo forward-deployed de HappyRobot apunta a enterprise buyers que quieren soluciones turnkey, no herramientas DIY. Retell = fricción self-serve; HappyRobot = deployment white-glove.

---

## Comparativa directa: Retell AI vs HappyRobot

| Dimensión | Retell AI | HappyRobot | Análisis |
|-----------|-----------|------------|----------|
| **Foco** | Voice agents (phone-first) | AI Workers multi-modal (phone + email + web chat) | HR más amplio |
| **Deployment** | Self-serve API + Enterprise tier | Forward-deployed engineers (white-glove) | Diferente modelo |
| **Arquitectura** | Voice infra + LLM orchestration | Agentic reasoning + deterministic logic + tool integration | HR más sofisticado |
| **Memory** | Sin persistent cross-call memory | Shared context & memory entre interacciones | Ventaja HR significativa |
| **Governance** | Compliance tooling (SOC2, HIPAA, PCI) | **AI Auditor + Evaluations** (capa governance única) | HR ventaja |
| **Vertical** | Healthcare, FinServ, Insurance | **Logistics & Supply Chain** (expertise profundo) | Sin solapamiento directo |
| **Target buyer** | Developers, tech-forward ops teams | Enterprise ops leaders (non-technical) | Diferente segmento |
| **Estrategia Europa** | Partner network (Telvia, Sentrovo) | **Expansión directa** (hiring GM España, AEs, FDEs) | HR ventaja España |
| **Pricing** | PAYG $0.13–$0.31/min | Enterprise contracts (AI Worker seats bundled) [estimate] | Diferente modelo |
| **Perfil cliente** | 1,000+ SMB-to-mid-market | Menos, más grandes enterprises (DHL, Samsara, Circle) | Diferente segmento |

---

## Fortalezas vs [HappyRobot](../empresa/happyrobot.md)

1. **Calidad de voz y latencia:** 600ms latency y turn-taking tech puede superar a HR en realismo conversacional para phone-only use cases.
2. **Velocidad developer:** API self-serve permite experimentación más rápida para equipos técnicos (vs. esperar deployment FDE).
3. **Cobertura vertical más amplia:** Tracción fuerte en healthcare, insurance, financial services (verticales regulados donde HR está expandiéndose).
4. **Transparencia de pricing:** Costes per-minute claros (vs. pricing enterprise opaco de HR).
5. **Momentum de mercado:** 1,000+ clientes, 30M llamadas/mes muestra fuerte product-market fit en segmento voice-first.
6. **Red Y Combinator:** Acceso a alumni YC, inversores y ecosistema para growth.

## Debilidades vs HappyRobot

1. **Sin persistent memory:** No mantiene contexto entre llamadas — crítico para workflows enterprise complejos (series de collections, sales multi-touch).
2. **Limitación single-channel:** Phone-only vs. agentes orquestados phone + email + web chat de HR.
3. **Sin capa de governance:** Sin equivalente al AI Auditor de HR para evaluar calidad de decisiones del agente.
4. **Fricción usuario non-technical:** Alta dependencia developer (vs. deployments FDE-managed para ops buyers).
5. **Expertise de dominio superficial:** Plataforma voice horizontal vs. conocimiento vertical profundo de HR en **logistics & supply chain**.
6. **Estrategia Europa:** Indirecta (partners) vs. **expansión directa de HR en España** con GM local, AEs, FDEs.
7. **Profundidad integración enterprise:** Menos adecuado para integración compleja ERP/WMS/TMS (vs. modelo forward-deployed de HR).
8. **Sin orquestación multi-agente:** Workflows single-agent vs. capacidad de HR de coordinar múltiples AI Workers con shared context.

---

## Relevancia para Lola (GM España)

### Talking points para entrevista

1. **"Retell es un competidor fuerte en voice-first, pero HappyRobot resuelve el problema más amplio de operaciones enterprise."** — Retell = llamadas telefónicas. HappyRobot = workflows orquestados cross-channel.

2. **"Su modelo developer-first funciona para equipos tech, pero enterprise ops buyers necesitan soporte forward-deployed."** — Background de Lola vendiendo a non-technical buyers (Uber city managers, Amazon vendors) se alinea con modelo FDE de HR, no con API self-serve de Retell.

3. **"El éxito de Retell en healthcare/insurance valida la demanda de voice AI — HappyRobot puede ganar logística con expertise de dominio más profundo."** — Usar tracción de Retell como proof-of-market, luego diferenciar en foco vertical.

4. **"En España, Retell depende de partners como Telvia. La expansión directa de HappyRobot con una GM nos da ventaja competitiva."** — Rol de GM de Lola = boots on ground, relaciones locales, ciclos de venta enterprise más rápidos.

5. **"Governance y memory son table-stakes para logística. Retell carece de ambos; HappyRobot tiene AI Auditor + Shared Context."** — Crítico para deployments a escala DHL donde decisiones de agentes necesitan auditing y workflows multi-step necesitan memoria.

6. **"El pricing $0.13–$0.31/min de Retell es transparente pero impredecible a escala. Contratos enterprise con AI Workers bundled dan certeza de coste."** — Frame del modelo de HR como mejor para conversaciones con CFOs.

---

## Registro de fuentes

### Fuentes primarias (Confianza A)

| ID | URL | Tipo |
|----|-----|------|
| [RETELL-WEB] | https://www.retellai.com | Web producto |
| [RETELL-PRICING] | https://www.retellai.com/pricing | Pricing |
| [RETELL-CB] | https://www.crunchbase.com/organization/retell-ai | Crunchbase |
| [RETELL-BLOG] | https://www.retellai.com/blog/seed-announcement | Blog funding |
| [RETELL-CASES] | https://www.retellai.com/customers | Clientes/cases |
| [RETELL-G2] | https://www.g2.com/products/retell-ai/reviews | G2 (4.8/5, 1,414 reviews) |
| [RETELL-DOCS] | https://docs.retellai.com | Docs técnicos |
| [RETELL-DOCS-COMP] | https://docs.retellai.com/general/compliance | Compliance docs |
| [RETELL-BLOG-SEC] | https://www.retellai.com/blog/enterprise-ai-calling-security | Security blog |

### Fuentes secundarias (Confianza B)

| ID | URL | Tipo |
|----|-----|------|
| [RETELL-LATKA] | https://getlatka.com/companies/retellai.com | SaaS metrics |
| [RETELL-LI] | https://www.linkedin.com/company/retellai | LinkedIn |
| [RETELL-INTL] | https://www.retellai.com/partners | Partners Europa |
| [RETELL-COMP] | https://www.retellai.com/comparisons/competitors-overview | Competidores |
| [RETELL-COMP-ANALYSIS] | https://www.dialora.ai/blog/retell-ai-pricing | Análisis pricing |

### Fuentes terciarias (Confianza C)

| ID | URL | Tipo |
|----|-----|------|
| [RETELL-REDDIT] | — | Community reviews (Reddit, Trustpilot aggregation) |
| [RETELL-TP] | https://www.trustpilot.com/review/retellai.com | Trustpilot |
