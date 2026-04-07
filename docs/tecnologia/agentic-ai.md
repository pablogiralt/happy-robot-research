---
title: "Agentic AI"
type: tecnologia
status: completo
tags: [tecnologia, agentic-ai, deterministic, hybrid, enterprise]
updated: 2026-04-07
---

# Agentic AI vs Deterministic — El Approach Híbrido

## Concepto

El debate central en AI enterprise es: **¿agentes inteligentes que razonan (agentic) o sistemas predecibles que ejecutan reglas (deterministic)?** La respuesta de [HappyRobot](../empresa/happyrobot.md) es que las empresas necesitan **ambos** — combinados en una arquitectura híbrida que es su diferenciador técnico principal [A: HR-HYBRID].

> *"For AI to be useful at scale, it must be as reliable as a script and as capable as a human."* — HappyRobot blog, marzo 2026

---

## El approach de HappyRobot

### Capa agéntica

| Aspecto | Detalle |
|---------|---------|
| **Propósito** | Manejo de interacción humana, comprensión contextual, adaptación |
| **Cómo funciona** | Razonamiento dinámico para navegar conversaciones impredecibles |
| **Ejemplo** | Si un cliente menciona un problema secundario durante una llamada de scheduling, el agente lo procesa, ajusta su ruta, y regresa al objetivo |
| **Fortaleza** | Flexibilidad ante lo inesperado — los humanos no siguen scripts |
| **Debilidad sin capa determinista** | Outputs impredecibles, riesgo de hallucinations, problemas de compliance |

### Capa determinista

| Aspecto | Detalle |
|---------|---------|
| **Propósito** | Cumplimiento de reglas de negocio, integridad de datos, compliance |
| **Cómo funciona** | Guardrails, API calls estructurados, validación, conditional branches (if-then) |
| **Ejemplo** | Cuando un AI Worker actualiza un shipment status en un ERP, sigue exactamente las reglas del cliente |
| **Fortaleza** | Predecibilidad, auditabilidad, zero tolerance para errores en operaciones críticas |
| **Debilidad sin capa agéntica** | Falla cuando el humano se desvía del script — rigidez tipo RPA |

### Ejemplo real: llamada de collections

| Capa | Función en la misma llamada |
|------|---------------------------|
| **Agéntica** | Entiende las circunstancias del deudor, responde con empatía apropiada, adapta el tono |
| **Determinista** | Asegura que los planes de pago cumplan guidelines financieros y que disclosures legales se entreguen verbatim |

---

## Por qué importa para enterprise

### El problema con approaches puros

| Approach | Problema para enterprise | Consecuencia |
|----------|------------------------|-------------|
| **Pure LLM agents** | Outputs impredecibles en contextos regulados | Riesgo de compliance, datos incorrectos en ERP, disclosures legales omitidos |
| **Pure RPA / scripts** | Falla cuando el humano se desvía del flujo esperado | Experiencia frustrante, escalaciones constantes, abandono |
| **Chatbots tradicionales** | Decision trees rígidos, no entienden contexto | "Lo siento, no he entendido su consulta" en loop |

### La ventaja del híbrido

| Dimensión | Beneficio |
|-----------|----------|
| **Auditabilidad** | Cada decisión agéntica queda registrada + las acciones deterministas son trazables |
| **Compliance** | La capa determinista garantiza cumplimiento regulatorio ([EU AI Act](../regulacion/eu-ai-act.md), [GDPR](../regulacion/gdpr-lopdgdd.md)) |
| **Escalabilidad** | La capa agéntica maneja edge cases sin necesidad de programar cada escenario |
| **Confianza enterprise** | Los CIOs confían más en un sistema que tiene guardrails que en un "AI que piensa solo" |

---

## Posición en el mercado

### Cómo se posicionan los competidores

| Competidor | Approach | Limitación |
|------------|----------|-----------|
| [Bland AI](../competidores/bland-ai.md) | Flow-based (más determinista) | Menos flexible para conversaciones complejas |
| [Synthflow](../competidores/synthflow.md) | No-code visual builder (determinista) | Visual builder = scripts visuales, poca agilidad agéntica |
| [Retell AI](../competidores/retell-ai.md) | API-first, LLM-driven | Más agéntico pero menos governance |
| [Sierra AI](../competidores/sierra-ai.md) | Agentic enterprise | Fuerte en razonamiento, sin vertical depth en operaciones complejas |
| [Parloa](../competidores/parloa.md) | Agentic enterprise (contact center) | Similar en approach, pero sin modelo FDE ni vertical depth multi-sector |
| **HappyRobot** | **Hybrid agentic + deterministic** | **Único en combinar ambos con governance + FDE + vertical depth (logistics beachhead → multi-vertical)** |

### Tendencia del mercado 2025-2026

La industria está convergiendo hacia el approach híbrido:

1. **OpenAI y Anthropic** están añadiendo tool use y function calling a sus modelos — básicamente, capa determinista
2. **Salesforce Agentforce** combina reasoning con business rules
3. **Microsoft Copilot Studio** mezcla flujos deterministas con generación agéntica
4. **La AEPD española** en su guía de IA agéntica (feb 2026) recomienda explícitamente "pasos hardcoded para seguridad" dentro de workflows agénticos — validando el approach de HappyRobot

---

## Relevancia para la entrevista

### Datos clave para Lola

| Punto | Cómo usarlo |
|-------|------------|
| **HappyRobot no es "otro chatbot"** | El approach híbrido es la respuesta a Q13 ("diferenciación vs another chatbot") |
| **AEPD valida el approach** | Guía de feb 2026 recomienda pasos deterministas dentro de flujos agénticos |
| **95%+ pilot→contrato** | La combinación híbrido + [FDE](forward-deployed.md) produce esta tasa de conversión |
| **10% mejor margen en negociación** | La capa agéntica negocia como humano + la determinista aplica floor pricing |

### Talking point para Aquilino

> "Lo que diferencia a HappyRobot técnicamente es la arquitectura híbrida. La capa agéntica maneja la conversación como un humano — entiende contexto, adapta tono, gestiona imprevistos. La capa determinista garantiza que cada acción cumple las reglas del cliente — pricing floors, disclosures legales, updates de ERP. Es la combinación la que produce el 95% de conversión de pilot a contrato."

---

*Fuentes: [HR-HYBRID] happyrobot.ai/blog/the-agentic-and-deterministic-hybrid-enterprises-need, [HR-BUILD] happyrobot.ai/build, [AEPD-AGENTIC] aepd.es/guides/agentic-artificial-intelligence.pdf*
