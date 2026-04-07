---
title: "Glosario de IA"
type: entrevista
status: completo
tags: [ia-101, glosario]
updated: 2026-04-07
---

# Glosario de IA

Referencia rápida para consulta antes o durante la preparación de entrevista. Los términos están en inglés porque así se usan en la industria; las definiciones, en español llano.

---

## 1. Fundamentos

**Artificial Intelligence (AI)** — Cualquier sistema que realiza tareas que normalmente requieren inteligencia humana: entender lenguaje, tomar decisiones, reconocer patrones. *Por qué importa:* HappyRobot vende "AI Workers" — agentes de IA que ejecutan operaciones empresariales de forma autónoma.

**Machine Learning (ML)** — Subcampo de la IA donde el sistema aprende patrones a partir de datos en lugar de seguir reglas escritas a mano. *Por qué importa:* Es la base técnica que permite a los agentes de HappyRobot mejorar con cada interacción y adaptarse a nuevos clientes.

**Deep Learning** — Tipo de ML que usa redes neuronales con muchas capas para procesar información compleja (texto, voz, imágenes). *Por qué importa:* Los modelos de lenguaje que dan inteligencia a los AI Workers de HappyRobot son modelos de deep learning.

**LLM (Large Language Model)** — Modelo de deep learning entrenado con enormes cantidades de texto que puede entender y generar lenguaje natural. Ejemplos: GPT-5.4, Claude 4.6, Llama 4. *Por qué importa:* Es el "cerebro" de cada AI Worker de HappyRobot. La empresa es model-agnostic — puede usar distintos LLMs según el cliente.

**Token** — La unidad mínima que procesa un LLM. Aproximadamente, 1 token = 3/4 de una palabra en inglés. *Por qué importa:* El coste de usar un LLM se mide en tokens. Cada llamada de voz o email que gestiona un AI Worker consume tokens = coste variable directo.

**Context Window** — Cantidad máxima de texto (en tokens) que un LLM puede "recordar" en una sola conversación. Los modelos más recientes (abril 2026) ofrecen desde 200K hasta 10M tokens. *Por qué importa:* Un context window grande permite al agente manejar conversaciones largas o acceder a más información del cliente sin perder el hilo.

**Inference** — El momento en que un modelo ya entrenado procesa una entrada y genera una respuesta. Cada vez que un AI Worker contesta una llamada, está haciendo inference. *Por qué importa:* La latencia y el coste de inference determinan la experiencia del usuario final y los márgenes del servicio.

**Fine-tuning** — Proceso de re-entrenar un modelo general con datos específicos de un dominio o empresa para que se especialice. *Por qué importa:* Permite adaptar el comportamiento de los agentes a la jerga y procesos de cada cliente (p.ej., terminología logística de DHL).

---

## 2. Agentes

**AI Agent** — Sistema de IA que no solo responde preguntas, sino que toma decisiones y ejecuta acciones de forma autónoma (enviar emails, actualizar un CRM, programar una cita). *Por qué importa:* Es exactamente lo que HappyRobot vende — agentes que ejecutan, no solo chatbots que informan.

**Agentic AI** — Paradigma donde la IA opera con autonomía: planifica pasos, usa herramientas, y decide cuándo escalar a un humano. Contrasta con IA puramente reactiva. *Por qué importa:* HappyRobot combina razonamiento agéntico (flexible) con lógica determinista (predecible) — su diferenciador arquitectónico clave.

**Tool Use / Function Calling** — Capacidad de un agente de IA para invocar herramientas externas: consultar una base de datos, llamar a una API, enviar un SMS. *Por qué importa:* Es lo que permite a un AI Worker de HappyRobot ir más allá de conversar — puede mover cargas en un TMS, actualizar facturas, o enviar confirmaciones.

**RAG (Retrieval-Augmented Generation)** — Técnica donde el agente busca información relevante en una base de conocimiento antes de responder, en lugar de depender solo de su entrenamiento. *Por qué importa:* Permite que los agentes accedan a datos actualizados del cliente (tarifas, políticas, estado de envíos) sin necesidad de re-entrenar el modelo.

**Prompt Engineering** — El arte de escribir instrucciones claras y precisas para que un LLM se comporte como queremos. *Por qué importa:* Los forward-deployed engineers de HappyRobot pasan buena parte de su tiempo ajustando prompts para cada cliente y caso de uso.

**Hallucination** — Cuando un LLM genera información que suena convincente pero es falsa o inventada. *Por qué importa:* En enterprise, una alucinación puede significar dar un precio incorrecto o una fecha de entrega falsa. Las guardrails de HappyRobot existen precisamente para minimizar este riesgo.

**Guardrails** — Reglas y controles que limitan lo que un agente de IA puede decir o hacer, para evitar errores, alucinaciones o acciones no autorizadas. *Por qué importa:* El sistema de Governance de HappyRobot (con AI auditor) es uno de sus diferenciadores principales frente a competidores — crítico para vender a enterprise.

**Human-in-the-Loop (HITL)** — Diseño donde un humano supervisa, aprueba o interviene en las decisiones del agente cuando la confianza es baja o el caso es complejo. *Por qué importa:* Los clientes enterprise exigen esto. HappyRobot lo implementa como parte de su flujo: el agente escala a un humano cuando detecta que no puede resolver solo.

---

## 3. Voz

**STT / ASR (Speech-to-Text / Automatic Speech Recognition)** — Tecnología que convierte audio hablado en texto escrito. *Por qué importa:* Es el primer paso cuando un AI Worker de HappyRobot atiende una llamada telefónica — necesita entender lo que dice el interlocutor.

**TTS (Text-to-Speech)** — Tecnología que convierte texto en voz sintetizada natural. *Por qué importa:* Es lo que permite que el AI Worker "hable" por teléfono con voz fluida. La calidad del TTS impacta directamente en la percepción del servicio.

**VAD (Voice Activity Detection)** — Sistema que detecta cuándo alguien está hablando vs. cuándo hay silencio. *Por qué importa:* Evita que el agente interrumpa al interlocutor o se quede callado demasiado tiempo — clave para que la conversación suene natural.

**EOT Detection (End of Turn)** — Algoritmo que determina cuándo una persona ha terminado de hablar y es el turno del agente para responder. *Por qué importa:* Si falla, el agente interrumpe o tarda demasiado en responder. Es uno de los problemas técnicos más difíciles en voice AI.

**Latency** — El tiempo que pasa entre que el usuario termina de hablar y el agente empieza a responder. Se mide en milisegundos. *Por qué importa:* Si supera ~800ms, la conversación se siente antinatural. HappyRobot presume de 0 min FRT (First Response Time) — la latencia es competitiva.

---

## 4. Enterprise

**POC / Pilot** — Proof of Concept: proyecto limitado (pocas semanas, un caso de uso) para demostrar el valor antes de un contrato grande. *Por qué importa:* Es el modelo de venta estándar en enterprise AI. Tu trabajo como GM incluirá gestionar el pipeline de POCs y su conversión a contratos.

**Forward-Deployed Engineer (FDE)** — Ingeniero que trabaja embebido con el cliente durante la implementación, adaptando el producto a sus sistemas y procesos. *Por qué importa:* Es el modelo de HappyRobot (inspirado en Palantir). España necesitará FDEs — una de las posiciones abiertas. Es clave para el éxito del cliente y para el upsell.

**SLA (Service Level Agreement)** — Compromiso contractual de rendimiento: tiempo de respuesta, disponibilidad, tasa de resolución. *Por qué importa:* Los clientes enterprise como DHL exigen SLAs estrictos. Negociarlos y cumplirlos será parte de tu responsabilidad como GM.

**Automation Rate** — Porcentaje de interacciones que el agente resuelve completamente sin intervención humana. *Por qué importa:* Es la métrica estrella para demostrar ROI. HappyRobot reporta 50%+ de resolución autónoma — cada punto porcentual de mejora es ahorro directo para el cliente.

**ROI (Return on Investment)** — Retorno sobre la inversión. En el contexto de HappyRobot: cuánto ahorra o genera el AI Worker vs. lo que cuesta. *Por qué importa:* HappyRobot reporta 119x ROI en collections. Es el argumento de venta más potente. Como GM, tendrás que construir business cases con ROI para cada cliente español.

---

## 5. Governance y Compliance

**SOC 2** — Certificación de seguridad que verifica que una empresa protege adecuadamente los datos de sus clientes. Tipos I (diseño) y II (operación continua). *Por qué importa:* HappyRobot tiene SOC 2 — es requisito imprescindible para vender a clientes enterprise. Sin esto, DHL ni te recibe.

**GDPR (General Data Protection Regulation)** — Regulación europea de protección de datos personales. En España, complementada por la LOPDGDD. *Por qué importa:* Todo AI Worker que procese datos de personas en Europa debe cumplir GDPR. Como GM España, serás responsable de que cada implementación cumpla.

**EU AI Act** — Regulación europea (en vigor desde 2024, aplicación gradual) que clasifica sistemas de IA por nivel de riesgo y exige transparencia, evaluaciones y registro. *Por qué importa:* Los AI Workers de HappyRobot en Europa deberán cumplir requisitos específicos según su nivel de riesgo. Puede ser ventaja competitiva si HappyRobot se adelanta al cumplimiento.

**Prompt Injection** — Ataque donde alguien intenta manipular al agente de IA insertando instrucciones maliciosas en su input (p.ej., "ignora tus instrucciones anteriores y..."). *Por qué importa:* Es el principal riesgo de seguridad en agentes de IA. Las guardrails y el AI auditor de HappyRobot están diseñados para detectar y bloquear estos ataques.
