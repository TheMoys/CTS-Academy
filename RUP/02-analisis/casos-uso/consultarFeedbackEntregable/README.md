<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [Fase 01: Requisitos](/RUP/01-requisitos/README.md) | [Fase 02: Análisis](/RUP/02-analisis/README.md) |
|:---:|:---:|:---:|:---:|

</div>

# Realización de Análisis: `consultarFeedbackEntregable()`

Este documento formaliza la colaboración de análisis entre clases estereotipadas Boundary-Control-Entity (BCE) que realiza el caso de uso `consultarFeedbackEntregable()`, permitiendo al alumno becario inspeccionar el veredicto formal, calificación y observaciones técnicas emitidas por el Tech Leader tras la revisión de código (*Code Review*).

---

## 1. Diagrama de Clases de Análisis (VOPC)

El diagrama de clases participantes delimita las responsabilidades de consulta y presentación de rúbricas técnicas y observaciones línea a línea.

<div align="center">

![Diagrama de Clases de Análisis](clasesAnalisis.svg)
*Figura 1: Clases de análisis participantes en `consultarFeedbackEntregable()`.*

</div>

### Participantes y Estereotipos

| Clase | Estereotipo | Responsabilidad |
| :--- | :---: | :--- |
| **`Alumno`** | `<<actor>>` | Estudiante becario autenticado que consulta la retroalimentación de su solución. |
| **`VistaFeedbackEntrega`** | `<<boundary>>` | Interfaz interactiva que presenta la calificación numérica, el dictamen formal, la rúbrica de calidad y los comentarios de código. |
| **`GestorFormacion`** | `<<control>>` | Controlador de lógica de negocio que valida la pertenencia de la entrega, extrae el dictamen y evalúa la superación curricular. |
| **`Alumno`** | `<<entity>>` | Expediente del alumno. |
| **`Laboratorio`** | `<<entity>>` | Ejercicio práctico evaluado. |
| **`EntregaLaboratorio`** | `<<entity>>` | Instancia de la solución enviada con su ciclo de vida y relación con el alumno. |
| **`RevisionCodigo`** | `<<entity>>` | Dictamen técnico emitido por el Tech Leader con su nota numérica y rúbrica sumativa. |
| **`ComentarioRevision`** | `<<entity>>` | Observaciones técnicas contextuales vinculadas a archivos y líneas específicas del código fuente. |

---

## 2. Diagrama de Realización de Análisis (Secuencia BCE)

La interacción formaliza la verificación de seguridad y la exposición de las observaciones de revisión.

<div align="center">

![Diagrama de Realización de Análisis](realizacionAnalisis.svg)
*Figura 2: Secuencia de mensajes BCE para `consultarFeedbackEntregable()`.*

</div>

### Flujo de Colaboración

1. El actor `Alumno` solicita acceder al detalle de retroalimentación de una entrega desde `VistaFeedbackEntrega`.
2. `VistaFeedbackEntrega` invoca a `GestorFormacion` (`obtenerFeedbackEntrega(idAlumno, idEntrega)`).
3. `GestorFormacion` comprueba en `EntregaLaboratorio` que la entrega pertenezca al alumno solicitante. En caso negativo, deniega el acceso.
4. Se verifica si la entrega ya cuenta con una revisión formal completada. Si sigue en cola de evaluación del líder técnico, se notifica el estado en espera.
5. Si la revisión existe:
   - Se recuperan los metadatos de `Laboratorio`.
   - Se extraen la calificación numérica, rúbrica y veredicto de `RevisionCodigo`.
   - Se compila la lista de `ComentarioRevision` asociados al Pull Request.
6. En cumplimiento de **RN-FORM-06**, `GestorFormacion` evalúa si la calificación es igual o superior a 7.0/10.0 y el veredicto es `APROBADO`.
7. Si el dictamen es `REQUIERE_CAMBIOS`, `VistaFeedbackEntrega` habilita el botón de acción para reenviar una nueva versión corregida reutilizando el flujo de entrega.
8. Si el dictamen es `APROBADO`, se presenta la certificación de superación del laboratorio y se inhabilita el reenvío.

---

## 3. Trazabilidad con Reglas de Negocio

- **RN-FORM-06 (Revisión Obligatoria para Avance):** Ningún laboratorio se computa como superado en el expediente curricular sin la aprobación expresa y una calificación numérica mayor o igual a 7.0/10.0 por parte del Tech Leader.

---

<div align="center">

[Volver al Índice de la Fase 02: Análisis](/RUP/02-analisis/README.md)

</div>
