<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

</div>

# Caso de Uso: `aprobarEntregable()`

<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/aprobarEntregable/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/aprobarEntregable/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## 📋 Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `LiderEquipo` |
| **Objetivo** | Permite al Tech Leader emitir el dictamen formal de aprobación (`APROBADO`) sobre un entregable práctico presentado por un alumno. El evaluador asigna una calificación numérica igual o superior a 7.0/10.0, completa la rúbrica multidimensional (diseño, código y pruebas) y redacta la retroalimentación cualitativa. Al registrarse, el sistema actualiza el avance curricular del alumno y evalúa si se desbloquea el siguiente hito formativo. |
| **Precondición** | El usuario debe estar autenticado con rol `LiderEquipo`. El entregable debe encontrarse en estado `PENDIENTE_REVISION`. |
| **Postcondición Éxito** | El entregable pasa a estado `APROBADO`. Se registra la calificación y el feedback cualitativo en el expediente del alumno. Se actualiza el avance porcentual del módulo correspondiente. Si todos los laboratorios del módulo están aprobados, se habilita el acceso al test técnico de fin de módulo. |

</div>

---

## 📑 Reglas de Negocio Asociadas

- **RN-LEAD-09 (Umbral Aprobatorio):** La nota mínima requerida para certificar un laboratorio práctico como `APROBADO` es de 7.0 puntos sobre 10.0.

---

## 🔗 Referencias

* [Modelo del Dominio: MotorFormacion](/RUP/00-modelo-del-dominio/README.md)
* [Diagramas de Contexto por Actor](/RUP/01-requisitos/01-actores-casos-uso/README.md)
* [Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md)

---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
