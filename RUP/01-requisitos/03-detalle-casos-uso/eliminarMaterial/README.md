<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [01 Requisitos](/RUP/01-requisitos/README.md) | [Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

</div>

# Caso de Uso: `eliminarMaterial()`

<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/eliminarMaterial/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/eliminarMaterial/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `LiderEquipo` |
| **Objetivo** | Permite al Tech Leader despublicar o eliminar lógicamente un recurso didáctico de un módulo formativo bajo su tutela. Requiere confirmación explícita para evitar supresiones accidentales y preserva la auditoría histórica de lecturas previas. |
| **Precondición** | El usuario debe estar autenticado con rol `LiderEquipo`. El recurso didáctico debe existir en el módulo correspondiente. |
| **Postcondición Éxito** | El recurso didáctico se marca como inactivo / eliminado lógicamente en la base de datos. Deja de mostrarse en el temario accesible por los alumnos del equipo. Se reindexa el orden secuencial de los materiales restantes del módulo. |

</div>

---

## Reglas de Negocio Asociadas

- **RN-LEAD-03 (Baja No Destructiva):** La eliminación es siempre lógica para preservar el histórico de métricas de lectura de alumnos de cohortes previas.

---

## Referencias

* [Modelo del Dominio: MotorFormacion](/RUP/00-modelo-del-dominio/README.md)
* [Diagramas de Contexto por Actor](/RUP/01-requisitos/01-actores-casos-uso/README.md)
* [Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md)

---

<div align="center">

[Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
