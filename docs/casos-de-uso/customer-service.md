---
title: "Customer Service"
type: caso-de-uso
status: completo
tags: [caso-de-uso, customer-service, soporte, contact-center, multi-canal]
updated: 2026-04-07
---

# Customer Service

## Métricas publicadas

| Métrica | Valor | Conf | Fuente |
|---------|-------|------|--------|
| Response rate | **100%** | B | HR-WEB |
| First Response Time | **0 min** | B | HR-WEB |
| Handled autonomously | **50%+** | B | HR-WEB |
| [DHL](../clientes/dhl.md) emails procesados | Cientos de miles/año | A | HR-DHL |
| [DHL](../clientes/dhl.md) voice minutes | Millones/año | A | HR-DHL |
| [Circle](../clientes/circle-logistics.md) call answer rate | 100%, 24/7, zero hold time | A | HR-CIRCLE |

---

## Descripción

Soporte al cliente 24/7 multi-canal: [voice AI](../tecnologia/voice-ai.md), email, web chat, SMS, WhatsApp. Los AI Workers de [HappyRobot](../empresa/happyrobot.md) gestionan el volumen masivo de interacciones repetitivas (tracking, scheduling, confirmaciones) y escalan a humanos solo las excepciones que requieren juicio.

### Cómo funciona

| Paso | Acción | Canal |
|------|--------|-------|
| 1. Recepción | AI Worker recibe la interacción (llamada, email, chat) | Multi-canal |
| 2. Clasificación | Identifica tipo de consulta, urgencia, contexto del cliente | Interno |
| 3. Resolución autónoma | Si está dentro de scope → resuelve directamente (consulta tracking, confirmación, FAQ) | Multi-canal |
| 4. Escalación inteligente | Si requiere juicio humano → escala con contexto completo al agente correcto | Interno |
| 5. Follow-up | Confirma resolución con cliente, actualiza sistemas | Multi-canal |

### Tipos de interacciones

| Tipo | Volumen | Complejidad | Autonomía AI |
|------|---------|-------------|-------------|
| Consultas de tracking | Muy alto | Baja | >90% autónomo |
| Confirmaciones de cita/entrega | Alto | Baja-media | >80% autónomo |
| Cambios de scheduling | Alto | Media | 60-80% autónomo |
| Reclamaciones/quejas | Medio | Alta | Escalación con contexto |
| Problemas técnicos/excepciones | Bajo | Alta | Escalación a humano |

---

## Diferenciación vs contact center tradicional

| Dimensión | Contact center tradicional | HappyRobot AI Workers |
|-----------|--------------------------|----------------------|
| **Disponibilidad** | 8-12h/día, L-V (o turnos caros 24/7) | 24/7/365, sin coste incremental |
| **Tiempo de respuesta** | 2-10 min espera promedio | 0 min — respuesta instantánea |
| **Consistencia** | Variable (depende del agente) | 100% consistente |
| **Escala** | Lineal (más volumen = más agentes) | Non-linear (más volumen = mismo coste) |
| **Idiomas** | Requiere contratar por idioma | 15+ idiomas simultáneos |
| **Multicanal** | Silos por canal (equipo teléfono ≠ equipo email) | Un AI Worker gestiona todos los canales |
| **Data capture** | Manual, inconsistente | Automático, estructurado, 100% de interacciones |
| **Coste por interacción** | EUR 3-8 por llamada | Fracción del coste |

### Diferenciación vs chatbots

| Chatbot tradicional | HappyRobot |
|--------------------|-----------|
| Decision trees rígidos | [Razonamiento agéntico](../tecnologia/agentic-ai.md) — entiende contexto |
| "No he entendido su consulta" | Maneja desvíos, preguntas inesperadas |
| Solo texto | Multi-canal (voz + email + chat + SMS + WhatsApp) |
| Información genérica | Integrado con TMS, ERP, datos en tiempo real |
| Sin memoria | Shared context — recuerda interacciones previas |

---

## Caso DHL Supply Chain

El deployment de customer service en [DHL](../clientes/dhl.md) es el más grande de HappyRobot [A: HR-DHL]:

| Dato | Valor |
|------|-------|
| **Canales** | Teléfono, email, SMS, WhatsApp |
| **Volumen email** | Cientos de miles/año |
| **Volumen voz** | Millones de minutos/año |
| **Use cases** | Transport status calls, routine email communications, appointment scheduling, driver follow-up, warehouse coordination |
| **Validación** | 18 meses de validación antes de deployment global |

> **Sally Miller, CIO DHL Supply Chain:** *"By taking over repetitive tasks, AI gives our people the space to focus on higher-value work."*

---

## Oportunidad en España

### Sector contact centers en España

| Dato | Valor |
|------|-------|
| España como hub de contact centers | Hub para EMEA por idioma + costes + timezone |
| Tamaño del sector | ~EUR 5B revenue, 90,000+ empleados directos |
| Empresas target | Operadores logísticos, e-commerce, utilities, telecoms |
| Presión de costes | Salarios subiendo, márgenes bajando — AI como alternativa |

### Pain points en customer service logístico español

| Pain point | Detalle | Métrica HappyRobot aplicable |
|------------|---------|----------------------------|
| **"¿Dónde está mi paquete?"** | Consulta #1 en paquetería y e-commerce logistics | 100% response rate, 0 min FRT |
| **Entregas fallidas** | 10-15% de entregas B2C fallan en primera entrega | AI para re-scheduling automático |
| **Horarios limitados** | Customer service 8-18h en la mayoría de operadores | 24/7 sin coste adicional |
| **Multilingüe** | Turistas, exportadores, operadores cross-border | 15+ idiomas nativos |
| **Picos estacionales** | Black Friday, Navidad, rebajas — volumen 3-5x | Escalado instantáneo sin contratar |

### Competencia local en customer service AI

| Proveedor | Oferta | Gap vs HappyRobot |
|-----------|--------|-------------------|
| **Aunoa** | Chatbots AI (ya en GLS Spain) | Solo texto, sin voz, sin integración logistics |
| **CallBotIA** | VoiceBots, ChatBots, WhatsApp Bots | Español market, pero sin agentic reasoning ni governance |
| **Vocalcom** | Contact center AI | Horizontal, sin vertical logistics |

**Conclusión:** No hay competencia de AI agents multi-canal en customer service logístico en España. Es mercado greenfield.

---

## Para la entrevista

### Dato clave

Customer service es el use case de **mayor volumen** pero no necesariamente el de mayor ROI. Para primeros POCs en España, [scheduling](logistics-operations.md) o [collections](collections.md) son mejores quick wins. Customer service es ideal como **segundo use case** una vez establecida la relación.

### Métrica para memorizar

- **100% response rate, 0 min FRT, 50%+ autónomo** — la frase completa para cualquier pregunta sobre customer service

---

*Fuentes: [HR-WEB] happyrobot.ai, [HR-DHL] group.dhl.com press release, [HR-CIRCLE] happyrobot.ai/blog/circle-logistics-case-study, [AUNOA-LOG] aunoa.ai*
