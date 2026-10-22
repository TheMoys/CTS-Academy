<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

</div>

# Caso de Uso: `editarMaterial()`

<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/editarMaterial/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/editarMaterial/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## 📋 Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `LiderEquipo` |
| **Objetivo** | Permite al Tech Leader actualizar el contenido pedagógico, los metadatos o los archivos adjuntos de un recurso didáctico existente dentro de los módulos asignados a su equipo. Los cambios surten efecto de manera inmediata para los estudiantes. |
| **Precondición** | El usuario debe estar autenticado con rol `LiderEquipo`. El recurso didáctico a editar debe existir y pertenecer a un módulo del equipo del Tech Leader. |
| **Postcondición Éxito** | El recurso didáctico se actualiza con la nueva versión del contenido. Los alumnos que abran el recurso accederán a la versión modificada sin alterar su registro de lecturas históricas. |

</div>

---

## 📑 Reglas de Negocio Asociadas

- **RN-LEAD-02 (Preservación de Trazabilidad):** Las modificaciones a guías formativas no invalidan las lecturas ya completadas por los alumnos que las leyeron previamente.

---

## 🔗 Referencias

* [Modelo del Dominio: MotorFormacion](/RUP/00-modelo-del-dominio/README.md)
* [Diagramas de Contexto por Actor](/RUP/01-requisitos/01-actores-casos-uso/README.md)
* [Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md)

---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
