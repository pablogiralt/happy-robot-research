---
title: "Sales — Inbound & Outbound"
type: caso-de-uso
status: completo
tags: [caso-de-uso, sales, inbound, outbound, leads, revenue]
updated: 2026-04-07
---

# Sales — Inbound & Outbound

Use case de generación de revenue: AI Workers que cualifican leads, hacen follow-up, prospectan, y generan pipeline de ventas para los clientes de [HappyRobot](../empresa/happyrobot.md).

---

## Métricas publicadas

| Métrica | Valor | Conf | Fuente |
|---------|-------|------|--------|
| Outbound sales ROI | **~19-20x** | B | HR-SERIEB (varía entre fuentes: 19x vs 20x) |
| Cost per lead reduction | **70%** | B | HR-WEB |
| Margin increase | **10%** (en carrier sales) | A | HR-CIRCLE |
| [Circle](../clientes/circle-logistics.md) cargas por rep | **25% más** freight/mes | A | HR-CIRCLE |
| Circle zero-touch freight | 18% de todo el freight booked sin intervención humana | A | HR-CIRCLE |

---

## Use cases de sales

### 1. Inbound Lead Qualification

| Aspecto | Detalle |
|---------|---------|
| **Qué hace** | Recibe llamadas/emails de leads inbound, cualifica según ICP, programa demo/reunión con AE |
| **Pain point** | SDRs dedican 60-70% del tiempo a leads que no cualifican. Respuesta lenta = lead perdido |
| **Resultado** | Respuesta instantánea 24/7, cualificación consistente, 70% menos cost per lead |
| **Canal** | Teléfono + email + web chat |

### 2. Outbound Sales / Prospecting

| Aspecto | Detalle |
|---------|---------|
| **Qué hace** | Llamadas y emails de prospección a targets fríos/tibios, presenta value prop, programa reuniones |
| **Pain point** | Outbound manual tiene tasa de contacto baja (~15-20%) y es tedioso para SDRs |
| **Resultado** | 19-20x ROI — AI hace volumen masivo de contactos, humanos se centran en cerrar |
| **Canal** | Teléfono + email |

### 3. Carrier Sales (específico logistics)

| Aspecto | Detalle |
|---------|---------|
| **Qué hace** | Recibe llamadas de carriers con capacidad disponible, presenta cargas, negocia tarifas, cierra booking |
| **Pain point** | Freight brokers reciben cientos de llamadas diarias de carriers — cada una es una oportunidad de revenue |
| **Resultado** | 5x returns, 10% mejores márgenes, 25% más freight por rep |
| **Canal** | Teléfono |
| **Cliente referencia** | [Circle Logistics](../clientes/circle-logistics.md) — primer use case y el más maduro |

### 4. Revenue Generation (New Streams)

| Aspecto | Detalle |
|---------|---------|
| **Qué hace** | Identifica oportunidades de upsell/cross-sell en base de clientes existente |
| **Pain point** | Equipos de account management no tienen tiempo para prospección proactiva en la propia cartera |
| **Resultado** | Generación de revenue incremental sin contratar más vendedores |
| **Canal** | Email + teléfono |

---

## Cómo funciona: el flujo completo

```
Lead entra (llamada/email/form)
  → AI Worker cualifica (ICP scoring, preguntas clave)
    → Si cualificado → programa reunión con AE humano + envía resumen
    → Si no cualificado → nurture automático (emails de seguimiento)
    → Si indeciso → follow-up programado en 3-7 días
```

### La ventaja del approach híbrido en sales

| Capa | Función en sales |
|------|-----------------|
| **[Agéntica](../tecnologia/agentic-ai.md)** | Conversación natural con el prospect, entiende objeciones, adapta pitch |
| **[Determinista](../tecnologia/agentic-ai.md)** | ICP scoring con criterios exactos, pricing floors en negociación, CRM updates |

---

## Oportunidad en España

### Sales AI en el contexto español

| Factor | Detalle |
|--------|---------|
| **Cultura de venta relacional** | En España, las ventas B2B se cierran con relación personal. AI no reemplaza al AE, le libera tiempo para las reuniones que importan |
| **Volumen de prospección** | 160K+ empresas logísticas = base enorme para prospección outbound |
| **Bajo coste de AE en España** | Enterprise AE en España: EUR 135-147K OTE vs $250-400K en SF. El ahorro permite invertir más en pipeline |
| **Robinson List** | Outbound marketing calls requieren verificar Lista Robinson. AI puede automatizar la verificación |

### Restricciones regulatorias para outbound en España

| Regulación | Impacto | Mitigación |
|-----------|---------|-----------|
| **[GDPR](../regulacion/gdpr-lopdgdd.md)** | Base legal necesaria para contactar (interés legítimo o consentimiento) | Documentar base legal por campaña |
| **Lista Robinson** | Verificar antes de llamadas comerciales | Automatizar verificación en workflow determinista |
| **ePrivacy Directive** | Llamadas comerciales automáticas sin consentimiento previo = ilegales en España | Solo usar para inbound, o con base legal explícita para outbound |
| **[EU AI Act](../regulacion/eu-ai-act.md) Art. 50** | Disclosure de AI | Anuncio al inicio de cada interacción |

!!! warning "Outbound frío con AI en España"
    Llamadas comerciales automatizadas sin consentimiento previo son ilegales en la UE. Esto limita el use case de outbound puro a frío. Alternativas: inbound (sin restricción), outbound con consentimiento previo (opt-in), o follow-up de leads que ya han mostrado interés (base legal de interés legítimo).

### Modelo para España: inbound-first

Dado el contexto regulatorio, el enfoque óptimo para sales AI en España es:

1. **Inbound qualification** — Sin restricción regulatoria, volumen alto, ROI inmediato
2. **Follow-up de leads warm** — Leads de eventos, website, referrals
3. **Outbound con base legal** — Carriers que ya son partners (carrier sales), clientes existentes (upsell)
4. **Carrier sales** — Carriers llaman buscando carga = inbound, sin restricción

---

## Relevancia para la entrevista

### Carrier sales: la joya oculta

El use case de carrier sales es especialmente relevante para España porque:

- Es **inbound** (carriers llaman buscando carga) → sin restricción regulatoria
- Es **alto volumen** en un mercado atomizado (160K+ empresas)
- Tiene **métricas probadas** (Circle: 5x ROI, 10% mejores márgenes, 25% más freight/rep)
- Demuestra **revenue generation** directa, no solo reducción de costes

### Dato para memorizar

- **19-20x ROI** en outbound sales
- **70% reducción** en cost per lead
- **25% más freight** por rep (carrier sales)

---

*Fuentes: [HR-SERIEB] GlobeNewswire, [HR-CIRCLE] case study Circle Logistics, [HR-WEB] happyrobot.ai, [HR-REVENUE] happyrobot.ai/blog/generating-new-revenue-streams*
