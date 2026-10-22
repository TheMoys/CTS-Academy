<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

</div>

# Caso de Uso: `evaluarCapacitacionAlumno()`

<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/evaluarCapacitacionAlumno/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/evaluarCapacitacionAlumno/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## 📋 Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `LiderEquipo` |
| **Objetivo** | Permite al Tech Leader emitir el informe final de desempeño y certificación de un alumno que ha completado la totalidad de los módulos formativos de su itinerario en el equipo técnico CTS. Evalúa competencias clave (arquitectura, calidad de software, autonomía y trabajo colaborativo) y emite el dictamen formal sobre su aptitud para integrarse a proyectos productivos reales de la organización. |
| **Precondición** | El usuario debe estar autenticado con rol `LiderEquipo`. El alumno tutelado debe haber completado el 100% de los módulos formativos y laboratorios exigidos en su itinerario. |
| **Postcondición Éxito** | Se genera y archiva el acta formal de evaluación final de capacitación. El estado del alumno pasa a `CAPACITACION_CONCLUIDA`. Se notifica automáticamente al Gestor de Admisiones y al Alumno con el informe de competencias. |

</div>

---

## 📑 Reglas de Negocio Asociadas

- **RN-LEAD-11 (Requisito de Completitud Curricular):** No es posible iniciar la evaluación final de capacitación si el alumno mantiene algún laboratorio en estado no aprobado o módulos pendientes de cursar.

---

## 🔗 Referencias

* [Modelo del Dominio: MotorFormacion](/RUP/00-modelo-del-dominio/README.md)
* [Diagramas de Contexto por Actor](/RUP/01-requisitos/01-actores-casos-uso/README.md)
* [Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md)

---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
