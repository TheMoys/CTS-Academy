<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

<sub>**Fase 01 Requisitos** › **Detalle de Caso de Uso** › `abrirPanelPostulacion()`</sub>

</div>

# Caso de Uso: `abrirPanelPostulacion()`


<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/abrirPanelPostulacion/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/abrirPanelPostulacion/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## 📋 Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `Candidato` (aspirante autenticado en proceso de admisión internacional) |
| **Objetivo** | Proporcionar al aspirante la visión unificada de su expediente de postulación, la fecha límite de la convocatoria y el estado de disponibilidad y ejecución de la batería de 3 tests diagnósticos (`TestActitud`, `TestAptitud`, `TestTecnico`), permitiendo iniciar o reanudar pruebas según las reglas de negocio |
| **Tipo** | Primario, esencial |
| **Nivel** | Objetivo de usuario |
| **Precondición** | El actor debe estar autenticado con rol `Candidato`; el expediente debe existir y estar vinculado a una convocatoria activa |
| **Postcondición Éxito** | Panel de postulación presentado con datos del expediente, convocatoria, estado individual de cada instrumento evaluativo y controles de inicio/reanudación habilitados según corresponda; contexto en `PANEL_POSTULACION_ABIERTO` |
| **Postcondición Fuera de Plazo** | Si la convocatoria alcanzó su fecha límite de cierre, el panel se presenta en modo de solo lectura, deshabilitando cualquier acción de inicio o reanudación |

</div>

---

## 📑 Reglas de Negocio Asociadas

1. **RN-POST-01 — Bloqueo Cruzado Multisesión**:
   * Si cualquier test de la batería se encuentra en estado `EN_CURSO`, los controles de inicio de los demás tests se presentan bloqueados e inhabilitados tanto en la interfaz como en la validación transaccional del backend. Se prohíbe taxativamente la ejecución simultánea o concurrente de más de un test.
2. **RN-POST-02 — Opacidad Absoluta de Indicadores (ADR-007)**:
   * La interfaz del candidato no expone puntuaciones, porcentajes de acierto ni notas de corte. Los estados visualizados para cada test son puramente procesales: `Pendiente`, `En curso`, `Completado` o `Tiempo agotado`.
3. **RN-POST-03 — Orden Flexible de la Batería de Tests**:
   * El aspirante tiene total libertad para rendir los 3 tests diagnósticos pendientes en el orden de su preferencia. Cada test cuenta con un único intento ininterrumpido.
4. **RN-POST-04 — Reconciliación Activa del Cronómetro en Servidor**:
   * Al invocar este caso de uso, el backend recalcula el tiempo remanente de cualquier evaluación con estado `EN_CURSO`. Si el temporizador del servidor expiró durante un corte de conexión o cierre del navegador, el sistema transiciona pasivamente el test a `EXPIRADO` y desbloquea el resto de la batería.
5. **RN-POST-05 — Delimitación de Agenda y Entrevistas (ADR-009)**:
   * El panel del candidato no incluye selectores de cita ni enlaces directos a Google Meet; la convocatoria a entrevista y su calendarización es responsabilidad exclusiva del `Gestor`.

---

## 🔗 Referencias

* [Modelo del Dominio: `Candidato`, `Convocatoria`, `Test`](/RUP/00-modelo-del-dominio/README.md)
* [Diagrama de Estados de Test](/RUP/00-modelo-del-dominio/estados-entidades/test-estados.puml)
* [Diagrama de Contexto Candidato](/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoCandidato.puml)
* [ADR-007: Admisión continua y batería de 3 tests diagnósticos](/RUP/BITACORA.md#adr-007-admisi%C3%B3n-continua-por-ciclos-acad%C3%A9micos-bater%C3%ADa-de-3-tests-e-inclusi%C3%B3n-de-entrevista)
* [ADR-009: Centralización del perfil de candidato y entrevista en el Gestor](/RUP/BITACORA.md#adr-009-centralizaci%C3%B3n-del-perfil-del-candidato-y-gesti%C3%B3n-de-entrevistas-en-el-gestor-profer)
---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
