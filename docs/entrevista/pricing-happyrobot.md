---
title: "Pricing HappyRobot — Preparación para entrevista con Mia"
type: entrevista
status: completo
tags: [entrevista, mia-bjorkenstam, pricing, deal-desk, palantir]
updated: 2026-05-21
---

# Pricing HappyRobot — Preparación para entrevista con Mia

> Nodo dedicado: qué sabemos del pricing de HappyRobot, qué es hipótesis, cómo lo pensaría [Mia](../personas/mia-bjorkenstam.md) (ex-FX sales 10 años + Palantir Deal Team OCEO 6 años) y cómo debe responder [Lola](../personas/lola-vilas.md) si le preguntan *"How does HappyRobot price?"*.

!!! warning "Regla fundamental para Lola"
    **NO inventar números concretos como si fueran datos de HR.** El pricing real es opaco por diseño. Lola debe demostrar dominio de los **vectores** y la **motion**, presentar rangos como **hipótesis razonada**, y cerrar invitando a Mia a validar. Mia respeta el framework por encima del número exacto.

---

## TL;DR — 5 bullets accionables

1. **El pricing de HR es opaco por diseño** (típico enterprise B2B sales-led). No hay pricing page pública en happyrobot.ai. La página de docs (`docs.happyrobot.ai/pricing`) existe pero está **gated por access code** — sólo se ve cuando ya eres cuenta. Esto en sí mismo es señal: HR vende named-account, no self-serve. [A: HR-DOCS, HR-WEB]
2. **ALERTA: el blog de openmic.ai cita tiers HR "$49 / $149 / $299 / Enterprise" con buckets de chats.** Esto es **SEO-fabricated o data del producto equivocado** — conflicta con la pricing docs gated de HR, los tiers son SMB chat (no enterprise voice/logistics) y el patrón es típico de affiliate listicles. **No usar como dato, ni siquiera mencionar que se ha leído.** [C: OPENMIC-ALT]
3. **Hipótesis razonada de ACV** (derivada de Serie B math + comparables): pilot/land **$50K–$150K**, expanded customer **$250K–$600K**, tier-1 DHL-scale **$1M–$5M+/año**. **Esto es hipótesis, no dato de HR.** [C: derivación propia]
4. **Mia preguntará pricing como deal-desk lens, no como número de catálogo.** Su DNA es 15 años de venta institucional senior (FX hedge funds + Palantir Deal Team OCEO). Lo que evalúa es: ¿sabe Lola pensar en levers, NRR, TCV, multi-year y discount policy? El número es secundario.
5. **Estrategia de respuesta:** vectores (platform + per-minute + per-action + FDE) → motion (land-and-expand) → Palantir parallel (AIP playbook aplicado a logistics) → cierre con *"I'd love to validate this with you"*. Humildad calibrada, no impostor.

---

## Sección 1. Lo público sobre pricing HR (poco)

### 1.1 Hechos confirmados

| Hecho | Conf | Fuente |
|---|---|---|
| Existe pricing page en `docs.happyrobot.ai/pricing` | A | [HR-DOCS] |
| La pricing page está **access-restricted** (login/access code requerido) | A | [HR-DOCS] verificación directa 2026-05-21 |
| No hay pricing page en `happyrobot.ai` (404 en `/pricing`) | A | [HR-WEB] verificación directa 2026-05-21 |
| Modelo **developer pay-as-you-go**: pagas por minutos de llamada usados | B | [FP-HR], síntesis search |
| **10 minutos gratis** al crear cuenta para testear plataforma | B | [FP-HR] |
| **Enterprise custom plans** para volumen alto, SLAs, use cases complejos — contacto `founders@happyrobot.ai` | A | [HR-DOCS-PUBLIC-COPY] (texto público fuera del paywall) |
| **70+ clientes enterprise**: DHL, Ryder, Schneider, Werner, MODE, US Xpress, WWEX, Circle, Samsara, Naturgy, CMA CGM, Job&Talent | A | [HR-SERIESB], [SAASNEWS-HR] |
| **DHL Supply Chain**: "millones de minutos/año" + cientos de miles de emails/año + 25% delivery-time reduction | A | [DHL-PR], [FREIGHTWAVES-DHL] |
| **Circle Logistics** ($800M freight broker): 5x+ ROI, 10% mejores márgenes, 18% loads booked zero-touch, 80–100% reducción manual calls, 100% calls answered 24/7 | A | [HR-CIRCLE-CASE] |
| Funding total: $62M ($15.6M Serie A dic 2024 + $44M Serie B sept 2025); valoración ~$500M | A | [HR-SERIESB], [SACRA-HR] |
| Pilot-to-contract conversion: **95%+** | B | [HR-UPSTARTS] |

### 1.2 Señal clave del modelo: **per-action en logistics**

HR factura **per-action en logistics workflows** — no voice puro tipo Bland/Vapi. Cita (síntesis de search, fuente secundaria):

> *"We charge per action — schedule a load, update a status, process a rate confirmation — not solely per minute."* [C: search synthesis]

Esto sugiere un **modelo híbrido outcome/per-action** alineado con la motion vertical-logistics, no commodity voice-AI. Es **lo que justifica el premium** sobre Bland ($0.11/min) o Vapi ($0.05–$0.25/min).

### 1.3 Lo que NO es público

- Per-minute rate específico (e.g., $0.10/min, $0.20/min) — sin fuente
- ACV / median deal size — sin fuente
- ARR exacto — sin fuente (Sacra y Tracxn no publican)
- Estructura del enterprise plan (platform fee + usage? deployment fee FDE? multi-year discounts?)
- Discount levers o policy

### 1.4 Alerta sobre el dato falso de openmic.ai

!!! danger "Dato en conflicto: el blog de openmic.ai NO es fiable"
    [OPENMIC-ALT] publica tiers de HappyRobot "$49 / $149 / $299 / Enterprise" con buckets "1,000 / 5,000 / 20,000 chats". **Esto es muy probablemente SEO-fabricated o data del producto equivocado**:

    1. Conflicta con la pricing docs gated de HR (que ni siquiera muestra estos tiers en su URL pública).
    2. Los buckets son **SMB chat tiers**, no enterprise voice/logistics — no encajan con el ICP HR (DHL, Ryder, Schneider).
    3. HR es **sales-led enterprise sin self-serve público** — no encaja con un menú de planes a precio fijo SMB.
    4. Las cifras son **redondas y genéricas**, patrón típico de affiliate listicles que rellenan tablas con números plausibles para SEO.

    **Confianza: C. No usar como dato. No mencionar en la entrevista que se ha leído. Si Mia menciona el blog, Lola puede confirmar que lo vio y descartarlo por los 4 motivos anteriores — demuestra criterio.**

---

## Sección 2. Hipótesis de modelo pricing

> **Aviso crítico:** toda esta sección es **derivación combinando señales del producto + comparables públicos + Serie B math**. **No tiene fuente HR oficial.** Lola debe presentarla como hipótesis, nunca como dato.

### 2.1 Vectores típicos en AI agents enterprise

Cinco palancas que vendors enterprise AI combinan en proporciones distintas:

| Vector | Qué es | Quién lo usa típicamente |
|---|---|---|
| **Platform fee anual** (entry floor) | Subscripción base que da derecho a usar la plataforma | Sierra ($50K setup), Decagon (redline $50K), Parloa (floor $300K) |
| **Per-minute voice** | $/minuto de conversación voice | Vapi $0.05–$0.25, Retell $0.07, Bland $0.11 |
| **Per-conversation / per-resolution** | $/conversación o resolución exitosa | Intercom Fin $0.99/res, Zendesk $1.50, Salesforce Agentforce $2.00 |
| **Per-action / per-workflow** (logistics-specific) | $/outcome operativo: "load booked", "rate confirmed", "check call completed" | Hipótesis HR; análogo Sierra outcome-based |
| **FDE deployment fee** | Fee de implementación con ingenieros embebidos | Palantir (Bootcamp/FDE), HR (modelo replicado) |
| **Outcomes-based** (Sierra-style) | $/resolución exitosa medida contra SLA | Sierra (per-resolution $1–$5) |

### 2.2 Hipótesis combinada para HR

Estructura híbrida con 4–5 componentes:

| Componente | Hipótesis del rango | Justificación |
|---|---|---|
| **Platform fee anual** | **$50K–$150K/año** floor para enterprise base | Estándar enterprise vertical-AI; alineado con Sierra/Decagon floors |
| **Per-minute voice** | **$0.10–$0.30/min all-in** | Premium sobre Vapi/Retell/Bland por fine-tuning vertical + compliance pack |
| **Per-action / per-workflow** | **$0.50–$5 por outcome** (load booked, check call completed, rate confirmed) | Alineado con outcomes logistics; análogo Sierra $1–$5 per resolution |
| **FDE deployment fee** | **$50K–$250K** one-time o anual (opcional/Tier-1) | Modelo Palantir Bootcamp/FDE; alinea con "forward deployed" en HR job postings |
| **Governance / Evals / Bridge add-on** | **$20K–$80K/año** | Módulo separable; Bridge es producto post-Serie B |
| **Multi-year commit discount** | **10–25%** por commit 2–3 años | Estándar enterprise SaaS |

### 2.3 ACV típico inferido

| Tier | ACV hipotético | Perfil |
|---|---|---|
| **Pilot / land deal** | **$50K–$150K** | 3–6 meses, 1 use case, 1 región |
| **Expanded customer** | **$250K–$600K** | Multi-use-case, multi-región |
| **Tier-1 (DHL-scale)** | **$1M–$5M+/año** | Multi-país, multi-vertical, FDE dedicados |
| **Mediana estimada del portfolio** | **$250K–$600K** | Consistente con comparables Sierra/Decagon |

### 2.4 Triangulación con comparables (datos públicos)

| Vendor | Modelo | ACV / floor | Fuente | Conf |
|---|---|---|---|---|
| **Sierra AI** | Outcome-based per resolved conv | Floor $150K; Y1 $200K–$350K; scale $350K–$750K; multi-channel enterprise $750K–$1.5M+; per-resolution $1–$5; setup $50K–$200K | [QUIQ-SIERRA], [LORIKEET-SIERRA] | A |
| **Decagon** | Custom enterprise per-conv o per-resolution | **Mediana $386K**; rango $95K–$590K+ (Vendr data); redline $50K | [VENDR-DECAGON], [EESEL-DECAGON] | A |
| **Parloa** | Custom enterprise | **Floor $300K/año** + integration/PS; no self-serve | [EESEL-PARLOA] | B |
| **Intercom Fin** | Per-resolution | $0.99/resolution | [QUICKCHAT-PRICING] | A |
| **Zendesk AI Agents** | Per-resolution | ~$1.50/resolution | [QUICKCHAT-PRICING] | A |
| **Salesforce Agentforce** | Per-resolution | $2.00/resolution | [QUICKCHAT-PRICING] | A |
| **Palantir AIP** | Custom enterprise multi-year TCV | **7–8 cifras típico**; Bootcamp gratis o custom | Conocimiento mercado; SEC 10-K | A |

**Síntesis:** la **mediana Decagon de $386K** y la **banda Sierra $200K–$750K** son el comparable más cercano a HR (también vertical, también enterprise, también deal-team driven). HR probablemente vive en esa misma banda con tail superior gracias a logos como DHL.

### 2.5 Serie B math (back-of-envelope)

- $500M valuation Serie B [A: SACRA-HR]
- Múltiplo vertical-AI 2025: 15–30x ARR forward
- → **ARR estimado $15M–$33M**
- 70+ clientes → **ACV medio $215K–$470K** [C: derivación propia]

Esta derivación es **consistente** con la triangulación Decagon/Sierra arriba — confianza B/C cualitativa de que el orden de magnitud es correcto.

!!! note "Recordatorio: todo lo de Sección 2 es HIPÓTESIS"
    Si Lola dice esto en la entrevista, debe etiquetarlo claramente: *"My read..."*, *"My back-of-envelope..."*, *"I'd hypothesise..."*. Nunca *"HR charges $X"*.

---

## Sección 3. Cómo pensaría Mia el pricing (ex-FX sales + Palantir Deal Team)

### 3.1 Las dos lentes que Mia trae

Mia tiene **dos backgrounds que convergen en la misma forma de pensar pricing**:

**Lente 1 — 10 años FX sales en banca City Londres (Barclays + UBS, 2010–2020)**
- Pricing en FX = **basis points por deal**, no catálogo público
- Cada cliente (hedge fund, asset manager) negocia spread basado en volumen, relación, compromiso
- El "precio" es **resultado de la negociación**, no un input al principio
- Mia internalizó: pricing = palanca de cierre, no atributo del producto

**Lente 2 — 6 años Palantir BD (2020–2026, Deployment Strategist → Commercial Lead Deal Team OCEO)**
- Palantir famously **no tiene pricing page**. Cada deal es custom multi-year TCV
- Levers: # de use cases, # de regiones, # de FDEs allocated, multi-year commit, governance tier
- Mia estuvo en el equipo que **co-diseña los grandes deals con el CEO** (OCEO = Office of CEO)
- TCV en Palantir = 7–9 figuras típico; pricing es **dimensión estratégica del deal**, no operativa

### 3.2 Implicación para Lola

Mia espera que Lola hable de pricing como **palanca de deal**, no como **atributo del producto**.

- ❌ "HR cobra $X/minuto" → suena a vendedora de commodity
- ✅ "El platform fee es el floor, pero la palanca real es expand de un use case a tres y de una región a tres, con commit multi-year" → suena a Deal Team

### 3.3 Levers que Mia esperaría en HR (su mapa mental)

| Lever | Aplicación HR | Por qué importa |
|---|---|---|
| **Deployment depth** | # de use cases activos (check calls, carrier sales, scheduling, collections...) | Cada use case = línea separable de revenue |
| **Channels** | voice + email + chat — cada canal es un upsell | NRR engine |
| **# regiones / business units** | Multi-país, multi-BU dentro del cliente | DHL → DHL Supply Chain US → DHL Express EU → DHL Global Forwarding |
| **Governance / Evals tier** | AI Auditor, compliance pack premium | Add-on con margen alto |
| **FDE allocation** | # de Forward Deployed Engineers dedicados | Servicios facturables o "incluido en tier premium" |
| **Multi-year commit** | 1y vs 2y vs 3y | Discount lever clásico |
| **Volume / minute commit** | Compromiso de minutos al año | Predictabilidad → discount |
| **Bridge add-on** | Producto nuevo post-Serie B | Net new ARR |

### 3.4 Discounting policy (hipótesis)

En Palantir, el discount es **mínimo** porque la venta es valor operacional (ROI), no comparable. HR probablemente:

- **NO** compite en precio vs Bland/Vapi (categorías distintas)
- **SÍ** compite en valor vs build-in-house o vs incumbents (Genesys, Twilio, Nice)
- Discounts grandes reservados para multi-year + reference customer + logo flagship (tipo DHL — descuento por co-marketing, no por precio)

### 3.5 Lo que descalifica un deal (HR floor inferido)

- Deal <$50K ACV → no fit (consistente con Decagon redline)
- Cliente sin volumen real (<100K llamadas/año) → no fit
- Use case fuera de logistics core o sin compliance need → menor prioridad
- Cliente no quiere FDE engagement → no fit (HR vende implementación, no API)

---

## Sección 4. Respuesta modelo para Lola si Mia pregunta *"How does HappyRobot price?"*

**Inglés, primera persona Lola, ~310 palabras. Estructura: honestidad sobre lo que no sabe → vectores → motion → Palantir parallel → invitación a validar.**

> "Honestly, the public pricing page is gated behind an access code — and that itself tells you a lot about how the company sells. So I'll share my hypothesis based on what is public and on the motion I can read from the outside.
>
> My read is that HappyRobot prices on a hybrid model with three or four levers. There's a platform fee — likely a five- or low-six-figure floor — that buys the workspace, governance, and the right to deploy AI Workers. On top of that, usage: per-minute for voice and, more interestingly, per-action for the logistics workflows — a load booked, a check call completed, a rate confirmation processed. That per-action piece is what justifies the premium versus a Bland or a Vapi, because we're not selling generic voice minutes — we're selling operational outcomes wrapped in a logistics-vertical context. And then I'd expect a Forward Deployed Engineering component, either bundled in the top tier or billed as a deployment fee, very much in the Palantir tradition you know well.
>
> The motion looks like a classic land-and-expand. Land on one use case in one region — the Circle case study describes exactly that: two years ago a carrier sales pilot, today quote-to-cash across multiple departments at 5x ROI. Then expand horizontally to new use cases, vertically into new regions and channels, and convert pilots into multi-year commits. With seventy-plus enterprise customers and a half-billion valuation, my back-of-envelope is a mid-six-figure median ACV with a meaningful tail of seven-figure accounts like DHL.
>
> But I'd love to validate this with you — because the actual lever structure, the floor, the discount policy, and where you'd want me to push pricing as a deal lever in Spain is exactly where your Palantir Deal Team instinct is sharper than my outside view. What's the actual model, and where would you want me to lean?"

### Por qué funciona esta respuesta

1. **Reconoce honestamente que no tiene acceso interno** — no finge saber.
2. **Demuestra observation skill** — la página gated misma es señal interpretable.
3. **Estructura por vectores** (platform + usage + per-action + FDE), no por número de catálogo — habla Deal Team, no SaaS rep.
4. **Invoca el playbook Palantir** ("you know well", "Palantir tradition") — Mia es ex-Palantir; reconocer su expertise sin ofuscar.
5. **Usa Circle case study como evidencia real**, no inventa — datos públicos verificables.
6. **Cierra con invitación a validar y a profundizar** — humildad calibrada + reconocimiento del expertise de Mia + pivote a deal lever en España.
7. **First-person ownership** ("my read", "my back-of-envelope") — no impostor, no charlatán.

### Antipatrones a evitar

- ❌ *"It's around $X per minute"* (inventar dato → descalifica al exponer un número no fundamentado)
- ❌ *"I don't know, I'd need to learn"* (descalifica para GM role — esperan que ya haya pensado)
- ❌ *"It's basically like Sierra"* (no lo es — Sierra es customer service, HR es logistics-vertical)
- ❌ Monólogo de 5 minutos sin invitar feedback
- ❌ Mencionar el blog openmic.ai como si fuera fuente válida

---

## Sección 5. 7 preguntas inteligentes sobre pricing que Lola puede hacer a Mia

Cuando Mia diga "good hypothesis" o asienta, Lola debe pivotar **inmediatamente** a preguntas que demuestran que ya está pensando como peer del Deal Team. Estas siete son intercambiables — Lola elige 2–3 según cómo fluya la conversación:

1. **"¿Cuál es la palanca de pricing más usada actualmente — platform fee, usage, o deployment? Y de las tres, ¿cuál crees que está infravalorada y deberíamos empujar más?"**
   *Por qué: pregunta de Deal Team senior, separa "lo que cobramos" de "lo que deberíamos cobrar".*

2. **"¿Tenemos NRR público o interno que pueda guiar el énfasis expansion vs new logo en España? Si Circle pasó de pilot a quote-to-cash en 24 meses, esa es la lever que más importa."**
   *Por qué: NRR es la métrica reina del Deal Team Palantir; mostrar que Lola la prioriza la coloca como peer.*

3. **"¿Qué autonomía tendría España en pricing Tier-1? ¿Hay un threshold de approval — deals >$X requieren OCEO sign-off como en Palantir, o el GM regional cierra?"**
   *Por qué: pregunta directa sobre governance del deal, lenguaje OCEO que Mia entiende de memoria.*

4. **"¿Hay precedentes de deals 7-figures fuera de DHL — y qué hizo la diferencia? Lo que quiero entender es si DHL es replicable o es outlier de logo flagship."**
   *Por qué: separa "trofeo de marketing" de "playbook reproducible". Pensamiento de account strategy.*

5. **"¿Cómo manejamos el discounting? Palantir famously no descontaba grandes salvo por multi-year + co-marketing. ¿Es la misma postura en HR, o hay más flexibilidad por estar en fase de land?"**
   *Por qué: cita explícita del playbook Palantir; demuestra que Lola lo conoce y lo está aplicando.*

6. **"Comparado con voice-only (Bland/Vapi) que son commodity per-minute, ¿qué premium nos permite el per-action en logistics? Quiero saber dónde está el price ceiling antes de empezar a negociar Iberdrola o Naturgy."**
   *Por qué: nombra cuentas españolas concretas; demuestra que ya está mapeando el territorio.*

7. **"Si entra una RFP de Iberdrola o BBVA pidiendo precio antes del piloto, ¿cómo respondemos sin revelar floor pero sin perder el deal? ¿Hay un template de pricing memo que el Deal Team usa, o lo construimos cuenta por cuenta?"**
   *Por qué: pregunta operativa de Deal Team — process question, no abstract. Mia respeta esto.*

**Por qué estas preguntas ganan:**

- Hablan de **levers, motion, governance** — no de números de catálogo
- Citan **NRR / TCV / floor / approval threshold** — vocabulario nativo Deal Team
- Mencionan **cuentas españolas concretas** (Iberdrola, BBVA, Naturgy) — Lola es ground truth local
- Invocan el **Palantir parallel** sin recitar — fluidez, no pretensión
- Posicionan a Lola como **peer del Deal Team**, no como subordinada esperando explicaciones

---

## Sección 6. Vocabulario pricing / deal desk para Lola

Tabla operativa de términos que activan / desactivan el registro Deal Team:

### 6.1 USAR (vocabulario nativo Mia)

| Término | Cuándo |
|---|---|
| **TCV** (Total Contract Value) | Hablando de deals multi-year o tier-1 |
| **ACV** (Annual Contract Value) | Mediana de portfolio, comparables |
| **NRR** (Net Revenue Retention) | Engine de expansion; lever más importante post-land |
| **Expansion ratio** | Multiplicador pilot → contrato → expansion |
| **Pricing as deal lever** | Marco mental Mia esperará |
| **Platform fee / usage tier / deployment fee** | Tres componentes del modelo híbrido |
| **Land-and-expand pricing** | Motion Palantir/HR replicado |
| **Multi-year commit / multi-year discount** | Lever clásico enterprise |
| **Executive sponsor sign-off / OCEO approval** | Governance del deal Palantir |
| **Deal team approval** | Modelo Mia conoce de memoria |
| **Pilot pricing vs production pricing** | Distinción crítica land vs scale |
| **Per-resolution / per-action / outcome-based** | Modelos modernos AI agents |
| **Floor / redline** | Lenguaje Deal Team — mínimo aceptable |
| **Discount lever** | No "descuento" plano — "lever" implica intencional |
| **Co-marketing concession** | Discount estratégico (DHL-style) |
| **Production within X weeks** | KPI Palantir/Mabrey — señal de fluidez |

### 6.2 EVITAR (delatan SaaS thinking, no Deal Team)

| Término | Por qué evitar |
|---|---|
| **"List price"** | HR no tiene list price; el concepto mismo es ajeno al modelo |
| **"Discount %"** plano | Suena a vendedora de catálogo; usar "discount lever" o "concession" |
| **"Sticker shock"** | Concepto SMB/consumer; no aplica en enterprise sales-led |
| **"Race to bottom"** | Asume competencia en precio; HR juega vertical premium |
| **"Out of the box pricing"** | HR no es out-of-the-box, es FDE-deployed |
| **"Per-seat licensing"** | No es el modelo HR; suena a HubSpot/Salesforce clásico |
| **"Freemium / free trial"** | HR no tiene tier freemium real (los 10 min son hook, no plan) |
| **"Customer journey"** | Consulting-speak; Palantir-mindset rechaza |
| **"Pricing optimization"** | Sin contexto suena a consultoría McKinsey |

### 6.3 Riesgo crítico — el dato falso de openmic.ai

> **Si Lola menciona "$49 / $149 / $299" como si fuera pricing de HR, queda descalificada al instante.** Mia o sabe que es falso (probable, dado que es ex-HR ahora) o no lo conoce — en cualquier caso es un fail. El blog [OPENMIC-ALT] tiene tiers fabricados. Si Mia menciona el blog primero, Lola puede validar la observación de que "esos tiers no encajan con el ICP enterprise" — demuestra criterio. Si Mia no lo menciona, Lola tampoco.

---

## Sección 7. Trampas comunes que Lola debe evitar

| Trampa | Por qué descalifica | Qué hacer en su lugar |
|---|---|---|
| **Inventar pricing concreto como dato** ("I think it's $200K/year") | Mia descubrirá inmediatamente que no tiene fuente; pérdida de credibilidad | Etiquetar como hipótesis: *"My read..."*, *"My back-of-envelope..."* |
| **Decir "no lo sé" plano** | Descalifica para GM role; esperan que ya haya pensado el tema | Honestidad calibrada: *"Public data is limited but here's my hypothesis based on..."* |
| **Citar el blog openmic.ai** ($49/$149/$299) | El dato es SEO-fabricated; Mia probablemente lo sabe; señal de juicio pobre | No mencionar. Si Mia lo trae, validar con los 4 motivos del Sección 1.4 |
| **Tratar pricing como problema-de-marketing** | Mia lo trata como deal lever; verlo como "comunicación de valor" es bajar nivel | Hablar de levers, governance, multi-year, discount policy |
| **Comparar HR con Bland/Vapi como competidor de pricing** | HR juega vertical premium, no commodity voice — equivocar la categoría es fail | Comparar con Sierra/Decagon/Parloa; explicar premium por per-action en logistics |
| **Recitar números de Palantir AIP** sin contexto | Sonar a wikipedia de Palantir, no a alguien que entiende cómo se aplica a HR | Citar el modelo (FDE + Bootcamp + multi-year TCV) y traducirlo al contexto HR |
| **Hablar de "list price" o "discount %"** | Vocabulario SaaS-de-catálogo; Mia viene de FX (basis points por deal) y Palantir (TCV custom) | "Pricing as deal lever", "discount lever", "multi-year concession" |
| **Sobrevender certeza** ("I know exactly how this works") | Mia respeta el framework + humildad; falsa certeza es señal red flag | Invitación explícita a validar: *"I'd love to validate this with you"* |
| **No conectar pricing con motion de cuenta** | Pricing aislado del motion es respuesta de junior PM, no de GM | Conectar a land-and-expand, NRR, expansion ratio Circle/DHL |
| **Hablar solo de US comparables** | Mia opera EMEA; falta contexto EU AI Act + GDPR + EU pricing dynamics | Mencionar dynamics EU: data residency, compliance pack como add-on monetizable |

---

## Sección 8. Conexiones con otros nodos

- [Mia Bjorkenstam](../personas/mia-bjorkenstam.md) — perfil completo de la entrevistadora
- [Palantir como North Star](../empresa/palantir-northstar.md) — playbook completo Palantir, NRR 134%, FDE, AIP Bootcamp
- [Producto HR](../empresa/producto.md) — AI Workers, hybrid agentic+deterministic, shared context, FDE
- [HappyRobot — Overview](../empresa/happyrobot.md) — funding, métricas, clientes
- [Expansión España](../empresa/expansion-espana.md) — posiciones abiertas, cuentas heredadas
- [Forward Deployed Engineer](../tecnologia/forward-deployed.md) — concepto operativo central
- [Preguntas Mia](preguntas-mia.md) — banco de preguntas específicas
- [Fit candidata](fit-candidata.md) — mapeo Lola ↔ HR
- [Primeros 90 días](primeros-90-dias.md) — plan accionable
- [Lola Vilas](../personas/lola-vilas.md) — perfil candidata
- [Javier Palafox](../personas/javier-palafox.md) — co-founder, probable manager directo de Mia
- [DHL](../clientes/dhl.md) — cuenta flagship logistics
- [Job&Talent](../clientes/job-and-talent.md) — cuenta heredada España

---

## Fuentes

| ID | URL | Tipo | Acceso | Conf |
|---|---|---|---|---|
| HR-WEB | https://www.happyrobot.ai/ | Web oficial HR | 2026-05-21 | A |
| HR-DOCS | https://docs.happyrobot.ai/general/pricing | Docs oficial (gated) | 2026-05-21 | A |
| HR-DOCS-PUBLIC-COPY | Texto público de docs.happyrobot.ai fuera del paywall | Docs oficial | 2026-05-21 | A |
| HR-SERIESB | https://www.happyrobot.ai/blog/series-b-announcement | Press release oficial HR | 2026-05-21 | A |
| HR-CIRCLE-CASE | https://www.happyrobot.ai/blog/circle-logistics-x-happyrobot-case-study | Case study oficial HR | 2026-05-21 | A |
| HR-UPSTARTS | https://www.upstartsmedia.com/p/happyrobot-spanish-founders-ai-logistics | Prensa long-form HR | 2026-05-21 | A |
| DHL-PR | https://group.dhl.com/en/media-relations/press-releases/2025/dhl-boosts-operational-efficiency-and-customer-communications-with-happyrobots-ai-agents.html | Press DHL oficial | 2026-05-21 | A |
| FREIGHTWAVES-DHL | https://www.freightwaves.com/news/dhl-partners-with-happy-robot-for-ai-efficient-operations | Prensa tier-2 | 2026-05-21 | A |
| SACRA-HR | https://sacra.com/c/happyrobot/ | Datos privados market | 2026-05-21 | B |
| SAASNEWS-HR | https://www.thesaasnews.com/news/happyrobot-raises-44-million-in-series-b | Prensa tier-2 | 2026-05-21 | A |
| FP-HR | https://www.futurepedia.io/tool/happyrobot | Directorio AI tools (síntesis) | 2026-05-21 | C |
| OPENMIC-ALT | https://www.openmic.ai/blog/5-best-happyrobot-ai-alternatives-pricing-features-in-2025 | Blog SEO competidor | 2026-05-21 | **C — pricing tiers HR FABRICADOS, NO usar** |
| SUPERU | https://www.superu.ai/blogs/voice-ai-pricing-what-vapi-retell-and-bland-ai-cost-per-minute | Comparativa voice AI | 2026-05-21 | B |
| RETELL-BLOG | https://www.retellai.com/blog/vapi-vs-bland | Blog competidor (parcial) | 2026-05-21 | B |
| QUIQ-SIERRA | https://quiq.com/blog/sierra-ai-pricing/ | Blog terceros | 2026-05-21 | B |
| LORIKEET-SIERRA | https://www.lorikeetcx.ai/articles/sierra-ai-pricing-alternatives | Blog competidor | 2026-05-21 | B |
| OPENNASH | https://opennash.com/blog/sierra-ai-pricing-what-outcome-based-really-costs-and-when/ | Blog análisis | 2026-05-21 | B |
| EESEL-DECAGON | https://www.eesel.ai/blog/decagon-ai-cost | Blog comparativa | 2026-05-21 | B |
| VENDR-DECAGON | https://www.vendr.com/marketplace/decagon-ai | Marketplace data | 2026-05-21 | A — datos transaccionales |
| EESEL-PARLOA | https://www.eesel.ai/blog/parloa | Blog comparativa | 2026-05-21 | B |
| PLTR-AIP | https://www.palantir.com/platforms/aip/ | Web oficial Palantir | 2026-05-21 | A |
| PLTR-BOOTCAMP | https://www.palantir.com/platforms/aip/bootcamp/ | Web oficial Palantir | 2026-05-21 | A |
| QUICKCHAT-PRICING | https://quickchat.ai/post/ai-agent-pricing-models | Blog análisis | 2026-05-21 | B |
| RAPIDCLAW | https://rapidclaw.dev/blog/ai-agent-pricing-models-compared | Blog análisis | 2026-05-21 | B |

### Nota de confianza

- **A:** Sitios oficiales HR (web, blog, press releases), press release DHL, datos transaccionales Vendr, web oficial Palantir.
- **B:** Análisis de terceros con metodología razonable (Sacra, blogs comparativos sector AI agents).
- **C:** Síntesis de búsqueda, directorios AI sin verificación primaria. **El blog openmic.ai con tiers "$49/$149/$299" está marcado explícitamente como NO usar — son cifras SEO-fabricated.**

**Marca clara dato vs interpretación:** la Sección 2 entera (hipótesis de modelo + ACV inferido + Serie B math) es **derivación propia**, no dato verificado de HR. Las tablas de la Sección 3 sobre "cómo pensaría Mia" son inferencia razonada basada en su trayectoria, no quote directa.
