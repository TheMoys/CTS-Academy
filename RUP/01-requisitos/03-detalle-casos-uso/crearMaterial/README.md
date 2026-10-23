<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [01 Requisitos](/RUP/01-requisitos/README.md) | [Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

</div>

# Caso de Uso: `crearMaterial()`

<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/crearMaterial/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/crearMaterial/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `LiderEquipo` (Tech Leader de equipo técnico CTS) |
| **Objetivo** | Permite al Tech Leader diseñar y publicar un nuevo recurso didáctico (guía técnica en Markdown, diagrama arquitectónico, especificación de laboratorio o recurso de referencia) dentro de un módulo formativo bajo su tutela. El material creado queda inmediatamente accesible para los alumnos asignados al equipo. |
| **Precondición** | El usuario debe estar autenticado con rol `LiderEquipo`. El Tech Leader debe tener permisos sobre el módulo seleccionado dentro de su equipo CTS asignado. |
| **Postcondición Éxito** | El nuevo recurso didáctico queda almacenado en la base de datos vinculado al módulo y orden de lectura establecido. Los alumnos del equipo pueden consultar el nuevo material en su temario. |

</div>

---

## Reglas de Negocio Asociadas

- **RN-LEAD-01 (Propiedad de Módulos):** Un Tech Leader solo puede dar de alta o modificar materiales en los módulos asociados a su equipo técnico CTS.

---

## Referencias

* [Modelo del Dominio: MotorFormacion](/RUP/00-modelo-del-dominio/README.md)
* [Diagramas de Contexto por Actor](/RUP/01-requisitos/01-actores-casos-uso/README.md)
* [Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md)

---

<div align="center">

[Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
