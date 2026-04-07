---
title: "Retell AI"
type: competidor
status: completo
tags: [competidor, voice-ai, usa, yc, developer-first, capital-efficient]
updated: 2026-04-07
---

# Retell AI

Plataforma developer-first de voice AI para automatización de llamadas telefónicas. Fundada en 2023 por un equipo de 5 co-founders ex-ByteDance/Google/Meta (YC W24), destaca por su **capital efficiency excepcional**: con solo $4.6M en seed funding y ~25 empleados, alcanzó **$40M+ ARR** en enero 2026, rentabilidad, y **50M+ llamadas/mes** para 3,000+ empresas. Nombrada en **Wing VC Enterprise Tech 30** (abril 2026). Compite con [HappyRobot](../empresa/happyrobot.md) en voice AI pero con modelo radicalmente distinto: Retell = self-serve developer platform para voz; HappyRobot = AI Workers multi-canal y multi-vertical con forward-deployed engineers para enterprise.

---

## Ficha rápida

| Dato | Valor | Conf. |
|---|---|---|
| **Web** | [retellai.com](https://www.retellai.com) | A |
| **HQ** | San Carlos, California | A |
| **Fundadores** | Bing Wu (CEO, ex-ByteDance), Zexia Zhang (CTO, ex-Google), Todd Li (President, ex-Google), Weijia Yu (COO, ex-Meta), Evie Wang (CMO, ex-ByteDance) | A |
| **Empleados** | ~25 FT on-site; ~94 estimado Latka/Tracxn | B |
| **Funding total** | ~$5.1M (seed) | A |
| **Última ronda** | $4.6M Seed (mayo 2024, Alt Capital lead) | A |
| **Valoración** | No divulgada; probablemente no necesitan Serie A dado $40M+ ARR y rentabilidad | C |
| **ARR estimado** | $40–50M (ene–abr 2026) | A/B |
| **Clientes** | 3,000+ empresas; Anker, PWC, Twilio, Sunshine Loans, Everise, Medical Data Systems | A |

!!! warning "Dato en conflicto: revenue y headcount"
    Latka reporta $7.2M revenue con 41 personas (2025), pero Retell claims $40M ARR con ~25 personas (nov 2025). Posible explicación: Latka mide revenue acumulado vs. ARR annualizado, y headcount 25 puede ser FT vs. 41 incluyendo contractors. Los $50M ARR de abril 2026 son self-reported vía PR.

---

## Producto

### Plataforma core

- **Posicionamiento:** "3rd generation Voice AI" — LLM-powered (vs. 1st gen IVR, 2nd gen NLP bots)
- **Enfoque:** "Production first, demos second" — infraestructura from scratch, no wrapper de APIs
- **Multi-canal (desde ene 2026):** Voice + chat + email + SMS

### Especificaciones técnicas

| Feature | Detalle | Conf. |
|---------|---------|-------|
| **Latencia** | ~600ms response time (reducida ~30% adicional en ene 2026) | A |
| **Turn-taking** | Modelo propietario: sabe cuándo hablar y escuchar, manejo natural de interrupciones | A |
| **Voices** | Ultra-realistic, ElevenLabs, OpenAI, Cartesia, Minimax, Fish | A |
| **LLM support** | GPT-4.1, GPT-5, Claude 4.6 Sonnet, Gemini, modelos budget (nano/mini) | A |
| **Idiomas** | 50+ idiomas (incluye español España + LatAm) | A |
| **Function calling** | Real-time: booking, pagos, actualización registros, live transfers | A |
| **Knowledge Base** | Streaming RAG con auto-sync | A |
| **Telephony** | SIP trunking, BYOC, caller ID branded, batch calling sin límite de concurrencia | A |
| **QA & Testing** | Automated QA (lanzado dic 2025) — simulación, monitoreo continuo, analytics | A |
| **No-code builder** | Drag-and-drop designer con guardrails | A |
| **Concurrencia** | 20 llamadas simultáneas gratis, escalable | A |

### Funcionalidades enterprise (ene 2026)

- SSO, role-based access control
- PII redaction y data masking
- Deployment: cloud, VPC, on-premises
- Batch calling campaigns sin límite de concurrencia

### Compliance y seguridad

| Certificación | Estado | Conf. |
|---------------|--------|-------|
| SOC 2 Type II | Sí | A |
| HIPAA | Sí | A |
| PCI-DSS | Sí | A |
| GDPR | Sí (Standard Contractual Clauses; **sin servidores en EU**) | B |
| EU AI Act | **No mencionado** | C |

**Nota GDPR:** Retell claims GDPR compliance pero **no tiene servidores en la UE**. Usa Standard Contractual Clauses. Competidores europeos como Famulor se posicionan como "GDPR alternative" con EU hosting — debilidad real para enterprise europeo.

### Logistics vertical

Retell tiene una **vertical page dedicada a logistics** con dispatch & load booking, rate negotiations, shipment status updates, carrier sourcing e integración TMS (DAT, Truckop, McLeod). **Pero:** solo 1 case study público en logistics (Spare: 5% → 30% call handling). Comparado con HappyRobot que tiene DHL, Circle (300K+ llamadas), Samsara, MODE, Syfan — expertise superficial.

---

## Clientes y métricas

### Cifras generales

| Métrica | Valor | Conf. | Fuente |
|---------|-------|-------|--------|
| Empresas | 3,000+ | A | retellai.com/customers |
| Llamadas AI/mes | 50M+ | B | Wing VC ET30 PR |
| Crecimiento usuarios | 300%+ QoQ | B | GlobeNewsWire dic 2025 |
| G2 rating | 4.8/5 (1,414+ reviews) | A | G2 |

### Clientes destacados

| Cliente | Sector | Resultado | Conf. |
|---------|--------|-----------|-------|
| **Anker** | Consumer Electronics | Transformed global customer support | A |
| **Sunshine Loans** | Financial Services | 700K+ monthly applications; abandonment rate 5% | A |
| **Medical Data Systems** | Debt Collection | $280K/mes en collections con AI | A |
| **Everise** | BPO | 65% ticket containment; 600 man-hours saved | A |
| **Matic Insurance** | Insurance | 8,000+ llamadas AI en Q1 2025 | A |
| **TripleTen** | EdTech | 3,000+ horas ahorradas | A |
| **Spare** | Logistics/Freight | IVR: 5% → AI: 30% calls handled | A |
| **AccioJob** | Recruiting | -70% false positives en assessments | A |
| **GiftHealth** | Healthcare | 4x operational efficiency | A |

### Trayectoria de revenue

| Período | ARR | Llamadas/mes | Conf. |
|---------|-----|-------------|-------|
| Jun 2024 | ~$3M | — | B |
| 2025 | $7.2M | 30M+ | B |
| Nov 2025 | $40M ARR | — | A |
| Abr 2026 | $50M ARR (claim) | 50M+ | B |

**Capital efficiency excepcional:** ~$5M raised → $40-50M ARR → profitable. Revenue/empleado: ~$1.6-2M ARR/persona.

---

## Modelo de negocio

### Estructura Pay-As-You-Go

| Componente | Coste/min | Notas |
|-----------|-----------|-------|
| **Base infrastructure** | $0.055 | Obligatorio |
| **TTS (Retell/Cartesia/OpenAI)** | $0.015 | ElevenLabs: $0.040 |
| **LLM Agent** | $0.003–$0.080 | Gemini nano → Claude 4.6 Sonnet |
| **Telephony (Retell carrier)** | $0.015 | $0 con BYOC |
| **Total real (producción)** | **$0.088–$0.190/min** | Rango típico |

### Add-ons

| Add-on | Coste |
|--------|-------|
| Knowledge Base | $0.005/min o $8/mes |
| Batch Calls | $0.005/dial |
| Branded Caller ID | $0.10/llamada outbound |
| PII Removal | $0.010/min |
| Safety Guardrails | $0.005/min |
| Concurrencia adicional | $8/mes por call slot (20 gratis) |

### Enterprise Plan

- **Umbral:** $3K+/mes de gasto
- **Tarifa:** Desde **$0.05/min** (all-in con descuentos)
- **Incluye:** Dedicated support, custom infrastructure, setup gestionado

### Free Tier

$10 de crédito al registrarse. Full platform access.

---

## HappyRobot vs Retell AI

| Dimensión | HappyRobot | Retell AI |
|---|---|---|
| **Modelo** | Managed service con forward-deployed engineers | Self-serve platform (API + no-code) |
| **Foco** | AI Workers multi-modal (phone + email + web chat) | Voice agents phone-first (+ chat/SMS desde 2026) |
| **Vertical core** | Multi-vertical (logistics beachhead + airlines, retail, finserv, utilities) | Horizontal: healthcare, finserv, insurance, retail |
| **Target buyer** | Enterprise ops leaders (non-technical) | Developers y tech-forward ops teams |
| **Memory** | **Shared context & memory** entre interacciones | Sin persistent cross-call memory |
| **Governance** | **AI Auditor + Evaluations** (capa governance única) | SOC2/HIPAA/PCI compliance tools |
| **Multi-agent** | Orquestación multi-agente con shared context | Single-agent workflows |
| **Latencia voz** | No publicado | ~600ms (best-in-class) |
| **Developer experience** | Menos developer-facing | API-first, altamente programable, SDKs |
| **Pricing** | Enterprise contracts (no público) | PAYG $0.088–$0.19/min transparente |
| **Escala clientes** | 70+ enterprise customers (DHL, Samsara, Circle, Job&Talent) | 3,000+ empresas (SMB → enterprise) |
| **Revenue** | No público | $40-50M ARR (con $5M raised) |
| **Europa/España** | **Expansión directa** (hiring GM, AEs, FDEs) | Indirecto (partners: Telvia, Sentrovo) |
| **GDPR/EU AI Act** | GDPR + EU AI Act compliance | GDPR via SCCs (**sin servidores EU**); EU AI Act no mencionado |

### Modelo Platform vs Managed Service

**Retell = "AWS de Voice AI":** Provee infraestructura; el cliente construye la solución. Escala horizontalmente con self-serve. Revenue per-minute usage-based.

**HappyRobot = "Palantir de AI Operations":** Despliega engineers on-site para construir soluciones custom en multiples verticales (logistics, airlines, retail, finserv, utilities). Escala verticalmente con enterprise contracts. Revenue por AI Worker seats.

Retell gana en **volumen de clientes y developer adoption**. HappyRobot gana en **depth of enterprise relationship y stickiness**.

---

## Debilidades y críticas

### De reviews y comunidad

| Debilidad | Detalle | Conf. |
|-----------|---------|-------|
| **Soporte al cliente** | "Non-existent" en múltiples reviews; solo Discord community | B |
| **Billing confuso** | Costes se apilan de forma impredecible; cargos inesperados | B |
| **Barrera técnica** | "Way too complicated" para non-technical; requiere developer para setup real | B |
| **GDPR dudoso** | Sin servidores en EU; "unclear GDPR compliance" según reviews europeos | B |
| **Prompt tuning necesario** | Sin heavy prompt engineering, voces suenan robóticas | B |
| **UK/Middle East gaps** | Falta de disponibilidad en UK; sin soporte nativo UAE | B |
| **RBAC limitado** | Role-based access control y audit logs insuficientes para enterprise | B |

### Debilidades estructurales vs HappyRobot

1. **Sin persistent memory cross-call** — Crítico para workflows multi-step (collections series, sales multi-touch)
2. **Sin governance layer** — Sin equivalente al AI Auditor de HR
3. **Expertise superficial en verticales enterprise** — Solo 1 case study en logistics (Spare) vs. 70+ enterprise customers de HR (DHL, Circle, Samsara en logistics; Job&Talent en recruiting)
4. **Sin orquestación multi-agente** — Single-agent workflows vs. coordinación de múltiples AI Workers
5. **Dependencia developer** — Enterprise ops buyers quieren soluciones turnkey, no APIs

---

## Noticias recientes

| Fecha | Noticia | Fuente |
|-------|---------|--------|
| **Abr 2026** | Nombrada en **Wing VC Enterprise Tech 30** | GlobeNewsWire [A] |
| **Mar 2026** | Evie Wang (CMO) en **Inc. Female Founders 500** | GlobeNewsWire [A] |
| **Ene 2026** | Multi-canal (voice + chat + email + SMS); $40M+ ARR; latencia -30%; 50+ idiomas | GlobeNewsWire [A] |
| **Dic 2025** | Lanzamiento **Automated QA**; $35M+ ARR; 300%+ user growth QoQ | SiliconAngle [A] |
| **Nov 2025** | $40M ARR con ~25 empleados, profitable | About Us [A] |

### Presencia en Europa

| Aspecto | Retell | HappyRobot |
|---------|--------|------------|
| Presencia directa | No | Sí (hiring GM, AEs, FDEs) |
| Data residency EU | **No** | Sí (GDPR + EU AI Act) |
| Partner local España | Telvia | Equipo propio |
| Soporte timezone | US Pacific | Presencia local España |
| Relaciones enterprise | Via partner | Directas (forward-deployed) |

---

## Relevancia para la entrevista

### Talking points concretos para Lola

1. **"Retell valida la oportunidad de voice AI, pero su modelo self-serve no resuelve lo que enterprise necesita."** — $40-50M ARR demuestra que el mercado es real, pero solo 1 case study en logistics (Spare: 30% call handling) vs. 70+ enterprise customers de HappyRobot — DHL, Circle (300K+ llamadas) en logistics, Job&Talent (1M+ AI interviews) en recruiting.

2. **"Su capital efficiency ($5M → $50M ARR) es impresionante, pero el modelo platform tiene techo en enterprise."** — Retell escala en volumen SMB. Para enterprise espanol — logistica (DHL, SEUR), retail, utilities, staffing — se necesita forward-deployed: integracion con sistemas legacy, procesos complejos, compliance local.

3. **"En España, Retell depende de Telvia. Una GM con equipo propio gana."** — Mi experiencia en Uber escalando de 7 a 19 ciudades con equipos locales demuestra que presencia directa > partners.

4. **"Retell no tiene servidores EU ni compliance EU AI Act — deal-breaker creciente para enterprise europeo."** — Post-EU AI Act (agosto 2025), enterprise europeo exige data residency y AI governance.

5. **"Governance es el diferenciador definitivo."** — Sin AI Auditor ni persistent memory, Retell no puede auditar decisiones ni mantener contexto en workflows multi-step. Para collections, freight dispatch, AI recruiting interviews, customer service enterprise: memory + governance = must-have.

6. **"El pricing transparente de Retell es buena óptica, pero los costes se apilan a escala."** — $0.088/min básico → $0.19/min en producción → enterprise desde $0.05/min. Contratos AI Worker bundled de HappyRobot dan certeza presupuestaria.

---

## Fuentes

| Código | URL | Tipo | Conf. |
|--------|-----|------|-------|
| RETELL-WEB | https://www.retellai.com | Web oficial | A |
| RETELL-ABOUT | https://www.retellai.com/about-us | About us | A |
| RETELL-PRICING | https://www.retellai.com/pricing | Pricing (abril 2026) | A |
| RETELL-CUSTOMERS | https://www.retellai.com/customers | Clientes y cases | A |
| RETELL-LOGISTICS | https://www.retellai.com/industry/logistics | Vertical logistics | A |
| RETELL-COMPLIANCE | https://docs.retellai.com/general/compliance | Compliance docs | A |
| RETELL-G2 | https://www.g2.com/products/retell-ai/reviews | G2 (4.8/5) | A |
| RETELL-CB | https://www.crunchbase.com/organization/retell-ai | Crunchbase | A |
| RETELL-YC | https://www.ycombinator.com/companies/retell-ai | YC profile | A |
| GNW-ENE26 | https://www.globenewswire.com/news-release/2026/01/29/3228780/0/en/ | PR ene 2026 | A |
| GNW-DIC25 | https://www.globenewswire.com/news-release/2025/12/17/3207048/0/en/ | PR dic 2025 | A |
| GNW-ABR26 | https://www.globenewswire.com/news-release/2026/04/03/3268014/0/en/ | PR abr 2026 | A |
| RETELL-LATKA | https://getlatka.com/companies/retellai.com | SaaS metrics | B |
| RETELL-TRUSTPILOT | https://www.trustpilot.com/review/retellai.com | Trustpilot | B |
| FAMULOR-GDPR | https://www.famulor.io/blog/retell-ai-alternative-gdpr | GDPR alternative | B |

---

*Ver también: [HappyRobot](../empresa/happyrobot.md), [Bland AI](bland-ai.md), [Synthflow](synthflow.md), [Tabla comparativa competidores](index.md)*
