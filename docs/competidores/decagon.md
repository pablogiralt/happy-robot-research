---
title: "Decagon AI"
type: competidor
status: completo
tags: [competidor, ai-agents, customer-support, enterprise, voice-ai, serie-d]
updated: 2026-04-07
---

# Decagon AI

"The AI concierge for every customer" -- plataforma de AI conversacional enterprise para customer experience. Con $481M levantados y valoracion de $4.5B, es uno de los players mas grandes del espacio de AI agents. Foco exclusivo en customer support/CX horizontal (fintech, SaaS, travel, e-commerce). Relevante para [HappyRobot](../empresa/happyrobot.md) como benchmark de velocidad de ejecucion y como referencia de TAM.

---

## Ficha rapida

| Dato | Valor | Conf. |
|---|---|---|
| **Web** | [decagon.ai](https://decagon.ai) | A |
| **HQ** | San Francisco, CA | A |
| **Oficinas** | SF, New York, Londres (dic 2025) | A |
| **Fundacion** | 2023 | A |
| **Fundadores** | Jesse Zhang (CEO, Harvard CS, ex-Citadel/Google, fundo Lowkey -> Niantic), Ashwin Sreenivas (CTO, Stanford CS, ex-Palantir, fundo Helia -> Scale AI) | A |
| **Empleados** | 300+ (marzo 2026) | A |
| **Funding total** | ~$481M (6 rondas) | A |
| **Ultima ronda** | $250M Serie D (ene 2026, Coatue + Index Ventures) | A |
| **Valoracion** | $4.5B (enero 2026) | A |
| **ARR estimado** | ~$35M annualized (oct 2025) | B |
| **Clientes enterprise** | 100+ (firmados en 2025) | A |
| **End customers servidos** | 10M+ | B |

---

## Producto

### Core: AI Concierge Platform

Agentes autonomos de customer support que no solo responden, sino ejecutan acciones reales: refunds, cambios de pedido, verificacion de identidad, creacion de tickets.

### Agent Operating Procedures (AOPs)

Instrucciones en **lenguaje natural** que se compilan en logica estructurada. Permiten definir workflows como si onboardearas a un nuevo empleado. **AOP Copilot** (sept 2025) convierte SOPs existentes en AOPs production-ready en segundos [B: Web oficial].

### Canales (Omnichannel)

| Canal | Estado |
|---|---|
| Chat (web widget) | GA -- core product original |
| Email | GA |
| SMS | GA |
| Voice (inbound) | GA -- sub-second latency, interruption handling |
| Voice (outbound) | GA (Spring 2026) -- campaigns, callbacks, voicemail |

### Voice AI (detalle)

- **Decagon Voice 2.0:** Inbound + outbound con sub-second latency
- **Speculative decoding:** Modelos draft mas pequenos que proponen tokens ahead del modelo principal -- permite que el agente empiece a hablar antes sin perder calidad [B: Together AI case study]
- **Integraciones voice:** Amazon Connect, RingCentral, SIP trunking

### Proactive Agents (Spring 2026)

- **User Memory:** Memoria persistente cross-session y cross-channel
- **Outbound Voice:** Agentes que inician llamadas proactivamente
- **Missions:** Gestion de campanas outbound a escala
- **Decagon Duet:** AI partner para construir agentes que se auto-mejoran

### Quality & Monitoring

- **Watchtower QA:** Monitoring automatizado de calidad
- **A/B testing:** Para iterar sobre logica de agentes
- **Agent Workbench** (Spring 2026): Debugging e iteracion

### Arquitectura tecnica

- **Multi-model orchestration:** Enruta cada query al mejor LLM (OpenAI, Anthropic, otros)
- **Azure hosting** para modelos off-the-shelf y fine-tuned, multi-region
- **Multi-agent ecosystem:** Agentes que trabajan juntos y revisan trabajo entre si

---

## Clientes y metricas

### Clientes tier-1 confirmados

| Cliente | Vertical | Detalle | Conf. |
|---|---|---|---|
| **Notion** | SaaS/Productivity | Gano RFP competitivo | A |
| **Rippling** | HR SaaS | +32% ticket deflection | A |
| **Duolingo** | EdTech | Reduccion de chat volume, expandiendo a email | A |
| **Avis Budget Group** | Travel/Rental | Enterprise deployment | A |
| **Deutsche Telekom** | Telecom | Enterprise | A |
| **Block (Square/CashApp)** | Fintech | -- | A |
| **Affirm** | Fintech | -- | A |
| **Chime** | Fintech/Neobank | -- | A |
| **Riot Games** | Gaming | -- | A |
| **Grubhub** | Food delivery | -- | A |
| **1-800-Flowers** | E-commerce | -- | A |
| **Eventbrite** | Events | -- | A |
| **Substack** | Media | -- | A |

### Metricas de plataforma

| Metrica | Valor | Conf. |
|---|---|---|
| Deflection rate promedio | 80% | B |
| Reduccion costes soporte | 65% | B |
| Agent quality score | 93% | B |
| ROI tipico | $800K ahorro por $250K gasto | B |
| Rippling: ticket deflection | +32% | A |

---

## Modelo de negocio

| Aspecto | Detalle | Conf. |
|---|---|---|
| Modelo | Usage-based (no per-seat) | A |
| Opcion 1 | Per conversation (~$0.99/conv) | B |
| Opcion 2 | Per resolution (~$1.50/resolucion) | B |
| Platform fee anual | ~$50K minimo | B |
| Contrato anual mediano | ~$386K (rango $95K-$590K+) | B |
| Self-serve | No existe. Solo enterprise sales | A |
| Tiempo implementacion | ~6 semanas | B |

---

## HappyRobot vs Decagon

| Dimension | HappyRobot | Decagon |
|---|---|---|
| **Foco vertical** | Multi-vertical (logistics beachhead + airlines, retail, finserv, utilities) | Customer support/CX horizontal |
| **Canales** | Phone, email, web chat | Chat, email, SMS, voice (in+outbound) |
| **Approach tecnico** | Razonamiento agentitico + logica determinista | Multi-model orchestration, AOPs en lenguaje natural |
| **Governance** | AI auditor, evaluations framework | Watchtower QA, A/B testing |
| **Compliance** | SOC 2, GDPR, HIPAA, EU AI Act | SOC 2 Type II, HIPAA |
| **Memoria/Contexto** | Shared context & memory (nativo) | User Memory (cross-session) -- Spring 2026 |
| **Funding** | $44M Serie B | $481M, valoracion $4.5B |
| **Europa** | Contratando en Espana (EAE, FDE, GTM Ops) | Londres (dic 2025) |
| **Clientes** | DHL, Circle, Samsara, MODE Global | Notion, Rippling, Duolingo, Deutsche Telekom |
| **Forward-deployed** | Forward-deployed engineers (modelo Palantir) | Dedicated support, ~6 semanas |
| **Revenue** | [no publico] | ~$35M ARR (oct 2025) |

---

## Debilidades y criticas

### Debilidades confirmadas por reviews

1. **"Black box" problem:** Dificil ver por que el AI tomo una decision. Disconnect entre marketing y experiencia real [B: eesel.ai review]
2. **Coste prohibitivo para no-enterprise:** Contratos desde $95K/ano, mediana $386K. Platform fee ~$50K antes de usage [B: Vendr data]
3. **Implementacion pesada:** Requiere "Agent Engineers" y semanas de setup. Integraciones avanzadas requieren developers [B: myaskai]
4. **Un solo agente generalista:** Usa un agente que intenta manejar todo, puede fallar en conversaciones complejas [B: G2 reviews]
5. **Agent Assist limitado a Zendesk** [B: eesel.ai]
6. **Performance bajo carga:** Slowdowns durante picos [C: Reviews agregadas]
7. **Analytics limitados:** Dificultad para filtrar por tipo de issue, SLA, o geografia [B: G2]
8. **Sin workforce management** [B: Assembled]

### Debilidades estrategicas

- **Foco 100% customer support** -- no tiene soluciones para sales, collections, recruiting, HR
- **Sin foco logistics** -- horizontal sin expertise vertical en supply chain
- **Europa = solo Londres** -- sin presencia en sur de Europa

---

## Noticias recientes

| Fecha | Evento | Fuente |
|---|---|---|
| Mar 2026 | Tender offer para empleados a $4.5B | TechCrunch |
| Mar 2026 | Lanzamiento Proactive Agents (User Memory + Outbound Voice) | BusinessWire |
| Mar 2026 | Lanzamiento Decagon Duet | Decagon blog |
| Mar 2026 | Agent Workbench para debugging | Decagon blog |
| Ene 2026 | Serie D $250M, valoracion $4.5B | BusinessWire |
| Dic 2025 | Apertura oficina Londres | Decagon blog |
| Sept 2025 | AOP Copilot lanzado | Web oficial |

---

## Relevancia para la entrevista

### Por que Decagon importa como referencia

- **Benchmark de velocidad:** De 0 a $4.5B en ~2.5 anos
- **Valida el mercado:** Serie D ($250M) confirma que inversores creen en AI agents enterprise
- **Su crecimiento beneficia a HappyRobot:** Normaliza la categoria

### Como diferencia HappyRobot

1. **"Decagon va horizontal en customer support. Nosotros dominamos logistics & supply chain -- eso es un moat que un horizontal no puede replicar facilmente."**

2. **"Decagon hace CX. Nosotros hacemos CX + sales + collections + recruiting + operations. Para enterprise, somos un platform play, no un point solution."**

3. **"EU AI Act compliance desde el principio. Decagon aun no ha anunciado compliance explicita -- eso importa para enterprise europeo."**

4. **"Decagon acaba de llegar a Londres. No tienen presencia en Espana ni sur de Europa. Tenemos first-mover advantage en mercado iberico."**

### Dato killer

> "Decagon ha levantado $481M y vale $4.5B haciendo AI agents para customer support generico. HappyRobot, con $44M, ha construido una plataforma que va mas alla de CX -- logistics operations, collections, sales, recruiting. Eso sugiere que con la ejecucion correcta en Europa, el upside es enorme."

---

## Fuentes

| Codigo | URL | Tipo | Conf. |
|---|---|---|---|
| DEC-WEB | [decagon.ai](https://decagon.ai) | Web oficial | A |
| DEC-BW-D | [BusinessWire Serie D](https://www.businesswire.com/news/home/20260128580542/en/) | PR oficial | A |
| DEC-BW-C | [BusinessWire Serie C](https://www.businesswire.com/news/home/20250623894798/en/) | PR oficial | A |
| DEC-TC | [TechCrunch Tender offer](https://techcrunch.com/2026/03/04/decagon-completes-first-tender-offer-at-4-5b-valuation/) | Prensa | A |
| DEC-BLOOM | [Bloomberg $4.5B](https://www.bloomberg.com/news/articles/2026-01-28/ai-customer-support-startup-decagon-valued-at-4-5-billion) | Prensa | A |
| DEC-SACRA | [Sacra Research](https://sacra.com/c/decagon/) | Analisis | B |
| DEC-CASES | [Decagon case studies](https://decagon.ai/case-studies) | Oficial | A |
| DEC-G2 | [G2 Reviews](https://www.g2.com/products/decagon/reviews) | Reviews | B |
| DEC-EESEL | [eesel.ai Review](https://www.eesel.ai/blog/decagon-ai-review) | Analisis | B |
| DEC-PRICING | [Featurebase Pricing](https://www.featurebase.app/blog/decagon-pricing) | Analisis | B |
| DEC-LONDON | [Decagon London](https://decagon.ai/resources/decagon-arrives-in-london) | Blog oficial | A |

---

*Ver tambien: [HappyRobot](../empresa/happyrobot.md), [Customer Service](../casos-de-uso/customer-service.md), [Sierra AI](sierra-ai.md)*
