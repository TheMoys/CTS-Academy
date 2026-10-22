<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

</div>

# Caso de Uso: `consultarModulo()`

<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/consultarModulo/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/consultarModulo/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## 📋 Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `Alumno` |
| **Objetivo** | Permite al alumno acceder al contenido detallado de un módulo formativo que se encuentre habilitado en su itinerario. Presenta las guías didácticas, los diagramas de arquitectura, las consignas de laboratorios prácticos, el estado de las entregas y revisiones de código, y el acceso al test técnico de fin de módulo cuando todos los requisitos prácticos previos hayan sido completados y aprobados. |
| **Precondición** | El alumno debe estar autenticado en la plataforma. El módulo seleccionado debe estar en estado `EN_CURSO` o `APROBADO`. |
| **Postcondición Éxito** | El sistema realiza la transición hacia el estado `MODULO_ABIERTO`. Se presenta la lista completa de recursos didácticos con opción de visualización. Se presentan los laboratorios prácticos habilitando el envío o la consulta de retroalimentación según corresponda. Se habilita el botón de inicio del test técnico únicamente si todos los laboratorios están aprobados. |

</div>

---

## 📑 Reglas de Negocio Asociadas

- **RN-FORM-04 (Habilitación del Test de Nivelación):** El test técnico de fin de módulo permanece estrictamente inactivo mientras existan laboratorios prácticos sin entregar o en estado distinto de `APROBADO`.

---

## 🔗 Referencias

* [Modelo del Dominio: MotorFormacion](/RUP/00-modelo-del-dominio/README.md)
* [Diagramas de Contexto por Actor](/RUP/01-requisitos/01-actores-casos-uso/README.md)
* [Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md)

---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
