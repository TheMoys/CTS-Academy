<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

</div>

# Caso de Uso: `editarPregunta()`

<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/editarPregunta/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/editarPregunta/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## 📋 Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `LiderEquipo` |
| **Objetivo** | Permite al Tech Leader ajustar el enunciado, las opciones de respuesta, la opción correcta o los parámetros métricos (dificultad, puntaje, tiempo sugerido) de una pregunta técnica registrada en el banco de evaluación. Los cambios aplican a futuros tests generados sin afectar los exámenes ya completados ni los que se encuentren en curso. |
| **Precondición** | El usuario debe estar autenticado con rol `LiderEquipo`. La pregunta técnica debe existir en el banco del equipo. |
| **Postcondición Éxito** | El reactivo técnico se actualiza en el catálogo de evaluación. Los nuevos tests técnicos generados a partir de ese momento utilizarán la versión actualizada del reactivo. |

</div>

---

## 📑 Reglas de Negocio Asociadas

- **RN-LEAD-05 (Inmutabilidad de Exámenes en Curso):** Si una pregunta está presente en un test que un candidato o alumno está respondiendo en ese instante, el examen en ejecución conserva una instantánea inmutable de la versión original.

---

## 🔗 Referencias

* [Modelo del Dominio: MotorFormacion](/RUP/00-modelo-del-dominio/README.md)
* [Diagramas de Contexto por Actor](/RUP/01-requisitos/01-actores-casos-uso/README.md)
* [Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md)

---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
