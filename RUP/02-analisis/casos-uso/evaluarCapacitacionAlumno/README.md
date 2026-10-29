<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [Fase 01: Requisitos](/RUP/01-requisitos/README.md) | [Fase 02: Análisis](/RUP/02-analisis/README.md) |
|:---:|:---:|:---:|:---:|

</div>

# Realización de Análisis: `evaluarCapacitacionAlumno()`

Este documento formaliza la colaboración de análisis entre clases estereotipadas Boundary-Control-Entity (BCE) que realiza el caso de uso `evaluarCapacitacionAlumno()`, permitiendo al Tech Leader emitir el informe final de desempeño y certificación de un alumno que ha superado el 100% de los módulos y prácticas de su itinerario formativo en el equipo técnico CTS.

---

## 1. Diagrama de Clases de Análisis (VOPC)

El diagrama de clases participantes delimita las responsabilidades de verificación de completitud curricular, ponderación multidimensional de competencias y notificación formal.

<div align="center">

![Diagrama de Clases de Análisis](clasesAnalisis.svg)
*Figura 1: Clases de análisis participantes en `evaluarCapacitacionAlumno()`.*

</div>

### Participantes y Estereotipos

| Clase | Estereotipo | Responsabilidad |
| :--- | :---: | :--- |
| **`LiderEquipo`** | `<<actor>>` | Tech Leader que evalúa el desempeño global del estudiante becario. |
| **`FormularioEvaluacionGlobal`** | `<<boundary>>` | Interfaz gráfica para registrar puntuaciones por competencia, informe cualitativo y veredicto de aptitud para proyectos reales. |
| **`ServicioNotificacionesEmail`** | `<<boundary>>` | Perímetro externo para despachar las actas formales de conclusión a la coordinación de admisiones y al alumno. |
| **`GestorRevisiones`** | `<<control>>` | Controlador de lógica de negocio que valida la completitud total, consolida la evaluación y transiciona el estado del alumno. |
| **`TechLeader`** | `<<entity>>` | Perfil del líder técnico tutor. |
| **`Alumno`** | `<<entity>>` | Expediente del alumno cuyo estado pasa a `CAPACITACION_CONCLUIDA`. |
| **`Capacitacion`** | `<<entity>>` | Malla curricular que certifica la superación de la totalidad de módulos formativos. |
| **`EvaluacionSumativa`** | `<<entity>>` | Acta final que archiva las calificaciones ponderadas y el informe de aptitud profesional. |

---

## 2. Diagrama de Realización de Análisis (Secuencia BCE)

La interacción formaliza la estricta compuerta de validación curricular antes de emitir la certificación final.

<div align="center">

![Diagrama de Realización de Análisis](realizacionAnalisis.svg)
*Figura 2: Secuencia de mensajes BCE para `evaluarCapacitacionAlumno()`.*

</div>

### Flujo de Colaboración

1. El actor `LiderEquipo` abre el formulario de evaluación final para un alumno tutelado desde `FormularioEvaluacionGlobal`.
2. `FormularioEvaluacionGlobal` solicita a `GestorRevisiones` comprobar la elegibilidad del alumno (`verificarCompletitudCurricular(idAlumno)`).
3. `GestorRevisiones` consulta a `Alumno` para obtener su itinerario activo y seguidamente a `Capacitacion` para verificar si todos los módulos y prácticas asociadas se encuentran formalmente aprobados.
4. En virtud de **RN-LEAD-11**, si existe algún laboratorio pendiente de aprobación o módulo incompleto, se bloquea la evaluación reportando el impedimento.
5. Si el 100% curricular está aprobado, se habilita la rúbrica multidimensional (arquitectura, calidad de código, autonomía y trabajo en equipo).
6. El Tech Leader confirma las calificaciones, informe de competencias y dictamen de aptitud para incorporarse a proyectos productivos.
7. `GestorRevisiones` archiva la entidad `EvaluacionSumativa`.
8. La entidad `Alumno` transiciona su máquina de estados hacia `CAPACITACION_CONCLUIDA`.
9. Se genera el acta formal de conclusión y `ServicioNotificacionesEmail` despacha copias certificadas al Gestor de Admisiones y al Alumno graduado.
10. Se confirma el éxito de la certificación al Tech Leader.

---

## 3. Trazabilidad con Reglas de Negocio

- **RN-LEAD-11 (Requisito de Completitud Curricular):** No es posible iniciar la evaluación final de capacitación si el alumno mantiene algún laboratorio en estado no aprobado o módulos pendientes de cursar.

---

<div align="center">

[Volver al Índice de la Fase 02: Análisis](/RUP/02-analisis/README.md)

</div>
