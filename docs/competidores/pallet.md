---
title: "Pallet / CoPallet"
type: competidor
status: completo
tags: [competidor, logistics-ai, ai-workforce, back-office, automation, usa, series-b]
updated: 2026-04-07
---

# Pallet / CoPallet

Startup que ha construido una **AI workforce para logistics back-office operations**. Fundada por **Sushanth Raman** (CEO) y **Andrew Spencer**, ambos ex-ingenieros tempranos de **Retool**. Ha levantado **$50M** (Serie B de $27M liderada por General Catalyst, mayo 2025). Su producto CoPallet automatiza tareas administrativas — data entry, document parsing, billing, quoting — a 10x la velocidad y <50% del coste de staffing tradicional. Con **70+ clientes** en producción incluyendo **Knight-Swift** (el carrier más grande de EE.UU.) y **Lineage Logistics** (líder global cold chain). Es **más complementario que competidor directo** de [HappyRobot](../empresa/happyrobot.md): Pallet es back-office; HappyRobot es front-office + operaciones de comunicación.

---

## Ficha rápida

| Dato | Valor | Conf. |
|---|---|---|
| **Web** | [pallet.com](https://www.pallet.com/) | A |
| **HQ** | San Francisco, CA | A |
| **Fundadores** | Sushanth Raman (CEO, ex-Retool), Andrew Spencer (ex-Retool) | A |
| **Empleados** | 51-100 (estimado) | B |
| **Funding total** | $50M (3 rondas) | A |
| **Última ronda** | $27M Serie B (mayo 2025, General Catalyst lead) | A |
| **Valoración** | [dato no disponible públicamente] | — |
| **ARR estimado** | [dato no disponible públicamente] | — |
| **Clientes** | 70+ organizaciones logísticas en producción; Knight-Swift, Lineage Logistics, Mallory Alexander, STG Logistics, Everest Transportation | A |

### Inversores

- **Bain Capital Ventures** (Seed + Serie A lead)
- **General Catalyst** (Serie B lead — también en Stripe, Snap, Airbnb)
- **Activant Capital**, **Bessemer Venture Partners**, **BoxGroup**
- **Angels Serie B:** Dan Lewis (CPO Microsoft, co-founder Convoy), Amit Agarwal (ex-President Datadog), Girish Rishi (ex-CEO BlueYonder), Michael Capellas (ex-CEO Compaq)
- **Angels Serie A:** Founders de Toast, CEO Dutchie, board Home Depot

---

## Producto

### Evolución del producto (tres capas)

#### Capa 1: Pallet OS — TMS/WMS all-in-one (producto original)

Sistema cloud-native que combina TMS + WMS + contabilidad/facturación. Target: flotas, freight brokers, 3PLs que quieren eliminar fragmentación tecnológica.

#### Capa 2: CoPallet — AI Workforce (producto estrella)

AI workers que completan workflows logísticos de forma autónoma. Se integra con TMS propio Y con TMS/WMS/ERP de terceros (McLeod, Revenova, Turvo), permitiendo vender a empresas con stack existente.

#### Capa 3: Pallet Core — Plataforma de agentes (marzo 2026)

- Plataforma para construir y desplegar agentes AI para cualquier caso de uso en supply chain
- **Modelo propietario** entrenado en datasets logísticos licenciados (claim: "supera a modelos frontier en benchmarks de speed y accuracy" — no verificado independientemente) [B: PALLET-CORE-BLOG]
- **Enterprise Memory Layer:** Codifica SOPs, reglas de cliente, excepciones, "tribal knowledge"
- Agent builder con orquestación de workflows, tool calls y pasos de validación
- Simulaciones con datos sintéticos para validar accuracy y eliminar alucinaciones [A: PALLET-CORE-BLOG]

### Workflows que automatiza CoPallet

| Workflow | Descripción | Conf. |
|----------|-------------|-------|
| **Order entry** | Procesamiento automático de órdenes (de 20 min → segundos) | A |
| **Document parsing** | AI vision — BOL, POD, facturas, documentos multi-página, escritura manual | A |
| **Invoice auditing** | Auditoría de facturas | A |
| **Quoting** | Cotización automatizada | A |
| **Portal updates** | Actualización de portales de clientes | A |
| **Shipment visibility** | Tracking y status updates | A |
| **Dispatching** | Asignación de cargas | A |
| **Customs processing** | Procesamiento aduanero | A |
| **Billing / facturación** | Generación y reconciliación de facturas | A |
| **Data reconciliation** | Fuzzy-matching entre TMS, WMS, ERP | A |
| **Import filings** | Declaraciones de importación (caso Mallory Alexander: 100% accuracy) | A |

### Integraciones técnicas

- **TMS:** McLeod, Revenova, Turvo (confirmados) [A: FW-AWARD]
- **Métodos:** API, EDI, browser automation [A: FW-AWARD, PALLET-BLOG-ENG]
- **AI Vision:** Lee formatos variados — documentos multi-página, tablas, escritura manual, convenciones inconsistentes [A: FW-AWARD]
- **Browser automation:** Navega aplicaciones web legacy con session management complejo, formularios multi-step [A: PALLET-BLOG-ENG]

### Métricas de rendimiento

| Métrica | Valor | Conf. | Fuente |
|---------|-------|-------|--------|
| Velocidad vs humanos | 10x más rápido | A | BW-SERIEB |
| Reducción de costes de staffing | 50-70% | A | DCVEL |
| Accuracy | 97%+ con guardrails | A | PALLET-WEB |
| Coste vs staffing tradicional | <50% | A | BW-SERIEB |

---

## Clientes y métricas

| Cliente | Tipo | Detalle | Conf. |
|---------|------|---------|-------|
| **Knight-Swift Transportation** | Carrier (el más grande de US) | En producción | A |
| **Lineage Logistics** | 3PL/Cold chain (líder mundial) | En producción | A |
| **Mallory Alexander** | 3PL/Freight forwarder | 100% accuracy en import filings | A |
| **STG Logistics** | 3PL/Intermodal | En producción | A |
| **Everest Transportation** | Carrier/Forwarder | 20+ workflows, +10% margen operativo | A |
| Carrier mid-size (Chicago, anónimo) | Carrier intermodal | 25 empleados reasignados, order processing 20min → segundos, 8 semanas de implantación | A |

**Total:** 70+ organizaciones logísticas en producción [A: PALLET-CORE-BLOG]

**Tipos:** Freight brokers, 3PLs, freight forwarders, carriers, shippers [A: BW-SERIEB]

!!! note "Clientes de alto calibre"
    Knight-Swift y Lineage son gigantes del sector. Knight-Swift es el carrier más grande de EE.UU.; Lineage es líder global en cold chain. Señal fortísima de product-market fit en enterprise logistics.

---

## Modelo de negocio

**Pricing público:** No disponible [C].

**Value proposition cuantificada:**
- "10x más rápido y <50% del coste de staffing tradicional" [A: BW-SERIEB]
- ~10% del gasto logístico va a trabajo administrativo manual [A: GC-INVESTMENT]

**Modelo probable:** SaaS enterprise con pricing basado en volumen de workflows/transacciones o por "AI worker" [C: inferencia].

---

## HappyRobot vs Pallet

| Dimensión | HappyRobot | Pallet (CoPallet) |
|---|---|---|
| **Foco principal** | Communication & coordination: llamadas, email, SMS, chat + operaciones | Back-office operations: data entry, document parsing, quoting, billing |
| **Canal principal** | Voz (teléfono), email, SMS, web chat (multi-canal comunicación) | Browser automation + API + EDI (opera dentro de sistemas) |
| **Vertical** | Logistics principal + customer service, sales, finance, HR | Logistics exclusivamente |
| **Producto adicional** | No tiene software operacional propio | TMS/WMS propio (Pallet OS) — lock-in potencial |
| **Modelo AI** | Cloud/model-agnostic (múltiples LLMs) | Propietario, entrenado en datos logísticos licenciados |
| **Clientes notables** | DHL Supply Chain, Circle Logistics, Samsara, MODE Global | Knight-Swift, Lineage, STG, Mallory Alexander, Everest |
| **Clientes en producción** | [dato no disponible con precisión] | 70+ |
| **Funding total** | $44M (Serie B) + anteriores | $50M |
| **Governance/Compliance** | SOC 2, GDPR, HIPAA, EU AI Act, AI auditor | Guardrails + simulaciones sintéticas |
| **Expansión internacional** | Abriendo España/Europa | No mencionada |
| **Idiomas** | 15+ idiomas en voice | [no mencionado] |

### Análisis de posicionamiento

**Pallet es back-office; HappyRobot es front-office + back-office.**

1. **Pallet automatiza el trabajo silencioso** — lo que pasa dentro de los sistemas (TMS, WMS, ERP): entrar órdenes, parsear documentos, reconciliar datos. El usuario final no interactúa con CoPallet.

2. **HappyRobot automatiza la comunicación + operaciones** — llamadas de teléfono, emails, check calls, scheduling, tracking updates. Los AI Workers interactúan directamente con carriers, shippers, clientes finales.

3. **Son más complementarios que competidores directos.** Una empresa podría usar Pallet para data entry/document parsing y HappyRobot para llamadas y comunicación. Hay solapamiento creciente: HappyRobot expande hacia operaciones; Pallet menciona "process calls" pero no es su core.

4. **Pallet tiene la ventaja del TMS/WMS propio** — "full stack" logístico (sistema operativo + AI workers encima), creando mayor lock-in. HappyRobot es system-agnostic: flexibilidad pero menos profundidad de integración.

5. **HappyRobot tiene ventaja en multi-canal y multi-idioma** — crucial para expansión internacional.

---

## Debilidades y críticas

| Debilidad | Detalle | Conf. |
|-----------|---------|-------|
| **Solo EEUU** | No hay mención de operaciones internacionales ni soporte multilingüe | B |
| **Foco estrecho** | Solo logistics — si AI agents se consolida, players multi-vertical pueden tener ventaja | B |
| **Back-office only** | No maneja comunicación directa (voz, email) como core | B |
| **Dependencia browser automation** | Para sistemas legacy, browser automation es frágil — cambios en UI rompen integraciones | B |
| **Modelo propietario no verificado** | Claim de "superar frontier models" sin benchmark independiente | C |
| **Sin reviews públicas** | No hay reviews en G2, Capterra, Reddit | B |
| **Competencia con TMS incumbents** | McLeod, TMW, MercuryGate ya añaden AI — Pallet compite con sus propios socios de integración | B |
| **TMS/WMS legacy puede ser distracción** | Mantener dos productos dispersa recursos en startup de 50-100 personas | C |

### Riesgos competitivos para HappyRobot

1. **Si Pallet añade voice/comunicación**, se convierte en competidor directo más fuerte
2. **El TMS propio les da data moat** — ven todas las operaciones de sus clientes TMS, alimenta sus modelos AI
3. **Knight-Swift y Lineage como clientes** da credibilidad enterprise que abre puertas
4. **General Catalyst como lead investor** es señal fuerte de calidad

---

## Noticias recientes

| Fecha | Evento | Fuente |
|-------|--------|--------|
| **Mar 2026** | Lanzamiento **Pallet Core** — plataforma de agentes con modelo propietario, Enterprise Memory Layer | PALLET-CORE-BLOG [A] |
| **Mar 2026** | **70+ clientes** en producción anunciados (Knight-Swift, Lineage, STG, Mallory Alexander, Everest) | PALLET-CORE-BLOG [A] |
| **Ene 2026** | **FreightWaves AI Excellence Award** (premio inaugural) | FW-AWARD [A] |
| **May 2025** | **$27M Serie B** liderada por General Catalyst | BW-SERIEB [A] |

---

## Equipo fundador

### Sushanth Raman — CEO

- Ex-ingeniero temprano en **Retool** (plataforma low-code)
- Conexión personal: abuelo tenía negocio de shipping [A: TC-PALLET]

### Andrew Spencer — Co-founder

- Ex-ingeniero temprano en **Retool**
- Conexión personal: padre dirige ingeniería en **MercuryGate** (TMS) [A: TC-PALLET]

### Equipo

- ~51-100 empleados [B]
- 1/3 del equipo viene de empresas logísticas: Worldwide Express, CEVA, Uber Freight [A: GC-INVESTMENT]
- También ex-YC founders y top performers de Meta, Scale AI, Rippling [A: GC-INVESTMENT]

---

## Relevancia para la entrevista

### Talking points concretos para Lola

1. **"Pallet y HappyRobot atacan el problema desde ángulos complementarios"** — Pallet es back-office (data entry, docs), HappyRobot es comunicación + operaciones. Juntos cubren el espectro completo, pero HappyRobot tiene el moat en voice/multicanal.

2. **"La expansión a Europa es donde HappyRobot tiene ventaja clara"** — Pallet no tiene presencia internacional ni capacidad multilingüe. HappyRobot con 15+ idiomas y oficina en España tiene first-mover advantage.

3. **"El modelo propietario de Pallet es interesante pero arriesgado"** — Entrenar tu propio modelo es caro y puede quedar obsoleto rápido. El approach model-agnostic de HappyRobot permite usar siempre el mejor modelo disponible.

4. **"Pallet valida el mercado"** — General Catalyst liderando una Serie B de $27M para AI logistics workforce confirma que el TAM es real y grande. Beneficia a HappyRobot también.

5. **"Los clientes enterprise de Pallet (Knight-Swift, Lineage) muestran que los grandes están comprando AI"** — Abre la puerta para HappyRobot en cuentas similares en Europa. DHL ya es cliente.

---

## Fuentes

| Código | URL | Tipo | Conf. |
|--------|-----|------|-------|
| TC-PALLET | https://techcrunch.com/2024/10/02/pallet-uses-ai-to-bring-logistics-into-the-21st-century/ | TechCrunch | A |
| BW-SERIEA | https://www.businesswire.com/news/home/20241002015291/en/ | PR Serie A | A |
| BW-SERIEB | https://www.businesswire.com/news/home/20250527164246/en/ | PR Serie B | A |
| PALLET-BLOG-B | https://www.pallet.com/blog/series-b | Blog Serie B | A |
| PALLET-CORE-BLOG | https://www.pallet.com/blog/pallet-core | Lanzamiento Pallet Core | A |
| PALLET-BLOG-ENG | https://www.pallet.com/blog/engineering-ai-agents-for-logistics | Blog engineering | A |
| GC-INVESTMENT | https://www.generalcatalyst.com/stories/our-investment-in-pallet | General Catalyst note | A |
| FW-AWARD | https://www.freightwaves.com/news/pallet-recognized-for-customer-specific-end-to-end-ai | FreightWaves award | A |
| DCVEL | https://www.dcvelocity.com/technology/artificial-intelligence/tech-startup-pallet-raises-27-million-for-workflow-ai | DC Velocity | A |
| PALLET-WEB | https://www.pallet.com/ | Oficial | A |
| THEORG | https://theorg.com/org/pallet-1 | Directorio | B |
| HIMALAYAS | https://himalayas.app/companies/trypallet | Directorio | B |

---

*Ver también: [HappyRobot](../empresa/happyrobot.md), [FleetWorks](fleetworks.md), [Lanesurf](lanesurf.md), [Logistics Operations](../casos-de-uso/logistics-operations.md), [Tabla comparativa competidores](index.md)*
