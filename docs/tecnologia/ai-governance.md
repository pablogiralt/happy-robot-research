---
title: "AI Governance"
type: tecnologia
status: completo
tags: [tecnologia, governance, compliance, observability, auditor, eu-ai-act]
updated: 2026-04-07
---

# AI Governance & Observabilidad

## Por qué importa

En enterprise AI, la capacidad de **auditar, explicar y controlar** cada decisión del sistema es tan importante como la capacidad del sistema de funcionar bien. Los CIOs y compliance officers no compran AI que no pueden supervisar. El governance de [HappyRobot](../empresa/happyrobot.md) es un diferenciador competitivo y, con el [EU AI Act](../regulacion/eu-ai-act.md) exigible desde agosto 2026, una obligación regulatoria.

---

## Governance en HappyRobot — AI Auditor

### Arquitectura del AI Auditor

Sistema avanzado de auditoría que combina tres capas [A: HR-TECH]:

| Capa | Función | Ejemplo |
|------|---------|---------|
| **Large Language Models (LLMs)** | Análisis contextual de interacciones | "¿El agente respondió correctamente a la objeción del cliente?" |
| **Classical ML** | Detección de patrones y anomalías | Detectar drift en calidad de respuestas over time |
| **Rule-based algorithms** | Compliance checks hard-coded | "¿Se entregó el disclosure legal verbatim?" |

### "Who validates the validators?"

HappyRobot mide el **agreement entre AI auditors y auditoría humana** por tipo de interacción, asegurando high F-scores a través de balanced precision y recall [A: HR-TECH]. Es decir, el auditor AI se calibra contra criterio humano — no es una caja negra.

### Métricas del Post-Call Auditor

| Categoría | Qué mide | Por qué importa |
|-----------|----------|-----------------|
| **Voice Experience** | Interrupciones, latencia, precisión de transcripción | Calidad de la experiencia del usuario final |
| **Engagement** | Escalaciones, sentimiento, turn-taking ratios | Si la conversación fluye o el usuario se frustra |
| **Data Accuracy** | Tool selection, retry logic, datos correctos | Si el agente ejecutó la acción correcta en el sistema correcto |
| **Business Outcomes** | Duración de llamada, resolution rate, conversion rates | ROI medible para el cliente |

---

## Capacidades clave

| Capacidad | Detalle |
|-----------|---------|
| **Visibilidad total** | Cada interacción registrada con decisiones, acciones, y resultados |
| **Testing continuo** | Evaluación automática de performance en producción |
| **Refinamiento proactivo** | El sistema identifica áreas de mejora antes de que el cliente las reporte |
| **Flags de excepciones** | Alertas automáticas cuando algo sale de parámetros |
| **Observable & explainable** | Cada decisión del agente es auditable en detalle |
| **Call classifications** | Categorización automática de interacciones para entrenar en edge cases |

---

## Compliance — Certificaciones y frameworks

| Framework | Status | Relevancia |
|-----------|--------|-----------|
| **SOC 2** | Certificado | Estándar US para seguridad de datos — requerido por enterprise |
| **GDPR** | Compliant | Obligatorio para operar en EU — protección de datos personales |
| **HIPAA** | Compliant | Healthcare US — señal de madurez enterprise |
| **[EU AI Act](../regulacion/eu-ai-act.md)** | Compliant | Regulación AI más exigente del mundo — Art. 50 transparencia exigible ago 2026 |
| **NIST CSF** | Aligned | Framework US de ciberseguridad |
| **DORA** | Compliant | Resiliencia digital sector financiero EU |

### Seguridad técnica

| Componente | Implementación |
|------------|----------------|
| **TLS 1.3** | En todos los public edges (REST, webhooks, SIP-TLS) |
| **SSO** | OAuth-based, MFA, fine-grained RBAC |
| **SRTP** | End-to-end para voice media |
| **Threat detection** | Anomaly alerts, policy audits, incident-response SOC-2 aligned |
| **SRE 24x7** | Métricas, logs, traces agregados y monitorizados |
| **Data sovereignty** | Routing por tenant para compliance con residencia de datos |

---

## Ventaja competitiva

### vs Competidores

| Competidor | Governance | Gap vs HappyRobot |
|------------|-----------|-------------------|
| [Bland AI](../competidores/bland-ai.md) | Básico (logs, analytics) | Sin AI Auditor, sin compliance EU |
| [Synthflow](../competidores/synthflow.md) | Básico (SOC2, GDPR, HIPAA) | Sin auditoría multi-capa |
| [Retell AI](../competidores/retell-ai.md) | Mínimo | Sin framework governance enterprise |
| [Vapi](../competidores/vapi.md) | Developer-focused, limitado | Sin enterprise compliance |
| [Sierra AI](../competidores/sierra-ai.md) | Enterprise-grade | Competidor directo en governance, pero sin FDE ni vertical depth multi-sector |
| [Parloa](../competidores/parloa.md) | Enterprise-grade (ISO 27001) | Competidor fuerte — ISO 27001 que HappyRobot no tiene |

### Governance como argumento de venta

| Contexto | Cómo usarlo |
|----------|------------|
| **Ventas enterprise** | "Cada decisión de nuestros AI Workers es auditable. Tu equipo de compliance puede revisar cualquier interacción" |
| **Regulación EU AI Act** | "Ya cumplimos Art. 50 antes de que sea obligatorio. Tu empresa no tiene riesgo regulatorio con nosotros" |
| **Diferenciación vs chatbots** | "No es un chatbot que no puedes controlar. Es un sistema con governance enterprise que auditamos continuamente" |
| **POC evaluation** | "Después del pilot, te damos un report detallado con métricas de cada interacción — voz, engagement, precisión, outcomes" |

---

## Alineamiento con regulación española

### Guía AEPD de IA agéntica (febrero 2026)

La AEPD publicó la primera guía regulatoria mundial sobre IA agéntica. Las recomendaciones **mapean directamente** a las capacidades de HappyRobot [A: AEPD-AGENTIC]:

| Recomendación AEPD | Capacidad HappyRobot |
|--------------------|--------------------|
| Framework cross-funcional de governance | AI Auditor con capas LLM + ML + rules |
| DPIA obligatoria para IA agéntica | Audit logs detallados que facilitan la DPIA del deployer |
| Transparencia — actualizar avisos de privacidad | Mecanismos de disclosure en todos los canales |
| Minimización — política "need to know" | Configuración de acceso granular por AI Worker |
| Memoria — separar operativa de gestión | Shared Context & Memory con perfiles acumulativos [B] |
| Supervisión humana configurable | Escalación inteligente configurable por use case |
| Pasos hardcoded para seguridad | Capa determinista con guardrails = [approach híbrido](agentic-ai.md) |

### Advertencia "BYOAgentic"

La AEPD advierte contra workflows de IA agéntica construidos fuera de governance corporativa. Esto **valida** el modelo HappyRobot de plataforma centralizada vs fragmentación de tools.

---

## Information gaps

| Área | Status |
|------|--------|
| ISO 27001 | No mencionado — [Parloa](../competidores/parloa.md) lo tiene, sería ventaja obtenerlo |
| SOC 2 Type I vs Type II | No especificado públicamente |
| Detalles de data sovereignty EU | "Routing por tenant" confirmado, pero arquitectura exacta no divulgada |
| Programa de sandbox AESIA | No hay evidencia de participación |

---

## Para la entrevista

### Número clave

**6 certificaciones/frameworks:** SOC 2 + GDPR + HIPAA + EU AI Act + NIST CSF + DORA. Ningún competidor voice AI tiene tantos.

### Talking point

> "El governance de HappyRobot no es solo compliance — es argumento de venta. En España, con el EU AI Act exigible desde agosto 2026 y la AEPD publicando guías específicas de IA agéntica, ser el proveedor que ya cumple es una ventaja enorme. Los CIOs españoles van a preguntar '¿cumplís EU AI Act?' antes de firmar. Nosotros decimos sí — Sierra, Parloa, tal vez también. Bland, Vapi, Retell, no."

---

*Fuentes: [HR-TECH] happyrobot.ai/blog/technical-overview, [HR-PROD] happyrobot.ai, [AEPD-AGENTIC] aepd.es/guides/agentic-artificial-intelligence.pdf, [EUAI-ART50] artificialintelligenceact.eu/article/50/*
