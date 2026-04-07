---
title: "Collections"
type: caso-de-uso
status: completo
tags: [caso-de-uso, collections, cobros, finance, roi]
updated: 2026-04-07
---

# Collections (Cobros)

Use case con el **ROI más impactante** de [HappyRobot](../empresa/happyrobot.md): más de 100x retorno sobre inversión en cobros automatizados.

---

## Métricas publicadas

| Métrica | Valor | Conf | Fuente |
|---------|-------|------|--------|
| ROI (cash collected vs cost to collect) | **>100x** (119x en materiales de Serie A, >100x en Serie B) | A | HR-SERIEB, HR-SERIEA |
| [Circle Logistics](../clientes/circle-logistics.md) ROI total | **5x+** (across all use cases) | A | HR-CIRCLE |

---

## Descripción

Gestión automatizada de cobros: el AI Worker llama a clientes/carriers con facturas pendientes, negocia plazos de pago, envía recordatorios por email/SMS, escala a humanos cuando es necesario, y actualiza los sistemas financieros del cliente.

### Cómo funciona

| Paso | Acción | Canal |
|------|--------|-------|
| 1. Trigger | Factura vence o alcanza umbral de días pendientes | Sistema financiero/ERP |
| 2. Primer contacto | AI Worker llama al deudor — identifica, verifica, pregunta por el pago | Teléfono |
| 3. Negociación | Si el deudor necesita plazo → negocia plan de pago dentro de guidelines [deterministas](../tecnologia/agentic-ai.md) | Teléfono |
| 4. Confirmación | Envía confirmación del acuerdo por email/SMS | Email + SMS |
| 5. Follow-up | Recordatorios automáticos según calendario acordado | Multi-canal |
| 6. Escalación | Si no hay contacto o acuerdo → escala a equipo humano de collections con contexto completo | Interno |

### Por qué el ROI es tan alto

| Factor | Explicación |
|--------|------------|
| **Cost to collect es muy bajo** | Una llamada AI cuesta centavos vs un humano que dedica 5-15 min por llamada |
| **Cash collected es sustancial** | Cada factura cobrada puede ser miles o decenas de miles de dólares |
| **Velocidad** | AI contacta inmediatamente al vencimiento, no espera a que un humano tenga tiempo |
| **Persistencia** | AI puede hacer 10 intentos de contacto sin coste marginal — humanos abandonan después de 2-3 |
| **24/7** | Contactar fuera de horario laboral (momentos donde el deudor tiene más disponibilidad) |
| **Sin vergüenza** | AI no se incomoda pidiendo dinero — consistente, profesional, sin emociones negativas |

### La capa híbrida en collections

| Capa | Función |
|------|---------|
| **[Agéntica](../tecnologia/agentic-ai.md)** | Entiende circunstancias del deudor, responde con empatía, adapta tono según la situación |
| **[Determinista](../tecnologia/agentic-ai.md)** | Asegura que planes de pago cumplan guidelines financieros, disclosures legales se entreguen verbatim, datos se registren correctamente |

---

## Oportunidad en España

### Cultura de pagos en España

| Dato | Valor | Fuente |
|------|-------|--------|
| Plazo medio de pago B2B (España) | **~80 días** (vs 60 días media EU) | Intrum European Payment Report |
| Empresas que pagan tarde | **~60%** sufren impacto por pagos tardíos | Intrum |
| Coste de morosidad para PYMEs | Causa principal de cierre de empresas | Cámaras de Comercio |
| Ley contra morosidad comercial | Plazo máximo legal 60 días (frecuentemente incumplido) | Ley 15/2010 |
| Sector logístico | Márgenes del 2-5% en transporte → morosidad = crisis de cash flow | Sector data |

### Por qué collections es perfecto para España

1. **Cultura de pago lento** — 80 días promedio vs 60 EU. Hay más que cobrar y más necesidad de cobrarlo.
2. **Atomización del sector** — 160K+ empresas logísticas, muchas pequeñas, muchas con cash flow ajustado.
3. **Márgenes bajos** — En transporte, márgenes del 2-5%. Cada factura cobrada antes = diferencia entre sobrevivir y cerrar.
4. **ROI fácil de demostrar** — "Invertimos X, cobramos 100X." Es el pitch más directo posible.
5. **No requiere cambio cultural** — No le pides al cliente que cambie procesos. Le pides que cobre lo que ya le deben.

### Restricciones regulatorias

| Regulación | Implicación | Mitigación |
|-----------|------------|-----------|
| **[GDPR](../regulacion/gdpr-lopdgdd.md)** | Datos de deudores = datos personales | Data residency EU, retención configurable |
| **Lista Robinson** | No aplica (collections no es marketing, es cobro de deuda existente) | Verificar caso por caso |
| **LPDP (cobros)** | Regulación de prácticas de cobro — no se puede acosar | Capa determinista con límites de contacto hard-coded |
| **[EU AI Act](../regulacion/eu-ai-act.md) Art. 50** | Disclosure de AI en la llamada | "Está hablando con un asistente de IA" al inicio |
| **Art. 22 GDPR** | Derecho a intervención humana en decisiones automatizadas | Ruta de escalación a humano siempre disponible |

---

## Modelo de ROI para España

### Ejemplo: operador logístico mediano

| Variable | Valor |
|----------|-------|
| Facturas pendientes mensuales | 500 |
| Valor promedio factura | EUR 2,000 |
| Tasa de cobro actual (manual) | 70% |
| Tasa de cobro con AI (estimada) | 85% |
| Incremento de cobro | 15% × 500 × EUR 2,000 = **EUR 150,000/mes** |
| Coste del servicio AI | ~EUR 1,000-3,000/mes (estimado) |
| **ROI** | **50-150x** |

!!! note "Estimación"
    Este modelo es una estimación basada en las métricas de HappyRobot en EEUU (>100x ROI) aplicadas a un escenario español. Los números reales dependerán del volumen, valor de facturas, y tasa de cobro actual del cliente específico.

---

## Competencia en collections AI en España

| Proveedor | Oferta | Gap vs HappyRobot |
|-----------|--------|-------------------|
| **Despachos de cobros tradicionales** | Gestión manual + llamadas | Caros (comisión 10-20%), lentos, inconsistentes |
| **Plataformas de gestión de cobros** (EOS, Intrum) | Software + equipo humano | Sin AI agents, sin automatización de llamadas |
| **AI genérica** | Chatbots para cobros | Sin voz, sin governance, sin vertical depth |

**No hay competencia de AI voice agents para collections en España.** Es mercado completamente greenfield.

---

## Para la entrevista

### Dato clave

**>100x ROI** es la métrica más impactante de todo el portfolio de HappyRobot. Si Lola solo puede mencionar un número, debería ser este.

### Talking point

> "Collections es probablemente el quick win más potente para el mercado español. España tiene una cultura de pago lento — 80 días promedio vs 60 en Europa. El ROI de HappyRobot en collections es más de 100x en EEUU. En un mercado donde los márgenes de transporte son del 2-5%, cobrar tus facturas 15% más rápido puede ser la diferencia entre crecer y cerrar."

---

*Fuentes: [HR-SERIEB] GlobeNewswire Serie B, [HR-SERIEA] Serie A PR, [HR-CIRCLE] case study Circle Logistics, [HR-FINANCE] happyrobot.ai/blog/finance-automation, Intrum European Payment Report*
