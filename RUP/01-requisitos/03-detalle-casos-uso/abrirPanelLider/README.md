<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [01 Requisitos](/RUP/01-requisitos/README.md) | [Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|
</div>

# Caso de Uso: `abrirPanelLider()`


<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/abrirPanelLider/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/abrirPanelLider/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `LiderEquipo` (Tech Leader - TL) |
| **Objetivo** | Proporcionar al Tech Leader el panel de gobierno técnico y formativo de su equipo asignado, centralizando la supervisión de sus alumnos PROFER, las alertas de Pull Requests pendientes de Code Review y el estado de sus módulos y banco de reactivos |
| **Precondición** | El actor debe encontrarse autenticado con rol `LiderEquipo` (`SESION_CERRADA` $\rightarrow$ `PANEL_LIDER_ABIERTO`) |
| **Postcondición Éxito** | Dashboard del Tech Leader presentado con alumnos del equipo, entregables pendientes de revisión y accesos directos a módulos formativos y banco de preguntas |

</div>

---

## Reglas de Negocio Asociadas

1. **RN-TL-01 — Aislamiento y Ámbito de Equipo**:
   * El Tech Leader únicamente accede y supervisa a los alumnos y contenidos correspondientes al `Equipo` CTS del cual es titular. No tiene visibilidad sobre la cartera global de candidatos (reservada al Gestor).
2. **RN-TL-02 — Alertas de Code Review**:
   * El panel destaca con alta prioridad los Pull Requests de laboratorio en estado `PENDIENTE_REVISION` para agilizar el ciclo de feedback formativo con los becarios.

---

## Referencias

* [Modelo del Dominio: `LiderEquipo`, `Equipo`, `Alumno`, `Modulo`](/RUP/00-modelo-del-dominio/README.md)
* [Diagrama de Contexto LiderEquipo](/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoLiderEquipo.puml)
---

<div align="center">

[Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
