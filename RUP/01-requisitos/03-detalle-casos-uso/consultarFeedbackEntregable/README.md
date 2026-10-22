<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

</div>

# Caso de Uso: `consultarFeedbackEntregable()`

<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/consultarFeedbackEntregable/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/consultarFeedbackEntregable/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## 📋 Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `Alumno` |
| **Objetivo** | Permite al alumno revisar el veredicto formal y las anotaciones técnicas emitidas por el Tech Leader tras la revisión de código (*Code Review*) de un laboratorio práctico entregado. Presenta la calificación asignada, el estado final (`APROBADO` o `CAMBIOS_SOLICITADOS`) y las observaciones detalladas sobre la calidad, arquitectura y cobertura de pruebas del Pull Request. Si se requieren cambios, habilita la opción de corrección y reenvío. |
| **Precondición** | El alumno debe estar autenticado en la plataforma. El laboratorio práctico debe haber sido previamente entregado y evaluado por el Tech Leader. |
| **Postcondición Éxito** | El alumno toma conocimiento formal del estado y comentarios de su entrega de código. Si el dictamen es `CAMBIOS_SOLICITADOS`, se habilita el reenvío de la entrega con las correcciones implementadas. Si el dictamen es `APROBADO`, el laboratorio computa como aprobado para los requisitos del módulo. |

</div>

---

## 📑 Reglas de Negocio Asociadas

- **RN-FORM-06 (Revisión Obligatoria para Avance):** Ningún laboratorio puede considerarse superado sin la aprobación expresa (`APROBADO`) y calificación numérica superior o igual a 7.0/10.0 por parte del Tech Leader.

---

## 🔗 Referencias

* [Modelo del Dominio: MotorFormacion](/RUP/00-modelo-del-dominio/README.md)
* [Diagramas de Contexto por Actor](/RUP/01-requisitos/01-actores-casos-uso/README.md)
* [Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md)

---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
