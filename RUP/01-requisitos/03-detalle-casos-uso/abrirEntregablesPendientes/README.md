<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [01 Requisitos](/RUP/01-requisitos/README.md) | [Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

</div>

# Caso de Uso: `abrirEntregablesPendientes()`

<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/abrirEntregablesPendientes/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/abrirEntregablesPendientes/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `LiderEquipo` |
| **Objetivo** | Permite al Tech Leader abrir y gestionar la bandeja centralizada de entregables de código (Pull Requests de GitHub) enviados por los alumnos de su equipo técnico CTS que se encuentran pendientes de evaluación. Presenta el estado de ejecución automática del pipeline de integración continua (*CI Sandbox*), la fecha de entrega y el tiempo transcurrido para asegurar el cumplimiento del acuerdo de nivel de servicio (SLA) de retroalimentación. |
| **Precondición** | El usuario debe estar autenticado con rol `LiderEquipo`. El Tech Leader debe tener alumnos asignados a su equipo CTS. |
| **Postcondición Éxito** | El sistema realiza la transición hacia el estado `REVISION_ENTREGABLES_ABIERTO`. Se presenta la cola ordenada de entregables priorizada por antigüedad de envío. Se habilita la selección individual para proceder a la revisión técnica detallada. |

</div>

---

## Reglas de Negocio Asociadas

- **RN-LEAD-07 (SLA de Code Review):** Todo entregable de alumno debe ser revisado y dictaminado por su Tech Leader en un plazo máximo no superior a 48 horas hábiles tras su envío.

---

## Referencias

* [Modelo del Dominio: MotorFormacion](/RUP/00-modelo-del-dominio/README.md)
* [Diagramas de Contexto por Actor](/RUP/01-requisitos/01-actores-casos-uso/README.md)
* [Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md)

---

<div align="center">

[Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
