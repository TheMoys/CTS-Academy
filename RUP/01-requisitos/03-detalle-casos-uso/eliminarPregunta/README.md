<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

</div>

# Caso de Uso: `eliminarPregunta()`

<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/eliminarPregunta/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/eliminarPregunta/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## 📋 Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `LiderEquipo` |
| **Objetivo** | Permite al Tech Leader dar de baja o desactivar una pregunta técnica del banco de evaluación de su especialidad. Para salvaguardar la coherencia estadística y la trazabilidad de los exámenes completados en el pasado, la eliminación se procesa como un borrado lógico (*soft delete*), cambiando el estado del reactivo a `INACTIVO`. |
| **Precondición** | El usuario debe estar autenticado con rol `LiderEquipo`. La pregunta técnica debe existir y encontrarse actualmente activa en el banco. |
| **Postcondición Éxito** | La pregunta técnica cambia su estado a `INACTIVO`. Queda excluida de los algoritmos de generación y aleatorización de nuevos exámenes. Se conservan todas las respuestas históricas asociadas a esta pregunta en evaluaciones ya cerradas. |

</div>

---

## 📑 Reglas de Negocio Asociadas

- **RN-LEAD-06 (No Eliminación Física de Reactivos):** Está estrictamente prohibido el borrado físico (`DELETE` relacional) de preguntas que hayan formado parte de al menos una evaluación ejecutada.

---

## 🔗 Referencias

* [Modelo del Dominio: MotorFormacion](/RUP/00-modelo-del-dominio/README.md)
* [Diagramas de Contexto por Actor](/RUP/01-requisitos/01-actores-casos-uso/README.md)
* [Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md)

---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
