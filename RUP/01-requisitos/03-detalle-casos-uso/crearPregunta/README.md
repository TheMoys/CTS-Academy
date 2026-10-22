<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

</div>

# Caso de Uso: `crearPregunta()`

<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/crearPregunta/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/crearPregunta/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## 📋 Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `LiderEquipo` |
| **Objetivo** | Permite al Tech Leader incorporar nuevos reactivos de evaluación técnica al banco de preguntas del sistema (utilizado tanto para tests diagnósticos de candidatos como para evaluaciones técnicas de fin de módulo de los alumnos tutelados). Soporta preguntas teóricas de opción múltiple (MCQ) y retos prácticos con plantillas base. |
| **Precondición** | El usuario debe estar autenticado con rol `LiderEquipo`. El Tech Leader debe tener acceso al banco de preguntas de su especialidad técnica. |
| **Postcondición Éxito** | La nueva pregunta queda registrada en estado `ACTIVA` asociada al banco de reactivos. Queda disponible para ser seleccionada aleatoriamente en la generación de tests técnicos. |

</div>

---

## 📑 Reglas de Negocio Asociadas

- **RN-LEAD-04 (Composición de Banco):** Cada pregunta debe estar catalogada obligatoriamente por dificultad (`BÁSICO`, `INTERMEDIO`, `AVANZADO`) para permitir el balanceo automático del motor de tests.

---

## 🔗 Referencias

* [Modelo del Dominio: MotorFormacion](/RUP/00-modelo-del-dominio/README.md)
* [Diagramas de Contexto por Actor](/RUP/01-requisitos/01-actores-casos-uso/README.md)
* [Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md)

---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
