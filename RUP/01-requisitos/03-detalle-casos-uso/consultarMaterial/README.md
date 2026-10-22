<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

</div>

# Caso de Uso: `consultarMaterial()`

<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/consultarMaterial/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/consultarMaterial/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## 📋 Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `Alumno` |
| **Objetivo** | Permite al alumno abrir y leer un material didáctico (guía técnica en Markdown, diagrama de arquitectura de sistemas, recurso interactivo o enlace a repositorio de referencia) perteneciente a un módulo formativo activo. Al finalizar la lectura, el sistema registra el evento para computar el porcentaje de avance del alumno en los recursos teóricos del módulo. |
| **Precondición** | El alumno debe estar autenticado en la plataforma. El módulo formativo al que pertenece el material debe estar habilitado (`EN_CURSO` o `APROBADO`). |
| **Postcondición Éxito** | El material queda marcado como leído en el expediente formativo del alumno. Se recalculan los indicadores de avance del módulo. El sistema retorna al estado `MODULO_ABIERTO`. |

</div>

---

## 📑 Reglas de Negocio Asociadas

- **RN-FORM-05 (Computo de Lectura Requerida):** Para considerar un módulo listo para evaluación de fin de módulo, el alumno debe haber registrado la lectura del 100% de los materiales catalogados como obligatorios por el Tech Leader.

---

## 🔗 Referencias

* [Modelo del Dominio: MotorFormacion](/RUP/00-modelo-del-dominio/README.md)
* [Diagramas de Contexto por Actor](/RUP/01-requisitos/01-actores-casos-uso/README.md)
* [Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md)

---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
