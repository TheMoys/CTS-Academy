<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [Fase 01: Requisitos](/RUP/01-requisitos/README.md) | [Fase 02: Análisis](/RUP/02-analisis/README.md) |
|:---:|:---:|:---:|:---:|

</div>

# Realización de Análisis: `solicitarCambiosEntregable()`

Este documento formaliza la colaboración de análisis entre clases estereotipadas Boundary-Control-Entity (BCE) que realiza el caso de uso `solicitarCambiosEntregable()`, permitiendo al Tech Leader emitir observaciones técnicas y requerir correcciones en el código presentado por un alumno, transicionando la entrega a `REQUIERE_CAMBIOS` con retroalimentación constructiva obligatoria.

---

## 1. Diagrama de Clases de Análisis (VOPC)

El diagrama de clases participantes delimita las responsabilidades para registrar observaciones, validar el feedback constructivo y notificar al estudiante.

<div align="center">

![Diagrama de Clases de Análisis](clasesAnalisis.svg)
*Figura 1: Clases de análisis participantes en `solicitarCambiosEntregable()`.*

</div>

### Participantes y Estereotipos

| Clase | Estereotipo | Responsabilidad |
| :--- | :---: | :--- |
| **`LiderEquipo`** | `<<actor>>` | Tech Leader que solicita correcciones de arquitectura, bugs o estilo. |
| **`DialogoCambiosRevision`** | `<<boundary>>` | Interfaz modal para redactar las observaciones globales y consolidar las notas de revisión. |
| **`GestorRevisiones`** | `<<control>>` | Controlador de lógica de negocio que valida la completitud de la retroalimentación técnica, actualiza el estado del laboratorio y despacha la alerta. |
| **`EntregaLaboratorio`** | `<<entity>>` | Instancia de la entrega cuya máquina de estados transiciona a `REQUIERE_CAMBIOS`. |
| **`RevisionCodigo`** | `<<entity>>` | Registro formal del dictamen técnico con veredicto `REQUIERE_CAMBIOS`. |
| **`ComentarioRevision`** | `<<entity>>` | Colección de comentarios específicos asociados a líneas del código fuente. |
| **`Notificacion`** | `<<entity>>` | Alerta interna encolada para el alumno con enlace directo al feedback. |

---

## 2. Diagrama de Realización de Análisis (Secuencia BCE)

La interacción formaliza la exigencia de justificación técnica antes de actualizar el estado del entregable.

<div align="center">

![Diagrama de Realización de Análisis](realizacionAnalisis.svg)
*Figura 2: Secuencia de mensajes BCE para `solicitarCambiosEntregable()`.*

</div>

### Flujo de Colaboración

1. El actor `LiderEquipo` abre el diálogo de solicitud de cambios desde `DialogoCambiosRevision`.
2. El Tech Leader redacta las observaciones generales que sintetizan las deficiencias a corregir.
3. `DialogoCambiosRevision` envía la solicitud a `GestorRevisiones` (`solicitarCambiosEntrega(...)`).
4. `GestorRevisiones` consulta a `ComentarioRevision` para verificar si existen anotaciones en líneas de código y evalúa la presencia de explicaciones globales en virtud de **RN-LEAD-10**.
5. Si no se provee retroalimentación constructiva, se rechaza la transacción exigiendo justificación técnica.
6. Habiendo superado la validación, se formaliza la entidad `RevisionCodigo` con veredicto `REQUIERE_CAMBIOS`.
7. La entidad `EntregaLaboratorio` transiciona su estado a `REQUIERE_CAMBIOS`, permitiendo al alumno preparar una nueva iteración de código.
8. Se encola una `Notificacion` informativa para el estudiante becario orientándolo hacia la consulta de las observaciones técnicas.
9. Se confirma la emisión de la solicitud al Tech Leader.

---

## 3. Trazabilidad con Reglas de Negocio

- **RN-LEAD-10 (Obligatoriedad de Feedback Constructivo):** Es mandatorio que toda solicitud de cambios incluya una explicación técnica detallada orientada a guiar al alumno en la subsanación de las deficiencias detectadas.

---

<div align="center">

[Volver al Índice de la Fase 02: Análisis](/RUP/02-analisis/README.md)

</div>
