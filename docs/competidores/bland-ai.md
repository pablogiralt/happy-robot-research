---
title: "Bland AI"
type: competidor
status: completo
tags: [competidor, voice-ai, usa, yc, series-b]
updated: 2026-04-07
---

# Bland AI

## Resumen ejecutivo

**Bland AI** es una plataforma voice-first de AI para automatización de llamadas telefónicas enterprise. Fundada en 2023 por Isaiah Granet y Sobhan Nejad (YC S23), ha crecido de forma explosiva — $65M de funding total en 3 rondas, 75 empleados y millones de llamadas automatizadas. Compite con [HappyRobot](../empresa/happyrobot.md) en un **solapamiento limitado** (atención telefónica, collections, scheduling) pero **diverge estratégicamente**: Bland es *infraestructura para voz*, mientras que HappyRobot es *orquestación de workflows multi-canal*.

**Takeaway para Lola:** Bland es un especialista en voz con ADN developer-first y volatilidad en pricing. El enfoque multi-canal de HappyRobot, el modelo forward-deployed y la especialización vertical en logística crean diferenciación defendible.

## Ficha de empresa

| Campo | Dato | Confianza | Fuente |
|-------|------|-----------|--------|
| **Nombre completo** | Bland AI | A | [BLAND-YC] |
| **Fundación** | 2023 | A | [BLAND-YC] |
| **Founders** | Isaiah Granet (CEO), Sobhan Nejad (COO) | A | [BLAND-YC] |
| **HQ** | San Francisco, CA | A | [BLAND-YC] |
| **Empleados** | ~75 (marzo 2026); rango 51–107 según fuente | B | [BLAND-TC1], [BLAND-PB], [BLAND-TR] |
| **Y Combinator** | Summer 2023 (S23) | A | [BLAND-YC] |
| **Producto** | Voice AI platform — agentes de IA para llamadas telefónicas enterprise | A | [BLAND-WEB] |
| **Canales** | Voz (principal), SMS y chat (secundarios) | A | [BLAND-WEB] |
| **Foco vertical** | Horizontal: financial services, insurance, healthcare, hospitality, telecom | A | [BLAND-WEB] |
| **Pricing** | Pay-per-minute ($0.11–$0.14/min) + suscripción mensual ($0–$499/mo) | A | [BLAND-PR1] |
| **España/Europa** | Sin presencia detectada | A | [BLAND-EU1] |

---

## Funding y valoración

| Ronda | Importe | Fecha | Lead / Inversores clave | Fuente |
|-------|---------|-------|-------------------------|--------|
| **Seed** | ~$9M [derived estimate] | 2023–2024 | Y Combinator, Max Levchin, Piotr Dąbkowski, Jeff Lawson | [BLAND-CB1] |
| **Serie A** | $16M | 2024 | Scale Venture Partners (lead) | [BLAND-CB1], [BLAND-VB] |
| **Serie B** | $40M | Feb 2025 | Emergence Capital (lead) | [BLAND-CB1] |
| **Total** | **$65M** | — | 18 inversores en 3 rondas | [BLAND-CB1] |

**Inversores destacados:** Bali Venture Partners, Emergence Equity Management, Horizon Venture Capital, Marble Creek Ventures, Plug and Play Tech Center [BLAND-CB1].

**Valoración:** No divulgada públicamente. [Estimate] Post-money Serie B probablemente $150–300M, asumiendo dilución típica del 15–25%.

**Velocidad de growth:** De pre-seed a Serie B en **10 meses** [BLAND-TC1] — excepcionalmente rápido. Revenue reportado de $3.8M en 2024 con equipo de 25 personas [BLAND-LT].

---

## Producto

**Categoría:** Voice AI infrastructure platform — IA conversacional para automatizar llamadas enterprise (inbound + outbound).

**Producto estrella:** **Norm** — "the first Voice AI builder", permite crear agentes de voz especificando la funcionalidad deseada [BLAND-WEB].

### Capacidades clave

- Creación de agentes de voz para customer service, scheduling, lead qualification, outbound sales
- SMS y chat (secundario a voz)
- Conversational Pathways para diseñar flujos de llamada
- Red global de entrega de voz con orquestación propietaria
- Custom voice cloning
- Transcripción en tiempo real, inferencia, TTS con modelos custom

### Módulos de la plataforma

| Módulo | Funcionalidad |
|--------|---------------|
| **Build** | Personas, pathways, selección de voz |
| **Deploy** | Integración SIP, API para disparar llamadas, batch uploads CSV |
| **Monitor** | Grabación de llamadas, transcripción, extracción de outcomes, compliance guardrails |
| **Refine** | Testbed para regression testing, detección automática de gaps en knowledge base |

### Opciones de despliegue

- Infraestructura hosted por Bland (default)
- On-premise
- Customer VPC

### Stack tecnológico

- Instancias dedicadas por cliente, datos sin pasar por terceros
- Optimización propietaria con **GPUs V100** (arquitectura Volta de NVIDIA — madura pero **no cutting-edge** en 2026; Blackwell/Hopper son las últimas) [BLAND-TECH1]
- Pipeline STT → LLM → TTS con latencia estructural de 700–1,000ms por turno [BLAND-LAT1]

### Integraciones

Salesforce, HubSpot, Twilio, Five9, Amazon Connect y principales plataformas CRM/CCaaS.

---

## Pricing

**Estructura:** Per-minute + suscripción mensual (introducido diciembre 2025, reemplazando tarifa flat de $0.09/min).

| Plan | Mensualidad | Coste/minuto | Notas |
|------|-------------|-------------|-------|
| **Start** (Free) | $0 | $0.14/min | +55% vs. tarifa anterior de $0.09/min |
| **Build** | $299/mo | $0.12/min | — |
| **Scale** | $499/mo | $0.11/min | — |

**Cargos adicionales:**

- Llamadas fallidas/cortas (<10 seg): $0.015 mínimo
- Transfers (números de Bland): $0.025/min (gratis con Twilio propio)
- SMS: $0.02 por mensaje (inbound o outbound)

**Sentimiento sobre pricing:** El aumento del 55% en diciembre 2025 fue muy criticado en Reddit [BLAND-RD1]. El modelo pay-per-minute dificulta presupuestar [BLAND-RD1].

---

## Verticales y casos de uso

**Verticales principales:** Financial services, insurance, healthcare, hospitality, telecomunicaciones.

**Casos de uso:**

- Inbound call handling (soporte, FAQ)
- Booking/scheduling de citas
- Financial intake
- Logistics ID verification (mencionado, no core)
- Collections
- Outbound sales/lead qualification

**Análisis:** Bland apunta a **automatización telefónica horizontal** sin especialización vertical profunda. La verificación de identidad logística se menciona pero no es pilar de go-to-market, a diferencia del foco logístico de [HappyRobot](../empresa/happyrobot.md).

---

## Clientes conocidos

| Cliente | Sector | Detalle |
|---------|--------|---------|
| TravelPerk | Travel tech | — |
| **Samsara** | IoT/Logistics | **Compartido con HappyRobot** |
| First Financial Bank | Banca | — |
| Kin Insurance | Seguros | — |
| Signant Health | Healthcare | — |
| Innovacer | Healthcare | — |
| Evenup | Legal tech | — |
| Mutual of Omaha | Seguros | — |
| Idaho Housing Finance Agency | Gobierno | — |
| Needle | — | 800K+ llamadas completadas |
| Cleveland Cavaliers | Deportes | — |
| Better.com | Hipotecas | — |
| **Slash** | Fintech/Banking | Case study detallado |

### Case study: Slash (plataforma de banca moderna)

- **Reto:** Crecimiento rápido → retrasos en onboarding, backlog de soporte
- **Solución:** Agentes de voz personalizados por nombre, context-aware, SMS follow-ups, warm transfers con contexto
- **Resultados:** Onboarding -3% tiempo, engagement +7%, CSAT +13 puntos, 5,000+ conversaciones/mes automatizadas [BLAND-CS1]

**Análisis:** Roster de clientes sesgado a **financial services, insurance, healthcare**. Escasos case studies en logística/supply chain vs. HappyRobot (DHL, Circle Logistics, MODE Global, Syfan).

---

## Métricas publicadas

| Métrica | Valor | Confianza | Fuente |
|---------|-------|-----------|--------|
| First-call resolution | 65%+ | B (marketing) | [BLAND-WEB] |
| Time to production | 30 días | B | [BLAND-WEB] |
| Ahorro enterprise | "$100s of millions annually" | C (vago) | [BLAND-WEB] |
| ROI (caso MyPlanAdvocate) | 262x | B | [BLAND-WEB] |

**Comparación con HappyRobot:** 100% response rate, 0min FRT, 50%+ handled autonomously, 119x ROI (collections), 1000x scheduling más rápido. Métricas no directamente comparables (diferentes definiciones).

---

## Latencia

| Métrica | Valor | Fuente |
|---------|-------|--------|
| Latencia real | 900ms – 1.4s | [BLAND-LAT2], [BLAND-LAT3] |
| Benchmark industria (2026) | 500–800ms (best enterprise) | [BLAND-LAT3] |
| Percepción usuario | "800ms creates awkward pauses" | [BLAND-RD1] |

**Bottleneck arquitectónico:** Pipeline STT→LLM→TTS = 700–1,000ms por turno, limitación estructural [BLAND-LAT1]. Latencia "slightly higher on average" vs. Vapi, Retell [BLAND-LAT2]. En producción real, +200–400ms sobre benchmarks anunciados [BLAND-LAT3].

---

## Compliance y governance

| Certificación | Estado | Fuente |
|---------------|--------|--------|
| SOC 2 Type I | Logrado (rápido vía Delve) | [BLAND-COMP1] |
| SOC 2 Type II | Logrado | [BLAND-COMP1] |
| HIPAA | Logrado | [BLAND-COMP1] |
| GDPR | Logrado | [BLAND-COMP1] |
| Pen testing trimestral | Sí | [BLAND-COMP1] |
| **EU AI Act** | **No mencionado** | — |

**Dato relevante:** Bland obtuvo SOC 2 Type I "in a matter of days" con Delve, desbloqueando $500K+ ARR en 1 semana [BLAND-COMP1].

**Comparación:** HappyRobot incluye explícitamente EU AI Act en su compliance. Bland no lo menciona — diferenciador clave para España.

---

## Presencia Europa / España

**Sin evidencia** de presencia física, equipo de ventas o forward-deployed engineers en Europa/España.

**Contexto España (2026):** España posicionándose como "AI epicenter of Europe" (inversión de Amazon de $21B), Agencia Española de Supervisión de IA en A Coruña, múltiples conferencias AI (Barcelona, Granada) [BLAND-EU1].

**Contraste con HappyRobot:** HappyRobot hiring activo en España/Europa — Enterprise Account Executive, Forward Deployed Engineer (Europe), GTM Operations. Founders son españoles (Pablo & Javier Palafox).

---

## Reviews y sentimiento

### G2

**Score:** 5.0/5 (solo 3 reviews) [BLAND-G2] — muestra demasiado pequeña, no estadísticamente significativa. Reviewers alaban Pathways, flexibilidad de webhooks, velocidad de deployment.

### Sentimiento positivo (reviews, Reddit, ProductHunt)

- Diseño intuitivo, ahorra tiempo para equipos de ventas [BLAND-RD1]
- APIs developer-friendly, flexibilidad para integraciones custom [BLAND-RD2]
- "Most powerful for controlling multi-prompt voice bot" (Reddit) [BLAND-RD1]
- Mejoras continuas de producto [BLAND-RD1]

### Sentimiento negativo

- **Soporte al cliente:** "Unresponsive", "difficult getting help", "feeling abandoned" [BLAND-RD1], [BLAND-RD2]
- **Herramientas no-code:** Queja #1 — "no user-friendly dashboard; can't just type 'Change greeting to Holiday Special' and hit save" [BLAND-RD2]
- **Latencia:** 800ms crea pausas incómodas [BLAND-RD1]
- **Pricing volatile:** +55% en diciembre 2025 [BLAND-PR2]
- **Pay-per-minute impredecible:** Dificulta presupuestar [BLAND-RD1]
- Enterprise users "rely on community Discord threads rather than formal support" [BLAND-RD2]

### Sentimiento Reddit (temas clave)

1. **Latencia = pain point #1** — múltiples usuarios reportan 800ms+ [BLAND-RD1]
2. **Soporte deficiente** — quejas dominan reviews negativos, reliance en Discord vs. soporte formal [BLAND-RD2]
3. **Developer vs. non-developer divide** — "Bland requires heavy engineering to get right" [BLAND-COMP2]
4. **Backlash de pricing** — subida de $0.09→$0.14/min (55%) muy criticada [BLAND-RD1]
5. **Quote relevante:** "Testing Bland, Retell, and Vapi — Bland is most powerful for multi-prompt bots, but with more possibilities there are more places where it can fail" [BLAND-RD1]

---

## Comparativa directa: Bland AI vs HappyRobot

| Dimensión | Bland AI | HappyRobot | Análisis |
|-----------|----------|------------|----------|
| **Foco producto** | Voice AI infrastructure (llamadas) | AI agents multi-canal (teléfono, email, web chat) | Bland = narrow/deep; HR = orquestación amplia de workflows |
| **Vertical** | Horizontal (finserv, insurance, health) | **Logistics & supply chain** (principal) | HR vertical focus = mejor product-market fit en logística |
| **Modelo cliente** | Developer-heavy, requiere ingeniería | Forward-deployed engineers (sin equipo dev del cliente) | HR de-risquea implementación para compradores no-técnicos |
| **Canales** | Voz (primario), SMS/chat (secundario) | Teléfono, email, web chat (peso igual) | HR = true omnichannel |
| **Latencia** | 900ms–1.4s | No benchmarkeado públicamente | Latencia de Bland = pain point conocido |
| **Pricing** | $0.11–$0.14/min + suscripción | No divulgado públicamente | Volatilidad de pricing de Bland criticada |
| **Europa** | Sin presencia detectada | Hiring activo en España/Europa, founders españoles | HR tiene ventaja estructural en expansión europea |
| **Compliance** | SOC 2, HIPAA, GDPR | SOC 2, HIPAA, GDPR, **EU AI Act** | HR menciona explícitamente EU AI Act |
| **Clientes logística** | Débil (logistics ID verification mencionado, sin cases) | **Fuerte** (DHL, Circle, Samsara, MODE, Syfan) | HR domina vertical logística |
| **Cliente compartido** | Samsara | Samsara | Potencial desplazamiento competitivo o coexistencia |

---

## Fortalezas vs [HappyRobot](../empresa/happyrobot.md)

1. **Expertise voice-native:** Foco singular en voz = optimizaciones más profundas (custom voice cloning, conversational pathways, grabación/transcripción).
2. **Ecosistema developer:** Pedigree YC, diseño API-first, equipo de 75 personas en crecimiento rápido = comunidad developer fuerte.
3. **Velocidad para voice use cases:** 30 días a producción [BLAND-WEB] — potencialmente más rápido que el modelo forward-deployed de HR para necesidades voice-only simples.
4. **Velocidad de funding:** $65M en <2 años señala fuerte confianza inversora y runway para land-grab.
5. **Flexibilidad horizontal:** No atado a vertical logística — puede pivotar/expandir a cualquier industria con automatización telefónica.

## Debilidades vs HappyRobot

1. **Limitación voice-only:** "Sole focus on voice helps differentiate but drastically limits usability — most enterprise contact centers require multi-channel and multimodal support" [BLAND-COMP5]. HR email/web chat = TAM más amplio.
2. **Dependencia developer:** "Bland requires heavy engineering to get right" [BLAND-COMP2]. Compradores no-técnicos (ops leaders, GMs) prefieren modelo forward-deployed de HR.
3. **Gap no-code:** Queja #1 de usuarios [BLAND-RD2]. Forward-deployed engineers de HR eliminan este problema.
4. **Soporte deficiente:** "Customer service complaints dominate" [BLAND-RD1], Discord-reliant. Forward-deployed model de HR = soporte embebido.
5. **Latencia:** 900ms–1.4s vs. industry best 500–800ms [BLAND-LAT3]. Fricción en conversaciones real-time.
6. **Pricing volatile:** +55% diciembre 2025 [BLAND-PR2], pay-per-minute impredecible. Enterprise buyers prefieren contratos estables.
7. **Presencia logística débil:** Sin case studies logísticos significativos vs. DHL, Circle, MODE, Syfan de HR.
8. **Sin Europa/España:** Zero footprint físico vs. founders españoles de HR + hiring activo en Europa.
9. **Sin shared context/memory:** No enfatizado en marketing de Bland vs. "shared context & memory" de HR.
10. **Sin governance avanzada:** Bland tiene compliance pero no equivalente al "AI Auditor" de HR.

---

## Relevancia para Lola (GM España)

### Talking points para entrevista

1. **"Bland es un player fuerte en infraestructura de voz, pero el approach multi-canal de HappyRobot desbloquea casos de uso que Bland no puede tocar."** — Logística necesita email (confirmaciones BOL), web chat (soporte portal) Y voz. Bland = solo voz.

2. **"El modelo developer-first de Bland genera fricción para empresas españolas sin equipos internos de AI. Nuestros forward-deployed engineers de-risquean la adopción."** — El sector logístico español (Logista, ID Logistics, Ceva) no tendrá ML engineers en plantilla.

3. **"La volatilidad de pricing de Bland (55% de subida en dic 2025) crea incertidumbre presupuestaria. Enterprise buyers en España prefieren contratos predecibles."**

4. **"El compliance con EU AI Act es table-stakes para la expansión en España. HappyRobot lo soporta explícitamente; Bland no lo menciona."** — Diferenciador crítico para empresas españolas risk-averse.

5. **"Nuestro foco vertical en logística nos da ventajas unfair: case studies DHL, Circle Logistics, MODE Global. Bland tiene cero clientes logísticos significativos."**

### Reconocer fortalezas de Bland (honestidad intelectual)

6. **"La expertise voice-native de Bland es best-in-class para pure phone use cases. Pero la mayoría de workflows enterprise son multi-canal."** — Demuestra comprensión del landscape competitivo sin ser dismissive.

7. **"Los $65M de funding de Bland y su red YC les dan fuerte mindshare developer. Nuestra ventaja es la ejecución forward-deployed y el lock-in vertical en logística."**

---

## Posicionamiento de mercado

| | Bland AI | HappyRobot |
|--|----------|------------|
| **Lane** | Voice-first infrastructure layer para software companies y enterprises embebiendo AI telefónico | End-to-end AI workflow orchestration para logistics/supply chain, multi-canal, forward-deployed |
| **Gana cuando** | Software companies necesitando embeddable voice APIs, orgs dev-heavy, pure-play voice, verticales no-logística | Enterprises logística/supply chain, compradores no-técnicos (ops/GM), workflows multi-canal, mercado EU/España, governance-sensitive |

**Zona de solapamiento:** Customer service telefónico, collections, scheduling en clientes compartidos como Samsara.

---

## Registro de fuentes

### Fuentes primarias (Bland AI oficial)

| ID | URL | Tipo | Confianza |
|----|-----|------|-----------|
| [BLAND-WEB] | https://www.bland.ai | Web producto | A |
| [BLAND-PR1] | https://docs.bland.ai/platform/billing | Docs oficiales | A |
| [BLAND-YC] | https://www.ycombinator.com/companies/bland-ai | Perfil YC | A |
| [BLAND-CS1] | https://www.bland.ai/case-studies/slash | Case study | A |

### Funding y datos financieros

| ID | URL | Tipo | Confianza |
|----|-----|------|-----------|
| [BLAND-CB1] | https://www.crunchbase.com/organization/bland-ai | Base datos funding | A |
| [BLAND-PB] | https://pitchbook.com/profiles/company/552888-28 | Base datos financiera | B |
| [BLAND-VB] | https://venturebeat.com/ai/bland-ai-scores-16m-to-automate-enterprise-phone-calls-with-agents | Noticia | A |
| [BLAND-LT] | https://getlatka.com/companies/bland.com | SaaS metrics | B |
| [BLAND-TR] | https://tracxn.com/d/companies/bland/__U3PFUE4xCNcou4lVFSJVlH5qI8FLOCBiCanU-A4pnzs | Base datos empresa | B |

### Reviews y sentimiento

| ID | URL | Tipo | Confianza |
|----|-----|------|-----------|
| [BLAND-G2] | https://serviceagent.ai/blogs/bland-ai-review/ | Review aggregation | B |
| [BLAND-RD1] | https://www.dialora.ai/blog/bland-ai-review | Review aggregation (Reddit) | B |
| [BLAND-RD2] | https://prospeo.io/s/bland-ai-pricing-reviews-pros-and-cons | Review aggregation | B |
| [BLAND-PR2] | https://www.lindy.ai/blog/bland-ai-pricing | Análisis pricing | A |

### Análisis competitivo

| ID | URL | Tipo | Confianza |
|----|-----|------|-----------|
| [BLAND-COMP1] | https://delve.co/case-study/bland-soc2-compliance-delve-success | Case study compliance | A |
| [BLAND-COMP2] | https://www.autointerviewai.com/blog/top-5-bland-ai-alternatives-2026 | Comparativa competidores | B |
| [BLAND-COMP5] | https://www.openmic.ai/blog/5-best-happyrobot-ai-alternatives-pricing-features-in-2025 | Comparativa competidores | B |

### Técnico y performance

| ID | URL | Tipo | Confianza |
|----|-----|------|-----------|
| [BLAND-TECH1] | https://www.fluence.network/blog/nvidia-v100/ | Análisis tech | A |
| [BLAND-LAT1] | https://www.retellai.com/blog/bland-ai-reviews | Review competidor | B |
| [BLAND-LAT2] | https://thegrowthengine.net/vapi-vs-bland-ai-real-world-voice-latency-benchmark/ | Benchmark terceros | B |
| [BLAND-LAT3] | https://www.trillet.ai/blogs/voice-ai-latency-benchmarks | Análisis industria | A |

### Noticias

| ID | URL | Tipo | Confianza |
|----|-----|------|-----------|
| [BLAND-TC1] | https://techcrunch.com/2026/03/26/why-hiring-the-weirdos-works/ | Noticia | A |
| [BLAND-EU1] | https://eadoz.com/amazon-21-billion-spain-investment-in-ai-and-data-centers-2026/ | Noticia | A |

### Niveles de confianza por categoría

| Categoría | Confianza | Notas |
|-----------|-----------|-------|
| Funding | **A** | Crunchbase + VentureBeat corroboran |
| Producto | **A** | Web oficial + docs |
| Pricing | **A** | Docs oficiales billing + cambios recientes |
| Empleados | **B** | Varianza entre fuentes (51–107) |
| Clientes | **A** | Web oficial + case studies |
| G2 Reviews | **C** | Solo 3 reviews — no estadísticamente válido |
| Sentimiento Reddit | **B** | Agregado desde review sites citando Reddit |
| Benchmarks latencia | **B** | Testing terceros, no publicado por Bland |
| Presencia Europa | **A** | Alta confianza en la ausencia de evidencia |
| Posicionamiento competitivo | **B** | Derivado de múltiples análisis competitivos |
