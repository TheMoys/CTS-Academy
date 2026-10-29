<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [Fase 01: Requisitos](/RUP/01-requisitos/README.md) | [Fase 02: Análisis](/RUP/02-analisis/README.md) |
|:---:|:---:|:---:|:---:|

</div>

# Realización de Análisis: `crearPregunta()`

Este documento formaliza la colaboración de análisis entre clases estereotipadas Boundary-Control-Entity (BCE) que realiza el caso de uso `crearPregunta()`, permitiendo al Tech Leader dar de alta un nuevo reactivo técnico en el banco de evaluación (preguntas teóricas de opción múltiple MCQ o consignas prácticas) con catalogación obligatoria por nivel de dificultad para el balanceo de exámenes.

---

## 1. Diagrama de Clases de Análisis (VOPC)

El diagrama de clases participantes delimita las responsabilidades de captura, validación de dificultad y estructuración de opciones de respuesta.

<div align="center">

![Diagrama de Clases de Análisis](clasesAnalisis.svg)
*Figura 1: Clases de análisis participantes en `crearPregunta()`.*

</div>

### Participantes y Estereotipos

| Clase | Estereotipo | Responsabilidad |
| :--- | :---: | :--- |
| **`LiderEquipo`** | `<<actor>>` | Tech Leader que formula reactivos para el banco de evaluación. |
| **`EditorPregunta`** | `<<boundary>>` | Interfaz gráfica para redactar el enunciado, fijar puntajes y asociar opciones de respuesta con explicaciones técnicas. |
| **`GestorBancoPreguntas`** | `<<control>>` | Controlador de lógica de negocio que valida la catalogación por dificultad y orquesta el alta del reactivo. |
| **`TechLeader`** | `<<entity>>` | Perfil del líder técnico tutor. |
| **`Modulo`** | `<<entity>>` | Unidad temática formativa a la cual se asocia el reactivo. |
| **`Pregunta`** | `<<entity>>` | Reactivo evaluativo que almacena enunciado, dificultad y puntaje base. |
| **`Opcion`** | `<<entity>>` | Alternativa de respuesta con su marca de corrección y justificación pedagógica. |

---

## 2. Diagrama de Realización de Análisis (Secuencia BCE)

La interacción formaliza la validación de la taxonomía del reactivo antes de su publicación en el banco de evaluación.

<div align="center">

![Diagrama de Realización de Análisis](realizacionAnalisis.svg)
*Figura 2: Secuencia de mensajes BCE para `crearPregunta()`.*

</div>

### Flujo de Colaboración

1. El actor `LiderEquipo` solicita registrar un nuevo reactivo desde `EditorPregunta`.
2. El Tech Leader ingresa el enunciado, tipo (teórico MCQ o práctico), dificultad, puntaje y alternativas de respuesta con su respectiva justificación.
3. `EditorPregunta` invoca al controlador `GestorBancoPreguntas` (`darDeAltaPregunta(...)`).
4. En cumplimiento de **RN-LEAD-04**, `GestorBancoPreguntas` valida que la dificultad esté obligatoriamente catalogada (`BÁSICO`, `INTERMEDIO` o `AVANZADO`). Si el campo está ausente, se deniega la transacción reportando el error.
5. Verificada la taxonomía, se valida la existencia del módulo receptor en `Modulo`.
6. Se crea la entidad `Pregunta` inicializada en estado activo.
7. Se persisten las entidades hijas `Opcion` asociadas al reactivo.
8. Se confirma la incorporación exitosa al Tech Leader y el reactivo queda disponible para la generación aleatoria de pruebas.

---

## 3. Trazabilidad con Reglas de Negocio

- **RN-LEAD-04 (Composición de Banco):** Cada pregunta debe estar catalogada obligatoriamente por dificultad (`BÁSICO`, `INTERMEDIO`, `AVANZADO`) para permitir el balanceo automático del motor de tests de admisión y de nivelación de módulos.

---

<div align="center">

[Volver al Índice de la Fase 02: Análisis](/RUP/02-analisis/README.md)

</div>
