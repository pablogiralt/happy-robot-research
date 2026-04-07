---
title: "Mercado AI Healthcare"
type: mercado
status: completo
tags: [healthcare, ai, mercado, voice-ai, agentic-ai, regulacion, enterprise]
updated: 2026-04-07
---

# Mercado AI Healthcare

## Overview ejecutivo

El mercado de inteligencia artificial en healthcare ha superado el punto de no retorno: en 2026 ya no es un experimento, es infraestructura. Con una valoración de ~$40-56B en 2025 y proyecciones que superan los $600B en 2034 a un CAGR del 37-44%, el sector es uno de los de mayor crecimiento en todo el ecosistema AI. Los casos de uso están madurando rápidamente: la documentación clínica ambient ya es un mercado de $600M que crece a 2.4x anual, el revenue cycle management con AI ha sido adoptado por el 46% de los hospitales en EE.UU., y los AI agents para patient engagement están ganando adopción masiva. El software "agentic" —capaz de tomar acciones autónomas sobre sistemas EHR, scheduling y billing— es la frontera activa de 2026. Las barreras regulatorias son reales (HIPAA en EE.UU., EU AI Act + MDR en Europa) pero actúan como moat para los actores bien posicionados. Para HappyRobot, cuya plataforma de AI Workers ya maneja workflows complejos en logistics, healthcare representa una expansión natural: misma arquitectura (voz, integración nativa, agentic reasoning, governance), diferente vertical.

---

## 1. Tamaño de mercado

### Global — AI en Healthcare

| Métrica | Valor | Conf | Fuente |
|---------|-------|------|--------|
| TAM Global AI Healthcare 2025 | $36.67B – $56.01B | B | [GVR-2025] [FBI-2025] [PREC-2025] — rango entre analistas |
| TAM Global AI Healthcare 2026 | $51.20B – $56.01B | B | [PREC-2025] [FBI-2025] |
| Proyección 2030 | $110.6B | B | [MM-2030] MarketsandMarkets |
| Proyección 2033 | $505.6B | C | [GVR-2033] — estimación a largo plazo, alta incertidumbre |
| Proyección 2034 | $613.8B – $1,033B | C | [PREC-2034] [FMI-2034] — rango muy amplio entre analistas |
| Proyección 2035 | $1,222B | C | [GN-2035] GlobeNewswire — estimación más agresiva |
| CAGR 2025–2034 | 36.83% – 43.96% | B | [PREC-2025] [FMI-2025] |
| Share regional: Norteamérica | >45% del mercado global | B | [PREC-2025] |
| Share regional: Asia-Pacífico | Crecimiento más rápido por CAGR | B | [PREC-2025] |

> **Nota metodológica:** Las estimaciones de TAM varían enormemente entre analistas (rango 2x-3x en el mismo año) por diferencias en qué se incluye (solo software vs. plataformas + servicios + devices, etc.). Los datos de 2025 son los más consistentes; las proyecciones a 2033-2035 tienen alta incertidumbre.

### Europa — AI en Healthcare

| Métrica | Valor | Conf | Fuente |
|---------|-------|------|--------|
| Mercado Europa AI Healthcare 2024 | $7.92B | B | [MDF-2024] MarketDataForecast |
| Mercado Europa AI Healthcare 2025 | $10.93B | B | [MDF-2025] |
| Proyección Europa 2033 | $143.02B | C | [MDF-2033] |
| CAGR Europa 2025–2033 | 37.91% | B | [MDF-2025] |
| Share Europa en mercado global (otra estimación) | $23.6B con CAGR 44.11% | C | [SR-EUR] StraitsResearch — estimación alternativa |
| Tecnología de mayor crecimiento en Europa | NLP (CAGR 50.3%) | B | [MDF-2025] — impulsado por asistentes virtuales y documentación clínica |
| Segmento servicios en Europa | CAGR 45.2% | B | [MDF-2025] — consultoría, implementación, mantenimiento |
| País líder en Europa | Alemania | B | [MDF-2025] — mayor inversión en infraestructura digital de salud |

### España — AI en Healthcare

| Métrica | Valor | Conf | Fuente |
|---------|-------|------|--------|
| Mercado AI Healthcare España 2025 | ~$84M | C | [NC-ESP] — estimación de fuente única, sin contrastar |
| Clínicos usando AI en España | 11% | C | [NC-ESP] — dato no verificado en fuente primaria |
| Clínicos planeando adoptar AI | 42% | C | [NC-ESP] |
| Startups activas en salud+AI en España | 127+ | B | [ASEBIO-2025] AseBio |
| Impacto económico AI en industria española 2025 | €16.5B en PIB estimado | B | [BDE-2025] Banco de España |
| Impacto potencial AI en economía española 2030 | €55B adicionales | C | [BDE-2025] |
| Financiación pública AI en salud (2021–2023) | EUR 600M | B | [EC-ESP] Comisión Europea / España |

---

## 2. Casos de uso principales

| Caso de uso | Descripción | ROI / Impacto documentado | Players líderes | Madurez |
|-------------|-------------|--------------------------|-----------------|---------|
| **Ambient clinical documentation** | AI escucha conversación médico-paciente y genera notas clínicas automáticamente | 16,000 horas ahorradas en 15 meses (sistema CA); 90% de clínicos dan atención sin distracciones (U. Chicago Medicine) | Abridge, Nuance DAX, Ambience, Suki, Nabla | Alta — ya $600M de mercado |
| **Prior authorization automation** | Automatiza solicitudes de autorización previa a aseguradoras (días → minutos) | Reducción de demoras en tratamientos; días → minutos | Cohere Health, Rhyme, Olive AI, grandes EHR | Media-alta |
| **Revenue cycle management (RCM)** | Automatiza codificación, seguimiento de reclamaciones, gestión de impagos | Auburn Community Hospital: -50% discharged-not-final-billed, +40% productividad codificadores | Commure, Waystar, Optum, R1 RCM | Alta — 46% hospitales EE.UU. |
| **Patient scheduling & access** | AI voice/chat para agendar, confirmar, reprogramar citas 24/7 | Houston Methodist: proyección 25-50% reducción de costes administrativos | Hippocratic AI, Prosper AI, Infinx, Amazon HealthScribe | Media-alta — crecimiento 4x desde Q2 2025 |
| **Patient engagement post-alta** | Llamadas AI para seguimiento post-alta, educación, recordatorios de medicación | Reducción de readmisiones ($8k-$12k por readmisión evitada) | Hippocratic AI (115M interacciones), Memora Health | Media |
| **Diagnóstico por imagen** | Deep learning para análisis de radiografías, escáneres, patología digital | 40% mejora en precisión diagnóstica (estimación general) | Google DeepMind (retina), Aidoc, Rad AI, Enlitic | Alta en imaging; regulatoriamente exigente |
| **Drug discovery** | AI para identificación y desarrollo de nuevos fármacos | Reducción de 10-15 años de ciclo de descubrimiento | Xaira Therapeutics ($1B), Isomorphic Labs ($600M), Insilico Medicine | Alta — mayores rondas de 2025 |
| **Clinical decision support** | AI que sugiere diagnósticos diferenciales o tratamientos en tiempo real | Override rate <2% en AI transparente vs. >73% en AI opaca (estudio 2025 Diagnostics) | OpenEvidence, Regard, Suki | Media — gobernanza compleja |
| **Triage & symptom checking** | Chatbots y voice agents para triaje inicial de pacientes | +20x crecimiento YoY en patient access tools | Babylon Health, K Health, Ada Health | Media |
| **Operaciones hospitalarias / OR scheduling** | Optimización de quirófanos, rotación de camas, staffing | West Tennessee Healthcare: mejora OR utilization con AI scheduling | Palantir, LeanTaaS, Qventus | Media |

---

## 3. Actores principales

### Startups — AI Healthcare (por segmento)

#### Documentación clínica / Ambient AI

| Company | HQ | Funding total | Valoración | Foco | Diferenciador |
|---------|-----|---------------|------------|------|---------------|
| **Abridge** | Pittsburgh, EE.UU. | $773M (Series E jun-2025) | $5.3B | Ambient scribe para sistemas de salud | Integración profunda con Epic; 150+ health systems |
| **Ambience Healthcare** | SF, EE.UU. | $320M (Series C jul-2025) | $1.25B | Ambient scribe multimodal | Inversores: a16z, Kleiner Perkins, OpenAI Fund |
| **Nuance DAX Copilot** | (Microsoft) | Adquisición $16B (2021) | — | Ambient scribe enterprise | Distribuido via Microsoft/Epic; 600+ orgs |
| **Suki AI** | Redwood City, EE.UU. | $165M (Series D oct-2024) | $500M | Voice AI para médicos | Integración nativa multi-EHR |
| **Nabla** | París, Francia | $120M (jun-2025) | N/D | Ambient AI para clínicos en Europa | Fuerte posición en mercado europeo; French-founded |

#### AI Agents para pacientes / Engagement

| Company | HQ | Funding total | Valoración | Foco | Diferenciador |
|---------|-----|---------------|------------|------|---------------|
| **Hippocratic AI** | Palo Alto, EE.UU. | $404M (Series C nov-2025) | $3.5B | AI agents para patient engagement clínico | 115M+ interacciones; 50+ health systems; 0 safety incidents |
| **Prosper AI** | EE.UU. | $5M (seed sep-2025) | N/D | Voice AI para scheduling y prior auth | Foco en el mercado de $450B de costes administrativos |

#### Drug discovery / Life Sciences AI

| Company | HQ | Funding | Foco |
|---------|-----|---------|------|
| **Xaira Therapeutics** | San Francisco | $1B Series A | AI platform para drug discovery |
| **Isomorphic Labs** | Londres (Google) | $600M | AI-driven drug discovery (AlphaFold) |
| **Insilico Medicine** | Hong Kong/NY | $100M Series E | Pharma R&D con generative AI |
| **Lila Sciences** | EE.UU. | $550M (2025, 3 rondas) | "Scientific superintelligence" |

### Corporates — Grandes plataformas

| Company | Producto AI healthcare | Posición | Dato clave |
|---------|------------------------|----------|------------|
| **Microsoft / Nuance** | DAX Copilot (ambient scribe), Azure OpenAI para salud | Líder en documentación clínica enterprise | 600+ organizaciones; partnership estratégico con Epic |
| **Epic Systems** | EHR con AI ambient scribe integrado | Plataforma dominante en EHR (>30% hospitales EE.UU.) | Ha lanzado su propio scribe; control del workflow |
| **Oracle Health** | AI-powered EHR con voice commands | Segundo mayor EHR tras Epic | Lanzó Oracle Clinical AI en 2025 |
| **Google / DeepMind** | Med-Gemini, imaging AI, AlphaFold | Fuerte en research clínico y life sciences | Med-Gemini aún no disponible públicamente |
| **Amazon** | Amazon HealthScribe, Amazon Comprehend Medical, agentic AI (mar-2026) | Servicios cloud y herramientas developer | Lanzó agentic AI para proveedores de salud en mar-2026 |
| **Salesforce** | Einstein AI en Health Cloud | CRM + patient engagement para payors | Integración nativa con datos de pacientes |
| **Palantir** | Ontology para hospitales (operaciones) | Fuerte en NHS UK y sistemas europeos | Contratos con NHS por $480M+ |

---

## 4. Tendencias 2025–2026

### 4.1 Ambient AI: de nicho a infraestructura

El ambient scribing es el primer breakout category de AI en healthcare. El mercado pasó de ~$250M en 2024 a $600M en 2025 (+2.4x YoY). Abridge y Ambience emergieron como unicornios, aunque ambas siguen por detrás de Nuance DAX en market share institucional [B: Menlo Ventures 2025]. En 2026, los grandes EHR (Epic, Oracle, athenahealth) han integrado sus propios ambient scribes, lo que amenaza a las startups independientes pero valida el mercado.

### 4.2 Agentic AI: el próximo salto (lento pero seguro)

El 69% de organizaciones de salud ya usa generative AI, pero solo el 22% usa AI agents [B: NVIDIA State of AI Healthcare 2026]. Los AI agents requieren acceso a sistemas core (EHR, scheduling, billing) y capacidad de actuar — no solo generar texto — lo que introduce mayor riesgo y exige gobernanza más robusta. Sin embargo, el 85% planea aumentar inversión en agentic AI en los próximos 2-3 años. Houston Methodist ya proyecta reducción de costes del 25-50% en funciones administrativas usando agentes autónomos.

### 4.3 Shift: de herramientas puntuales a arquitecturas modulares

McKinsey [B] identificó en 2025 el shift de "AI point solutions" a "modular AI architecture": los sistemas de salud quieren plataformas donde puedan desplegar múltiples agentes especializados con shared context, gobernanza centralizada y auditoría. Esto es exactamente lo que HappyRobot ofrece en logistics.

### 4.4 Multimodal AI en diagnóstico

Los modelos de 2026 combinan texto, imagen médica y señales vitales para alertas de deterioro temprano y soporte a decisiones de especialidad. Aún requieren supervisión clínica, pero los pilotos están mostrando resultados consistentes.

### 4.5 Revenue para AI en healthcare supera otras verticales

El funding de AI healthcare alcanzó $10.7B en 2025 (+24.4% sobre 2024) [A: Crunchbase]. Las empresas AI-enabled capturaron el 62% de los dólares de VC en digital health, con un ticket medio 83% superior al de las no-AI. Esto confirma que los inversores ven healthcare AI como la apuesta más segura del ecosistema.

### 4.6 Consolidación y amenaza de los EHR

Epic, Oracle y athenahealth están integrando ambient AI en su core. Esto crea "feature creep" que amenaza a startups del segmento, pero también valida que el workflow nativo de AI es inevitable. La oportunidad está en los casos de uso que los EHR no pueden cubrir: patient engagement multicanal, voice outbound, agentic operations.

### 4.7 España: adopción temprana pero regulación como acelerador

España tiene 127+ startups de AI en salud [B: AseBio] y €600M de financiación pública. El EU AI Act y el European Health Data Space (EHDS), previsto para 2026, crearán un marco regulatorio que paradójicamente acelerará la adopción al dar certeza jurídica a los compradores institucionales (hospitales públicos, aseguradoras).

---

## 5. Regulación y compliance

### 5.1 HIPAA (EE.UU.)

| Requisito | Descripción | Implicación para AI |
|-----------|-------------|---------------------|
| Cifrado PHI en reposo | AES-256 mínimo | Todos los modelos deben procesar datos cifrados o en entornos seguros |
| Cifrado PHI en tránsito | TLS 1.2+ | APIs de AI deben usar canales seguros |
| Control de acceso + MFA | RBAC + autenticación multifactor | Los AI agents no pueden acceder libremente a datos de pacientes |
| Audit logs | Registro completo de accesos a PHI | Trazabilidad de cada acción del agente |
| Business Associate Agreements (BAA) | Contrato con todo vendor que maneje PHI | Cualquier plataforma AI (incluido HappyRobot) debe firmar BAA |
| Incident response plan | Plan de respuesta a brechas | Obligatorio para cualquier sistema con acceso a datos clínicos |

> HappyRobot tiene certificación SOC 2 y cumplimiento HIPAA declarado en su web [B: HR-WEB]. Esto es tabla stakes para entrar al mercado sanitario americano.

### 5.2 EU AI Act aplicado a Healthcare

| Aspecto | Detalle | Fecha clave |
|---------|---------|-------------|
| Clasificación de riesgo | Los AI systems para diagnóstico o soporte clínico se clasifican como **High Risk** bajo Annex III | Agosto 2025 (en vigor) |
| Medical Device AI (MDAI) | Si el AI es safety component de un medical device → también cae bajo MDR/IVDR | Aplica ya |
| Requisitos adicionales | Data governance, explainability, human oversight, audit trails, bias testing | Full compliance agosto 2027 |
| Evaluación de conformidad | Dispositivos MDR clase IIa/IIb/III → evaluación por notified body requerida | 2027 |
| Overlap MDR + EU AI Act | MDCG 2025-6 guidance (publicada 2025): clarifica interplay entre ambas regulaciones | Activo |

> **Implicación clave:** Los AI Workers de HappyRobot en healthcare (scheduling, patient calls, RCM) probablemente NO caen bajo la categoría de medical device y no requieren conformidad MDR. Pero sí caen bajo EU AI Act como "high-risk" si se usan en decisiones que afectan acceso a atención, lo cual exige transparencia, auditoría y human oversight — precisamente los diferenciadores de HappyRobot.

### 5.3 MDR — Medical Device Regulation (UE)

| Aspecto | Detalle |
|---------|---------|
| Scope | Productos sanitarios físicos y software que sea "medical device" (SaMD — Software as a Medical Device) |
| Clasificación de riesgo | Clase I (bajo) a Clase III (alto, e.g., implantes activos) |
| Software clínico | Un algoritmo de diagnóstico = SaMD; una app de scheduling = NO SaMD |
| Certificación CE | Obligatoria para SaMD en el mercado europeo |
| Relevancia para HappyRobot | Los AI Workers de HappyRobot para scheduling, RCM, patient engagement NO son SaMD → no requieren CE como MD |

### 5.4 GDPR aplicado a datos de salud

| Aspecto | Detalle |
|---------|---------|
| Categoría especial | Datos de salud = "special category data" bajo GDPR Art. 9 — máxima protección |
| Base legal para procesamiento | Consentimiento explícito O interés vital O atención médica (Art. 9.2.c/h) |
| Data minimization | AI solo puede procesar los datos estrictamente necesarios |
| Right to explanation | Decisiones automatizadas significativas → paciente tiene derecho a explicación (Art. 22) |
| Data residency | Muchos hospitales europeos exigen datos en servidores EU |
| DPA notification | Breaches con datos de salud → notificación a autoridad en 72h |

> HappyRobot ya tiene certificación GDPR declarada [B: HR-WEB], lo cual es un punto de partida fuerte para el mercado europeo.

### 5.5 European Health Data Space (EHDS)

El EHDS, previsto para entrar en vigor progresivamente desde 2026, creará un marco de interoperabilidad de datos de salud en toda la UE. Permitirá a sistemas AI acceder (con consentimiento) a datos de salud secundarios para investigación e innovación. Para HappyRobot, el EHDS podría ser un catalizador: facilitará que los AI Workers accedan a datos necesarios para operar (scheduling, historial, etc.) con un marco legal claro.

---

## 6. Barreras de entrada y oportunidades

### Barreras

| Barrera | Descripción | Nivel de impacto |
|---------|-------------|-----------------|
| **Complejidad regulatoria** | HIPAA + EU AI Act + MDR + GDPR = stack regulatorio multicapa; especialmente exigente para SaMD | Alto |
| **Ciclos de venta largos** | Hospitales públicos: 12-24 meses; necesidad de pilotos clínicos, aprobaciones de dirección, comités de ética | Alto |
| **Interoperabilidad / EHR lock-in** | Los datos están en silos de Epic, Oracle, SAP. Las APIs son limitadas, caras y no estandarizadas | Alto |
| **Resistencia clínica** | Override rate de 73% en AI opaca vs. <2% en AI transparente (Diagnostics 2025 [B]). Trust gap crítico | Alto |
| **Madurez del producto** | 77% de encuestados cita "falta de madurez de herramientas AI" como mayor barrera (survey PMC 2025 [B]) | Medio |
| **Responsabilidad legal** | Marco de liability para clínicos que usan AI aún incierto en Europa y parcialmente en EE.UU. | Medio |
| **Coste de implementación** | Integraciones EHR son caras; forward-deployed engineers necesarios | Medio |
| **Privacy / datos pacientes** | Hospitales son muy conservadores con datos; BAAs, DPIAs, auditorías antes de cualquier contrato | Alto |

### Oportunidades

| Oportunidad | Por qué existe | Potencial |
|------------|----------------|-----------|
| **Costes administrativos sanitarios ($450B solo en EE.UU.)** | 1/3 de la plantilla hospitalaria es administrativa; tareas altamente repetitivas y no clínicas | Muy alto |
| **Escasez de personal sanitario** | Déficit de 10M de trabajadores de salud global para 2030 (OMS) [C: estimación widely cited]; AI como amplificador de capacidad | Alto |
| **Hospitales privados y aseguradoras como early adopters** | Menor fricción regulatoria que SNS; incentivo económico claro (coste por interacción) | Alto para entrada rápida |
| **NLP para idiomas no-ingleses** | Mayoría de soluciones optimizadas para inglés; mercado español/europeo subservido | Alto para HappyRobot en España |
| **EHDS como catalizador de datos** | Nuevo acceso legal a datos de salud en Europa (2026+) facilita entrenar y desplegar modelos | Medio-alto (2027+) |
| **Convergencia logistics + healthcare en supply chain** | Distribución de medicamentos, gestión de almacenes farmacéuticos, cold chain AI — extensión natural del core de HappyRobot | Medio |

---

## 7. Relevancia para HappyRobot

### Por qué healthcare es una expansión natural

HappyRobot ya opera en logistics con AI Workers que ejecutan tareas complejas por voz, email y chat, integran con sistemas empresariales, y operan con governance y auditoría built-in. Healthcare comparte exactamente el mismo patrón:

| Capacidad HappyRobot | Aplicación en logistics | Aplicación en healthcare |
|---------------------|------------------------|--------------------------|
| AI Workers multicanal (voz, email, chat) | Carrier calls, load tracking, dispatch | Patient scheduling calls, appointment reminders, post-discharge follow-up |
| Integración nativa con sistemas enterprise | TMS, WMS, ERP | EHR (Epic, Oracle), scheduling systems, billing platforms |
| 100% response rate, 0 min FRT | 24/7 carrier communication | 24/7 patient access, no missed calls |
| Governance & evaluations (AI Auditor) | Compliance en operaciones logísticas | HIPAA audit trails, EU AI Act transparency requirements |
| Shared context & memory | Historial de cargas y proveedores | Historial de paciente, interacciones anteriores |
| Forward-deployed engineers | Implementación en operaciones complejas | Integración con sistemas hospitalarios legacy |
| SOC 2 + GDPR + HIPAA | Compliance supply chain | Compliance sanitario ya cubierto |
| Cloud/model-agnostic | Flexibilidad de deploy | Adaptable a restricciones de data residency |

### Casos de uso concretos para HappyRobot en healthcare

1. **Patient scheduling inbound/outbound** — AI Workers gestionan llamadas de scheduling exactamente como gestionan carrier calls. Integración con EHR para disponibilidad en tiempo real. ROI documentado: 25-50% reducción costes administrativos (Houston Methodist [B]).

2. **Revenue cycle management calls** — Llamadas de seguimiento de reclamaciones, verificación de beneficios, prior authorization. Mercado: $450B en costes administrativos anuales en EE.UU. [A: Prosper AI, múltiples fuentes].

3. **Post-discharge patient engagement** — Protocolo de llamadas automatizadas para seguimiento clínico, educación sobre medicación, detección temprana de readmisiones. Hippocratic AI compite directamente aquí con 115M+ interacciones [A: Hippocratic AI press].

4. **Healthcare supply chain** — Extensión directa del core: gestión de inventario farmacéutico, coordinación de distribución de medicamentos, logística de dispositivos médicos. Clientes naturales: DHL Supply Chain (ya cliente de HappyRobot) tiene división Healthcare Logistics.

### Diferenciación frente a competidores en healthcare

| Competidor | Fortaleza | Vulnerabilidad frente a HappyRobot |
|-----------|-----------|-------------------------------------|
| Hippocratic AI | Especialización clínica profunda, 115M interacciones | Solo patient-facing; no cubre back-office ni supply chain |
| Nuance DAX | Integración Epic dominante | Solo ambient scribing; no voz outbound ni agentic ops |
| Prosper AI | Voice AI nativo en RCM | Early stage ($5M); sin track record enterprise |
| Epic (ambient scribe) | EHR nativo | Solo documentación; no multi-canal ni outbound |

**Posición competitiva de HappyRobot:** Plataforma horizontal con verticalizaciones — puede atacar healthcare con el mismo stack que logistics, añadiendo compliance HIPAA/EU AI Act que ya tiene. La diferencia está en que HappyRobot no es solo patient-facing ni solo clinical: puede cubrir todo el workflow operativo de un hospital (scheduling + RCM + supply chain + back-office) desde una sola plataforma con governance centralizada.

### Riesgo de entrada

- Ciclos de venta hospitalarios son más largos que en logistics (12-24 meses vs. 3-6 meses)
- Requiere personal con experiencia sanitaria en el equipo de sales/forward-deployed
- Competidores especializados (Hippocratic AI, Abridge) tienen ventaja de domain credibility
- **Estrategia recomendada:** Entrar por healthcare supply chain (extensión natural de DHL) y RCM back-office antes que patient-facing clinical AI

---

## 8. Fuentes

### Fuentes primarias / corporativas

| ID | Descripción | URL | Nivel |
|----|-------------|-----|-------|
| HR-WEB | HappyRobot website — compliance HIPAA, SOC 2, GDPR | https://www.happyrobot.ai/ | A |
| HIPPOCRATIC-PRESS | Hippocratic AI Series C $126M announcement | https://hippocraticai.com/hippocratic-ai-announces-series-c-funding-126-million/ | A |
| PROSPER-GN | Prosper AI raise $5M GlobeNewswire | https://www.globenewswire.com/news-release/2025/09/23/3154716/0/en/Prosper-AI-raises-5M-to-be-the-default-voice-AI-platform-for-healthcare-s-450B-admin-crisis.html | A |

### Informes de mercado

| ID | Fuente | URL | Nivel |
|----|--------|-----|-------|
| PREC-2025 | Precedence Research — AI Healthcare Market | https://www.precedenceresearch.com/artificial-intelligence-in-healthcare-market | B |
| GVR-2025 | Grand View Research — AI in Healthcare Market | https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-ai-healthcare-market | B |
| FBI-2025 | Fortune Business Insights — AI Healthcare | https://www.fortunebusinessinsights.com/industry-reports/artificial-intelligence-in-healthcare-market-100534 | B |
| MM-2030 | MarketsandMarkets — AI Healthcare worth $110.61B by 2030 | https://www.marketsandmarkets.com/PressReleases/artificial-intelligence-healthcare.asp | B |
| GN-2035 | GlobeNewswire — AI Healthcare $1,222B by 2035 | https://www.globenewswire.com/news-release/2026/03/04/3249111/0/en/Artificial-Intelligence-in-Healthcare-Market-Size-to-Reach-USD-1222-12-Billion-by-2035 | C |
| MDF-2025 | MarketDataForecast — Europe AI Healthcare | https://www.marketdataforecast.com/market-reports/europe-ai-in-healthcare-market | B |
| SR-EUR | StraitsResearch — Healthcare AI Europe | https://straitsresearch.com/report/healthcare-artificial-intelligence-market | C |

### Prensa y research

| ID | Fuente | URL | Nivel |
|----|--------|-----|-------|
| MENLO-2025 | Menlo Ventures — State of AI in Healthcare 2025 | https://menlovc.com/perspective/2025-the-state-of-ai-in-healthcare/ | B |
| CB-2025 | Crunchbase — Healthcare AI funding $10.7B 2025 | https://news.crunchbase.com/health-wellness-biotech/ai-healthcare-funding-rises-2025/ | A |
| FIERCE-2025 | FierceHealthcare — Healthcare AI $4B VC 2025 | https://www.fiercehealthcare.com/health-tech/healthcare-ai-rakes-nearly-4b-vc-funding-buoying-digital-health-market-2025 | A |
| ABRIDGE-STAT | STAT News — Abridge $300M Series E | https://www.statnews.com/2025/06/24/ai-clinical-documentation-ambient-scribe-abridge-raises-300-million/ | A |
| NABLA-STAT | STAT News — Nabla $70M raise | https://www.statnews.com/2025/06/17/nabla-raises-70-million-ambient-market-heats-up/ | A |
| BCG-2026 | BCG — How AI Agents Will Transform Health Care in 2026 | https://www.bcg.com/publications/2026/how-ai-agents-will-transform-health-care | B |
| BECKER-2026 | Becker's — Ambient AI to Agentic Workflows 2026 | https://www.beckershospitalreview.com/healthcare-information-technology/from-ambient-ai-to-agentic-workflows-whats-ahead-for-healthcare-in-2026/ | B |
| DELOITTE-2025 | Deloitte — AI Scale, Governance, ROI in Healthcare | https://www.deloitte.com/us/en/Industries/life-sciences-health-care/blogs/health-care/ais-next-phase-in-health-care-scale-governance-roi.html | B |
| NVIDIA-2026 | NVIDIA State of AI Healthcare 2026 (citado en Becker's) | — | B |
| MKSY-2025 | McKinsey — Evolution of Healthcare AI Modular Architecture | https://www.mckinsey.com/industries/healthcare/our-insights/the-coming-evolution-of-healthcare-ai-toward-a-modular-architecture | B |

### Regulación

| ID | Fuente | URL | Nivel |
|----|--------|-----|-------|
| MDCG-2025-6 | European Commission MDCG 2025-6 — AI Act & Medical Devices | https://health.ec.europa.eu/document/download/b78a17d7-e3cd-4943-851d-e02a2f22bbb4_en?filename=mdcg_2025-6_en.pdf | A |
| RS-EUAIACT | ReedSmith — EU AI Act and Medical Devices | https://www.reedsmith.com/our-insights/blogs/viewpoints/102kq35/the-eu-ai-act-and-medical-devices-navigating-high-risk-compliance/ | B |
| GROOVY-2026 | GroovyWeb — Healthcare App Compliance 2026 | https://www.groovyweb.co/blog/healthcare-app-compliance-guide-2026 | B |

### España

| ID | Fuente | URL | Nivel |
|----|--------|-----|-------|
| ASEBIO-2025 | AseBio — Spanish AI Healthcare Landscape | https://www.asebio.com/en/actualidad/noticias/inteligencia-artificial-sector-salud-espana | B |
| BDE-2025 | Banco de España — Adopción AI en empresas españolas | https://www.bde.es/f/webbe/SES/Secciones/Publicaciones/InformesBoletinesRevistas/BoletinEconomico/25/T2/Fich/be2502-art06.pdf | A |
| NC-ESP | Nucamp — AI Healthcare Spain 2025 (fuente C, no verificada) | https://www.nucamp.co/blog/coding-bootcamp-spain-esp-healthcare-the-complete-guide-to-using-ai-in-the-healthcare-industry-in-spain-in-2025 | C |
| EC-ESP | European Commission / Spain — AI acceleration healthcare | https://spain.representation.ec.europa.eu/noticias-eventos/noticias-0/la-comision-pone-en-marcha-dos-estrategias-para-acelerar-la-adopcion-de-la-ia-en-la-industria-y-la-2025-10-08_es | B |

---

*Nodo actualizado: 2026-04-07. Para cross-links: [HappyRobot](../empresa/happyrobot.md) · [AI Agents](../tecnologia/agentic-ai.md) · [Voice AI](../tecnologia/voice-ai.md) · [EU AI Act](../regulacion/eu-ai-act.md) · [GDPR](../regulacion/gdpr-lopdgdd.md) · [Enterprise AI Europa](enterprise-ai-europa.md)*
