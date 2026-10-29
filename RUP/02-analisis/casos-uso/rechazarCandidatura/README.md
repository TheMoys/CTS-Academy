<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [01 Requisitos](/RUP/01-requisitos/README.md) | [02 Análisis](/RUP/02-analisis/README.md) | [Catálogo Requisitos](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

<sub>**Fase 02 Análisis** › **Realización de Casos de Uso** › `rechazarCandidatura()`</sub>

</div>

# Realización de Caso de Uso: `rechazarCandidatura()`

Esta especificación describe la realización de análisis del caso de uso `rechazarCandidatura()` mediante clases BCE, detallando la motivación obligatoria del descarte, la revocación inmediata de credenciales temporales de examen y la emisión de comunicaciones institucionales constructivas.

---

<div align=center>

| Diagrama de Clases de Análisis (VOPC) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/rechazarCandidatura/clasesAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](clasesAnalisis.puml)</i></sup> |

| Diagrama de Realización de Análisis (Secuencia BCE) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/rechazarCandidatura/realizacionAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](realizacionAnalisis.puml)</i></sup> |

</div>

---

## Clases de Análisis Participantes

<div align=center>

| Clase | Estereotipo | Tipo | Responsabilidad Principal |
| :--- | :---: | :---: | :--- |
| **`DialogoRechazo`** | `<<boundary>>` | Frontera | Interfaz modal de selección de motivos institucionales tipificados y captura de justificación técnica interna; confirmación y aviso de sellado. |
| **`ServicioAccesoAutenticacion`** | `<<boundary>>` | Frontera (Externa) | Interfaz con el subsistema de acceso (`PK01 - Acceso`); revoca los tokens de postulación del aspirante (`RN-RECH-03`). |
| **`ServicioNotificacionesEmail`** | `<<boundary>>` | Frontera (Externa) | Adaptador transaccional de correo; despacha la resolución negativa institucional con recomendaciones pedagógicas (`RN-RECH-02`). |
| **`GestorAdmisiones`** | `<<control>>` | Control | Verificación de admisibilidad para descarte, validación de justificación obligatoria (`RN-RECH-01`) y orquestación del archivo permanente en `RECHAZADO`. |
| **`Candidato`** | `<<entity>>` | Entidad | Aspirante desestimado; custodia el motivo tipificado, justificación cualitativa y fecha formal de resolución. |

</div>

---

## Flujo de Realización (Colaboración BCE)

### Flujo Principal: Formalización del Rechazo de Candidatura
1. El **`Gestor`** pulsa "Descartar candidatura" desde el perfil del aspirante.
2. **`DialogoRechazo`** presenta el catálogo de motivos tipificados (desajuste competencial, incompatibilidad de régimen on-site, inasistencia a entrevista, etc.).
3. El evaluador selecciona el motivo e introduce la justificación interna obligatoria (**RN-RECH-01**).
4. **`DialogoRechazo`** remite la orden formal a **`GestorAdmisiones`**.
5. **Comprobación de Estado No Resuelto**: Se valida en **`Candidato`** que el expediente no cuente con resolución previa.
6. **Sellado e Inmutabilidad de la Desestimación**:
   - Se invoca `marcarRechazado(motivo, justificacion)` en **`Candidato`**.
   - El estado transiciona a `RECHAZADO`, archivando el expediente en la convocatoria activa.
7. **Revocación de Accesos (RN-RECH-03)**: **`GestorAdmisiones`** ordena a **`ServicioAccesoAutenticacion`** revocar las credenciales del candidato, impidiendo nuevos accesos al panel de postulación.
8. **Comunicación Constructiva (RN-RECH-02)**: Se despacha la notificación oficial mediante **`ServicioNotificacionesEmail`** agradeciendo la postulación y preservando las relaciones institucionales con la sede.
9. **`DialogoRechazo`** confirma el cierre y transiciona al Gestor hacia el panel general de admisiones.

### Flujo Alternativo: Expediente Ya Resuelto
1. Si el candidato ya cuenta con dictamen cerrado (`ADMITIDO` o `RECHAZADO`):
   - **`GestorAdmisiones`** rechaza la operación y **`DialogoRechazo`** emite un aviso de bloqueo, manteniendo el expediente en modo de solo lectura.

---

## Trazabilidad con la Fase de Requisitos

| Requisito / Artefacto Fase 01 | Realización en Fase 02 (Análisis) |
| :--- | :--- |
| **Caso de Uso `rechazarCandidatura()`** | Orquestación mediante `GestorAdmisiones` asociando `Candidato`, `ServicioAccesoAutenticacion` y `ServicioNotificacionesEmail`. |
| **RN-RECH-01 (Motivación Obligatoria)** | Validación obligatoria de los parámetros `motivoTipificado` y `justificacionTexto` en `GestorAdmisiones`. |
| **RN-RECH-02 (Comunicación Constructiva)** | Uso de plantillas pedagógicas institucionales en `ServicioNotificacionesEmail`. |
| **RN-RECH-03 (Revocación de Credenciales)** | Llamada a `revocarCredencialesCandidato()` en `ServicioAccesoAutenticacion`. |

---

<div align="center">

[Volver a Fase 02: Análisis](/RUP/02-analisis/README.md) • [Ver Especificación de Requisitos (Fase 01)](/RUP/01-requisitos/03-detalle-casos-uso/rechazarCandidatura/README.md)

</div>
