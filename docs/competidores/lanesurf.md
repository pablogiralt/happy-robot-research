---
title: "Lanesurf"
type: competidor
status: completo
tags: [competidor, voice-ai, logistics-ai, freight, negociacion, usa, yc]
updated: 2026-04-07
---

# Lanesurf

Plataforma de voice AI especializada exclusivamente en **carrier sourcing, rate negotiation y load booking** para freight brokers en EE.UU. Fundada por Pratham Bansal (CEO, ex-IIT Delhi, Caltech, Booz & Co.) y Sarthak Singh Chauhan (CTO), ambos con un exit previo en biotech AI. Aceptados en YC S25 con ~$500K de funding confirmado y ~30+ clientes logísticos. Es un **competidor directo pero acotado** de [HappyRobot](../empresa/happyrobot.md): point solution para negociación de carriers vs. plataforma completa de AI Workers.

---

## Ficha rápida

| Dato | Valor | Conf. |
|---|---|---|
| **Web** | [lanesurf.com](https://www.lanesurf.com/) | A |
| **HQ** | San Francisco, CA | A |
| **Fundadores** | Pratham Bansal (CEO, IIT Delhi/Caltech/Booz & Co.), Sarthak Singh Chauhan (CTO, IIT Delhi) | A |
| **Empleados** | 4-10 (YC dice 4; job posting dice 11-50) | B |
| **Funding total** | ~$500K (pre-seed) | B |
| **Última ronda** | Pre-seed (YC S25) | A |
| **Valoración** | [dato no disponible públicamente] | — |
| **ARR estimado** | $550K (2025, equipo de 5) | C |
| **Clientes** | 30+ logistics service providers | B |

!!! warning "Dato en conflicto: $18M de funding"
    Algunas fuentes mencionan "$18M de funding" pero no se ha podido verificar. Crunchbase indica ~$500K pre-seed. **Tratar como no verificado.**

!!! warning "Dato en conflicto: General Catalyst y Jawed Karim como inversores"
    No se ha encontrado confirmación pública. Los inversores confirmados son YC, Naval Ravikant, Rajul Garg/Leo Capital y Transpose Platform Management. **Tratar como no verificado.**

### Inversores confirmados

- **Y Combinator** (S25, partner Jon Xu)
- **Naval Ravikant** (angel)
- **Rajul Garg / Leo Capital**
- **Transpose Platform Management**
- **Advisors:** Ejecutivos de Convoy, TQL, Walmart [B: FW-SPEAKER]

---

## Producto

### Qué hace Lanesurf

Automatiza el proceso más tedioso del freight brokerage: llamar a decenas de carriers para cubrir un load. La IA negocia en paralelo por teléfono, email y SMS.

### Flujo de trabajo

1. **SOURCING** → AI llama, envía email y SMS a múltiples carriers simultáneamente. Busca capacidad disponible, recoge info de carrier y datos de vetting.
2. **BOOKING** → Confirma detalles, negocia rates con múltiples opciones en paralelo, ejecuta bookings con compliance checks.
3. **TRACKING** → Monitoriza ETAs y status, contacta drivers para actualizaciones, flaggea delays y escala con contexto.

### Capacidades técnicas

| Capacidad | Detalle | Conf. |
|-----------|---------|-------|
| **Llamadas paralelas** | 96-100+ carriers simultáneamente por teléfono, email y SMS | A |
| **Negociación con memoria** | Retiene historial de conversaciones, rates, preferencias de lane y compliance | B |
| **Vetting de compliance** | Verifica MC numbers, seguros y cumplimiento antes del outreach | A |
| **Real-time market signals** | Preferencias del carrier, precios de fuel, clima, tendencias de mercado | B |
| **Customización** | MC vetting, compliance checks, lógica de escalación, tono de negociación, umbrales de pricing por lane | B |
| **Onboarding** | <1 hora start con Excel; <10 días integración completa; sin IT necesario | B |

### Demo en vivo: F3 Future of Freight Festival (2025)

- Load real: Bolingbrook, IL → Columbus, GA
- En el timeframe del demo: 48 outbound calls + 28 outbound emails
- AI negoció de $1,900 ofertados a $2,000 acordados (vs standard $2,100), aprovechando historial de relación [A: FW-ARTICLE]

### Integración y compliance

- Conecta con mayoría de TMS modernos, load boards, portales de compliance y CRMs [B: LANESURF-WEB]
- SOC-2 Type II certificado, GDPR compliant, AES-256 at rest, TLS 1.2+ in transit [B: LANESURF-WEB]

---

## Clientes y métricas

| Métrica | Valor | Conf. | Fuente |
|---------|-------|-------|--------|
| Loads cubiertos con AI | 60-80% de los loads | B | LANESURF-WEB |
| Mejora de buy rates | 8-10% mejores rates por load | B | LANESURF-WEB |
| Ahorro de tiempo/rep | 4+ horas manuales ahorradas por rep/día | B | LANESURF-WEB |
| Margen extra por load | +$50 de media | B | YC-LANESURF |
| Tiempo de booking | <10 minutos (vs horas manualmente) | A | FW-DEMO |
| Clientes | 30+ logistics service providers | B | LANESURF-WEB |
| Revenue 2025 | $550K (equipo de 5) | C | GETLATKA |

!!! warning "Verificación de testimonios"
    Los nombres/empresas en testimonios de la web (Mike Reynolds, Sarah Chen, etc.) no se han podido verificar independientemente. Podrían ser nombres cambiados por privacidad o representativos. **No citar como clientes confirmados en entrevista.**

### Perfil de cliente típico

- **Mid-sized US freight brokers** — no enterprise Fortune 500
- Brokerages que bookean miles de loads diariamente
- Target: 1 operador supervisa lo que antes requería equipo completo de carrier sales

---

## Modelo de negocio

| Aspecto | Detalle | Conf. |
|---------|---------|-------|
| Modelo | SaaS — por usuario/mes (estimado) | C |
| Rango estimado | $50-200/usuario/mes | C |
| Pricing público | No disponible en la web | A |
| ROI pitch | "Se paga solo en las primeras 2 semanas" | B |
| Referral program | $3,000 por intro a freight broker/3PL que convierte | A |

Es probable que evolucionen a pricing basado en volumen o valor (per-load fee o % del ahorro) dado que el +$50 de margen extra por load supera con creces el precio del SaaS.

---

## HappyRobot vs Lanesurf

| Dimensión | HappyRobot | Lanesurf |
|---|---|---|
| **Scope** | Plataforma: AI Workers para todo el ciclo (check calls, scheduling, collections, sales, CS, HR, finance) | Point solution: solo carrier sourcing + rate negotiation + booking |
| **Vertical** | Logistics principal + expansión multi-vertical | Solo freight brokerage (US) |
| **Canales** | Voice + email + web chat (true multi-channel) | Voice + email + SMS (centrado en voice para negociación) |
| **Diferenciador core** | AI Workers con governance, memory compartida, auditor AI, lógica agéntica + determinista | Negociación paralela de rates (96-100+ llamadas simultáneas) |
| **Clientes** | DHL Supply Chain, Circle Logistics, Samsara, MODE Global, Syfan (enterprise) | 30+ mid-size freight brokers |
| **Geografía** | EE.UU. + expansión Europa (España) | Solo EE.UU. |
| **Stage** | Serie B $44M, 150-200 empleados | Pre-seed / YC S25, ~$500K, ~4-10 empleados |
| **Compliance** | SOC 2, GDPR, HIPAA, EU AI Act | SOC-2 Type II, GDPR |
| **Onboarding** | Forward-deployed engineers para customización | <1 hora start, <10 días full integration |
| **Revenue** | [dato no disponible] | ~$550K (2025, no verificado) |

### Análisis estratégico

1. **Point solution vs Platform.** Lanesurf resuelve UN problema muy bien (carrier negotiation). HappyRobot cubre múltiples workflows. Para un broker que solo quiere automatizar outreach a carriers, Lanesurf es más simple. Para enterprise que quiere transformar operaciones completas, HappyRobot es la opción.

2. **Velocidad de ejecución impresionante.** Con ~5 personas han llegado a $550K revenue y 30+ clientes. La demo de 96 llamadas paralelas en 10 minutos es muy visual y se vende sola.

3. **Mercado diferente por ahora.** Lanesurf vende a mid-size freight brokers en US. HappyRobot a enterprise (DHL, Samsara). Solapamiento en el middle market.

4. **Riesgo real para HappyRobot:** Lanesurf puede capturar el mercado de freight brokers mid-size antes de que HappyRobot baje a ese segmento. Si se convierte en "el standard" para carrier negotiation, sería difícil desplazarlos.

---

## Debilidades y críticas

| Debilidad | Detalle |
|-----------|---------|
| **Scope limitado** | Solo carrier sourcing/negotiation/booking. No cubre check calls, scheduling, collections, CS ni otros workflows |
| **Solo US** | Sin presencia internacional; limitado al freight brokerage americano |
| **Equipo muy pequeño** | 4-10 personas; riesgo de key-person dependency y capacidad limitada de soporte |
| **Funding limitado** | ~$500K confirmed vs $44M de HappyRobot; mucho menos runway |
| **Sin enterprise track record** | Clientes mid-size; no ha demostrado servir a Fortune 500 |
| **No hay reviews públicas** | No se encuentran reviews en G2, Capterra, Reddit — producto muy nuevo |
| **Testimonios no verificables** | Los testimonios en la web no se pueden confirmar independientemente |
| **Single vertical** | Solo freight brokerage; TAM se reduce si brokers grandes construyen in-house |

---

## Noticias recientes

| Fecha | Evento | Fuente |
|-------|--------|--------|
| **Abr 2026** | YC launch post en LinkedIn — "Freight still runs on phone calls" | YC-LINKEDIN |
| **Abr 2026** | Hiring: Agent Engineer, Principal ML Research Engineer, Forward Deployed Engineer | YC-LANESURF |
| **2025** | Demo en F3: Future of Freight Festival — 96 llamadas paralelas en 10 min | FW-ARTICLE [A] |
| **2025** | Aceptados en **YC Summer 2025** | YC-LANESURF [A] |

---

## Equipo fundador

### Pratham Bansal — CEO

| Campo | Detalle |
|-------|---------|
| Educación | IIT Delhi (ingeniería) |
| Research | ML research en Caltech y Rice |
| Experiencia | Consultant en Booz & Co. — AI automation para Fortune 500 logistics |
| Exit anterior | Vendió producto de vertical AI en biotech (six-figure ARR) a empresa backed by NVIDIA |
| Conexión freight | Familia en la industria; meses embebido con equipos de brokers escuchando calls reales |

### Sarthak Singh Chauhan — CTO

| Campo | Detalle |
|-------|---------|
| Educación | IIT Delhi (ingeniería) |
| Research | Co-authored transformer-based ML research pre-LLM era |
| Experiencia | Compute-efficient inference algorithms adoptados por Fortune 100 biopharma |
| Exit anterior | Mismo producto biotech AI (co-fundador con Pratham) |

---

## Relevancia para la entrevista

### Si preguntan "¿Cómo ves a Lanesurf como competidor?"

> "Lanesurf es un ejemplo perfecto de por qué el timing de HappyRobot en España es clave. Son un equipo pequeño pero muy enfocado — hacen una cosa muy bien: negociación automática de rates con carriers por voz. Pero ahí está la diferencia: Lanesurf es una point solution, HappyRobot es una plataforma. Un freight broker que adopta Lanesurf sigue necesitando soluciones separadas para check calls, tracking, collections, scheduling. Con HappyRobot, tiene AI Workers para todo el ciclo. Además, Lanesurf solo opera en US y solo en freight brokerage. HappyRobot ya tiene clientes enterprise como DHL y está expandiendo a Europa."

### Si preguntan "¿Qué podemos aprender de Lanesurf?"

> "Dos cosas: primera, la demo de 96 llamadas paralelas en 10 minutos es brillante como herramienta de venta — tangible, medible, genera wow. HappyRobot debería tener demos igual de impactantes. Segunda, el onboarding es impresionantemente rápido — menos de una hora para empezar. Eso reduce fricción en el ciclo de venta, especialmente para el mid-market donde no puedes desplegar forward-deployed engineers en cada cliente."

---

## Fuentes

| Código | URL | Tipo | Conf. |
|--------|-----|------|-------|
| LANESURF-WEB | https://www.lanesurf.com/ | Oficial | A |
| YC-LANESURF | https://www.ycombinator.com/companies/lanesurf | YC profile | A |
| FW-ARTICLE | https://www.freightwaves.com/news/this-ai-booked-a-load-in-10-minutes-by-speaking-to-96-carriers-at-the-same-time | FreightWaves | A |
| FW-SPEAKER | https://live.freightwaves.com/event-speakers/pratham-bansal | FreightWaves bio | A |
| CRUNCHBASE-LS | https://www.crunchbase.com/organization/lanesurf | Crunchbase | A |
| TARO-JOB | https://www.jointaro.com/jobs/lanesurf/founding-aivoice-engineer-46843a19/ | Job posting | B |
| GETLATKA | https://getlatka.com/companies/lanesurf.com | Revenue data | C |
| YC-LINKEDIN | https://www.linkedin.com/posts/y-combinator_freight-still-runs-on-phone-calls... | YC LinkedIn | B |
| FREIGHTCAVIAR | https://www.freightcaviar.com/these-three-companies-are-creating-freight-broker-ai-agents/ | Newsletter sector | B |

---

*Ver también: [HappyRobot](../empresa/happyrobot.md), [FleetWorks](fleetworks.md), [Pallet](pallet.md), [Logistics Operations](../casos-de-uso/logistics-operations.md), [Tabla comparativa competidores](index.md)*
