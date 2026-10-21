<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

<sub>**Fase 01 Requisitos** › **Detalle de Caso de Uso** › `admitirAlumnoProfer()`</sub>

</div>

# Caso de Uso: `admitirAlumnoProfer()`


<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/admitirAlumnoProfer/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/admitirAlumnoProfer/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## 📋 Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `Gestor` (`GestorProfer`) |
| **Objetivo** | Formalizar la resolución favorable de admisión de un aspirante, promoviendo la entidad `Candidato` a `Alumno` (`AlumnoProfer`), asignándolo obligatoriamente a uno de los 6 equipos de desarrollo de CTS con un rol técnico específico, matriculándolo en la capacitación del equipo y despachando la carta de admisión institucional |
| **Tipo** | Primario, esencial para la gobernanza |
| **Nivel** | Objetivo de usuario |
| **Precondición** | El Gestor debe encontrarse autenticado y en el expediente del aspirante (`PERFIL_CANDIDATO_ABIERTO`); la candidatura debe estar en estado `EVALUACION_COMPLETADA` o con entrevista cualitativa realizada; el equipo seleccionado debe contar con plazas disponibles en el periodo activo |
| **Postcondición Éxito** | Entidad `Candidatura` transiciona a `ADMITIDO`; se crea la instancia `Alumno` vinculada a `Equipo`, `LiderEquipo` y `Capacitacion`; se generan credenciales de acceso para rol `Alumno`; se despachan notificaciones transaccionales a candidato y sede; el contexto transiciona a `PANEL_ADMISIONES_ABIERTO` |
| **Postcondición Bloqueo** | Si el expediente ya contaba con dictamen previo o el equipo seleccionado no dispone de vacantes, el sistema emite un aviso de bloqueo y mantiene al Gestor en el perfil sin alterar el estado |

</div>

---

## 📑 Reglas de Negocio Asociadas

1. **RN-ADM-01 — Asignación Obligatoria de Equipo y Rol Técnico**:
   * Ningún candidato puede ser admitido sin asignación explícita a uno de los 6 equipos formadores de CTS (`Equipo 01` a `Equipo 06`) y a un rol técnico junior específico, vinculándose de inmediato al `LiderEquipo` tutor responsable de su seguimiento y code reviews.
2. **RN-ADM-02 — Control de Plazas y Capacidad por Equipo**:
   * Cada equipo de desarrollo cuenta con una cuota máxima de becarios por ciclo académico (definida en `MotorEquipos`). El sistema valida la disponibilidad de vacantes en el momento de la confirmación, bloqueando la admisión si el cupo se encuentra saturado.
3. **RN-ADM-03 — Promoción de Rol y Activación de Credenciales**:
   * La admisión ejecuta la transición de rol en el subsistema de acceso (`PK01 - Acceso`). Las credenciales anteriores de `Candidato` quedan revocadas y se generan los permisos operativos de `Alumno`, habilitando el acceso a `INICIO_ALUMNO_ABIERTO` y a los módulos de formación.
4. **RN-ADM-04 — Inmutabilidad del Dictamen Favorable**:
   * Una vez formalizada la admisión, el expediente del candidato queda cerrado permanentemente en la convocatoria, impidiendo reactivaciones o modificaciones directas sin un procedimiento formal de baja.

---

## 🔗 Referencias

* [Modelo del Dominio: `Candidato`, `Alumno`, `Equipo`, `LiderEquipo`](/RUP/00-modelo-del-dominio/README.md)
* [Diagrama de Estados de Candidatura (`REGISTRADO` → `EN_EVALUACION` → `ADMITIDO`)](/RUP/00-modelo-del-dominio/estados-entidades/candidatura-estados.puml)
* [Diagrama de Contexto Gestor](/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoGestor.puml)
* [Caso de Uso: `abrirPerfilCandidato()`](/RUP/01-requisitos/03-detalle-casos-uso/abrirPerfilCandidato/README.md)
* [ADR-007: Admisión continua y batería de 3 tests diagnósticos](/RUP/BITACORA.md#adr-007-admisi%C3%B3n-continua-por-ciclos-acad%C3%A9micos-bater%C3%ADa-de-3-tests-e-inclusi%C3%B3n-de-entrevista)
---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
