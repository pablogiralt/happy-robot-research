---
title: "Sierra AI"
type: competidor
status: completo
tags: [competidor, enterprise-ai, customer-service, usa, serie-b, unicornio, madrid]
updated: 2026-04-07
---

# Sierra AI

Plataforma de conversational AI enterprise de mayor valoracion del mercado ($10B), fundada por **Bret Taylor** (ex co-CEO Salesforce, ex CTO Facebook, Chairman OpenAI) y **Clay Bavor** (18 anos en Google, VP Labs/AR/VR). Ha levantado **$635M total** y alcanza **$150M ARR estimado** (ene 2026). Sirve al 40% del Fortune 50 con agentes AI para customer experience generalista. Tiene **oficina en Madrid** (inaugurada marzo 2026). Es el competidor mas formidable en Europa para [HappyRobot](../empresa/happyrobot.md). Historicamente operaban en **lanes diferentes** (Sierra = CX generalista; HappyRobot = logistics), pero con HR expandiendose a multi-vertical (Airlines, Retail, Financial Services, Utilities, Customer Support), **el terreno de solapamiento crece significativamente**. Sierra no tiene ningun cliente logistico publico, pero ambos compiten ahora en enterprise CX. La ventaja de HR: metricas de produccion de 70+ clientes, compliance EU (incluyendo EU AI Act), y modelo FDE. El moat de logistics es real pero time-bounded (18-24 meses) — Sierra es la amenaza mas seria por capital + marca + presencia Madrid.

---

## Ficha rapida

| Dato | Valor | Conf. |
|---|---|---|
| **Web** | [sierra.ai](https://sierra.ai/) | A |
| **HQ** | San Francisco, CA | A |
| **Oficinas** | SF, New York, Atlanta, London, Singapore, Tokyo, Paris, **Madrid**, Toronto, Sydney | A |
| **Fundacion** | 2023 | A |
| **Fundadores** | Bret Taylor (co-CEO, ex co-CEO Salesforce, CTO Facebook, Chairman OpenAI), Clay Bavor (co-CEO, 18 anos Google, VP Labs) | A |
| **Empleados** | ~500-600 (feb 2026, dato en conflicto segun fuente) | B |
| **Funding total** | $635M+ | A |
| **Ultima ronda** | $350M Serie B (sept 2025, Greenoaks lead) | A |
| **Valoracion** | $10B | A |
| **ARR** | $150M (ene 2026, estimado Sacra) / $100M (nov 2025, dato oficial) | A/B |
| **Clientes** | 100+ enterprise, 40% del Fortune 50 (self-reported) | B |

!!! warning "Dato en conflicto: headcount"
    Tracxn (feb 2026): 603 | PitchBook: 488 | BitScale (ene 2026): 490 | TrueUp: 370 | Getlatka (2025): 165. Variabilidad por contractors, timing o metodologia.

---

## Producto

### Agent OS 2.0 (nov 2025)

| Componente | Descripcion |
|---|---|
| **Agent OS** | Sistema operativo core para build, deploy, manage agentes |
| **Agent SDK** | Framework declarativo con composable skills (triage, respond, confirm) |
| **Agent Studio 2.0** | Interfaz no-code con Journeys (natural language) |
| **Agent Data Platform** | Memoria + inteligencia: unifica datos no estructurados y estructurados |
| **Insights 2.0** | Analytics con Explorer y Expert Answers |
| **Live Assist** | Augmenta agentes humanos con AI en real-time |
| **Experience Manager** | Auditoria de conversaciones para equipos tecnicos y no-tecnicos |
| **Ghostwriter** (mar 2026) | Self-service agent builder: sube SOPs/transcripts -> agente production-ready en 30+ idiomas |

### Canales

Chat, SMS, WhatsApp, email, voz, integracion ChatGPT (one-click via OpenAI Apps SDK).

### Arquitectura

- **Multi-model constellation:** OpenAI, Anthropic, Meta -- no depende de un solo provider
- **Supervisor model:** Capas supervisoras para reducir hallucinations y asegurar seguridad
- **Interacciones deterministas** cuando accede a sistemas de record
- **PII encryption** automatica

### Compliance

| Certificacion | Estado | Conf. |
|---|---|---|
| SOC 2 | Si | A |
| ISO 27001 | Si | A |
| ISO 42001 | Si | A |
| HIPAA | Si | A |
| GDPR | Si | A |
| CCPA | Si | A |
| EU AI Act | No mencionado explicitamente | B |

### Research: tau-bench

Sierra publica benchmarks open-source (tau-bench, tau2-bench, tau3-bench) para evaluacion de agentes en dominios reales incluyendo knowledge retrieval y voice. Inversion en legitimidad cientifica [A: github sierra-research].

---

## Clientes y metricas

### Clientes con metricas publicadas

| Cliente | Sector | Metrica | Conf. |
|---|---|---|---|
| **Rocket Mortgage** | Financial services | 4x higher conversion rates | A |
| **SoFi** | Fintech | +33 puntos NPS | A |
| **Brex** | Fintech | 90% faster customer service | B |
| **Ramp** | Fintech | 90% case resolution | B |
| **Chime** | Fintech | 70%+ resolution rate | B |
| **Redfin** | Real estate | 2x more listings viewed | A |
| **Guild** | Education | 4.8/5 CSAT | A |
| **Singtel** | Telecom | <10 weeks to live; 70%+ resolution | A |
| **Next** (UK) | Retail | 6 weeks to live; 48 idiomas, 83 paises | A |
| **Cigna** | Healthcare | 8 weeks deploy; 80% reduccion tiempo autenticacion | A |

### Lista de clientes conocidos (parcial)

**Fintech:** Rocket Mortgage, SoFi, Chime, Nubank, Brex, Ramp, FINRA
**Media:** SiriusXM, Tubi, Sonos, Vivid Seats
**Retail/Consumer:** WeightWatchers, Casper, Nordstrom, OluKai, AG1, Thrive Market
**Tech:** CLEAR, CDW
**Auto:** Safelite, RunBuggy, Rivian
**Healthcare:** Cigna, Blue Shield of California (piloto)

**Zero clientes en logistics/supply chain/freight.** RunBuggy (vehicle transport) es lo mas cercano pero es auto logistics, no freight.

---

## Modelo de negocio

### Outcome-based pricing

Cobra solo cuando los agentes logran outcomes especificos: conversacion resuelta, cancelacion evitada, upsell completado. No cobra por escalaciones a humano (mayoria de casos) [A: sierra.ai].

### Estimaciones de coste

| Componente | Rango | Conf. |
|---|---|---|
| Ano 1 total | $200K-$350K+ | B |
| Setup fees | $50K-$200K | B |
| Contrato anual minimo | ~$150K | B |
| Deployment time | 3-6 meses | B |

**No hay pricing publico.** Todo via enterprise sales + custom contracts.

### Revenue

| Metrica | Valor | Conf. |
|---|---|---|
| ARR (ene 2026) | $150M | B |
| ARR (nov 2025) | $100M (milestone publico, 7 quarters desde launch) | A |
| ARR (end 2024) | ~$26M | B |
| Crecimiento | ~5x YoY | B |

---

## Presencia Europa / Espana

### Oficinas europeas

| Ciudad | Estado | Foco |
|---|---|---|
| **London** | Activa | UK enterprise (Next, Marshmallow) |
| **Paris** | Activa | Luxury, aerospace |
| **Madrid** | Inaugurada marzo 2026 | Enterprise espanol |

### Detalle Madrid

- Blog post dedicado "Building in Spain" por Clay Bavor [A: sierra.ai]
- "Already working with a number of the biggest businesses in Spain" -- **sin nombres divulgados** [B]
- Hiring activamente (sierra.ai/careers?location=es-madrid) [A]
- Bret Taylor visito Barcelona y Madrid, reuniones en Instituto Elcano [B]

**Amenaza competitiva directa** para expansion de HappyRobot en Espana. Sierra tiene head start en Madrid pero su foco es CX generalista. Con HR expandiendose a multi-vertical (CX, Retail, Financial Services, etc.), el solapamiento en Madrid es real y creciente.

---

## HappyRobot vs Sierra AI

| Dimension | HappyRobot | Sierra AI |
|---|---|---|
| **Valoracion** | ~$100-300M (est.) | $10B |
| **Funding** | $44M Serie B | $635M |
| **Revenue** | No divulgado | $150M ARR |
| **Foco vertical** | Multi-vertical (logistics beachhead + airlines, retail, finserv, utilities) | Horizontal CX (finserv, retail, telecom, health) |
| **Clientes enterprise** | 70+ (DHL, Circle, Samsara, MODE, Syfan, Job&Talent) | **Zero publicos** |
| **Espana** | Hiring (GM, AE, FDE) | Oficina Madrid activa (mar 2026) |
| **Pricing** | Mas accesible (usage-based) | $200K-$350K+ ano 1 (outcome-based) |
| **Deployment** | Mas rapido (pre-tuned vertical workflows) | 3-6 meses |
| **Multi-canal** | Phone, email, web chat | Chat, SMS, WhatsApp, email, voice, ChatGPT |
| **Compliance** | SOC 2, GDPR, HIPAA, **EU AI Act** | SOC 2, ISO 27001/42001, HIPAA, GDPR |
| **ROI metrics** | 119x collections, 1000x scheduling | CSAT, resolution rates (genericos) |
| **Founders** | Pablo/Javier Palafox (espanoles) | Bret Taylor (Salesforce CEO) + Clay Bavor (Google VP) |
| **Self-service** | No conocido | Ghostwriter (mar 2026) |

---

## Debilidades y criticas

### Debilidades de producto/implementacion

| Debilidad | Detalle | Conf. |
|---|---|---|
| **Pricing opaco** | Outcome-based puede generar facturas impredecibles; "defining a resolution can be messy" | B |
| **Coste alto** | $200K-$350K+ ano 1; six-figure commitment antes de modelar ROI | B |
| **Dependencia consultoria** | Opera como consultancy; cambiar workflows requiere pagar consultants | B |
| **Deployment lento** | 3-6 meses setup con Forward-Deployed Engineers | B |
| **Customizacion limitada** | "Does not allow client customization" | B |
| **Latencia voz** | 700ms+ delay por multi-LLM routing | B |
| **Perdida de contexto** | Struggles con conversaciones largas; respuestas repetitivas | B |
| **Vendor lock-in** | Closed Agent OS = alto switching cost | B |

### Criticas en comunidades

**TeamBlind:** Thread "Is Sierra AI a scam?" -- escepticismo sobre estructura organizacional. Para 40 en engineering, tienen 30 "product managers" -- ratio inusual [C: teamblind.com].

**G2:** 4.9/5 -- score alto pero reviews limitados [B].

### El dilema Ghostwriter

Ghostwriter intenta resolver debilidades (dependencia FDE, deployment lento, coste alto) pero **commoditiza su propia ventaja competitiva** (high-touch implementation).

---

## Noticias recientes

| Fecha | Evento | Fuente |
|---|---|---|
| Mar 2026 | Ghostwriter launch (self-service agent builder) | sierra.ai |
| Mar 2026 | Oficina Madrid inaugurada | sierra.ai |
| Mar 2026 | Oficina Sydney | sierra.ai |
| Mar 2026 | Adquisicion Opera Tech (Tokyo) | sierra.ai |
| Mar 2026 | tau3-bench (benchmark knowledge + voice) | sierra.ai |
| Mar 2026 | Partnership Singtel | sierra.ai |
| Ene 2026 | Partnership Stellarus + Blue Shield CA (voice agent piloto) | PR Newswire |
| Dic 2025 | Inversion SoftBank + oficina Tokyo | Axios |
| Nov 2025 | Sierra Summit: Agent OS 2.0 launch | sierra.ai |
| Nov 2025 | $100M ARR milestone (7 quarters) | sierra.ai |
| Sept 2025 | Serie B $350M, valoracion $10B | TechCrunch |

---

## Relevancia para la entrevista

### Si preguntan: "Como compites con Sierra en Espana?"

1. **"Ya competimos directamente -- y con ventaja."** Sierra vende a CMOs/Heads of CX de Fortune 500 (SoFi, Brex, WeightWatchers). HappyRobot opera en Airlines, Retail, Financial Services, Utilities, Customer Support — terreno donde Sierra es fuerte. La diferencia es que nosotros llegamos con metricas de produccion reales de 70+ enterprise customers (incluyendo Job&Talent con 1M+ AI interviews y 20K+ hires), no con demos. En logistics, donde tenemos depth unica con DHL, Circle o Samsara, Sierra no tiene presencia.

2. **"Nuestro moat de logistics es real pero time-bounded."** Sierra podria entrar en logistics, y nosotros ya estamos en su terreno de CX enterprise. La ventaja competitiva no es solo vertical — es execution speed, FDE model, y compliance (EU AI Act, que Sierra no menciona).

3. **"Su pricing excluye mid-market."** Sierra cobra $200K-$350K+ en ano 1. En Espana, en logistica, retail, utilities y staffing, el mid-market es enorme. Nosotros servimos enterprise (DHL, Job&Talent) y mid-market.

4. **"Ganamos en time-to-value y ROI specificity."** Sierra: 3-6 meses deployment, CSAT generico. Nosotros: agentes pre-tuned por vertical, 119x ROI collections, 1000x scheduling speed, 1M+ AI interviews para Job&Talent con 20K+ hires -- hard dollars para CFOs, no vanity metrics.

5. **"Nuestros founders son espanoles."** Pablo y Javier Palafox entienden regulacion espanola, cultura business, dinamicas laborales. Sierra es Silicon Valley parachuting en Madrid -- nosotros estamos construyendo desde dentro.

### Si preguntan: "Que admiras de Sierra?"

1. **"Su ejecucion GTM es world-class."** $100M ARR en 7 quarters, 40% del Fortune 50 -- apalancaron el network de Bret Taylor brillantemente.

2. **"El outcome-based pricing es el modelo correcto."** Alinea incentivos. Referencia para como deberiamos pensar pricing.

3. **"Han normalizado la valoracion $10B para AI agents."** Hace que nuestra Serie B de $44M parezca capital-efficient por comparacion.

### Si preguntan: "Sierra podria entrar en logistics?"

> "Podrian, pero les costaria 18-24 meses construir la profundidad que nosotros tenemos. Logistics requiere domain expertise profundo -- datasets de llamadas reales, integracion con TMS/WMS, comprension de workflows operacionales. Tendrian que construir desde cero mientras nosotros tenemos 70+ enterprise customers, incluyendo clientes logisticos como DHL y Circle, y anos de datos anotados. Y ya no estamos solo en logistics: operamos en Airlines, Retail, Financial Services, Utilities — Job&Talent (1M+ AI interviews, 20K+ hires) demuestra que el modelo escala a otras verticales. Llegamos a su terreno de CX enterprise con production metrics reales, no solo producto."

---

## Fuentes

| Codigo | URL | Tipo | Conf. |
|---|---|---|---|
| SIERRA-WEB | [sierra.ai](https://sierra.ai/) | Web producto | A |
| SIERRA-ABOUT | [sierra.ai/about](https://sierra.ai/about) | About | A |
| SIERRA-BLOG-SPAIN | [Building in Spain](https://sierra.ai/blog/building-in-spain) | Blog | A |
| SIERRA-BLOG-ARR | [$100M ARR](https://sierra.ai/blog/100m-arr) | Blog | A |
| SIERRA-TC | [TechCrunch Serie B](https://techcrunch.com/2025/09/04/bret-taylors-sierra-raises-350m-at-a-10b-valuation/) | Prensa | A |
| SIERRA-CNBC | [CNBC Serie A](https://www.cnbc.com/2024/10/28/bret-taylors-ai-startup-sierra-valued-at-4point5-billion-in-funding.html) | Prensa | A |
| SIERRA-SACRA | [Sacra Research](https://sacra.com/c/sierra/) | Analisis | B |
| SIERRA-G2 | [G2 Reviews](https://www.g2.com/products/sierra/reviews) | Reviews | B |
| SIERRA-FEATUREBASE | [Pricing analysis](https://www.featurebase.app/blog/sierra-ai-pricing) | Analisis | B |
| SIERRA-EESEL | [Reviews](https://www.eesel.ai/blog/sierra-reviews) | Analisis | B |
| SIERRA-TRACXN | [Tracxn](https://tracxn.com/d/companies/sierra/) | Base datos | B |
| SIERRA-WIKI | [Wikipedia Bret Taylor](https://en.wikipedia.org/wiki/Bret_Taylor) | Enciclopedia | A |
| SIERRA-BLIND | [TeamBlind thread](https://www.teamblind.com/post/is-sierra-ai-a-scam-vgp0n56z) | Comunidad | C |

---

*Ver tambien: [HappyRobot](../empresa/happyrobot.md), [Parloa](parloa.md), [Decagon](decagon.md), [Expansion Espana](../empresa/expansion-espana.md)*
