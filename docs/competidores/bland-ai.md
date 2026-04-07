---
title: "Bland AI"
type: competidor
status: completo
tags: [competidor, voice-ai, usa, yc, series-b, developer-first]
updated: 2026-04-07
---

# Bland AI

Plataforma voice-first de AI para automatización de llamadas telefónicas enterprise. Fundada en 2023 por Isaiah Granet y Sobhan Nejad (YC S23), ha crecido de forma explosiva — $65M de funding total en 3 rondas, ~75 empleados y millones de llamadas automatizadas. Se posiciona como "Twilio for AI phone calls" — API-first, developer-focused. Compite con [HappyRobot](../empresa/happyrobot.md) en un **solapamiento limitado** (atención telefónica, collections, scheduling) pero **diverge estratégicamente**: Bland es *infraestructura para voz*, HappyRobot es *orquestación de workflows multi-canal*.

---

## Ficha rápida

| Dato | Valor | Conf. |
|---|---|---|
| **Web** | [bland.ai](https://www.bland.ai) | A |
| **HQ** | San Francisco, CA | A |
| **Fundadores** | Isaiah Granet (CEO, BS 2022 WashU), Sobhan Nejad (COO) | A |
| **Empleados** | ~75 (marzo 2026); rango 51–107 según fuente | B |
| **Funding total** | $65M (3 rondas) | A |
| **Última ronda** | $40M Serie B (ene–feb 2025, Emergence Capital lead) | A |
| **Valoración** | No divulgada; estimación $150–300M post-money Serie B | C |
| **ARR estimado** | $3.8M (2024, equipo de ~25) | B |
| **Clientes** | Cleveland Cavaliers, Better.com, Hertz, Slash, Samsara (compartido con HR), Mutual of Omaha, Needle (800K+ llamadas) | A/B |

---

## Producto

### Core: Voice AI Infrastructure Platform

Bland permite construir, desplegar y gestionar agentes de voz que hacen y reciben llamadas telefónicas. Recientemente expandido a SMS y web chat (omnichannel), aunque voz sigue siendo el producto principal [A: BLAND-WEB].

### Producto estrella: Norm (marzo 2026)

"The first AI assistant that builds production-ready voice agents from a single prompt" — reduce drásticamente el tiempo de creación de agentes. Nuevos agentes en producción en días, no semanas [A: PR Newswire].

### Módulos de la plataforma

| Módulo | Funcionalidad |
|--------|---------------|
| **Build** | Personas, pathways, selección de voz, knowledge bases |
| **Deploy** | Integración SIP, API para disparar llamadas, batch uploads CSV, web widgets |
| **Monitor** | Grabación, transcripción, extracción de outcomes, compliance guardrails |
| **Refine** | Testbed para regression testing, detección automática de gaps |

### Capacidades técnicas

| Capacidad | Detalle | Conf. |
|-----------|---------|-------|
| **API** | REST API completa, developer-first, webhooks, batch calls vía CSV | A |
| **Voice models** | Motor TTS propietario (entrenado con millones de horas de audio conversacional) | A |
| **Custom voices** | Voice cloning desde muestras cortas; 1–15 clones según plan | A |
| **Latencia real** | 900ms–1.4s en producción; ~800ms promedio | B |
| **Conversational Pathways** | Workflow builder para flujos de llamada | B |
| **Integraciones** | Salesforce, Notion, Cal.com, Calendly, HubSpot, Twilio, Five9, Amazon Connect | A |
| **Fine-tuning** | Modelos custom por cliente en infraestructura dedicada | A |
| **Idiomas** | Multi-idioma (inglés principal; español/francés mencionados); solo inglés fiable en producción | B |
| **Escalabilidad** | Hasta 1M llamadas concurrentes (claim marketing) | C |
| **Guard Rails** | Monitoreo real-time de compliance: detección de violaciones TCPA, lenguaje discriminatorio | A |

### Stack tecnológico

- Instancias dedicadas por cliente enterprise, datos sin pasar por terceros [A: BLAND-WEB]
- GPUs V100 (Volta de NVIDIA — madura pero **no cutting-edge** en 2026) [B: análisis tech]
- Pipeline STT → LLM → TTS con latencia estructural de 700–1,000ms por turno [B: Retell AI review]

### Opciones de despliegue

- Infraestructura hosted por Bland (default)
- On-premise / Customer VPC (enterprise)
- BYOT (Bring Your Own Twilio) para reducir costes de transfer

---

## Clientes y métricas

| Cliente | Sector | Detalle | Conf. |
|---------|--------|---------|-------|
| Cleveland Cavaliers | Deportes | — | A |
| Better.com | Hipotecas | Agentes custom de AI | A |
| Hertz | Alquiler vehículos | — | B |
| **Slash** | Fintech/Banking | Case study: onboarding -3% tiempo, engagement +7%, CSAT +13 pts, 5K+ conv./mes | A |
| **Certus AI** | Hospitality | Built voice product on Bland para restaurantes | A |
| **Samsara** | IoT/Logistics | **Compartido con HappyRobot** | B |
| TravelPerk | Travel tech | — | B |
| Needle | — | 800K+ llamadas completadas | B |
| Mutual of Omaha | Seguros | — | B |
| MyPlanAdvocate | Healthcare/Insurance | "$42M en revenue tangible" (claim cliente) | B |

### Métricas publicadas

| Métrica | Valor | Conf. | Fuente |
|---------|-------|-------|--------|
| First-call resolution | 65%+ | B | Marketing web |
| Time to production | 30 días | B | Marketing web |
| ROI (MyPlanAdvocate) | 262x | B | Bland blog |
| Revenue tangible (MPA) | $42M en pocos meses | B | Claim de cliente, no verificado |
| SOC 2 → revenue | $500K+ ARR en 1 semana tras certificación | A | Delve case study |

---

## Modelo de negocio

### Estructura: Per-minute + suscripción mensual

Introducido diciembre 2025, reemplazando tarifa flat anterior de $0.09/min [A: Bland docs].

| Plan | Mensualidad | Coste/min (connected) | Daily Cap | Concurrency | Conf. |
|------|-------------|----------------------|-----------|-------------|-------|
| **Start** (Free) | $0 | $0.14/min | 100 calls | 10 | A |
| **Build** | $299/mo | $0.12/min | 2,000 calls | 50 | A |
| **Scale** | $499/mo | $0.11/min | 5,000 calls | 100 | A |
| **Enterprise** | Custom | Custom | Unlimited | Unlimited | A |

### Cargos adicionales

| Concepto | Coste | Conf. |
|----------|-------|-------|
| Llamadas fallidas/cortas | $0.015/call mínimo | A |
| Transfer time (números Bland) | $0.03–$0.05/min | A |
| SMS | $0.02/mensaje | A |
| BYOT (Bring Your Own Twilio) | Transfer gratis | A |

!!! warning "Subida de pricing del 55%"
    De $0.09/min flat → $0.14/min (plan Start) en dic 2025. Muy criticada en Reddit. Costes ocultos (turbo mode, transfer fees) elevan el effective cost por encima de lo anunciado [B: reviews].

---

## HappyRobot vs Bland AI

| Dimensión | HappyRobot | Bland AI |
|---|---|---|
| **Foco producto** | AI agents multi-canal (teléfono, email, web chat) | Voice AI infrastructure (llamadas) |
| **Approach** | Platform + forward-deployed engineers | API-first, DIY, developer builds |
| **Vertical** | **Logistics & supply chain** (principal) | Horizontal (finserv, insurance, health, hospitality) |
| **Canales** | Teléfono, email, web chat (peso igual) | Voz (primario), SMS/chat (reciente, secundario) |
| **Modelo delivery** | Forward-deployed engineers in situ | Self-service + soporte enterprise |
| **Governance** | AI Auditor + evaluations + EU AI Act | Compliance (SOC2, HIPAA, GDPR) + guardrails básicos |
| **Memory** | Shared context & memory entre agentes | No enfatizado |
| **Europa** | Founders españoles, hiring activo España/Europa | Sin presencia; solo números +1 (US) |
| **Latencia** | No benchmarkeado públicamente | 900ms–1.4s real (pain point) |
| **Pricing** | No divulgado (enterprise contracts) | $0.11–$0.14/min + suscripción; volátil |
| **Clientes logística** | DHL, Circle, Samsara, MODE, Syfan | Débil (Samsara compartido, sin cases logísticos) |
| **Funding** | $44M Serie B + anteriores | $65M total ($40M Serie B) |
| **Equipo** | 150-200 personas (est.) | ~75 personas |

### Síntesis competitiva

Bland y HappyRobot operan en **lanes distintas** con solapamiento limitado:

- **Bland** = infraestructura de voz para empresas tech-savvy que quieren embeber AI telefónico via API
- **HappyRobot** = orquestación end-to-end de workflows multi-canal para logistics/supply chain con implementación managed

**Zona de solapamiento:** Customer service telefónico, collections, scheduling — particularmente visible en el cliente compartido Samsara.

---

## Debilidades y críticas

### Problemas técnicos

| Problema | Detalle | Conf. |
|----------|---------|-------|
| **Latencia** | 800ms–1.4s crea pausas incómodas; "awkward silences" reportadas | B |
| **Calidad de voz** | "Voices often feel synthetic and lacking expressiveness" | B |
| **Fiabilidad multi-idioma** | Solo inglés funciona de forma fiable en producción | B |

### Problemas de producto

| Problema | Detalle | Conf. |
|----------|---------|-------|
| **Gap no-code** | Queja #1: "No user-friendly dashboard where a business owner can type changes and hit save" | B |
| **Requiere engineering** | "Bland requires heavy engineering to get right" — barrera para compradores no-técnicos | B |
| **Sin visual workflow builder** | Toda configuración via código; competidores ofrecen builders visuales | B |

### Problemas de soporte

| Problema | Detalle | Conf. |
|----------|---------|-------|
| **Soporte deficiente** | "Unresponsive and unhelpful customer support" — queja dominante en reviews negativos | B |
| **Sin ticketing formal** | Depende de Discord vs. soporte estructurado | B |
| **Abandono percibido** | "Feeling abandoned when issues arise" | B |

### Quote relevante de Reddit

> "Testing Bland, Retell, and Vapi — Bland is most powerful for multi-prompt bots, but with more possibilities there are more places where it can fail" [B: Reddit]

---

## Noticias recientes

| Fecha | Noticia | Fuente |
|-------|---------|--------|
| **Mar 2026** | Lanzamiento de **Norm** — AI assistant que construye voice agents desde un prompt | PR Newswire [A] |
| **Mar 2026** | TechCrunch: "Why hiring the weirdos works" — perfil de Isaiah Granet | TechCrunch [A] |
| **Dic 2025** | **Nuevo modelo de pricing** por planes reemplaza flat rate de $0.09/min | Bland docs [A] |
| **Dic 2025** | Lanzamiento **plataforma de integraciones** (Salesforce, Notion, Cal.com, Calendly) | Product Recap [A] |
| **2025** | Expansión a **SMS y Web Chat** (omnichannel) | Product Recap [A] |
| **Ene–Feb 2025** | **Serie B de $40M** liderada por Emergence Capital | Múltiples fuentes [A] |

### Presencia en Europa

**Sin presencia detectada en Europa/España** [A: alta confianza en la ausencia].

| Aspecto | Estado | Conf. |
|---------|--------|-------|
| Oficinas en Europa | No | A |
| Números de teléfono europeos | Solo +1 (US); puede llamar internacionalmente | A |
| Soporte idioma español en producción | Mencionado pero no fiable según usuarios | B |
| Compliance EU AI Act | **No mencionado** | A |

---

## Relevancia para la entrevista

### Talking points concretos para Lola

1. **"Bland es un player fuerte en infraestructura de voz, pero operar en España requiere multi-canal (email para BOLs, web chat, voz) — exactamente donde HappyRobot tiene ventaja."**

2. **"El modelo developer-first de Bland genera fricción para empresas logísticas españolas sin equipos internos de AI. Nuestros forward-deployed engineers eliminan esa barrera."**

3. **"Bland no tiene presencia en Europa, solo soporta números +1, y no menciona EU AI Act. Para el mercado español, eso es un deal-breaker regulatorio."**

4. **"La volatilidad de pricing de Bland (55% de subida en dic 2025) crea incertidumbre presupuestaria. Enterprise buyers en España prefieren contratos predecibles."**

5. **"Nuestro foco vertical en logística nos da ventajas unfair: DHL, Circle Logistics, MODE Global, Syfan. Bland tiene zero case studies logísticos significativos."**

6. **(Honestidad intelectual)** **"Reconozco que la expertise voice-native de Bland es fuerte para pure phone use cases, y sus $65M de funding les dan runway para expandir. Pero la mayoría de workflows enterprise logístico son multi-canal."**

7. **"El riesgo competitivo de Bland es a medio plazo: si expanden a Europa y mejoran soporte no-inglés. Mi rol como GM España sería consolidar la ventaja de HappyRobot antes de que eso ocurra."**

---

## Fuentes

| Código | URL | Tipo | Conf. |
|--------|-----|------|-------|
| BLAND-WEB | https://www.bland.ai | Web producto | A |
| BLAND-PR1 | https://docs.bland.ai/platform/billing | Docs pricing | A |
| BLAND-YC | https://www.ycombinator.com/companies/bland-ai | Perfil YC | A |
| BLAND-CS-SLASH | https://www.bland.ai/case-studies/slash | Case study | A |
| BLAND-CS-CERTUS | https://www.bland.ai/case-studies/certus | Case study | A |
| BLAND-BLOG-RECAP | https://www.bland.ai/blogs/2025-bland-product-recap | Product recap 2025 | A |
| BLAND-BLOG-B | https://www.bland.ai/blogs/bland-raises-a-40m-series-b | Serie B announcement | A |
| BLAND-NORM | https://www.prnewswire.com/news-releases/bland-unveils-first-ai-assistant... | PR Newswire Norm | A |
| BLAND-CB | https://www.crunchbase.com/organization/bland-ai | Crunchbase | A |
| BLAND-VB | https://venturebeat.com/ai/bland-ai-scores-16m... | VentureBeat | A |
| BLAND-EMCAP | https://www.emcap.com/thoughts/ai-that-speaks-volumes-why-were-backing-bland | Emergence Capital | A |
| BLAND-TC-HIRING | https://techcrunch.com/2026/03/26/why-hiring-the-weirdos-works/ | TechCrunch profile | A |
| BLAND-DELVE | https://delve.co/case-study/bland-soc2-compliance-delve-success | SOC 2 case study | A |
| BLAND-BASETEN | https://www.baseten.co/resources/customers/blandai/ | Infra case study | B |
| BLAND-LATENCY | https://thegrowthengine.net/vapi-vs-bland-ai-real-world-voice-latency-benchmark/ | Benchmark | B |

---

*Ver también: [HappyRobot](../empresa/happyrobot.md), [Retell AI](retell-ai.md), [Synthflow](synthflow.md), [Tabla comparativa competidores](index.md)*
