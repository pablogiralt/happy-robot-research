---
title: "EU AI Act"
type: regulacion
status: completo
tags: [regulacion, eu-ai-act, europa, compliance, transparencia, voice-ai]
updated: 2026-04-07
---

# EU AI Act

Reglamento (UE) 2024/1689 — el primer marco jurídico integral para regular la inteligencia artificial en el mundo. Impacto directo en la operación de [HappyRobot](../empresa/happyrobot.md) en Europa y España.

---

## 1. Clasificación de riesgo para HappyRobot

La clasificación depende del **caso de uso y contexto**, no de la tecnología subyacente. El producto core de HappyRobot es de riesgo limitado, pero despliegues específicos de los clientes (deployers) pueden escalar a alto riesgo.

| Sistema AI | Clasificación | Fundamento | Conf. |
|---|---|---|---|
| Voice AI agents (llamadas telefónicas) | **Riesgo limitado** | Interacción directa con personas naturales — Art. 50 | A |
| Chat agents (web chat) | **Riesgo limitado** | Misma razón: interacción directa | A |
| Email agents | **Riesgo limitado** | Genera contenido textual sintético | A |
| Agentes para decisiones de empleo | **Potencialmente alto riesgo** | Recruiting/HR — Anexo III, área 4 (empleo) | A |
| Agentes para cobros/crédito | **Potencialmente alto riesgo** | Evaluación de solvencia — Anexo III, área 5b | A |

**Fuentes:** [EUAI-SUMMARY] [EU AI Act Risk Classification](https://artificialintelligenceact.eu/high-level-summary/), [EUAI-ANNEX3] [Anexo III](https://artificialintelligenceact.eu/annex/3/). Confianza A.

---

## 2. Requisitos de transparencia (Artículo 50) — CRITICO

Aplicable desde el **2 de agosto de 2026**. Es la obligación más relevante para HappyRobot.

### Para proveedores (HappyRobot como constructor de la plataforma)

1. **Divulgación de interacción con AI:** Los sistemas deben informar a las personas de que interactúan con IA, "salvo que sea evidente desde el punto de vista de una persona razonablemente bien informada, observadora y perspicaz."
2. **Marcado de contenido sintético:** Los outputs de audio, imagen, vídeo o texto deben marcarse en **formato legible por máquina** (watermarking, metadatos).
3. **Etiquetado de voz sintética:** Las voces generadas por IA deben identificarse como sintéticas en metadatos e interfaces de usuario.

### Para deployers (clientes enterprise de HappyRobot)

1. **Divulgación al usuario final** de que interactúa con IA.
2. **Divulgación de deep fakes** para audio/vídeo manipulado.
3. **Divulgación de reconocimiento emocional** si se usa.

### Implementación práctica para voice AI

Para canal telefónico, el interlocutor no puede leer texto, por lo que se necesita **anuncio verbal explícito al inicio de la conversación**:

> *"Estás hablando con un asistente de inteligencia artificial. Di 'agente' en cualquier momento para hablar con una persona."*

**Fuentes:** [EUAI-ART50] [Artículo 50](https://artificialintelligenceact.eu/article/50/), [TELNYX-EUAI] [Telnyx EU AI Act Voice AI Guide](https://telnyx.com/resources/eu-ai-act). Confianza A.

---

## 3. Timeline de implementación

| Fecha | Hito | Relevancia para HappyRobot |
|---|---|---|
| **2 feb 2025** | Prácticas prohibidas en vigor | Ya en efecto. Sin IA manipulativa, social scoring, ni reconocimiento emocional en trabajo. |
| **2 ago 2025** | Reglas GPAI; autoridades nacionales designadas | España debe tener AESIA plenamente operativa. |
| **2 feb 2026** | Directrices de Comisión sobre Art. 6 | Clarificación de límites de alto riesgo. |
| **2 ago 2026** | **FECHA PRINCIPAL DE APLICACIÓN**: Reglas Anexo III, transparencia (Art. 50), sandboxes | **Deadline crítico de HappyRobot.** Todas las obligaciones de transparencia para voice/chat son exigibles. Multas posibles. |
| **2 ago 2027** | IA de alto riesgo en productos regulados (Anexo I) | Menos relevante salvo que HappyRobot se embeba en dispositivos médicos. |

**Fuentes:** [EUAI-TIMELINE] [Timeline](https://artificialintelligenceact.eu/implementation-timeline/), [EUAI-SERVICEDESK] [AI Act Service Desk](https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act). Confianza A.

---

## 4. Régimen sancionador (Artículo 99)

| Nivel | Infracción | Sanción máxima |
|---|---|---|
| **Nivel 1** (máximo) | Prácticas prohibidas (Art. 5) | EUR 35M o **7% facturación global anual** |
| **Nivel 2** | Requisitos de alto riesgo y transparencia | EUR 15M o **3% facturación global anual** |
| **Nivel 3** (mínimo) | Información incorrecta/engañosa a autoridades | EUR 7,5M o **1% facturación global anual** |

Para PYMES se aplica la cifra menor de las dos opciones (absoluta vs. porcentaje).

**Fuentes:** [EUAI-ART99] [Artículo 99](https://artificialintelligenceact.eu/article/99/), [HOLISTIC-PENALTIES] [Holistic AI Penalties Analysis](https://www.holisticai.com/blog/penalties-of-the-eu-ai-act). Confianza A.

---

## 5. Distinción Provider vs. Deployer

HappyRobot ocupa **ambos roles** según el contexto:

| Rol | Quién | Obligaciones clave |
|---|---|---|
| **Provider** | HappyRobot (constructor de la plataforma) | Diseñar sistemas que permitan divulgaciones de transparencia, marcar contenido sintético, documentación técnica, evaluación de conformidad (para alto riesgo) |
| **Deployer** | Clientes enterprise ([DHL](../clientes/dhl.md), [Circle Logistics](../clientes/circle-logistics.md), etc.) | Informar realmente a usuarios finales, realizar DPIAs específicas del dominio, garantizar supervisión humana |

**Implicación clave:** HappyRobot debe incorporar compliance tooling en la plataforma (mecanismos de divulgación, audit logs, rutas de escalado humano) para que los deployers puedan cumplir sus obligaciones. Esto es tanto un requisito regulatorio como un **diferenciador competitivo**.

**Fuente:** [AOS-LIMITED] [A&O Shearman: Limited Risk Obligations](https://www.aoshearman.com/en/insights/ao-shearman-on-tech/zooming-in-on-ai-11-eu-ai-act-what-are-the-obligations-for-the-limited-risk-ai-systems). Confianza A.

---

## 6. Prácticas prohibidas (Art. 5 — en vigor desde feb 2025)

Lo que HappyRobot **NO puede hacer**:

- IA que use técnicas subliminales, manipulativas o engañosas para distorsionar comportamiento
- Explotación de vulnerabilidades de grupos específicos (edad, discapacidad, situación socioeconómica)
- Social scoring
- **Reconocimiento emocional en entornos laborales o educativos** (relevante: HappyRobot no puede ofrecer análisis emocional para QA de empleados en la UE)
- Identificación biométrica remota en tiempo real en espacios públicos (con excepciones limitadas)

**Fuente:** [EUAI-SUMMARY]. Confianza A.

---

## 7. Implementación nacional en España

### Arquitectura supervisora

| Autoridad | Rol |
|---|---|
| **AESIA** (Agencia Española de Supervisión de la Inteligencia Artificial) | Autoridad principal de supervisión del AI Act. Operativa desde **junio 2024**. España fue el **primer estado miembro de la UE** en crear una agencia dedicada a supervisión de IA. |
| **AEPD** | Competencia en temas biométricos y protección de datos relacionados con IA |
| **Autoridades sectoriales** | CNMV (mercados), Banco de España (banca), DGSFP (seguros), CGPJ (justicia) — supervisión sectorial |

### Legislación nacional

El **11 de marzo de 2025**, el gobierno aprobó la primera lectura del *Anteproyecto de Ley para el buen uso y la gobernanza de la Inteligencia Artificial* — transpone el EU AI Act a derecho español:

- Prácticas prohibidas alineadas con EU AI Act
- Obligaciones de sistemas de alto riesgo
- Requisitos de transparencia (incluyendo etiquetado de contenido generado por IA)
- Arquitectura supervisora liderada por AESIA
- Sanciones alineadas con niveles del EU AI Act
- Medidas de sandbox e innovación
- Fechas de aplicación alineadas con hitos de la UE (ago 2025/2026)

**Fuentes:** [REGSAI-SPAIN] [Regulations.AI Spain](https://regulations.ai/regulations/spain-summary), [ALGWATCH-AESIA] [AlgorithmWatch](https://algorithmwatch.org/en/what-to-expect-from-europes-first-ai-oversight-agency/), [TWOBIRDS-SPAIN] [Bird & Bird Spain](https://www.twobirds.com/en/capabilities/artificial-intelligence/ai-legal-services/ai-regulatory-horizon-tracker/spain). Confianza A-B.

---

## 8. Guía AEPD sobre IA agéntica (febrero 2026) — DIRECTAMENTE RELEVANTE

El **18 de febrero de 2026**, la AEPD publicó *"Inteligencia artificial agéntica desde la perspectiva de la protección de datos"* — una guía de 71 páginas. Es **uno de los primeros documentos regulatorios del mundo que aborda específicamente sistemas de IA agéntica** desde protección de datos. Aplicable directamente a los AI Workers de HappyRobot.

### Requisitos clave

| Área | Requisito | Detalle |
|---|---|---|
| **Governance** | Framework cross-funcional | Business owners + IT + calidad + DPO involucrados desde el inicio |
| **DPIA** | Obligatoria para IA agéntica | La AEPD indica que "ordinariamente cumplirá el umbral" del Art. 35 GDPR |
| **Transparencia** | Actualizar avisos de privacidad | Cuando la IA introduce nuevos destinatarios, retención, decisiones automatizadas, transferencias internacionales |
| **Minimización** | Política "need to know" | Agentes solo acceden a datos necesarios para la tarea específica |
| **Memoria** | Separar memoria operativa de gestión | Auto-limpieza, zonas "no log", desactivar memoria en subtareas de alto riesgo |
| **Supervisión humana** | Niveles de autonomía configurables | Aprobación humana obligatoria antes de acciones de alto impacto o irreversibles |
| **Roles** | Mapeo de relaciones con terceros | Determinar si servicios externos son processors, controllers, o no-processors |
| **Seguridad** | Cada llamada API = exportación parcial de datos | Allowlists de herramientas, validación de cadenas de razonamiento, pasos hardcoded para seguridad |

### Amenazas identificadas por la AEPD

| Tipo | Amenazas |
|---|---|
| **Procesamiento autorizado** | Governance gaps, accountability drift, no-reproducibilidad, feedback loops, desalineamiento de objetivos, automation bias, shadow-leak de datos, profiling no autorizado |
| **Acceso no autorizado** | Prompt injection, data exfiltration, session hijacking, memory poisoning, zero-click attacks, reasoning chain attacks, ataques compuestos |

### Advertencia "BYOAgentic"

La AEPD advierte explícitamente contra empleados construyendo workflows de IA agéntica fuera de estructuras de gobernanza usando plataformas fáciles de usar. Esto **valida el enfoque de HappyRobot** de gobernanza centralizada y AI Auditor como buena práctica Y expectativa regulatoria.

**Fuentes:** [AEPD-AGENTIC] [Anuncio AEPD](https://www.aepd.es/prensa-y-comunicacion/notas-de-prensa/la-agencia-publica-unas-orientaciones-sobre-inteligencia), [AEPD-AGENTIC-PDF] [Guía PDF](https://www.aepd.es/en/guides/agentic-artificial-intelligence.pdf), [LINKLATERS-AEPD] [Linklaters](https://techinsights.linklaters.com/post/102mk6z/agentic-ai-and-data-protection-guidance-from-the-spanish-aepd). Confianza A.

---

## 9. Checklist de compliance para HappyRobot en España

### Obligaciones como proveedor (platform-level)

| # | Requisito | Base legal | Deadline |
|---|---|---|---|
| 1 | **Mecanismo de divulgación AI** en todos los canales (voz/chat/email) | Art. 50(1) | Ago 2026 |
| 2 | **Marcado de outputs sintéticos** en formato legible por máquina | Art. 50(2) | Ago 2026 |
| 3 | **Rutas de escalado humano** en todas las interacciones | Art. 50 + Art. 22 [GDPR](gdpr-lopdgdd.md) | Ya |
| 4 | **Retención de datos configurable** por cliente/caso de uso | GDPR Art. 5(1)(e) | Ya |
| 5 | **Audit logging** con registros de decisiones | Art. 50 + Guía AEPD | Ago 2026 |
| 6 | **Redacción de PII** en transcripciones y logs | GDPR Art. 5(1)(c) | Ya |
| 7 | **Residencia de datos en la UE** como opción | GDPR Cap. V | Critico para ventas enterprise UE |
| 8 | **Tooling para DPIA** para deployers | Guía AEPD agéntica | Recomendado |
| 9 | **Gestión de memoria** (separación, auto-limpieza, zonas no-log) | Guía AEPD agéntica | Recomendado |
| 10 | **Derechos del interesado** (acceso, supresión, portabilidad) para datos de interacción | GDPR Arts. 15-20 | Ya |

### Certificaciones

| Certificación | Estado | Prioridad |
|---|---|---|
| SOC 2 Type II | Declarado en web | Verificar vigencia |
| GDPR compliance | Declarado | Documentar DPAs, SCCs, TIAs |
| EU AI Act compliance | Declarado | Validar contra requisitos de ago 2026 |
| HIPAA | Declarado | Relevante para healthcare |
| ISO 27001 | No mencionado | Considerar para credibilidad enterprise UE |

---

## 10. Compliance como ventaja competitiva

### Posicionamiento en mercado europeo

| Ventaja | Detalle |
|---|---|
| **First-mover en EU AI Act** | La mayoría de competidores US-only ([Bland AI](../competidores/bland-ai.md), [Retell](../competidores/retell-ai.md), [Air AI](../competidores/air-ai.md), [Vapi](../competidores/vapi.md)) no tienen infraestructura de compliance UE |
| **Alineamiento con guía AEPD** | Las features de governance y evaluación de HappyRobot (AI Auditor, shared context & memory) mapean directamente a las medidas recomendadas por la AEPD |
| **Residencia de datos UE** | Elimina riesgo de transferencias transfronterizas — deal-breaker para muchas enterprises europeas |
| **Founders españoles** | [Pablo](../personas/pablo-palafox.md) y [Javier Palafox](../personas/javier-palafox.md) aportan credibilidad cultural al hablar de compliance regulatorio con clientes españoles |
| **Enterprise trust signal** | En industrias reguladas (logística, finanzas, healthcare), compliance EU AI Act se está convirtiendo en requisito de procurement |

### Landscape competitivo en compliance

| Competidor | Estado compliance UE | Ventaja HappyRobot |
|---|---|---|
| [Bland AI](../competidores/bland-ai.md) | US-focused, sin presencia UE | Full compliance UE + oficina España |
| [Retell AI](../competidores/retell-ai.md) | Documentación mínima UE | Framework governance/audit |
| [Synthflow](../competidores/synthflow.md) | Algo de presencia UE (fundada en Alemania) | Compliance enterprise más completo |
| [Vapi](../competidores/vapi.md) | Developer-focused, features compliance limitadas | Governance enterprise-grade |
| [Sierra AI](../competidores/sierra-ai.md) | Enterprise pero US-centric | Residencia datos UE + equipo local |
| [Parloa](../competidores/parloa.md) | **Fundada en Alemania, compliance UE fuerte** | Competidor directo en compliance; necesita paridad |
| [Poly AI](../competidores/poly-ai.md) | **Basada en UK, GDPR-aware** | Postura compliance similar; diferenciar en producto |

**Insight clave:** Parloa y Poly AI son los competidores más maduros en compliance europeo. El diferenciador de HappyRobot vs. ellos debe ser la **capa de AI governance/auditor** combinada con **forward-deployed engineering** para configuraciones custom de compliance.

---

## 11. Riesgos y vigilancia

| Riesgo | Prob. | Impacto | Mitigación |
|---|---|---|---|
| Invalidación DPF ("Schrems III") | Media | Alto | SCCs como backup; ofrecer residencia datos UE |
| Reclasificación a alto riesgo | Media-baja | Alto | Capas de compliance modulares; documentar límites de casos de uso |
| Acciones de enforcement AESIA | Baja en 2026 | Medio | Compliance proactivo; participar en sandbox AESIA |
| Cambios en ley española de IA | Media | Medio | Monitorizar progreso del Anteproyecto |
| ePrivacy Regulation (sustituyendo Directiva) | Media-baja | Medio | Monitorizar; framework actual estable hasta ~2027 |

---

## 12. Experiencia de Lola

[Lola](../personas/lola-vilas.md) tiene experiencia regulatoria profunda navegando regulación con Uber en España — directamente transferible a navegar EU AI Act. Su experiencia con reguladores de movilidad (CNMC, ayuntamientos, Ministerio de Transportes) y su capacidad de construir relaciones institucionales son activos estratégicos para la expansión regulatoria de HappyRobot en España.

---

## Números clave para entrevista

| Métrica | Valor |
|---|---|
| Fecha aplicación transparencia EU AI Act | **2 agosto 2026** |
| Multa máxima (prácticas prohibidas) | **EUR 35M o 7% facturación global** |
| Multa máxima (transparencia) | **EUR 15M o 3% facturación global** |
| Multa máxima GDPR | **EUR 20M o 4% facturación global** |
| Guía AEPD IA agéntica publicada | **18 febrero 2026** |
| AESIA operativa desde | **Junio 2024** |
| Anteproyecto ley IA española | **11 marzo 2025** (primera lectura) |
| Clasificación HappyRobot (core) | **Riesgo limitado** |
| Obligación clave Art. 50 | **Divulgar interacción con IA a usuarios** |

---

*Fuentes principales: [EU AI Act oficial](https://artificialintelligenceact.eu/), [AEPD](https://www.aepd.es/), [A&O Shearman](https://www.aoshearman.com/), [Telnyx](https://telnyx.com/resources/eu-ai-act), [Holistic AI](https://www.holisticai.com/), [Regulations.AI](https://regulations.ai/), [Linklaters](https://techinsights.linklaters.com/)*
