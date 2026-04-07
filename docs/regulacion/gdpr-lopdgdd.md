---
title: "GDPR & LOPDGDD"
type: regulacion
status: completo
tags: [regulacion, gdpr, lopdgdd, españa, privacidad, datos-personales, voice-ai]
updated: 2026-04-07
---

# GDPR & LOPDGDD

Marco de protección de datos aplicable a [HappyRobot](../empresa/happyrobot.md) operando AI agents (voz, chat, email) en España y la UE.

---

## 1. Datos de voz como datos personales

Bajo GDPR, las grabaciones de voz son **datos personales** (PII) porque pueden revelar género, origen étnico, condiciones de salud e identificar unívocamente a individuos.

Si los datos de voz se procesan para **identificación del hablante** (extracción de voice embeddings, creación de perfiles de speaker, diarización), cruzan al territorio del **Artículo 9** como **datos biométricos** — categoría especial que requiere **consentimiento explícito**.

| Tipo de dato | Clasificación GDPR | Base legal necesaria | Conf. |
|---|---|---|---|
| Grabación de voz (conversacional) | Dato personal | Art. 6 — base legal estándar | A |
| Voice embeddings / perfiles de speaker | **Dato biométrico** (Art. 9) | **Consentimiento explícito** | A |
| Transcripción con PII | Dato personal | Art. 6 — base legal estándar | A |
| Datos de interacción (metadata) | Dato personal (si identificable) | Art. 6 — base legal estándar | B |

**Fuentes:** [IAPP-AUDIO] [IAPP Audio Recording Under GDPR](https://iapp.org/news/a/how-do-the-rules-on-audio-recording-change-under-the-gdpr), [SUMMIT-BIOMETRIC] [Summit AI Notes](https://summitnotes.app/blog/gdpr-voice-recordings-biometric-data/). Confianza A-B.

---

## 2. Bases legales para llamadas AI y grabación

| Base legal | Cuándo aplicable | Requisitos | Conf. |
|---|---|---|---|
| **Consentimiento explícito** (Art. 6(1)(a)) | Llamadas de marketing, procesamiento biométrico | Libre, específico, informado, inequívoco. Acción afirmativa clara. | A |
| **Interés legítimo** (Art. 6(1)(f)) | Llamadas operativas B2B (coordinación logística, scheduling) | Balancing test documentado. No puede prevalecer sobre derechos del interesado. | A |
| **Ejecución de contrato** (Art. 6(1)(b)) | Llamadas para cumplir obligaciones contractuales existentes | Debe ser genuinamente necesario para la ejecución del contrato. | A |
| **Obligación legal** (Art. 6(1)(c)) | Llamadas requeridas por ley (compliance regulatorio, servicios financieros) | Debe estar mandado por disposición legal específica. | A |

### Requisitos prácticos para HappyRobot

- Informar a los interlocutores de que la llamada puede ser grabada **antes de que comience la grabación** (anuncio pre-llamada)
- Documentar la base legal para cada tipo de procesamiento
- Habilitar **mecanismos de opt-out**
- Implementar políticas de retención de datos configurables por cliente

**Fuentes:** [ANSWERINGAGENT-GDPR] [GDPR Compliance for AI Voice Agents](https://answeringagent.com/blog/gdpr-compliance-for-ai-voice-agents), [FIREFLIES-GDPR] [Fireflies GDPR Recording](https://fireflies.ai/blog/gdpr-call-recording-best-practices/). Confianza B.

---

## 3. Toma de decisiones automatizada (Artículo 22)

El Art. 22 GDPR otorga a los interesados el **derecho a no ser objeto de una decisión basada únicamente en el tratamiento automatizado** que produzca efectos jurídicos o le afecte significativamente.

### Excepciones (cuando se permite)

1. Necesaria para celebrar o ejecutar un contrato
2. Autorizada por derecho de la UE o Estado miembro con garantías adecuadas
3. Basada en consentimiento explícito

### Garantías obligatorias (incluso con excepciones)

- Derecho a obtener **intervención humana**
- Derecho a expresar su punto de vista
- Derecho a **impugnar la decisión**

### Relevancia para casos de uso de HappyRobot

| Caso de uso | Activa Art. 22? | Razón |
|---|---|---|
| Cobros/collections (decidir perseguir, escalar, liquidar) | **Probablemente sí** | Afecta significativamente a la persona |
| Recruiting/screening candidatos | **Definitivamente sí** | Efectos jurídicos sobre empleo |
| Logística/routing/scheduling | **Probablemente no** | No afecta significativamente a individuos |
| Ventas inbound (cualificación leads) | **Depende del contexto** | Si determina acceso a servicios, posiblemente |
| Customer service (resolución reclamaciones) | **Depende del contexto** | Si la resolución tiene efectos jurídicos, sí |

**Implicación clave: siempre debe existir una ruta de escalado humano.**

**Fuentes:** [GDPR-ART22] [Art. 22 GDPR](https://gdpr-info.eu/art-22-gdpr/), [FIELDFISHER-ART22] [Fieldfisher AI and Art. 22](https://www.fieldfisher.com/en/insights/artificial-intelligence-and-automated-individual-decision-making). Confianza A.

---

## 4. Retención y minimización de datos

### Principios GDPR aplicables

| Principio | Artículo | Requisito para HappyRobot |
|---|---|---|
| **Limitación de finalidad** | Art. 5(1)(b) | Datos recogidos para un fin no pueden reutilizarse sin nueva base legal |
| **Limitación de conservación** | Art. 5(1)(e) | Datos personales solo mientras sean necesarios para la finalidad declarada |
| **Minimización de datos** | Art. 5(1)(c) | Recoger solo lo estrictamente necesario |

### Recomendaciones prácticas para grabaciones y transcripciones AI

- Definir periodos de retención por caso de uso (ej. 30 días para llamadas operativas, más para compliance regulatorio)
- Implementar **eliminación automática programada**
- **Redacción de PII** en transcripciones donde no se necesite texto completo
- **No almacenar datos "por si acaso"** ni exclusivamente para optimización de modelos AI (advertencia explícita de la [AEPD — guía IA agéntica](eu-ai-act.md))

---

## 5. Transferencias internacionales de datos (UE a EEUU)

### Estado actual (abril 2026)

El **EU-US Data Privacy Framework (DPF)**, adoptado en julio 2023, proporciona un mecanismo de adecuación. Una sentencia del Tribunal General de septiembre 2025 confirmó su validez. Organizaciones US certificadas pueden recibir datos personales UE sin Standard Contractual Clauses (SCCs).

### Incertidumbre significativa

| Factor | Estado | Impacto |
|---|---|---|
| **Impugnación NOYB ante TJUE** | Pendiente | Si se invalida ("Schrems III"), se necesitarían SCCs + medidas suplementarias |
| **Posible sentencia** | **Finales de 2026** [estimate] | Alto impacto en todas las transferencias UE-US |
| **SCCs como backup** | Recomendado siempre | Mitigación independiente del resultado judicial |

### Recomendaciones para HappyRobot

1. Mantener **SCCs como backup** independientemente del estado del DPF
2. Ofrecer **opciones de residencia de datos en la UE** (procesar y almacenar datos de clientes UE dentro de la UE)
3. Documentar Transfer Impact Assessments (TIAs)
4. Considerar **infraestructura cloud en la UE** para clientes europeos

**Fuentes:** [TECHGDPR-XBORDER] [TechGDPR Cross-Border AI Transfers](https://techgdpr.com/blog/gdpr-compliance-for-ai-managing-cross-border-data-transfers/), [INSIDEPRIVACY-XBORDER] [InsidePrivacy Cross-Border Roundup](https://www.insideprivacy.com/cross-border-transfers/roundup-of-cross-border-data-transfer-developments/). Confianza A-B.

---

## 6. Régimen sancionador GDPR

| Nivel | Infracciones | Sanción máxima |
|---|---|---|
| **Superior** | Principios de tratamiento, consentimiento, derechos de interesados | Hasta EUR 20M o **4% facturación global anual** (el mayor) |
| **Inferior** | Obligaciones técnicas y organizativas | Hasta EUR 10M o **2% facturación global anual** (el mayor) |

---

## 7. LOPDGDD — Especificidades españolas

La LOPDGDD (Ley Orgánica 3/2018, de 5 de diciembre, de Protección de Datos Personales y garantía de los derechos digitales) complementa el GDPR con provisiones específicas de España. No reemplaza al GDPR sino que cubre los márgenes donde el GDPR permite derogaciones nacionales.

### Adiciones clave de la LOPDGDD

| Provisión | Descripción | Relevancia para HappyRobot | Conf. |
|---|---|---|---|
| **Art. 22 LOPDGDD** | Trabajadores y representantes deben ser informados de herramientas algorítmicas o basadas en IA que afecten decisiones de empleo | Si la IA de HappyRobot se usa para HR/recruiting en España, los empleadores deben informar a comités de empresa | A |
| **Título X — Derechos digitales** | Garantiza derechos incluyendo desconexión digital, privacidad de comunicaciones digitales | Relevante para agentes AI que operan en contextos de empleados | A |
| **Edad de consentimiento** | Fijada en **14 años** (vs. 16 por defecto en GDPR) para consentimiento de menores | Relevante si agentes AI interactúan con menores | B |
| **DPO obligatorio** | Categorías más amplias que el mínimo GDPR (telecoms, entidades financieras, seguros, etc.) | HappyRobot y/o sus clientes españoles probablemente necesitan DPO | A |
| **Derechos laborales** | Estatuto de los Trabajadores Art. 64.4.d — comité de empresa tiene derecho a ser informado sobre parámetros/reglas de algoritmos que afecten condiciones laborales | Crítico si HappyRobot reemplaza funciones de empleados | A |

**Fuentes:** [LOPDGDD-OVERVIEW] [LOPDGDD Overview](https://globalprivacylaws.com/laws/lopdgdd/), [PROKOPIEV-AEPD] [Prokopiev Law AEPD Agentic AI](https://www.prokopievlaw.com/post/spanish-dpa-issues-guidance-on-agentic-ai-and-data-protection-obligations-february-2026). Confianza A-B.

---

## 8. ePrivacy: LSSI, Ley General de Telecomunicaciones y Lista Robinson

### Regulación de comunicaciones electrónicas comerciales en España

| Regulación | Ámbito | Reglas clave | Sanciones |
|---|---|---|---|
| **LSSI** (Ley 34/2002) | Comunicaciones comerciales electrónicas | Prohíbe email/SMS comercial no solicitado sin consentimiento previo (Art. 21) | EUR 150K-600K por infracciones sistemáticas |
| **LGT** (Ley 11/2022, General de Telecomunicaciones) | Llamadas telefónicas/marketing | Llamadas comerciales generalmente requieren consentimiento previo (Art. 66.1.b). Interés legítimo puede bastar en escenarios B2B limitados per Circular AEPD 1/2023 | Variable según gravedad |
| **Lista Robinson** | Mecanismo de opt-out | Lista DNC de España. Las empresas deben consultar antes de realizar llamadas comerciales | Incluido en sanciones LSSI/LGT |

### Implicaciones por tipo de llamada AI de HappyRobot

| Tipo de llamada | Régimen aplicable | Nivel de flexibilidad |
|---|---|---|
| **Ventas/marketing outbound** | Requiere consentimiento o check Robinson List | Restrictivo |
| **Operaciones logísticas** (scheduling, coordinación de entregas) | Interés legítimo viable | Más flexible |
| **Collections/cobros** | GDPR + normativa específica de protección al consumidor | Intermedio |
| **Seguimiento de conductores** (B2B) | Interés legítimo en contexto contractual | Más flexible |
| **Recruiting/HR** | Consentimiento recomendado + informar comité empresa | Restrictivo |

**Fuentes:** [DLAPIPER-SPAIN] [DLA Piper Electronic Marketing Spain](https://www.dlapiperdataprotection.com/?t=electronic-marketing&c=ES), [DEALFRONT-COLDCALL] [Dealfront Cold Calling Europe](https://www.dealfront.com/blog/essential-guide-to-cold-calling-and-emailing/). Confianza A-B.

---

## 9. Requisitos DPIA para IA agéntica

Según la guía de la AEPD de febrero 2026, los sistemas de IA agéntica como los de HappyRobot **ordinariamente cumplen el umbral** para DPIA obligatoria bajo Art. 35 GDPR.

### Contenido requerido de la DPIA

| Elemento | Requisito |
|---|---|
| Mapeo de flujos de datos | A través de toda la arquitectura agéntica |
| Roles de terceros | Documentar si son processors, controllers, o non-processors |
| Destinatarios de datos | Identificar todos los receptores de datos personales |
| Decisiones automatizadas | Evaluar triggers de Art. 22 |
| Transferencias internacionales | Documentar y evaluar |
| Medidas de minimización | Need-to-know, zonas no-log, auto-limpieza de memoria |

---

## 10. Experiencia de Lola

La experiencia de [Lola](../personas/lola-vilas.md) navegando regulación de privacidad y protección de datos en Uber (ride-hailing, datos de geolocalización, drivers como autónomos) es directamente transferible a los retos GDPR/LOPDGDD de HappyRobot. Su comprensión del equilibrio entre innovación tecnológica y cumplimiento regulatorio es un activo clave para la expansión en España.

---

## Números clave para entrevista

| Métrica | Valor |
|---|---|
| Multa máxima GDPR (nivel superior) | **EUR 20M o 4% facturación global** |
| Multa máxima GDPR (nivel inferior) | **EUR 10M o 2% facturación global** |
| DPF UE-US | **Válido (sept 2025) pero impugnado** |
| Edad consentimiento menores España | **14 años** |
| Art. 22 LOPDGDD | **Informar a trabajadores sobre algoritmos** |
| DPIA obligatoria para IA agéntica | **Sí** (guía AEPD feb 2026) |
| Lista Robinson | **Consulta obligatoria antes de llamadas comerciales** |

---

*Fuentes principales: [GDPR oficial](https://gdpr-info.eu/), [AEPD](https://www.aepd.es/), [IAPP](https://iapp.org/), [DLA Piper](https://www.dlapiperdataprotection.com/), [TechGDPR](https://techgdpr.com/), [Fieldfisher](https://www.fieldfisher.com/)*
