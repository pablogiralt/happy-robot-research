---
title: "PolyAI"
type: competidor
status: completo
tags: [competidor, voice-ai, enterprise, uk, serie-d, hospitality, cx]
updated: 2026-04-07
---

# PolyAI

Plataforma enterprise de voice AI con sede en Londres, especializada en agentes de voz conversacionales que reemplazan agentes humanos a escala en customer service. Fundada en 2017 por tres PhD de Cambridge (Nikola Mrksic, Tsung-Hsien Wen, Pei-Hao Su), ha levantado **$200M+** ($86M Serie D en dic 2025, valoracion ~$750M). Opera con 2,000+ deployments en 25+ paises. Nombrada "fastest-growing AI company in Europe" (FT 1000, marzo 2026). Destaca por su **calidad de voz lider** (modelos propietarios Owl y Raven) y foco en **hospitality y financial services**. Relevante para [HappyRobot](../empresa/happyrobot.md) como referencia de voice AI enterprise pero **sin presencia en logistics ni en Espana**.

---

## Ficha rapida

| Dato | Valor | Conf. |
|---|---|---|
| **Web** | [poly.ai](https://poly.ai) | A |
| **HQ** | Londres, UK (Paddington) | A |
| **Oficinas** | Londres, New York, San Mateo | A |
| **Fundacion** | 2017 | A |
| **Fundadores** | Nikola Mrksic (CEO, PhD Cambridge, ex-Apple/VocalIQ), Tsung-Hsien Wen (CTO, PhD Cambridge, ex-Google), Pei-Hao Su (Chief Scientist, PhD Cambridge, ex-Facebook AI) | A |
| **Empleados** | 340-360 | B |
| **Funding total** | $200M+ | A |
| **Ultima ronda** | $86M Serie D (dic 2025, Georgian lead) | A |
| **Valoracion** | ~$750M | C |
| **Revenue 2025** | ~$35M (camino a $40M+ ARR) | C |
| **Crecimiento** | 3.5x YoY (2024->2025) | B |
| **Clientes** | 200+ enterprises, 2,000+ deployments | A |
| **Idiomas** | 45+ | A |
| **Paises** | 25+ | A |

---

## Producto: Agent Studio

### Stack tecnologico propietario

| Componente | Nombre | Descripcion | Conf. |
|---|---|---|---|
| **ASR** | **Owl** | ASR propietario. WER 0.122 (mejor que competidores). Maneja acentos, ruido, interrupciones. Vocabularios domain-specific intercambiables mid-conversation | A |
| **LLM** | **Raven** | LLM propietario entrenado en billions de conversaciones. Sub-second responses. Exclusivo para customer service | A |
| **Voice Synthesis** | Propietario | Mezcla grabaciones humanas + sintesis neural. Voces que "respiran como persona real". Customizables por marca | A |
| **Runtime** | Agentic Runtime | Combina modelos generativos + retrieval AI + dialogue policy patentada | A |

### Plataforma Agent Studio (abril 2025)

- **Conversation Review:** Cada turno muestra que documentos de knowledge base uso el agente
- **PolyScore:** Scoring automatico de calidad conversacional
- **Call Categorization:** LLM para clasificar calls por tono, intent, compliance
- **Test Cases:** Guardar conversaciones reales como test cases, re-ejecutar contra versiones draft
- **Smart Analyst:** Sampling de hasta 500 conversaciones para patterns
- **Connected Knowledge:** Retrieval de documentos con source preview inline
- **conv.memory:** Persistencia de valores entre conversaciones

### Agentic AI Team (sept 2025)

| Agent | Funcion |
|---|---|
| **QA Agent** | Score automatico de cada call en 6 factores de calidad |
| **Analyst Agent** | Interfaz conversacional para explorar millones de conversations |
| **Builder Agent** | Guia onboarding, desarrollo y mantenimiento de agentes |

### Canales e integraciones

- **Voice:** SIP/PSTN, integracion nativa con CCaaS
- **Text:** Soporte messaging (omnicanal pero voice-first)
- **Integraciones:** Salesforce, NICE, Genesys, Twilio
- **Deployment:** ~6 semanas (managed service)
- **Partnerships:** Microsoft Azure, AWS Travel & Hospitality Competency

### Compliance

- SOC 2 Type II
- HIPAA
- [EU AI Act y GDPR no mencionados explicitamente en materiales publicos]

---

## Clientes y metricas

### Clientes confirmados

| Cliente | Vertical | Detalle | Conf. |
|---|---|---|---|
| **Marriott** | Hospitality | Voice assistant 24/7/365 para reservas y servicio | A |
| **Caesars Entertainment** | Hospitality/Gaming | Voice assistant para contact center | A |
| **PG&E** | Energy/Utilities | Customer service automation | A |
| **UniCredit** | Financial Services | Deployment europeo | A |
| **Foot Locker** | Retail | -- | A |
| **Allstate** | Insurance | -- | A |
| **Hopper** | Travel | Voice assistant | B |
| **Whitbread** | Hospitality (UK) | Voice assistant | B |
| **The Melting Pot** | Restaurants | $250K bookings after-hours | A |

### Metricas agregadas

| Metrica | Valor | Conf. |
|---|---|---|
| ROI (Forrester TEI, 3 anos) | 391% | A |
| Ahorro promedio por cliente | $10.3M | B |
| Call containment rates | 50-87% segun deployment | B |
| First-call resolution | 72% | B |
| CSAT | 93% | B |
| Resolution rate | 97% | B |
| Conversion rate (Cote Brasserie) | 76% bookings | A |

### Verticales principales

1. **Hospitality & Travel** (vertical estrella -- Marriott, Caesars, Hopper)
2. **Financial Services** (UniCredit)
3. **Energy & Utilities** (PG&E)
4. **Retail** (Foot Locker)
5. **Insurance** (Allstate)
6. **Healthcare**

!!! warning "Logistics NO es vertical de PolyAI"
    PolyAI NO tiene presencia visible en logistics/supply chain/freight. Foco en customer experience inbound (hospitality, finserv, retail, utilities).

---

## Modelo de negocio

| Aspecto | Detalle | Conf. |
|---|---|---|
| **Modelo** | Platform fee fijo + usage-based (per-minute) | B |
| **Contrato minimo** | ~$150,000/ano | B |
| **Mid-tier** | $10,000-$20,000/mes | C |
| **Enterprise** | $30,000+/mes | B |
| **Implementacion** | $20,000-$50,000+ (one-time, puede superar $100K) | B |
| **Trial/self-serve** | No disponible -- solo demo con sales | A |
| **Deployment** | Managed service (~6 semanas) | B |

---

## HappyRobot vs PolyAI

| Dimension | HappyRobot | PolyAI |
|---|---|---|
| **Foco vertical** | Logistics & supply chain | CX horizontal (hospitality, finserv, retail, utilities) |
| **Tipo interaccion** | Operations (scheduling, collections, sales, recruiting) | Inbound CX (soporte, reservas, billing) |
| **Stack tecnologico** | Model-agnostic + razonamiento agentitico + logica determinista | Propietario end-to-end (Owl + Raven + sintesis) |
| **Canales** | Multi-canal nativo (telefono, email, web chat) | Voice-first (+ text messaging) |
| **Governance** | AI Auditor, evaluations, compliance framework | Agent Studio analytics + QA Agent |
| **Idiomas** | Multi-idioma (numero no publicado) | 45+ |
| **Clientes** | DHL, Circle, Samsara, MODE Global | Marriott, Caesars, PG&E, UniCredit |
| **Revenue** | [no publico] | ~$35M (2025) |
| **Funding** | $44M Serie B | $200M+, ~$750M valoracion |
| **Deployment** | Forward-deployed engineers | Managed service (~6 semanas) |
| **Pricing** | [no publicado] | $150K+ annual minimum |
| **Espana** | Expandiendo (EAE, FDE, GTM Ops) | Sin presencia |
| **Compliance** | SOC 2, GDPR, HIPAA, EU AI Act | SOC 2, HIPAA |

---

## Debilidades y criticas

### Debilidades por reviews

| Debilidad | Detalle | Fuente |
|---|---|---|
| **Pricing opaco y caro** | $150K+ minimo anual, sin self-serve | SoftwareCurio |
| **Deployment lento** | ~6 semanas managed service | Reviews |
| **Analytics basicos** | Dashboards limitados, sin deep sentiment tracking | G2, SoftwareCurio |
| **Sin sandbox/developer tools** | Sin prompt-level controls ni scripting para developers agiles | SoftwareCurio |
| **Rigidez operativa** | Cambios requieren intervencion de account teams | Reddit, reviews |
| **Latencia 700-900ms** | Buena pero no ideal para conversaciones de alta presion | Reviews |
| **Voice-only en esencia** | Omnicanal en teoria pero disenado para voice inbound | Analisis competitivo |
| **Solo CX inbound** | No optimizado para outbound sales, collections agresivos | Assembled |
| **Sin vertical logistics** | Cero presencia en freight/supply chain | Busqueda propia |
| **Reviews escasos** | 12 reviews G2, 2 Capterra -- bajo volumen validacion publica | G2, Capterra |

### Cultura (Glassdoor)

- **Positivo:** 92% recomendarian, culture 4.7/5, entorno colaborativo, talento de alta calidad
- **Negativo:** Procesos internos inmaduros (Salesforce desordenado, reporting manual), tipico de hyper-growth

---

## Noticias recientes

| Fecha | Evento | Fuente |
|---|---|---|
| Mar 2026 | #1 Enterprise AI en FT 1000 Europe | PR Newswire |
| Mar 2026 | Stevie Award -- Best Customer Service Solution 2026 | PR Newswire |
| Dic 2025 | $86M Serie D a ~$750M valoracion | SiliconANGLE |
| Sept 2025 | Lanzamiento Agentic AI Team (QA, Analyst, Builder agents) | PR Newswire |
| Jul 2025 | Partnership Microsoft Azure | Microsoft UK blog |
| Abr 2025 | Lanzamiento Agent Studio | PR Newswire |
| 2025 | AWS Travel & Hospitality Competency | Blog PolyAI |

---

## Presencia en Espana y Europa

- **Oficinas Europa:** Solo HQ en Londres. Sin oficinas en Europa continental [B]
- **Clientes europeos:** UniCredit (Italia), Whitbread (UK) [A]
- **Espana:** Sin evidencia de oficina, clientes espanoles, marketing en espanol, ni anuncios de expansion [C]
- **Assessment:** PolyAI es UK-centric con footprint limitado en Sur de Europa. Su vertical hospitality tiene relevancia en Espana (turismo) pero hoy no tiene presencia local.

---

## Relevancia para la entrevista

### Como posicionar HappyRobot vs PolyAI

1. **"PolyAI es lider en voice CX, pero no compite en nuestro core."** Su foco es inbound customer service (hospitality, finserv, utilities). HappyRobot opera en logistics operations, collections, scheduling -- procesos operacionales complejos, no solo CX.

2. **"Su stack propietario es impresionante pero rigido."** Owl + Raven son best-in-class en voice quality, pero ser model-agnostic (como HappyRobot) da flexibilidad ante evolucion rapida de LLMs.

3. **"$750M de valoracion valida el mercado, no amenaza nuestro nicho."** Su crecimiento viene de hospitality y financial services, no de logistics.

4. **"Su modelo managed service no escala como forward-deployed engineers."** 6 semanas de deployment vs. la flexibilidad de FDEs integrados con el cliente.

5. **"En Espana, PolyAI no tiene presencia. Nosotros estamos entrando ahora."** Aunque podrian expandir (turismo/hospitality), hoy no tienen oficina ni equipo local.

6. **"Governance es nuestra ventaja."** PolyAI tiene QA agents y analytics, pero HappyRobot tiene AI Auditor y compliance framework incluyendo EU AI Act -- critico en Europa.

### Reconocer fortaleza

> "PolyAI ha hecho un trabajo excelente en calidad de voz y customer service enterprise. Su ROI validado por Forrester (391%) es impresionante. Pero son fundamentalmente un managed service voice-first para inbound support. El sweet spot de HappyRobot son AI Workers operacionales en logistica."

---

## Fuentes

| Codigo | URL | Tipo | Conf. |
|---|---|---|---|
| POLY-WEB | [poly.ai](https://poly.ai) | Web oficial | A |
| POLY-TECH | [poly.ai/technology](https://poly.ai/technology) | Producto | A |
| POLY-PR | [PR Serie D](https://www.prnewswire.com/news-releases/polyai-raises-86m-to-transform-how-enterprises-talk-to-their-customers-302641889.html) | PR oficial | A |
| POLY-FT1000 | [PR FT 1000](https://www.prnewswire.com/news-releases/polyai-named-the-fastest-growing-ai-company-in-europe-in-ft-1000-rankings-302707736.html) | PR oficial | A |
| POLY-AGENTIC | [PR Agentic AI Team](https://www.prnewswire.com/news-releases/polyai-launches-agentic-ai-team-to-drive-cx-insights-and-growth-qa-analyst-and-builder-agents-302554505.html) | PR oficial | A |
| POLY-CB | [Crunchbase](https://www.crunchbase.com/organization/poly-ai) | Base datos | A |
| POLY-CASES | [poly.ai/case-studies](https://poly.ai/case-studies/) | Case studies | A |
| POLY-ROI | [Forrester TEI](https://poly.ai/blog/polyai-customers-391-percent-roi-total-economic-impact-study) | Estudio terceros | A |
| POLY-SILICON | [SiliconANGLE $750M](https://siliconangle.com/2025/12/15/call-center-chatbot-startup-polyai-raises-86m-750m-valuation/) | Prensa | A |
| POLY-SIFTED | [Sifted Serie D](https://sifted.eu/articles/polyai-series-d-86m) | Prensa | A |
| POLY-G2 | [G2 Reviews](https://www.g2.com/products/polyai/reviews) | Reviews | B |
| POLY-LATKA | [Latka Revenue](https://getlatka.com/companies/poly.ai) | Base datos | C |
| POLY-AMADEUS | [Amadeus Founders story](https://www.amadeuscapital.com/success-stories-voice-ai-with-nikola-mrksic-and-polyai/) | Inversor | B |
| POLY-GLASSDOOR | [Glassdoor](https://www.glassdoor.com/Reviews/PolyAI-Reviews-E2360836.htm) | Empleados | B |

---

*Ver tambien: [HappyRobot](../empresa/happyrobot.md), [Parloa](parloa.md), [Sierra AI](sierra-ai.md), [Voice AI](../tecnologia/voice-ai.md)*
