---
title: "Deal Desk España — Tactical Moves por Cuenta"
type: entrevista
status: completo
tags: [entrevista, mia-bjorkenstam, deal-desk, espana, tactical, named-accounts]
updated: 2026-05-21
---

# Deal Desk España — Tactical Moves por Cuenta

> El playbook tactical deal-by-deal para responder a [Mia Bjorkenstam](../personas/mia-bjorkenstam.md) cuando pregunte *"what concrete moves would you make in Spain to sell or unblock a deal?"*. Complemento — no sustituto — de [Primeros 90 días](primeros-90-dias.md), [Preguntas Mia](preguntas-mia.md) y [Pricing HappyRobot](pricing-happyrobot.md).

!!! tip "Cómo usar este documento"
    Cada cuenta es una respuesta independiente. Cuando Mia pregunte por una cuenta concreta, [Lola](../personas/lola-vilas.md) debe poder responder: **estado actual del deal → champion (rol, no nombre) → wedge use case → ángulo de entrada → blocker típico → su movimiento concreto semana 1-4 → expansion path 18 meses en €**. Ese es el shape que el Deal Team Palantir/OCEO evalúa.

!!! warning "Honestidad sobre los gaps de Lola"
    Lola NO es enterprise SaaS B2B veterana. NO viene de logistics. NO es FDE técnica. Mia lo sabe. La jugada NO es pretender expertise que no tiene — es enmarcar la combinación única de Lola (regulatorio + scale ops + medios + network institucional ES) como **"el ground truth español que Mia necesita y no tiene"**. Outsider que aprende rápido, no veterana fingida.

---

## TL;DR — 10 bullets accionables (lo que Lola diría si Mia preguntase "what would you do tomorrow?")

1. **El wedge HappyRobot en cuentas españolas es OPERACIONAL, no horizontal.** BBVA/Santander/Telefónica/Iberdrola están **cerradas** con OpenAI/Microsoft/AWS/Salesforce para foundation models y chat. Pero **siguen abiertas en voice ops customer-facing, collections, scheduling, field coordination**. No competir donde no se puede; abrir donde no han mirado.

2. **Naturgy es la jugada NRR más rápida del repo.** HR aparece integrado en el simulador de servicios de Naturgy [B: blink.new] vía Nedgia/IBM Consulting (jul 2025). El motion está validado. Expansion lateral a Naturgy Comercializadora + Generación + Latam es viable. **Target: €1-1.5M ARR en 18 meses.**

3. **CMA CGM tiene €100M comprometidos con Mistral AI** (abril 2025). NO competir. El ángulo HR = **voice infrastructure complementaria** (Algeciras hub, multilingüe ES/PT/EN/FR) — Mistral es foundation model + chat-first; HR es voice-native ops. Wedge España = CEVA Logistics (más federada) + Algeciras hub.

4. **Job&Talent (HQ Madrid, ya cliente HR con Clara = 1M+ entrevistas) es el multiplier ES.** Co-event Madrid Q3 2026 (€5-15K) con 8-10 prospects ETT + retail seasonal. Lo más rentable por palanca.

5. **DHL ES: NO intentar venderla.** Está gestionada por el equipo global. Lola activa DHL ES como **case study mediático Q3 2026 en prensa ES** (Cadena de Suministro + Cinco Días + El Economista) para abrir SEUR, GLS, Logista. Lead gen indirecta.

6. **EU AI Act Art. 50 = sales trigger explícito.** Enforcement 2 ago 2026. Cualquier cliente con voice agents legacy (Genesys, Avaya, NICE) tiene 75 días para evitar multa €15M / 3% global turnover. HR cumple nativamente; competidores US-only no. **Esto convierte "queréis comprar AI?" en "tenéis 75 días para evitar la multa".**

7. **DORA (jan 2025) + AESIA + sovereign-AI = sales trigger para banca/seguros.** BBVA, Santander, MAPFRE, Mutua están obligados a hacer third-party criticality assessment. OpenAI/Azure exponen CLOUD Act risk. HR ofrece EU data residency + on-prem opcional + DPA EU-compliant.

8. **Telefónica = canal, no cliente.** Telefónica Tech revende HR como **voice AI infra white-label** para sus clientes SME/mid-market. Lola debe SABER que el modelo Palantir desconfía de channels y articularlo a Mia: *"sé que es heterodoxo; lo planteo como canal con guardrails, no como reseller masivo"*.

9. **Cuentas a EVITAR los primeros 90 días:** Ministerio Defensa (Palantir cerrado + riesgo político Sumar), Inditex (Quiet AI insourced), Mercadona (lento + Google Cloud lock-in), AENA/Renfe/Adif (Ley 9/2017 = 6-12 meses procurement). Demuestra criterio ICP a Mia.

10. **Primer entregable día 30 NO es "€X de pipeline". Es "Deal Desk Spain — Top 12 accounts brief"**: 12 páginas, una por cuenta, con champion (rol), use case priorizado, blocker, palanca de unblock, primer move, pilot-to-prod target, expansion 18 meses. Habla el idioma del Deal Team Palantir/OCEO directamente.

---

## Mapa rápido — dónde foca Lola las primeras 4 semanas

| Cuenta | Eje | Estado HR | Prioridad Lola sem 1-4 |
|---|---|---|---|
| **Naturgy** | NRR | Ya integrado vía Nedgia/IBM | #1 — expansion lateral |
| **CMA CGM Iberia** | NRR | Cliente global heredado | #2 — Algeciras embedding |
| **Job&Talent** | NRR | Cliente HR (Clara) | #3 — co-event Q3 |
| **DHL ES** | NRR (indirecta) | Cliente global | #4 — case study media + co-marketing SIL |
| **BBVA** | Net new | Greenfield voice ops | Outbound + warm intro ICADE/LBS |
| **Iberdrola** | Net new | Greenfield voice ops (AWS solo IT internal) | EV charging wedge |
| **MAPFRE** | Net new | Greenfield voice ops | FNOL auto wedge |
| **Repsol** | Net new | Greenfield voice ops | Fleet distribución wedge |
| **SEUR** | Net new | Greenfield | Last-mile customer service |
| **Telefónica** | Net new (canal) | Atrapada Azure | Telefónica Tech partnership |
| Inditex / Mercadona / Defensa / AENA / Santander / CaixaBank / Mutua / Endesa / El Corte Inglés / Renfe | EVITAR mes 1-3 | Cerradas o procurement imposible | Demostrar disciplina ICP |

---

## EJE 1: NRR plays — expansion en cuentas EMEA existentes

Esto es lo más rápido en revenue. Vocabulario Palantir: *expansion path $30K → $300K → $3M*. Mia heredó 4 cuentas día 1 (Naturgy, Job&Talent, CMA CGM, DHL). Lola NO redescubre — orquesta y profundiza.

### 1.1 Naturgy — la jugada NRR más rápida del repo

**Estado actual confirmado:**
- Nedgia (gas distributor del grupo Naturgy) lanzó AI agents virtuales con IBM Consulting (jul 2025) para appointment scheduling, lectura de contador, modificación de datos de suministro [A: NATURGY-NEDGIA-IBM, NATURGY-AI-PLATFORM].
- HappyRobot aparece integrado en el simulador de servicios de Naturgy [B: NATURGY-HR-BLINK].
- Naturgy adherida al **EU AI Pact** (sept 2025).
- "AI-native digital platform" como narrativa pública del grupo [B: NATURGY-AI-PLATFORM].

**Mapa de la cuenta — unidades del grupo:**

| Unidad | Tamaño aprox. | Use case HR | Estado |
|---|---|---|---|
| **Nedgia** (gas distribución) | ~4M puntos suministro | Appointments inspección, lectura contador | YA cliente vía IBM — palanca para expansion |
| **Naturgy Comercializadora** | ~9M clientes (luz+gas) | Customer service masivo, churn calls, retention, billing disputes | Probablemente cubierto por Genesys legacy — wedge: voice AI Art-50-compliant |
| **Naturgy Generación** | Plantas + parques eólicos | Field ops scheduling, maintenance dispatch | Greenfield |
| **Naturgy Latam** (Argentina, Brasil, Chile, México, Panamá) | ~3M clientes | Multi-país customer service ES, collections | Greenfield — natural extension |

**Stakeholder map:**
- **CDO / Head of Digital Transformation Naturgy** — sponsor estratégico, ya alineado con narrativa "AI-native". Champion.
- **Director Customer Experience / Atención al Cliente** — economic buyer comercializadora.
- **Director Operaciones Generación** — economic buyer field ops.
- **Blocker probable:** Procurement Naturgy lento (sector regulado) + Genesys legacy contact center con contrato multi-año + IBM Consulting como partner actual.

**Movimiento Lola — semana 1:**
1. Pedir a Mia el deck original presentado a Naturgy + contacto del champion CDO + handover formal de la cuenta.
2. Mail al CDO ofreciendo 45 min: *"ya validasteis el voice agent en inspecciones técnicas de Nedgia; la misma arquitectura puede atacar collections de impagos en comercializadora con ROI 119x según datos HR finance vertical"* [B: HR-BLOG-FIN].
3. Llevar a la reunión un mockup workflow específico Naturgy (no genérico). Input: pliego típico de retention. Output: AI agent intentando retain 30s antes de churn final.

**Unblock plays:**
- **Procurement lento** → usar ticket Nedgia ya firmado como referencia intra-grupo. Evitar nuevo proceso completo.
- **Genesys legacy** → posicionar HR como *layer encima* de Genesys, no reemplazo.
- **IBM partner** → NO competir; mantener IBM Consulting como integrador del deal. HR es producto, IBM es servicio.

**KPI 18 meses + ACV target:**
- Q3 2026: pilot Naturgy comercializadora retention/collections — ~€80K
- Q1 2027: rollout customer service Naturgy España — ~€300K
- Q3 2027: Naturgy Latam (Argentina + México) — €500K-1M
- **Total ARR 18 meses target: €1-1.5M** [C: estimación propia derivada de pricing-happyrobot.md]

**Lectura para Mia:**
> *"Naturgy es mi cuenta #1 porque el motion está validado. Quiero convertir 4M puntos suministro Nedgia en 12M puntos suministro grupo + Latam en 18 meses. Trabajo con IBM como integrador, no contra."*

---

### 1.2 CMA CGM Iberia — voice infra complementaria a Mistral

**Estado actual confirmado:**
- Cliente EMEA heredado por Mia (press release feb 2026) [A: GNW-MIA].
- CMA CGM anunció **€100M / 5 años con Mistral AI** (abril 2025) [A: CMACGM-MISTRAL].
- Operación directa España: Algeciras, Bilbao, Valencia, Barcelona + CEVA Logistics (top-10 3PL España).
- CMA CGM España ≈ €500M revenue estimado [B], >800 empleados.

**Por qué España es expansion natural:**
- **Algeciras** = hub mundial transbordo Europa-África-LATAM (APM Terminals + CMA CGM TCB).
- **Valencia + Barcelona** = 10M+ TEUs/año combinados.
- **CEVA Logistics ES** = top-10 3PL en España.

**Mapa de la cuenta:**

| Unidad | Use case HR diferenciado vs Mistral | Hook |
|---|---|---|
| **CMA CGM Iberia** (shipping) | Voice agents ES/PT/EN/FR para coordinación con shippers/freight forwarders en Algeciras, Valencia, Bilbao. Mistral = chat/text-first; HR = voice-native | Multilingüe + voz |
| **CEVA Logistics ES** | Carrier sourcing voice, scheduling, customer service tracking | "DHL playbook" aplicado |
| **Cross-border México-Algeciras** | Voice bilingüe ES/EN/FR customs coordination | Único en mercado |

**Stakeholder map:**
- **Head of Operations CMA CGM Iberia** (Algeciras / Madrid) — economic buyer local.
- **CDO CMA CGM** (Marsella) — strategic sponsor del Mistral deal. Lola NO va a Marsella; Mia ya tiene esa relación.
- **Director CEVA Iberia** — más federado, ticket más rápido. Champion ideal.
- **Blocker probable:** decisión centralizada Marsella + Mistral partnership comprometido + bandera francesa "sovereign AI champion".

**Movimiento Lola — semana 2:**
1. Coordinar con Mia: ella tiene la relación central. Lola va a Algeciras.
2. **Visita física puerto Algeciras** — "una mañana en operaciones". Lenguaje Palantir-perfect (Echo embedded). Sentarse 2-3 horas con el dispatcher coordinator que hace 200+ llamadas/día.
3. Documentar 5 workflows reales (1 página cada uno) y devolverlos al cliente semana siguiente como "AI Worker brief — Algeciras hub".
4. Pedir pilot scope-limited: AI agent para slot booking confirmation de container pickup. KPI binario: response time <30s vs media actual >4h.

**Unblock plays:**
- **Mistral lock-in perceptual** → posicionar HR como *"voice infrastructure complementaria"*. Frase: *"Mistral es el cerebro general; nosotros somos el operador de teléfono / email / WhatsApp."*
- **Decisión Marsella** → ir por CEVA primero (federada), usarla como caballo de Troya hacia CMA CGM shipping.
- **Sovereign AI francesa** → NO atacar Mistral. Enfatizar founders españoles + EU data residency + Madrid hub.

**KPI 18 meses:**
- Q3 2026: pilot Algeciras slot booking voice — ~€60K
- Q1 2027: rollout CEVA España carrier sourcing — ~€250K
- Q2 2027: CMA CGM Iberia customer service multilingüe — ~€400K
- **18 meses: €700K-1M ARR España solo** [C]

**Lectura para Mia:**
> *"CMA CGM es disciplina: NO compito con Mistral. Vendo lo que Mistral no hace. España es el wedge porque Algeciras es ground zero del transbordo global y CEVA es la unidad más permeable."*

---

### 1.3 DHL Supply Chain ES — lead gen indirecta, NO venta directa

**Estado actual confirmado:**
- Partnership global anunciada nov 2025 tras 18 meses validation [A: HR-DHL].
- DHL Express Spain (~€800M revenue) + DHL Supply Chain Spain.
- Decisión centralizada en Bonn.

**Por qué Lola NO debe intentar "vender DHL España":**
- El equipo global HR ya gestiona la cuenta.
- Decisión Bonn, no Madrid.
- **Mia evaluará negativamente si Lola dice "voy a vender DHL España"** — clásico move de un AE que no entiende el playbook FDE.

**Lo que Lola SÍ debe hacer — ángulo Echo / Deployment Strategist:**

| Acción | Por qué | Output |
|---|---|---|
| **Activar DHL ES como case study mediático Q3 2026** | Lola tiene 30+ apariciones tier-1 medios desde Uber. Sabe colocar historias en Cadena de Suministro + El Economista + Expansión | 2-3 piezas con CIO DHL Iberia. Halo para abrir SEUR, GLS, Logista |
| **Co-marketing con DHL ES en SIL Barcelona 2026** | Mayor feria logística sur Europa, jun 2026 | Demo joint. Pipeline 20-30 conversaciones |
| **Mapeo cross-sell DHL ES → clientes DHL ES** | DHL ES tiene cientos de clientes corporates (Inditex usa DHL para parte de logística) | Lead gen indirecta: clientes DHL que vean los AI agents pueden querer lo mismo |
| **Reference call con CIO DHL Iberia para prospects** | Cuando Lola venda a SEUR/GLS, una llamada de referencia desde DHL Iberia (no Bonn) es 10x más potente | Sales asset reutilizable |

**Movimiento Lola — semana 3:**
- Coordinar con global AM DHL para pedir 30 min con CIO DHL Iberia (Madrid). Not a sale — discovery + co-marketing apetito.
- Llevar brief 2 páginas: "Cómo otros clientes logísticos españoles podrían ver lo que vosotros estáis haciendo, y cómo eso os beneficia (employer brand, supplier confidence)".

**Unblock plays:**
- **Decisión global Bonn** → NO bypass; sumar al equipo global como co-protagonista, no como bloqueo.
- **DHL no comparte deal details públicamente** → vender la *forma* del deal sin métricas exactas — "millions of voice minutes processed annually" ya está publicado.

**KPI 18 meses:** No es expansion DHL — es **lead generation indirecta**. Target: **5 prospects nuevos en logistics ES atribuibles a un DHL touch point en 6 meses.**

**Lectura para Mia:**
> *"DHL ES no la vendo; la activo. Es mi halo para SEUR, GLS, Logista, Correos Express. La métrica es 5 logos nuevos atribuibles a un DHL touch point en 6 meses, no ARR DHL directo."*

---

### 1.4 Job&Talent — el multiplier local

**Estado actual confirmado:**
- ~4,000 empleados, 10 países, 3,250+ companies served.
- 1M+ AI interviews via Clara, 20K+ hires, +60% shift confirmation.
- HQ Madrid. Case study publicado abiertamente feb 2026 [A: HR-JT].

**Mapa de la cuenta:**

| Vector | Estado | Use case adicional HR |
|---|---|---|
| **Recruiting (Clara)** | ✅ Live | Capturado. 60% vacantes vía AI |
| **Worker engagement post-hire** | Greenfield | Voice agent retention workers temporales |
| **Shift management automation** | Greenfield | Voice/SMS confirmación turnos + sustitución last-minute |
| **Payroll dispute resolution voice** | Greenfield | Workers temporales tienen dudas constantes — wedge eficiencia |
| **Customer (company) success voice** | Greenfield | AI agent para QBRs, NPS, expansion |

**Stakeholder map:**
- **CEO Juan Urdiales** (co-founder J&T) — Mia probablemente tiene contacto directo. Founder-to-founder.
- **CTO** — el que activó Clara originalmente. Champion técnico.
- **VP Operations** — economic buyer shift management.
- **Blocker probable:** J&T competidor directo de Adecco/Randstad → tensión perceptual en co-events.

**Movimiento Lola — semana 1-2:**
1. Reunión low-key con sponsor de Clara (probablemente CTO) — 30 min, café Madrid (no Zoom). *"Estoy nueva, dime qué funciona y qué te gustaría que hiciéramos mejor en 6 meses."*
2. Documentar 3-5 ideas expansion (worker retention voice, shift confirmation, payroll Q&A). Brief semana siguiente.
3. **Co-event Q3 2026**: J&T + HR + Mia + Lola en Madrid. Invitar 10-12 personas: peers de J&T (Adecco, Randstad, Manpower España), retailers seasonal (Inditex picos, Mercadona, El Corte Inglés), logistics que contratan drivers (SEUR, Logista). **Coste: €5-15K. ROI: 2-3 conversaciones reales abiertas.**

**Unblock plays:**
- **Tensión competitiva con Adecco/Randstad** → posicionar evento como *"AI in workforce ops cross-industry"*, NO "Clara case study". Foco en problema (rotación, shift management), no en J&T.

**KPI 12 meses:**
- Q2 2026: pilot worker retention voice — ~€50K
- Q4 2026: shift confirmation automation — ~€150K
- **12 meses: €300-500K ARR expansion J&T** [C]
- Lead gen indirecta: 5-8 conversaciones ETT/retailers desde co-event.

**Lectura para Mia:**
> *"Job&Talent es mi multiplier. No es solo NRR; es la palanca para abrir el resto del mid-market workforce + retail seasonal en España. €5-15K de evento bien hecho = 5-8 conversaciones reales."*

---

## EJE 2: Net new opens — 6 cuentas Tier-1 ES profundas

Disciplina ICP — 6 cuentas profundas, no 14 superficiales. Fit Palantir-style: Fortune-equivalent, ops multi-billion, datos fragmentados, costo de ineficiencia alto. Para cada una:

!!! warning "CRITICAL — el wedge es operacional, no horizontal"
    BBVA / Santander / Iberdrola / Telefónica están **cerradas con OpenAI / Microsoft Azure / AWS / Salesforce para foundation models y chat enterprise**. No competir ahí. Pero **siguen abiertas en voice ops customer-facing, collections, scheduling, field coordination** — donde los megacontratos no han mirado. **El wedge HR es voice ops, no AI horizontal.**

### 2.1 BBVA — wedge collections + DORA palanca

**Por qué priorizada:**
- Top 2 banca España. Revenue ~€32B (2024).
- Adopción AI muy alta: deal con OpenAI (dic 2025) + ChatGPT Enterprise a 120K empleados + roadmap "The Eight" con 8 iniciativas estratégicas (Blue digital advisor, Banker AI, Risk ops, etc) [A: BBVA-OAI, BBVA-EIGHT].
- BBVA fue **founding partner de DeployCo** (OpenAI deployment company) [A: BBVA-DEPLOYCO] → apetito por third-party AI deployment.
- **CRITICAL**: el roadmap "The Eight" NO incluye voice AI para collections o customer-facing voice ops. Es el wedge.

**Sponsor potencial (rol, no nombre):**
- **Head of AI / Chief AI Officer BBVA** — owner roadmap "The Eight". Champion estratégico.
- **Director Recuperaciones / Collections** — economic buyer del wedge.
- **Director Atención al Cliente** — economic buyer del scale use case.

**Use case wedge: collections voice AI.** Por qué resuena:
- Cartera retail + SME enorme. Collections = coste + impacto EBT directo.
- HR métrica pública: 119x ROI finance vertical [B: HR-BLOG-FIN].
- **DORA (jan 2025) + Art. 50 (ago 2026) + AESIA** favorecen a HR (EU-AI-Act-native + EU data residency) vs OpenAI/Azure (US-hosted, CLOUD Act risk, complica DORA third-party criticality).

**Ángulo de entrada:**
1. **Warm intro vía red ICADE/LBS de Lola.** BBVA tiene exalumnos ICADE históricamente (semillero) + LBS visibles en organigrama. Lola hace 2-3 calls preparatorias antes del outbound formal.
2. **Reference Tokio Marine** (inversor HR Series B) como señal de credibilidad insurance/financial vertical [B: HR-SERIEB].
3. **Pieza de prensa firmada por Lola en Expansión / Cinco Días sobre "voice AI + DORA"** — Lola tiene 30+ apariciones tier-1 desde Uber → editor commit es realista. Convierte a Lola en interlocutor que el CAIO de BBVA quiera conocer.

**Blocker típico + how to unblock:**
- **OpenAI lock-in perceptual** → NO atacar OpenAI. Posicionar HR como **operational layer encima de OpenAI**: *"vosotros tenéis foundation model + DeployCo; nosotros somos el AI Worker que llama, escribe, escala, con compliance EU AI Act nativo"*.
- **DORA criticality assessment** → BBVA debe demostrar resilience operativa para terceros AI. HR ofrece: deployment on-prem opcional, EU data residency, código abierto componentes auditables. Esto es **palanca, no friction**.
- **Compliance / regulatory team es el unblock real, no IT.** Lola involucra Compliance BBVA desde semana 2.

**Movimiento Lola — semanas 2-4:**
- **Semana 2:** Outbound mail al Head of AI BBVA + Director Recuperaciones. Subject: *"Voice AI for collections — DORA-compliant deployment model from a Series B founded by Spaniards"*. Adjuntar 1-pager: workflow específico recuperación impagos retail + métricas HR finance + mapeo DORA + Art. 50.
- **Semana 3:** Reunión 45 min Head of AI. **Lola lleva un FDE técnico al call — NO va sola.** Demuestra "Echo + Delta" en acción.
- **Semana 4:** Si tracción → propuesta "AI Worker Bootcamp" 5 días con datos sintéticos collections BBVA. Cliente paga el bootcamp (€25-40K — ver [pricing-happyrobot.md](pricing-happyrobot.md)). Output: workflow operativo replicado sobre dataset BBVA.

**Pricing band hipotético:** ACV target 6 figuras inicial → 7 figuras 18 meses (ver [pricing-happyrobot.md](pricing-happyrobot.md) para bandas detalladas).

**KPI 18 meses + ACV target:**
- Q4 2026: bootcamp + pilot collections retail — €100K
- Q2 2027: rollout collections retail full — €500K
- Q4 2027: customer service expansion 1 línea producto — €800K
- **18 meses target: €1-1.5M ARR** [C]

---

### 2.2 Iberdrola — EV charging wedge + customer service masivo

**Por qué priorizada:**
- Top 1 utility España. Revenue ~€49B (2024). 32M+ customers globalmente.
- AI Center of Excellence + 150+ AI use cases presentados Digital Summit (jun 2025) [A: IBE-AI-CENTRE].
- **CRITICAL: deal con AWS Bedrock AgentCore es para IT operations internas (ServiceNow change requests, incident enrichment), NO para customer-facing voice ops** [A: IBE-AWS].
- Iberdrola adherida al EU AI Pact (sept 2025).

**Sponsor potencial:**
- **Chief AI Officer Iberdrola / Director AI Center of Excellence** — sponsor estratégico.
- **Director Customer Experience España** — economic buyer customer service.
- **Director Operaciones EV charging** — owner del wedge específico (Iberdrola lidera redes públicas EV España).

**Use case wedge en orden de prioridad:**

| Use case | Por qué resuena | Ticket inicial |
|---|---|---|
| **EV charging customer support + scheduling** | Crecimiento explosivo, multilingüe, multi-país. Wedge acotado. | €100-200K |
| **Customer service voice masivo** ("dónde está mi factura", "tengo corte de luz") | 9M+ clientes ES, picos tormentas/calor | €300-500K |
| **Field ops scheduling (técnicos instalación)** | Coordinación masiva teléfono actual | €200-400K |

**Por qué EV charging es el wedge perfecto:**
- Use case acotado, técnicamente bonito (multi-canal: voice + WhatsApp + email).
- Métricas claras (response rate, FRT).
- **Conecta con narrativa pública de Lola en Uber** (escaló electrificación 5%→30% EV). Esto es Echo magic — Lola conoce el mundo EV personalmente.

**Ángulo de entrada — warm intro:**
- Lola pide reunión al Director EV Iberdrola desde la perspectiva: *"ex-Uber Spain que escaló EV 5%→30%, ahora en HR. ¿Podemos hablar 30 min sobre customer ops EV?"* Esto es **anclaje a fortaleza única de Lola** — no pretende expertise utility que no tiene, usa lo que sí tiene.

**Blocker típico + how to unblock:**
- **AWS lock-in para IT ops** → pero NO para customer-facing voice. Diferenciación clara.
- **Procurement utility lento** (sector regulado) → empezar wedge pequeño (EV charging ~€100K) que no requiera comité ejecutivo, sino budget de innovation/Director EV.
- **Compliance EU AI Act** → Iberdrola adherida AI Pact = JUEGA a favor de HR (Art. 50 compliance nativo).

**Movimiento Lola — semana 2:**
1. Outbound directo al Director EV charging Iberdrola con ángulo Uber EV.
2. Llevar a reunión 1 mockup AI Worker EV customer support: *"Cliente llama → ubica nearest available charger → si está ocupado, reserva slot → envía SMS confirmación. Todo en 90s, vs media actual 8+ min."*
3. Proponer pilot 60 días región Madrid o País Vasco (HQ Iberdrola). KPI binario: 70%+ resolución first call, response time <30s.

**Pricing band hipotético:** Wedge €100-200K Q3 → expansion €1-1.5M ARR 18 meses (ver [pricing-happyrobot.md](pricing-happyrobot.md)).

**KPI 18 meses:**
- Q3 2026: pilot EV charging customer ops — €80-100K
- Q1 2027: rollout EV España — €300K
- Q3 2027: expansion customer service Iberdrola comercializadora — €600K-1M
- **18 meses: €1-1.5M ARR** [C]

---

### 2.3 Telefónica — channel play, NO direct sale

**Por qué priorizada (de forma heterodoxa):**
- Top 1 telecom España. Revenue ~€41B grupo (2024).
- **Telefónica está atrapada con Microsoft Azure AI Foundry sobre su platform Kernel** [A: TEF-MSFT-KERNEL] — NO targetable como cliente directo voice AI enterprise.
- **Pero Telefónica Tech (división B2B) tiene >1,000 clientes corporates/SMEs y NO tiene voice AI agent platform propia.** Lanzaron "GenAI Platform" pero es chat/text [A: TEF-GENAI].

**Sponsor potencial:**
- **CEO Telefónica Tech** (rol — confirmar nombre exacto).
- **Director GenAI Platform Telefónica Tech** — champion técnico.

**Use case wedge: HR como infraestructura voice white-label revendida por Telefónica Tech para sus clientes SME/mid-market.**

**Pricing model:**
- Telefónica Tech revende HR como capa voice; HR mantiene margen software, Telefónica Tech captura servicio.
- Revenue split TBD pero target: HR vende €1-2M ARR a través de Telefónica Tech en 12 meses **sin equipo de ventas dedicado** [C].

**Blocker típico + how to unblock:**
- **Telefónica prefiere build vs buy culturalmente** → positioning explícito: *"vosotros sois GenAI horizontal; nosotros somos voice ops infra. Complementario, no competidor."*
- **Modelo Palantir desconfía de channel/reseller.** Lola debe SABER esto y articularlo a Mia con honestidad:

> *"Sé que el modelo Palantir es no-channel. Pero en mid-market ES, Telefónica Tech es el único way to scale sin agotar FDEs. Lo planteo como canal con guardrails (deal qualification compartido, FDE HR en deals >€500K, training mínimo), no como reseller masivo. Si tu instinto es no-channel-period, lo retiro."*

**Esto es CRÍTICO**: Lola demuestra que entiende el playbook Palantir Y tiene criterio para proponer adaptaciones, no copy-paste ciego.

**Movimiento Lola — mes 2-3 (NO semana 1):**
1. Mes 2: outbound exploratorio CEO Telefónica Tech vía red MBA LBS / network institucional.
2. Mes 3: workshop interno con Mia para presentar tesis "Telefónica Tech como canal mid-market ES" — Mia decide go/no-go antes de pitch formal.

**KPI 12 meses (si Mia aprueba):**
- Q4 2026: piloto white-label con 2-3 clientes SME Telefónica Tech — €200K
- 12 meses: €1-2M ARR vía canal [C]

---

### 2.4 Repsol (Moeve) — wedge fleet distribución

**Por qué priorizada:**
- Top energy España. Revenue ~€60B (2024).
- Datos públicos: 670 digital cases, 400 con AI, 34 agents desplegados con **Microsoft Copilot + Accenture + NVIDIA** [A: REPSOL-AI, REPSOL-RAIP].
- **CRITICAL: los agents están en internal ops + R&D + manufacturing, NO en customer-facing voice ni en coordination con drivers/transportistas.**
- Repsol rebrand a "Moeve" en su división marketing+global commercial (2025) — Lola debe estar al tanto.

**Sponsor potencial:**
- **Chief Digital Officer Repsol** — owner roadmap RAIP (Repsol Artificial Intelligence Products).
- **Director Estaciones de Servicio** (3,000+ gasolineras en España) — economic buyer del wedge retail fuel.
- **Director Logistics & Distribution** — owner de coordinación con camioneros de combustible. **Champion ideal del wedge.**

**Use case wedge: driver coordination fleet distribución.** Es PURO HR — playbook Circle Logistics + DHL aplicado a Repsol. Venta lateral *"AI Worker para coordinar tu fleet de camiones"*.

**Ángulo de entrada:**
- Reference DHL (logística) + Circle Logistics (300K+ AI calls) como proof points.
- Warm intro vía red ICADE (Repsol tiene exalumnos ICADE históricamente).

**Blocker típico + how to unblock:**
- **Accenture + NVIDIA partnership** → posiblemente intentará captar el deal. Estrategia: invitar Accenture como SI partner (no competitor) — Accenture hace integración + change management; HR es el producto.
- **Microsoft Copilot lock-in** → solo para internal ops, NO para coordination con drivers externos. Diferenciación clara.

**Movimiento Lola — semana 3:**
1. Outbound al CDO Repsol: *"fleet coordination is the unsung AI wedge in oil & gas — DHL achieved 80%+ automation; we can do the same for Repsol distribución."*
2. Pedir referencia warm vía red ICADE.
3. Reunión 1: 30 min discovery. Reunión 2: workshop 3 horas con Director Distribución + 2-3 dispatcher coordinadores reales en planta La Coruña o Cartagena.

**Pricing band:** ver [pricing-happyrobot.md](pricing-happyrobot.md).

**KPI 18 meses:**
- Q4 2026: pilot driver coordination región concreta — €100K
- Q2 2027: rollout España distribución — €400K
- Q4 2027: expansion customer service estaciones — €600K
- **18 meses: €900K-1.2M ARR** [C]

---

### 2.5 MAPFRE — FNOL voice + AI Manifesto alignment

**Por qué priorizada:**
- Top 1 seguros España. 22M+ clientes globales.
- Muy madura en AI: 115+ AI use cases, 70% clientes ES interactúan con AI, MIA GPT virtual assistant 90K consultas/año, 80%+ CSAT [A: MAPFRE-AI].
- **CRITICAL: MAPFRE lanzó AI Manifesto (may 2025) "humanistic, ethical, responsible AI"** — narrativa muy alineada con EU AI Act / HR positioning [A: MAPFRE-AI-MANIFESTO].

**Sponsor potencial:**
- **Director AI Center MAPFRE** (entidad lanzada 2025) — strategic sponsor.
- **Director Claims España** — economic buyer wedge claims.
- **Director MAPFRE LATAM** — sponsor cross-border (México, Brasil, Perú).

**Use case wedge en orden de prioridad:**

| Use case | Por qué resuena | Ticket |
|---|---|---|
| **First Notice of Loss (FNOL) voice agent** | Cliente llama tras accidente → AI recoge datos estructurados → envía back-office. Wedge perfecto: high volume, KPI claro | €150-300K |
| **Collections impagos primas** | Volumen masivo, ROI claro | €200K |
| **Customer service multi-país LATAM** (México, Brasil, Perú) | MAPFRE LATAM expansion natural; HR multilingüe ES/PT | €400-800K |

**Ángulo de entrada:**
- **Tokio Marine como referencia** (inversor HR Series B + insurance vertical) — credibilidad insurance instantánea.
- **AI Manifesto MAPFRE + EU AI Act compliance HR = mismo lenguaje.** Lola lleva el manifesto en mano y mapea cada principio MAPFRE con feature HR (transparencia, human oversight, AI Auditor).

**Blocker típico + how to unblock:**
- **Mutua Madrileña ya usó Google Cloud** (700 question types, 60% interactions digital) [A: MUTUA-GCP] — MAPFRE no querrá ser segundo. Mitigación: posicionar HR como complementario (voice vs chat) — Mutua usa chat, MAPFRE puede liderar en voice.
- **MAPFRE es mutua, decisión colegiada lenta** → ir por wedge claims FNOL (sponsor: Director Claims, no requiere comité ejecutivo).

**Movimiento Lola — semana 3-4:**
1. Outbound al Director AI Center MAPFRE con ángulo: *"matched the AI Manifesto principle-by-principle with HR product capabilities"*.
2. Reunión con 1 mockup específico FNOL voice agent para auto (use case más volumen MAPFRE).
3. Proponer co-investigación "voice AI ethical principles" — paper conjunto. Activa el ego del AI Center + da PR mutual.

**KPI 18 meses:**
- Q4 2026: pilot FNOL auto España — €150K
- Q2 2027: rollout claims España multi-line — €500K
- Q4 2027: expansion LATAM (México first) — €800K
- **18 meses: €1.2-1.8M ARR** [C]

---

### 2.6 SEUR Geopost — la cuenta logística más fácil de ganar

**Por qué priorizada:**
- Líder paquetería España, ~€1,200M+ revenue. Subsidiaria DPDgroup (parte La Poste).
- Mercado paquetería ES muy concentrado: SEUR + DHL + GLS + Correos = ~70% mercado.
- **DHL es competidor directo SEUR → DHL es la referencia perfecta.**

**Por qué es la cuenta más rápida para Lola:**
- DHL es competidor directo de SEUR. Use cases idénticos: scheduling, driver follow-up, customer service tracking, last-mile.
- Mercado paquetería ES extremadamente competitivo — SEUR no puede permitirse no automatizar mientras DHL lo hace.
- Lola tiene contactos vía Uber (paquetería + transporte se solapan).

**Sponsor potencial:**
- **CEO SEUR España** — sponsor estratégico más probable.
- **Director Operaciones SEUR** — economic buyer.
- **CDO / Head of Digital SEUR** — sponsor técnico.

**Use case wedge: last-mile customer service** (cliente final → *"dónde está mi paquete"*, reprogramación entrega). HR métrica 100% response rate, 0min FRT. Volumen masivo. Coste actual = call center externalizado LATAM o Marruecos.

**Ángulo de entrada:**
- **Warm intro red Uber** — Lola tiene Rolodex en transporte ES. Probable cruce con SEUR.
- **Reference DHL** — explicit. *"DHL hace esto. Vosotros vais detrás."*
- **AECOC + UNO Logística + CEL** — networking sectorial.

**Blocker típico + how to unblock:**
- **DPDgroup decide en París para deals grandes** → empezar piloto España (decisión SEUR ES autónoma) y escalar a DPDgroup desde adentro.
- **GLS ya usa Aunoa** (chatbot básico) → SEUR puede tener tentación soluciones más baratas. Diferenciación: voice (Aunoa = chat-only), enterprise compliance, escalable [A: AUNOA-LOG].

**Movimiento Lola — semana 1 (es de las primeras):**
1. Outbound directo CEO SEUR (probabilidad respuesta media-alta dada referencia DHL).
2. Si no responde 5 días → vía Director Operaciones + CEL networking.
3. **Reunión 1: demo en vivo de AI Worker llamando a un "cliente simulado"** — Lola hace customer en vivo, AI agent en español responde. **Demo de 5 minutos vale más que 30 min de slides.**

**KPI 18 meses:**
- Q3 2026: pilot SEUR last-mile customer service Madrid — €80K
- Q1 2027: rollout España — €300K
- Q3 2027: scheduling entregas — €500K
- **18 meses: €700K-1M ARR** [C]

---

### Cuentas Tier-1 deliberadamente NO priorizadas (criterio Palantir-style)

Demostrar disciplina ICP a Mia importa tanto como la lista priorizada.

| Cuenta | Por qué NO | Cuándo reconsiderar |
|---|---|---|
| **Inditex** | Cultura "Quiet AI" insourced, no compra plataformas voice externas visibles. Supply chain integration interna avanzada (Operational Platform, digital twin) [B: INDITEX-QUIET-AI] | Solo si champion warm intro vía red Lola + use case muy específico (HR/recruiting o customer service tienda) |
| **Mercadona** | Legendariamente lento, insourced, Google Cloud lock-in para data [B: MERCADONA-GCP] | Año 2+ |
| **Santander** | OpenAI strategic alliance dic 2025, AI ya generando €200M savings [A: SANT-OAI] | Wedge muy específico (collections) año 2 |
| **CaixaBank** | Salesforce Agentforce gestiona 6K conversaciones/mes website+app [A: CAIXA-AGENTFORCE] | Año 2, wedge voice (no chat) |
| **Mutua Madrileña** | Google Cloud + AI virtual assistant resolviendo 86% inquiries [A: MUTUA-GCP] | Año 2+ |
| **Ministerio Defensa España** | Palantir cerrado, Sumar denunció en Cortes feb 2026 = riesgo político | NUNCA mientras Palantir esté ahí |
| **AENA** | Sector público, Ley 9/2017 procurement 6-12 meses solo licitación | Año 2 si licitación abierta |
| **Renfe / Adif** | Sector público, regulación pesada, decisión lenta | Año 2 |
| **El Corte Inglés** | Estructura familiar, decisiones opacas, ciclo largo | Año 2 |
| **Endesa** | Parte de Enel — decisión Italia + procurement utility lento. Esperar track record Iberdrola/Naturgy | Q4 2026 / Q1 2027 |

**Lectura para Mia:**
> *"Estas 10 cuentas las descarto en mes 1-3. Disciplina ICP. Año 2 algunas se reevalúan; ahora no encajan en few accounts deep expansion. Mejor 6 cuentas profundas que 16 superficiales."*

---

## EJE 3: CMA CGM — nota especial sobre cómo abrir conversación con Mistral en medio

> CMA CGM merece eje propio. La complejidad del €100M Mistral deal cambia el playbook estándar.

### El hecho difícil

CMA CGM firmó **partnership 5 años / €100M con Mistral AI** en abril 2025 [A: CMACGM-MISTRAL]. **Mistral es campeón nacional francés de soberanía AI.** CMA CGM es francés. Macron empuja sovereign AI. Hay narrativa política y comercial atada.

### Por qué HR puede entrar igual

Mistral es **foundation model + chat-first + R&D-focused**. El partnership cubre:
- LLMs custom para shipping ops
- Chat assistants internos
- Knowledge management
- Generative AI workflows

**Lo que el partnership Mistral NO cubre:**
- Voice agents multilingües ES/PT/EN/FR para coordinación humana
- Customer service voice masivo en hubs europeos
- Carrier sourcing automation
- Customs coordination cross-border

Esto es donde HR vende **voice infrastructure complementaria** — no competidor.

### Cómo abrir la conversación con CMA CGM España sin chocar con Marsella

**Frase verbal Lola al Head of Operations CMA CGM Iberia (Algeciras / Madrid):**

> *"Veo que tenéis a Mistral como brain layer para shipping ops. Eso resuelve el R&D + chat workflow side. Donde yo creo que podríamos sumar es en voice ops del hub Algeciras: confirmaciones de slot booking, coordinación con shippers/freight forwarders en ES/PT/EN/FR, customer service multilingüe LATAM. No competimos con Mistral; somos el voice layer encima."*

**Por qué funciona:**
1. **Reconoce explícitamente Mistral** — no oculta, no compite.
2. **Define un espacio diferente** — voice ops, no foundation models.
3. **Es operacional, no estratégico** — el Head of Operations decide; no requiere ratificación Marsella.
4. **España es ground zero** — Algeciras es el hub que Marsella nunca opera personalmente.

### Playbook concreto

| Fase | Acción | Sponsor | Output |
|---|---|---|---|
| **Semana 2** | Visita física Algeciras 2 días | Head of Ops Iberia | 5 workflows mapeados, 1 elegido |
| **Semana 3** | Brief "AI Worker — Algeciras hub" 1 página por workflow | Head of Ops Iberia | Pilot scope-limited propuesto |
| **Semana 4** | Pilot slot booking voice — KPI binario response <30s | Director CEVA Iberia | Pilot firmado o no |
| **Q3 2026** | Pilot live | Director CEVA Iberia | Métricas vs baseline |
| **Q4 2026** | Si pilot OK → expansion brief para Marsella (vía Mia) | Mia + CDO CMA CGM | Decisión expansion EMEA |

**KPI 18 meses CMA CGM ES + CEVA:** €700K-1M ARR [C] — ver detalle en 1.2 arriba.

### Riesgo a articular honestamente a Mia

> *"El riesgo aquí es que Mistral expanda alcance — si en 6 meses añaden voice native, mi wedge desaparece. Mitigación: empezar por CEVA (más federada), tener pilot productivo en 90 días, asegurar 3-5 artefactos irreversibles (ontology operacional Algeciras, runbook multilingüe, integraciones TMS) antes que Mistral pueda igualar."*

---

## EJE 4: Pilot-to-production unblock moves

> Mia viene del Deal Team Palantir. El litmus test interno era *"if an application is not in production within four weeks, it gets escalated"* (Ted Mabrey). El AIP Bootcamp comprime el ciclo. Lola debe articular movimientos concretos **pre/durante/post-pilot**.

### 4.1 Semana 1 del pilot — 3 acciones para garantizar producción

1. **Embedding 2-3 días en ops floor del cliente (no Zoom)** — Echo motion Palantir. *"Sit with the customer for two weeks before promising anything"*. Output: 5 workflows mapeados, 1 elegido. Documentación métricas baseline (sin baseline NO hay "irreversibilidad").
2. **Definir 1 KPI binario success/fail** firmado por sponsor. Sin claridad, el pilot se convierte en *"interesting"* pero no en *"production"*. Ejemplos por vertical:
   - Banca collections: *"+15% cash collected vs baseline en 60 días"*
   - Utility CS: *"80%+ first call resolution para top-10 query types"*
   - Logistics: *"Driver confirmation rate de 60% → 90% en 30 días"*
   - Insurance FNOL: *"Tiempo captura datos 12min → <2min"*
3. **Pedir al sponsor day-1: *"¿quién más debe estar en la sala? Necesito IT, Legal, Compliance, y al menos un operativo real. Si los traes desde día 1, salimos a producción en 6 semanas. Si no, en 6 meses."*** — frase Palantir Deal Team que Lola debe poder decir tal cual a Mia.

**NUNCA aceptar pilots con KPI vago tipo "explore use of AI" o "improve customer experience".** Muerte segura.

### 4.2 Señales tempranas "this pilot won't close" (detectables en semanas 1-4)

**Semana 1:**
- ¿El sponsor sigue en la sala en cada review? Si manda al "AI guy" en su lugar, mala señal.
- ¿IT/security ha empezado el assessment? Si todavía no, bloqueo silencioso.
- ¿El equipo operativo testa el agent activamente? Si solo "esperamos feedback de IT" → muerte lenta.

**Semana 2-3:**
- ¿Hay datos reales fluyendo? Si todavía es sintético, alerta roja.
- ¿El cliente ha mencionado procurement, legal, compliance? Si no, no está pensando en producción.
- ¿Hay otro stakeholder además del sponsor? Si no, single-point-of-failure.

**Semana 4:**
- ¿Hay plan de transición a producción documentado? Si no, escalation interna.

**Señales positivas "esto sí va a cerrar":**
- Cliente empieza a hablar de "fase 2" o "expansion" sin que tú lo menciones.
- IT/security pide reuniones para preparar deployment, no para bloquear.
- Sponsor habla del agent en términos de *"nuestro"* no *"vuestro"*.

### 4.3 Stakeholder strategy más allá del champion — el "stuck in IT" killer

**El "stuck in IT" es el killer #1 en España.** Para evitarlo, Lola orquesta 5 stakeholders desde semana 1:

| Stakeholder | Cuándo involucrar | Qué pedirle |
|---|---|---|
| **Champion / sponsor business** | Día 0 | Vision, KPI binario, budget |
| **IT / Security** | Semana 1 | Security review preview (no aprobación). Identifica blockers temprano |
| **Compliance / Legal** | Semana 1 (mandatorio banca/seguros) | DPA, AI Act assessment, GDPR review preview |
| **End user operativo** (el que va a USAR el agent) | Semana 2 | Feedback real, no del champion |
| **Procurement** | Semana 3 | Si no se involucra antes, contrato se atasca 60 días |

### 4.4 Artefactos a producir durante el pilot que vuelvan irreversible la decisión

Lola piensa el pilot como un **investment del cliente** — y por tanto el output debe ser un asset que el cliente **NO PUEDA tirar**.

| Artefacto | Por qué irreversible |
|---|---|
| **Ontología operativa documentada del cliente** (catálogo objetos, acciones, relaciones) | El cliente NO va a re-pagar a otra empresa para reconstruirla. **Esto es exactamente lo que Mia llama "ontology" en lenguaje Palantir** |
| **Runbook operativo** (cómo funciona el AI Worker en contexto específico) | Embedded knowledge — perderlo cuesta meses |
| **Integraciones técnicas live** con sistemas cliente (TMS, ERP, CRM, contact center) | Switching cost masivo |
| **Data tags y conversation flow** entrenados con datos cliente | Reentrenar = pagar de nuevo |
| **Dashboard de gobernanza** con métricas tiempo real visibles al sponsor | Sponsor ya no quiere perderlo — lo enseña a su jefe |

**Frase Lola para Mia:**
> *"Cada pilot tiene que dejar tras de sí 3-5 artefactos que el cliente NO PUEDA tirar. Si saco esos artefactos, el contrato a producción es inevitable. Si solo dejo un 'PoC interesante', el cliente lo tira a las 6 semanas y se va con otro vendor."*

### 4.5 "Stuck in IT" — 3 unblock plays específicos

1. **Security review preview semana 1**, no semana 6. Lola lleva al kick-off un **architecture brief + DPA template + SOC2 reports** y los entrega al CISO/CIO ese mismo día. Reduce ciclo IT 60→15 días.
2. **AI Auditor como demo**, no como spec. Cuando IT pregunta *"¿cómo gobernáis los outputs del agent?"* — Lola enseña dashboard en vivo, no PDF. Las dudas IT se desactivan en 15 min.
3. **Compliance officer como aliado, no obstáculo.** Lola activa al Compliance del cliente con: *"vuestro AI Auditor sale del paquete y mapea automáticamente a las guías AESIA + Art. 50. Os auditará la AEPD; nosotros os damos el informe formateado."* Compliance se convierte en sponsor, no bloqueador.

### 4.6 KPI interno HR España — pilot-to-prod conversion %

Lola propone a Mia un KPI público interno:

> **"Pilot-to-production conversion rate España: target 85%+ en primeros 12 meses."**

Esto:
- Alinea con métrica global HR (~95% pilots → contract en FDE model).
- Le da a Mia un dial accionable para evaluar performance Lola.
- Fuerza a Lola a ser selectiva con qué pilots firma (**better no pilot than failed pilot**).

---

## EJE 5: Palancas regulatorias España como sales triggers

> Estos son los unblock moves que Mia probablemente NO conoce (ex-Palantir UK / Londres) y que Lola **DEBE** saber. Es donde la formación Derecho+ADE + experiencia regulatoria Uber de Lola le da ventaja única vs un AE genérico.

Ver también: [EU AI Act](../regulacion/eu-ai-act.md), [GDPR / LOPDGDD](../regulacion/gdpr-lopdgdd.md), [Oportunidades regulatorias España 2026](../regulacion/oportunidades-regulatorias-espana-2026.md).

### 5.1 EU AI Act Art. 50 — enforcement 2 ago 2026

**Qué es:** Art. 50 (transparency obligations) entra en vigor **2 agosto 2026**. Aplica a chatbots, virtual assistants, voice agents que interactúan con humanos + sistemas que generan contenido sintético (audio, vídeo, texto) + reconocimiento emociones + deepfakes.

**Obligaciones:**
1. Disclosure: el usuario debe saber que está hablando con una IA.
2. Diseño: el sistema debe estar diseñado para que la IA se identifique.
3. Contenido sintético: marcar como tal (machine-readable).
4. Documentación: provider debe documentar conformidad.

**Multas:** hasta **€15M o 3% global turnover** (lo que sea mayor).

**Por qué urge ahora:** Estamos a 75 días del enforcement al cierre de mes 1 de Lola (si entrevista mayo, empieza junio = 60 días).

**Qué cuenta abre:** TODA cuenta Tier-1 con voice agents legacy. BBVA, Iberdrola, Naturgy comercializadora, MAPFRE, SEUR, Telefónica.

**Qué decir al sponsor:**
> *"Estáis a 75 días del enforcement Art. 50. Si vuestros agents actuales (Genesys / Avaya / NICE / Atento BPO) no hacen disclosure automático en cada interacción, estáis en riesgo de €15M de multa. HR cumple nativamente; AI Auditor genera el log de conformidad. ¿Cuándo podemos hacer el assessment?"*

**Trigger conversacional Lola:** *"75 días para evitar multa €15M"*. Convierte la conversación de *"queréis comprar AI?"* a *"tenéis 75 días para evitar la multa"*.

### 5.2 DORA — Digital Operational Resilience Act (banca/seguros)

**Qué es:** Aplicación desde **17 ene 2025**. Aplica a 20 tipos de financial entities + ICT third-party providers. Critical Third-Party Providers (CTPPs) bajo oversight EBA/EIOPA/ESMA [A: DORA-EIOPA].

**Por qué urge ahora:** BBVA, Santander, CaixaBank, MAPFRE, Mutua, Línea Directa están obligados a hacer **third-party criticality assessment** de cada vendor AI desde hace meses. Compliance officers están sufriendo con los contratos OpenAI/Azure (CLOUD Act risk).

**Qué cuenta abre:** BBVA, Santander, MAPFRE, Mutua, Línea Directa, CaixaBank.

**Qué decir al sponsor:**
> *"Vuestros compliance officers están sufriendo con vuestro contrato OpenAI/Azure. Nosotros somos EU AI Act-native + DORA-friendly desde día 1. Deployment hybrid (cloud + on-prem opcional), BCP/DR documentado, SLA con penalties. Os ayudo a hacer la transición de use cases críticos a HR sin cambiar el resto."*

**Diferenciación vs Palantir/Sierra/Decagon:** Esos son US-headquartered con menor footprint EU compliance. HR es **EU AI Act-native + EU data residency option + founders españoles** = sovereign-friendly stack sin el baggage Karp/Thiel.

### 5.3 AESIA — Agencia Española de Supervisión de IA

**Qué es:** España es **primer país EU con agencia de supervisión AI dedicada**. AESIA tiene sede en A Coruña. Publicó 16 guías técnicas (2026) cubriendo conformity assessment, quality management, risk management, human oversight, data governance, transparency.

**Por qué urge ahora:** AESIA es el regulador. Vender enterprise sin entender AESIA = amateur. Las guías 2026 establecen el marco que las empresas Tier-1 españolas tendrán que cumplir en 2026-2027.

**Qué cuenta abre:** **Toda cuenta enterprise ES**. Es palanca transversal.

**Qué decir al sponsor (loss leader):**
> *"Te ofrezco gratis un AESIA-readiness audit — output 1 página resumiendo vuestro gap vs las 16 guías AESIA. Coste cero. Output útil para tu CIO/Compliance independientemente de si comprais HR."*

Esto es **loss leader Palantir-style**. Output: lead qualification + trust building + Lola se convierte en interlocutor regulatorio.

### 5.4 GDPR / LOPDGDD + AEPD — voz como dato personal

**Qué es:** Una grabación de voz es **dato personal especial** bajo LOPDGDD + GDPR. Implica:
- Consentimiento informado para grabación (Art. 5 LOPDGDD + Art. 6 GDPR).
- Disclosure de uso de AI durante conversación (Art. 50 EU AI Act → obligatorio desde 2 ago 2026).
- Data retention policy explícita.
- Derecho de acceso, rectificación, supresión, portabilidad.
- DPIA (Data Protection Impact Assessment) si hay procesamiento masivo.
- **AEPD publicó guía específica de AI agéntica feb 2026** [A: AEPD-AGENTIC].

**Palanca de venta:**
- HR ya tiene DPA estándar EU-compliant.
- HR ofrece **EU data residency** (Madrid / Frankfurt / Dublin).
- HR ofrece **AI Auditor** que mapea automáticamente al cumplimiento AEPD + guía agéntica.
- Competidores US-only (Bland AI, Vapi, Retell, Synthflow) NO tienen esto.

**Frase de venta:**
> *"Cuando os audite la AEPD (y os auditará, está en el plan 2026-2027), nuestro AI Auditor exporta el informe en el formato que AEPD pide. Lo único que tenéis que hacer es subirlo al portal."*

### 5.5 Sector público España — Ley 9/2017 Contratos del Sector Público

**Qué es:**
- **Procedimiento abierto** (default): mínimo 35 días desde publicación a presentación ofertas.
- **Procedimiento abierto simplificado**: mínimo 15 días.
- **Procedimiento negociado sin publicidad** (lo que usó Defensa con Palantir): solo casos específicos.
- **Acuerdos marco**: duración máx 4 años.
- **Procurement típico end-to-end: 6-12 meses.**

**Implicación para Lola:**
- **Sector público NO es el motor inicial.** Año 1 = enterprise privado.
- Reservar AENA, Renfe, Adif, sanidad pública para año 2+.
- **Una excepción posible:** Ayuntamiento Madrid / Comunidad Madrid si hay sponsor político alineado con HR (Aquilino Peña / Kibo Ventures tiene presencia ecosistema Madrid).

**Evitar trampa Palantir-like:** No perseguir contratos de Defensa, CIFAS, ni licitaciones grandes. Palantir las tiene cerradas + son políticamente tóxicas en EU (Sumar denunció en Cortes feb 2026).

### 5.6 Sovereign AI + EU data residency — palanca vs Palantir / Sierra / Decagon

**Hecho:** Palantir es US-headquartered (NSA/CIA history). Sierra (Bret Taylor, US). Decagon (US). En Alemania, la Bundeswehr rechazó Palantir por soberanía. En Francia, Macron empuja soberanía digital. **En España todavía no hay discurso fuerte, pero llegará 2026-2027.**

**Diferenciación HR:**
- HR es US-headquartered también — pero con **founders españoles** + **EU data residency option** + **Madrid hub** + **EU AI Act native**.
- **Narrativa única:** *"tech europea con velocidad US, sin baggage geopolítico Karp/Thiel."*

**Lola debe poder articular esto en 30 segundos:**
> *"Soy consciente de que Palantir está en España. Pero Palantir España es government-led, Gotham para Defensa. HR es enterprise privado, voice infrastructure, fundadores españoles, EU AI Act nativo, sin contratos opacos. Es una propuesta diferente a un comprador diferente."*

---

## EJE 6: Primeros 30 días deal-desk (semana a semana)

> Esto NO duplica [primeros-90-dias.md](primeros-90-dias.md) (estratégico, foundations). Esto es **el calendario tactical deal-by-deal de las primeras 4 semanas como GM España**.

### Lunes Semana 1 (Día 1)

**Mañana:**
- 9:00 — Reunión Mia (Londres) o Pablo/Javier (SF, Zoom). Confirmar prioridades top 3.
- 10:00 — Acceso a CRM HR + listado cuentas EMEA con tags España.
- 11:00 — Lectura deck de cuenta Naturgy, CMA CGM Iberia, Job&Talent, DHL ES. Notas a mano de blockers actuales.

**Tarde:**
- 14:00 — 30 min con el AE/Echo EMEA que gestione actualmente España (probable: alguien de UK). Handover formal.
- 15:00 — Mapping personal de Rolodex: lista 30 contactos logística + 30 enterprise diversos (banca, utility, retail, insurance). Tag por warmth.
- 17:00 — **Email a los 12 más warm**: *"soy nueva, café 30 min próxima semana?"*

**Día 1 entregable:** Lista 30 contactos + 12 mails enviados + brief 2 páginas de gaps que necesita cubrir.

**Las 5 primeras llamadas (día 1-3):**
1. Mia — handover EMEA + prioridades top 3.
2. CDO Naturgy — discovery only, no pitch.
3. CEO Juan Urdiales Job&Talent — *"qué funciona, qué mejorarías"*.
4. Aquilino Peña (Kibo) — 5 warm intros enterprise.
5. CIO DHL Iberia — co-marketing apetito.

**Los 3 primeros emails (día 1):**
1. Head of AI BBVA + Director Recuperaciones — subject *"Voice AI for collections — DORA-compliant from a Series B founded by Spaniards"*.
2. Director EV Charging Iberdrola — ángulo *"ex-Uber lideré EV 5%→30%"*.
3. CEO SEUR — ángulo *"DHL playbook applied to SEUR"*.

### Semana 1 — días 2-5

**Día 2:**
- Reunión CIO/CDO Naturgy. 30 min. Discovery only.
- Lectura completa case study Job&Talent.

**Día 3:**
- Call CEO Juan Urdiales Job&Talent (warm intro vía Mia). 20 min.
- Outbound mail CEO SEUR.

**Día 4:**
- Visita oficina HR Chamberí. Reunión Aquilino Peña (Kibo Ventures, co-organizador hackathon dic 2025). 30 min. Pedir 5 warm intros enterprise.
- Outbound mail Director EV Charging Iberdrola.

**Día 5:**
- Document brief cuenta Naturgy (1 página, propio). Expansion path documentado.
- **Friday wrap: send Mia weekly report. Format: 3 movements done, 3 next week, 1 blocker.**

### Semana 2 — 5 cosas concretas

**Lunes:**
- Coordinar con global AM DHL para pedir 30 min con CIO DHL Iberia.
- Outbound Head of AI BBVA.

**Martes-Miércoles:**
- **Visita física Algeciras (puerto) — 2 días.** Sentarse con ops floor CMA CGM + CEVA. Output: 5 workflows mapeados, 1 elegido, brief 1 página.

**Jueves:**
- Reunión 45 min Head of Operations CMA CGM Iberia. Llevar brief Algeciras.
- Reunión 30 min CTO Job&Talent (follow-up CEO call).

**Viernes:**
- Reunión 30 min CIO DHL Iberia. Pedir co-marketing SIL Barcelona.
- Friday wrap a Mia.

**Entregable semana 2:** Algeciras brief + 4 reuniones C-level completadas + 2 outbounds nuevos enviados.

### Semana 3 — primeros deals movidos

**Lunes:**
- Outbound CDO Repsol.
- Outbound Director AI Center MAPFRE.

**Martes:**
- Reunión Head of AI BBVA (asumiendo respuesta semana 2). **Lola lleva FDE técnico al call — NO va sola.** Esto es Echo + Delta pair en acción. Crítico para Mia.

**Miércoles-Jueves:**
- **Embedding 2 días Nedgia/Naturgy ops floor** — appointment scheduling team. Output: brief expansion Naturgy comercializadora + retention voice.

**Viernes:**
- **Pitch breakfast 8-10 prospects ETT + retail Madrid** (co-hosted con Job&Talent). Coste €5-8K.
- Friday wrap a Mia.

**Entregable semana 3:** 3 nuevas C-level meetings + Naturgy expansion brief + 1 evento ejecutado + pilot collections BBVA en discussion.

### Semana 4 — consolidación + entregable final

**Lunes:**
- Reunión CDO Repsol (si respondió). Llevar mockup driver coordination fleet.
- Outbound CEO SEUR (follow-up si no respondió + warm intro vía CEL).

**Martes:**
- Reunión Director EV Charging Iberdrola.
- Reunión Director AI Center MAPFRE.

**Miércoles — día interno:**
- Documentar **"Deal Desk Spain — Top 12 accounts brief"**. 12 páginas, 1 por cuenta. Format Palantir-style:
  - Champion identificado (rol)
  - Use case priorizado
  - Blocker actual
  - Palanca de unblock
  - Next move concreto + fecha
  - Pilot-to-prod target
  - Expansion path 18 meses (€)

**Jueves:**
- **Entregar el brief a Mia. Reunión 60 min — walkthrough cuenta por cuenta.** Mia tiene 12 dial-ups de cada cuenta. Esto le da control y le señala a Lola como **builder, no como talker**.

**Viernes:**
- Friday wrap mes 1 a Mia + Pablo/Javier.
- Plan mes 2 (high-level).

### KPI Tactical 30 días — NO revenue, sí motion

Métricas concretas reportables a Mia día 30:

| Métrica | Target | Cómo medir |
|---|---|---|
| **C-level meetings completadas** | 12+ | CRM log |
| **Cuentas existentes EMEA con expansion plan documentado** | 4/4 (Naturgy, CMA CGM, DHL, J&T) | Brief 1 página por cuenta |
| **Nuevos prospects Tier-1 ES con sponsor identificado** | 5+ (BBVA, Iberdrola, Repsol, MAPFRE, SEUR) | CRM + brief |
| **Pilots scoped (con KPI binario)** | 2+ | Documento firmado por sponsor |
| **Unblocks ejecutados en cuentas existentes** | 3+ | Lista blockers resueltos (security review iniciada, procurement contactado, IBM integrator framing Naturgy, etc.) |
| **Sector network activated** | CEL + Ametic membership iniciada, SIL speaker confirmado | Logística + tech |
| **PR / media** | 1 pieza firmada para Q3 2026 (Expansión / Cinco Días, "voice AI + DORA") | Editor commit |
| **Hire pipeline** | 5+ candidatos para Enterprise AE / FDE | Ashby |
| **Case study Naturgy expansion en draft** | 1 | Internal doc |

**Nota crítica:** estos KPI son **motion metrics**, no outcome metrics. Mia, como ex-Deal Team Palantir, valora motion como leading indicator. **A partir de mes 3, KPI vira a outcome (pilots-in-prod, ARR).**

---

## Anclaje a fortalezas de Lola — qué palancas únicas usar

> Lola NO es FDE técnica, NO es enterprise SaaS veterana, NO viene de logistics. Mia lo sabe. La jugada es enmarcar lo que SÍ tiene Lola como ventaja única, no fingir lo que no tiene.

### Network ICADE/LBS — intros warm específicas

**ICADE (Derecho+ADE):**
- **Banca**: ICADE es semillero histórico BBVA, Santander, CaixaBank. Lola tiene 10-15 contactos directos C-level reachables en 1 llamada.
- **Energía**: Iberdrola, Repsol tienen exalumnos ICADE en organigrama.
- **Big4**: KPMG (donde Lola empezó) + BCG + Deloitte tienen exalumnos en cliente Tier-1. Útil como segundos saltos.

**LBS (MBA):**
- **Londres senior network**: cruce natural con Mia (16 años Londres). LBS career services / LinkedIn alumni search es low-cost.
- **C-level multinacionales ES**: Telefónica, Iberdrola, BBVA tienen MBAs LBS visibles.

**Movimiento concreto semana 1:** Lola identifica 15 warm intros (5 ICADE banca, 5 ICADE energía, 5 LBS multinacionales) y activa 8 con un "café 30 min próxima semana".

### Experiencia regulatoria — Derecho+ADE + Uber regulado

**Lola habla el idioma legal/compliance que un AE genérico NO.**

- 7+ años Uber lidiando con regulación local española multi-ciudad (BOE, ordenanzas municipales, tribunales).
- **Influenció legislación en 3+ regiones**.
- Doble grado Derecho+ADE en ICADE — credibilidad jurídica nativa.

**Cómo usarlo:** Cuando Lola se sienta con el CISO BBVA, Compliance MAPFRE, DPO Iberdrola, **NO habla como vendedora — habla como peer regulatorio**. Esto desactiva un blocker que un AE generic tarda 3 meses en desactivar.

**Frase concreta:** *"Soy abogada de formación. Vuestra DPO y yo hablamos el mismo idioma. ¿La invitamos a la próxima sesión?"*

### Media presence Uber — 30+ apariciones tier-1

**Lola sabe colocar historias en prensa española tier-1.** Útil para:
- **DHL ES case study Q3 2026** en Cadena de Suministro + Cinco Días + El Economista.
- **POV thought leadership** sobre AI ops España (Expansión, Cinco Días, El Confidencial).
- **PR personal** que convierte a Lola en interlocutor que el CAIO de BBVA quiera conocer.

**Pieza concreta semana 4:** Lola pitchea a Expansión o Cinco Días una pieza "Voice AI + DORA — los compliance officers que están sufriendo". Editor commit antes de mes 1.

### Scale ops Uber 7→19 ciudades — credibilidad multi-region

**Mia vendrá probablemente con sesgo "Country Manager Uber Mobility ≠ Enterprise SaaS B2B".** Lola debe reframear:

- *"Lideré 12 lanzamientos de ciudad, cada uno con su propio regulador local, fleet partners, customer ops setup. Es exactamente la disciplina multi-account que necesito ahora — pero aplicada a 6-10 cuentas enterprise Tier-1 en vez de a 19 ciudades."*

**Esto convierte el "gap" en credencial.**

### Idiomas — ES, CAT, EN bilingüe, FR avanzado, DE intermedio

- **CMA CGM (FR-headquartered)**: Lola puede hacer las primeras llamadas en francés.
- **MAPFRE LATAM**: ES nativo + PT cercano cubre México, Brasil.
- **Sucursales EU clientes ES**: DE intermedio útil con MAPFRE Alemania, Iberdrola Alemania, Naturgy Latam.

**Esto es ventaja real vs FDE/Echo importado de US o UK.**

### Honestidad sobre gaps — outsider que aprende rápido

**NO pretender:**
- "Tengo background enterprise SaaS B2B" — Lola NO lo tiene.
- "Conozco profundamente logistics" — Lola NO lo conoce (Uber Mobility ≠ logistics).
- "Soy FDE técnica" — Lola NO lo es.

**SÍ articular (frase Lola a Mia):**
> *"Mi background es B2C marketplace + retail multi-vertical Amazon, no enterprise SaaS B2B puro. Eso es un gap real. Lo compenso con tres cosas: (1) ground truth español que tu equipo EMEA no tiene; (2) network ICADE/LBS warm intros que aceleran 6 meses el outreach; (3) experiencia regulatoria que desactiva blockers compliance que un AE tarda meses en navegar. Hire me y en 90 días te tengo 4 cuentas existentes con expansion plan + 6 prospects Tier-1 con sponsor + 2 pilots scoped. No voy a fingir que soy una FDE; voy a ser el Echo que orquesta los FDEs."*

**Esto es Palantir-aligned**: honestidad sobre lo que sabes y lo que no + plan operativo concreto.

---

## Vocabulario / frases para usar con Mia

> Mia es ex-Deal Team Palantir OCEO + 10 años FX sales institucional Londres. Lenguaje deal-desk + sales senior + nórdico-londinense direct. NO consulting-speak, NO transformation talk, NO oversell.

### Usar (deal-desk language)

- *"Wedge use case, not full AI strategy"* (vs horizontal)
- *"Operational ops, not foundation models"* (frente a OpenAI/MSFT/AWS)
- *"EU AI Act native"*
- *"Sovereign-friendly stack"*
- *"Expansion path $30K → $300K → $3M"* (Pascal Unger / FDE model — frase canónica HR/Palantir)
- *"Land in the workflow, expand into the org"*
- *"Account-based, no funnel"*
- **TCV (Total Contract Value)** vs ACV (Annual Contract Value)
- **NRR (Net Revenue Retention)** — Mia conoce el 134% Palantir
- **Pilot-to-prod conversion rate %**
- **Time-to-first-AI-Worker-in-production** (litmus test Mabrey)
- **Bootcamp** (1-5 días con data real cliente, cliente paga)
- **Echo (Deployment Strategist) + Delta (FDE) pair** — si Mia lo trae primero
- **Land-and-expand**
- **Few accounts, deep expansion** (frase canónica Palantir)
- **Sponsor / champion / economic buyer / decision committee** — vocabulario MEDDIC/MEDDPICC
- **Pricing levers**: implementation fee + ARR + usage-based on top
- **Operational impact / measurable business value** (lenguaje literal Mia)
- **Workflow** (no "use case" abstracto)
- **Ontology / operational ontology** — si Mia lo trae primero
- **Production within 4 weeks** (litmus Mabrey)
- **Critical Third-Party Provider (CTPP)** — DORA specifically

### Evitar

- "Digital transformation"
- "Synergies"
- "Best practices"
- "Awareness campaigns"
- "Brand building"
- "AI pilot" como objetivo final (queremos producción)
- "Sales pipeline" abstracto sin nombres de cuenta
- "Channel partners / reseller strategy" en exceso
- "Demand generation"
- "Holistic approach"
- "Customer journey"
- "Ecosystem play"
- "Industry-leading platform"
- "Deploying AI" (sin más) — Mia opone explícitamente a "rethinking how work gets done"

### Frases que sellan credibilidad deal-desk

- *"I won't sign a pilot without a binary KPI documented and a procurement contact identified day-1."*
- *"Every pilot has to leave behind 3-5 artifacts the customer can't throw away — ontology, runbook, integrations, dashboard, trained flows. That's what makes it irreversible."*
- *"Echo + Delta day-1 at the customer. The AE comes when 3 accounts are live."*
- *"I'm targeting 85% pilot-to-production conversion in year 1 — better no pilot than a failed pilot."*
- *"DORA + Art. 50 + AESIA is my sales trigger sequence for banking/insurance. Aug 2026 is 75 days from contract close."*
- *"Naturgy is my fastest NRR play. The motion is validated through Nedgia. I'm not discovering — I'm orchestrating."*
- *"CMA CGM: I don't compete with Mistral. I sell voice infrastructure Mistral doesn't do."*

---

## Riesgos / supuestos a validar pre-entrevista

### Supuestos críticos del playbook

1. **Naturgy + HappyRobot integración está activa** (basado en blink.new simulator + Nedgia/IBM partnership). Lola debe confirmar con Mia o equipo HR la profundidad real.
2. **DHL ES tiene operación local con CIO local accesible**. Plausible dado tamaño DHL Express Spain (~€800M). Confirmar.
3. **CMA CGM-Mistral partnership es exclusiva ONLY para foundation models, no voice infra**. Plausible (anuncio enfatiza shipping logistics workflows generative AI). Confirmar leyendo press release completo.
4. **Job&Talent + HR relación tiene CEO-founder warmth**. Plausible dado case study publicado abiertamente. Mia probablemente tiene contacto.
5. **BBVA roadmap "The Eight" no incluye voice AI collections**. Basado en descripción pública. Validar.
6. **Iberdrola AWS partnership es ONLY para IT internal**. Confirmado parcialmente (AWS blog enfatiza ServiceNow). Podría haber voice customer service interno.
7. **OpenAI/Santander/BBVA deals NO cubren voice ops**. Hipótesis razonable (deals son foundation models + ChatGPT Enterprise). Podrían expandirse.
8. **Telefónica Tech está abierta a partnership voice infra**. Hipótesis no validada. Mes 2-3.

### Lo que Lola debería validar pre-entrevista o early-stage

1. **¿Mia ya tiene asignados AEs/Echos a Naturgy, CMA CGM, J&T, DHL ES?** ¿Cuál es el split de responsabilidad esperada Lola vs Mia?
2. **Pedir a Mia el playbook actual EMEA** — pricing, deal structure, ACV averages, ramp times. Sin esto, Lola está inventando.
3. **Confirmar autonomía pricing España** (% descuento sin escalation, ACV mínimo, ACV óptimo). Ver [pricing-happyrobot.md](pricing-happyrobot.md).
4. **Confirmar disponibilidad FDE pool EMEA**. Sin FDE, pilots no se ejecutan. Si la respuesta es "tenemos 2 FDEs EMEA full-time", Lola diseña diferente.

### Riesgos del playbook

1. **Sobrecarga mes 1**: 12+ C-level meetings + 4 expansion plans + 5 outbounds + visit Algeciras + embedding Nedgia + brief 12 cuentas = brutal. **Mitigación:** definir cuáles 2-3 cuentas son "yo personal" y cuáles "AE futuro" desde día 1.
2. **Caer en demo theatre vs deal motion.** Tentación de hacer 15 demos en mes 1 = anti-Palantir. **Mitigación:** disciplina ICP, max 6 cuentas profundas.
3. **Confundir "Mia ya tiene la cuenta" con "Lola no toca"**. Si Naturgy/DHL están bajo Mia/EMEA team, Lola debe orquestar handoff explícito, no asumir.
4. **Underestimating procurement España.** Banca + utility + insurance procurement ES es 3-6 meses post-pilot. Plan financial accordingly.
5. **OpenAI/Microsoft footprint en cuentas españolas es MAYOR de lo que parece desde fuera.** BBVA + Santander + Telefónica + Iberdrola ya son OpenAI/Azure-heavy. HR debe vender complementariedad, no reemplazo.

---

## Conexiones

- [Mia Bjorkenstam](../personas/mia-bjorkenstam.md) — perfil entrevistadora + lente evaluación
- [Lola Vilas](../personas/lola-vilas.md) — candidata, fortalezas y gaps
- [Palantir como North Star](../empresa/palantir-northstar.md) — modelo estructural HR replica
- [Pricing HappyRobot](pricing-happyrobot.md) — bandas pricing por segment / use case
- [Preguntas Mia](preguntas-mia.md) — Q&A directas con Mia
- [Primeros 90 días](primeros-90-dias.md) — plan estratégico (este doc es complementario tactical)
- [Expansión España](../empresa/expansion-espana.md) — contexto del rol GM
- [DHL Supply Chain](../clientes/dhl.md) — cliente EMEA heredado
- [Job&Talent](../clientes/job-and-talent.md) — cliente EMEA heredado ES
- [EU AI Act](../regulacion/eu-ai-act.md) — Art. 50 enforcement Aug 2026
- [GDPR / LOPDGDD](../regulacion/gdpr-lopdgdd.md) — voz como dato personal
- [Oportunidades regulatorias España 2026](../regulacion/oportunidades-regulatorias-espana-2026.md) — AESIA + DORA + sectoriales
- [Fit candidata](fit-candidata.md) — mapeo Lola ↔ HR
- [Preguntas GTM](preguntas-gtm.md) — Q&A categoría GTM

---

## Fuentes

| ID | URL | Tipo | Acceso | Conf |
|---|---|---|---|---|
| HR-MIA | happyrobot.ai/blog/welcoming-mia-bjorkenstam | Oficial HR | 2026-05-21 | A |
| GNW-MIA | globenewswire.com/2026/02/18/HappyRobot-EMEA-Mia | Press release | 2026-05-21 | A |
| HR-JT | happyrobot.ai/blog/job-talent | Blog oficial | 2026-05-21 | B |
| HR-DHL | group.dhl.com/2025/dhl-happyrobot-press | Press release oficial | 2026-05-21 | A |
| HR-BLOG-FIN | happyrobot.ai/blog/finance-automation | Blog oficial | 2026-05-21 | B |
| HR-SERIEB | globenewswire.com/HR-series-B | Press release | 2026-05-21 | A |
| BBVA-OAI | openai.com/index/bbva-collaboration-expansion | Press release | 2026-05-21 | A |
| BBVA-EIGHT | bbva.com/innovation/the-eight-strategy-ai | Comunicación corporativa | 2026-05-21 | A |
| BBVA-DEPLOYCO | bbva.com/innovation/deployco-openai | Comunicación corporativa | 2026-05-21 | A |
| IBE-AWS | aws.amazon.com/blogs/iberdrola-bedrock-agentcore | Blog técnico AWS | 2026-05-21 | A |
| IBE-AI-CENTRE | iberdrola.com/innovation/centre-excellence-ai | Comunicación corporativa | 2026-05-21 | A |
| TEF-MSFT-KERNEL | telefonica.com/microsoft-kernel-genai | Press release | 2026-05-21 | A |
| TEF-GENAI | telefonicatech.com/genai-platform | Comunicación corporativa | 2026-05-21 | A |
| INDITEX-QUIET-AI | smdailypress.com/zara-quiet-ai-revolution-2026 | Prensa | 2026-05-21 | B |
| NATURGY-NEDGIA-IBM | newsroom.ibm.com/2025-07-14-nedgia-virtual-ai-agent | Press release | 2026-05-21 | A |
| NATURGY-AI-PLATFORM | en.ara.cat/naturgy-ai-native-digital-platform | Prensa | 2026-05-21 | B |
| NATURGY-HR-BLINK | blink.new/p/naturgy-one-shot-simulator | Plataforma | 2026-05-21 | B |
| CMACGM-MISTRAL | smartmaritimenetwork.com/2025/04/08/cma-cgm-mistral-ai-100m | Prensa sectorial | 2026-05-21 | A |
| CMACGM-AI | dcvelocity.com/cma-cgm-bespoke-ai-110m | Prensa sectorial | 2026-05-21 | A |
| REPSOL-AI | cio.com/repsol-digitalization-ai | Prensa tech | 2026-05-21 | A |
| REPSOL-RAIP | repsol.com/innovation/digitalization/raip | Comunicación corporativa | 2026-05-21 | A |
| MAPFRE-AI-MANIFESTO | insurance-edge.net/2025/05/08/mapfre-ai-manifesto | Prensa sectorial | 2026-05-21 | A |
| MAPFRE-AI | mapfre.com/insights/innovation/ai-digitalization | Comunicación corporativa | 2026-05-21 | A |
| MUTUA-GCP | cloud.google.com/customers/mutua-madrilena | Case study Google | 2026-05-21 | A |
| SANT-OAI | santander.com/stories/santander-data-ai-first-openai | Comunicación corporativa | 2026-05-21 | A |
| CAIXA-AGENTFORCE | caixabank.com/headlines/caixabank-ai-agent | Comunicación corporativa | 2026-05-21 | A |
| MERCADONA-GCP | cloud.google.com/customers/mercadona | Case study Google | 2026-05-21 | B |
| JT-OVERVIEW | linkedin.com/company/jobandtalent | Comunicación corporativa | 2026-05-21 | B |
| DORA-EIOPA | eiopa.europa.eu/digital-operational-resilience-act-dora | Regulación oficial | 2026-05-21 | A |
| EUAIACT-ART50 | artificialintelligenceact.eu/article/50 | Regulación oficial | 2026-05-21 | A |
| AEPD-AGENTIC | aepd.es/guia-agentic-ai | Regulación oficial ES | 2026-05-21 | A |
| AESIA-GUIDES | (referenciado pearlcohen) | Regulación oficial ES | 2026-05-21 | B |
| LEY9-2017 | boe.es/buscar/pdf/2017/BOE-A-2017-12902-consolidado.pdf | Regulación oficial ES | 2026-05-21 | A |
| AUNOA-LOG | aunoa.ai/case-studies | Plataforma | 2026-05-21 | B |

### Nota sobre confianza y interpretación

- **A**: fuentes primarias oficiales (press releases corporativos, blogs oficiales, regulación EU/ES).
- **B**: análisis terceros razonables, prensa sectorial firmada, plataformas con datos contrastables.
- **C**: hipótesis no validadas, estimaciones propias (flagged explícitamente con `[C]` en el texto).

**Marca clara dato vs interpretación:** todas las secciones "Movimiento Lola — semana X" + "KPI 18 meses + ACV target" + bandas pricing son **interpretación tactical propia** derivada del playbook Palantir + market intelligence ES. **NO son directiva de HR.** Lola debe validar con Mia antes de ejecutar.

---

*Documento operativo complementario a [primeros-90-dias.md](primeros-90-dias.md) (estratégico), [preguntas-mia.md](preguntas-mia.md) (Q&A entrevista) y [pricing-happyrobot.md](pricing-happyrobot.md) (bandas). Usar para preparar respuestas a Mia tipo "what would you do tomorrow on account X?".*
