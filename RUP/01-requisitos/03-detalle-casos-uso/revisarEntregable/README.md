<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [01 Requisitos](/RUP/01-requisitos/README.md) | [Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

</div>

# Caso de Uso: `revisarEntregable()`

<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/revisarEntregable/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/revisarEntregable/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `LiderEquipo` |
| **Objetivo** | Permite al Tech Leader inspeccionar detalladamente un entregable de laboratorio práctico presentado por un alumno. Presenta la información completa de la entrega: el enlace al Pull Request de GitHub, la rama de trabajo, las notas explicativas del estudiante, el informe del runner de pruebas automatizadas en contenedor Docker y los criterios de la rúbrica técnica de evaluación, habilitando la posterior emisión de dictamen de aprobación o solicitud de cambios. |
| **Precondición** | El usuario debe estar autenticado con rol `LiderEquipo`. El entregable debe encontrarse en estado `PENDIENTE_REVISION`. |
| **Postcondición Éxito** | El sistema presenta el expediente completo de la entrega de código. Se habilita la selección de las acciones resolutivas: aprobar formalmente el entregable o requerir cambios técnicos. |

</div>

---

## Reglas de Negocio Asociadas

- **RN-LEAD-08 (Auditoría Integral):** La revisión debe contemplar tanto la aprobación sintáctica de los tests automáticos en el sandbox como la evaluación cualitativa de legibilidad, arquitectura y estándares de código por parte del Tech Leader.

---

## Referencias

* [Modelo del Dominio: MotorFormacion](/RUP/00-modelo-del-dominio/README.md)
* [Diagramas de Contexto por Actor](/RUP/01-requisitos/01-actores-casos-uso/README.md)
* [Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md)

---

<div align="center">

[Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
