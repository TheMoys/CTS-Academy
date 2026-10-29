<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [Fase 01: Requisitos](/RUP/01-requisitos/README.md) | [Fase 02: Análisis](/RUP/02-analisis/README.md) |
|:---:|:---:|:---:|:---:|

</div>

# Realización de Análisis: `eliminarPregunta()`

Este documento formaliza la colaboración de análisis entre clases estereotipadas Boundary-Control-Entity (BCE) que realiza el caso de uso `eliminarPregunta()`, permitiendo al Tech Leader dar de baja un reactivo técnico del banco de evaluación mediante una desactivación lógica (*soft delete*), excluyéndolo de futuras evaluaciones sin vulnerar la integridad de los resultados históricos de candidatos o alumnos.

---

## 1. Diagrama de Clases de Análisis (VOPC)

El diagrama de clases participantes delimita las responsabilidades para verificar la preservación histórica y conmutar el estado del reactivo a inactivo.

<div align="center">

![Diagrama de Clases de Análisis](clasesAnalisis.svg)
*Figura 1: Clases de análisis participantes en `eliminarPregunta()`.*

</div>

### Participantes y Estereotipos

| Clase | Estereotipo | Responsabilidad |
| :--- | :---: | :--- |
| **`LiderEquipo`** | `<<actor>>` | Tech Leader que da de baja el reactivo del catálogo. |
| **`DialogoEliminacionPregunta`** | `<<boundary>>` | Interfaz modal que advierte sobre la naturaleza lógica de la baja y solicita confirmación expresa. |
| **`GestorBancoPreguntas`** | `<<control>>` | Controlador de lógica de negocio que valida la no supresión física y excluye el ítem de las plantillas activas. |
| **`TechLeader`** | `<<entity>>` | Perfil del líder técnico tutor. |
| **`Pregunta`** | `<<entity>>` | Reactivo evaluativo que transiciona su estado a `INACTIVO`. |
| **`RespuestaEvaluacion`** | `<<entity>>` | Registros históricos de respuestas y puntajes emitidos en exámenes cerrados que se preservan íntegros. |

---

## 2. Diagrama de Realización de Análisis (Secuencia BCE)

La interacción formaliza el borrado lógico no destructivo conforme a las normativas de auditoría técnica.

<div align="center">

![Diagrama de Realización de Análisis](realizacionAnalisis.svg)
*Figura 2: Secuencia de mensajes BCE para `eliminarPregunta()`.*

</div>

### Flujo de Colaboración

1. El actor `LiderEquipo` solicita dar de baja un reactivo desde `DialogoEliminacionPregunta`.
2. `DialogoEliminacionPregunta` invoca al controlador `GestorBancoPreguntas` (`prepararBajaReactivo(...)`).
3. `GestorBancoPreguntas` verifica en `TechLeader` la especialidad técnica del evaluador y obtiene los datos del reactivo desde `Pregunta`.
4. Se consulta a `RespuestaEvaluacion` para contabilizar las respuestas históricas emitidas en evaluaciones pasadas.
5. `DialogoEliminacionPregunta` presenta la advertencia indicando que el reactivo será archivado lógicamente para proteger las evaluaciones históricas.
6. El Tech Leader confirma la baja.
7. En estricto cumplimiento de **RN-LEAD-06**, `GestorBancoPreguntas` ejecuta la desactivación lógica en `Pregunta`, cambiando su estado a `INACTIVO`.
8. Se excluye el reactivo del pool de selección para futuros exámenes aleatorios.
9. Se confirma la desactivación al Tech Leader.

---

## 3. Trazabilidad con Reglas de Negocio

- **RN-LEAD-06 (No Eliminación Física de Reactivos):** Está estrictamente prohibido el borrado físico (`DELETE` relacional) de preguntas que hayan formado parte de al menos una evaluación ejecutada; la baja se aplica exclusivamente mediante conmutación de estado a `INACTIVO`.

---

<div align="center">

[Volver al Índice de la Fase 02: Análisis](/RUP/02-analisis/README.md)

</div>
