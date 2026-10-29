<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [Fase 01: Requisitos](/RUP/01-requisitos/README.md) | [Fase 02: Análisis](/RUP/02-analisis/README.md) |
|:---:|:---:|:---:|:---:|

</div>

# Realización de Análisis: `editarPregunta()`

Este documento formaliza la colaboración de análisis entre clases estereotipadas Boundary-Control-Entity (BCE) que realiza el caso de uso `editarPregunta()`, permitiendo al Tech Leader ajustar enunciados, opciones de respuesta o baremos de un reactivo del banco de evaluación, garantizando la inmutabilidad de los exámenes que se encuentren en curso de resolución en ese mismo instante.

---

## 1. Diagrama de Clases de Análisis (VOPC)

El diagrama de clases participantes delimita las responsabilidades para la edición controlada del reactivo y el aislamiento de exámenes activos.

<div align="center">

![Diagrama de Clases de Análisis](clasesAnalisis.svg)
*Figura 1: Clases de análisis participantes en `editarPregunta()`.*

</div>

### Participantes y Estereotipos

| Clase | Estereotipo | Responsabilidad |
| :--- | :---: | :--- |
| **`LiderEquipo`** | `<<actor>>` | Tech Leader que modifica el contenido técnico o ponderación de una pregunta. |
| **`EditorPregunta`** | `<<boundary>>` | Interfaz interactiva para modificar el enunciado, taxonomía y alternativas de respuesta. |
| **`GestorBancoPreguntas`** | `<<control>>` | Controlador de lógica de negocio que orquesta el versionado del reactivo y el blindaje inmutable de exámenes en ejecución. |
| **`TechLeader`** | `<<entity>>` | Perfil del líder técnico tutor. |
| **`Pregunta`** | `<<entity>>` | Reactivo evaluativo cuya versión se incrementa al persistir los cambios. |
| **`Opcion`** | `<<entity>>` | Alternativas de respuesta sincronizadas con el nuevo contenido. |
| **`Test`** | `<<entity>>` | Examen que aísla una instantánea inmutable para los estudiantes o candidatos activos. |

---

## 2. Diagrama de Realización de Análisis (Secuencia BCE)

La interacción formaliza el congelamiento de instantáneas en memoria o persistencia para exámenes concurrentes.

<div align="center">

![Diagrama de Realización de Análisis](realizacionAnalisis.svg)
*Figura 2: Secuencia de mensajes BCE para `editarPregunta()`.*

</div>

### Flujo de Colaboración

1. El actor `LiderEquipo` abre el formulario de edición de una pregunta desde `EditorPregunta`.
2. `EditorPregunta` carga los datos completos del reactivo y sus alternativas de respuesta a través de `GestorBancoPreguntas`.
3. El Tech Leader realiza los ajustes deseados (enunciado, opciones, justificaciones o dificultad) y confirma la edición.
4. `GestorBancoPreguntas` interroga a `Test` para comprobar si existen sesiones de examen activas en curso que contengan dicho reactivo.
5. En virtud de **RN-LEAD-05**, si hay exámenes en curso de resolución, `Test` genera y congela una instantánea inmutable de la versión previa para que los usuarios no sufran alteraciones durante su evaluación.
6. Se actualizan los datos de `Pregunta` y se incrementa el número de versión del reactivo.
7. Se sincronizan las entidades `Opcion` asociadas.
8. Se confirma la edición exitosa al Tech Leader, asegurando que los nuevos tests generados utilizarán la versión recién actualizada.

---

## 3. Trazabilidad con Reglas de Negocio

- **RN-LEAD-05 (Inmutabilidad de Exámenes en Curso):** Si una pregunta está presente en un test que un candidato o alumno está respondiendo en ese instante, el examen en ejecución conserva una instantánea inmutable de la versión original.

---

<div align="center">

[Volver al Índice de la Fase 02: Análisis](/RUP/02-analisis/README.md)

</div>
