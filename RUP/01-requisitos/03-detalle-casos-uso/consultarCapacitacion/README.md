<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [01 Requisitos](/RUP/01-requisitos/README.md) | [Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

</div>

# Caso de Uso: `consultarCapacitacion()`

<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/consultarCapacitacion/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/consultarCapacitacion/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `Alumno` |
| **Objetivo** | Permite al alumno consultar la hoja de ruta formativa completa (itinerario de especialización) vinculada a su equipo técnico CTS. Presenta la secuencia curricular de módulos, las competencias técnicas a desarrollar, las estimaciones horarias, los estados de desbloqueo de cada módulo y los requisitos necesarios para avanzar en el itinerario formativo. |
| **Precondición** | El alumno debe estar autenticado en la plataforma. El alumno debe tener asignado un rol técnico y un equipo CTS con un itinerario formativo activo. |
| **Postcondición Éxito** | El sistema realiza la transición hacia el estado `CAPACITACION_ABIERTO`. Se presentan todos los módulos formativos con su estado correspondiente (`APROBADO`, `EN_CURSO` o `BLOQUEADO`). Se permite acceder al detalle de los módulos que se encuentren activos o completados. |

</div>

---

## Reglas de Negocio Asociadas

- **RN-FORM-03 (Bloqueo de Módulos Futuros):** Un módulo en estado `BLOQUEADO` no permite el acceso a sus laboratorios ni al test técnico hasta que el módulo anterior sea formalmente aprobado por el Tech Leader.

---

## Referencias

* [Modelo del Dominio: MotorFormacion](/RUP/00-modelo-del-dominio/README.md)
* [Diagramas de Contexto por Actor](/RUP/01-requisitos/01-actores-casos-uso/README.md)
* [Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md)

---

<div align="center">

[Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
