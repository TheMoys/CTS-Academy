<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [01 Requisitos](/RUP/01-requisitos/README.md) | [Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

</div>

# Caso de Uso: `solicitarCambiosEntregable()`

<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/solicitarCambiosEntregable/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/solicitarCambiosEntregable/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `LiderEquipo` |
| **Objetivo** | Permite al Tech Leader solicitar correcciones o refactorizaciones sobre un laboratorio práctico entregado por un alumno cuando el código no cumple con los estándares de calidad, presenta fallos en los tests del sandbox o carece de buenas prácticas arquitectónicas. Al registrarse, el estado del entregable cambia a `CAMBIOS_SOLICITADOS`, permitiendo al estudiante subsanar las observaciones y reenviar su Pull Request. |
| **Precondición** | El usuario debe estar autenticado con rol `LiderEquipo`. El entregable debe encontrarse en estado `PENDIENTE_REVISION`. |
| **Postcondición Éxito** | El entregable pasa a estado `CAMBIOS_SOLICITADOS`. Se registra el desglose de observaciones técnicas en la bitácora del entregable. El alumno recibe notificación inmediata y se le habilita la opción de reenvío de la entrega corregida. |

</div>

---

## Reglas de Negocio Asociadas

- **RN-LEAD-10 (Obligatoriedad de Feedback Constructivo):** Es mandatorio que toda solicitud de cambios incluya una explicación técnica detallada orientada a guiar al alumno en la subsanación de las deficiencias detectadas.

---

## Referencias

* [Modelo del Dominio: MotorFormacion](/RUP/00-modelo-del-dominio/README.md)
* [Diagramas de Contexto por Actor](/RUP/01-requisitos/01-actores-casos-uso/README.md)
* [Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md)

---

<div align="center">

[Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
