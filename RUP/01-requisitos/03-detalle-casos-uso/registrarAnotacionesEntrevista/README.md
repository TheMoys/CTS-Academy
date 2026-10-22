<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|
</div>

# Caso de Uso: `registrarAnotacionesEntrevista()`


<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/registrarAnotacionesEntrevista/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/registrarAnotacionesEntrevista/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## 📋 Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `Gestor` (`GestorProfer`) |
| **Objetivo** | Registrar formalmente en la bitácora del expediente las observaciones cualitativas y la valoración tipificada de la rúbrica competencial obtenida durante la entrevista personal (Google Meet), consolidando la evidencia requerida para emitir el dictamen final de admisión |
| **Precondición** | El Gestor debe encontrarse autenticado y en el expediente del aspirante (`PERFIL_CANDIDATO_ABIERTO`); la entrevista debe estar en estado editable; el expediente no debe contar con dictamen definitivo cerrado |
| **Postcondición Éxito** | Entrada cualitativa incorporada como evento inmutable en la bitácora `Entrevista.anotaciones` con autoría, marca temporal, momento de captura y puntuaciones de rúbrica; el contexto permanece en `PERFIL_CANDIDATO_ABIERTO` |
| **Postcondición Bloqueo** | Si el expediente ya cuenta con resolución formal cerrada (`ADMITIDO` o `RECHAZADO`), el sistema bloquea cualquier entrada de datos y degrada la interfaz a modo de solo lectura |

</div>

---

## 📑 Reglas de Negocio Asociadas

1. **RN-ANOT-01 — Dimensiones Estructuradas de Rúbrica (ADR-007)**:
   * La evaluación cualitativa exige calificar obligatoriamente 4 dimensiones tipificadas en escala de 1 a 5 (Comunicación y argumentación técnica, Fit cultural con la metodología CTS, Actitud profesional y Compromiso con régimen on-site / movilidad), complementadas con observaciones de evidencia empírica.
2. **RN-ANOT-02 — Bitácora Append-Only y Trazabilidad Cronológica (ADR-009)**:
   * Las anotaciones operan bajo un modelo de eventos acumulativos (*append-only*), etiquetadas según el momento de captura (`PRE_ENTREVISTA`, `EN_SESION`, `POST_DELIBERACION`). Quedan prohibidas las modificaciones destructivas para salvaguardar la trazabilidad de la deliberación del comité evaluador.
3. **RN-ANOT-03 — Inmutabilidad Administrativa Post-Dictamen**:
   * Una vez formalizado el dictamen de admisión (`admitirAlumnoProfer()`) o rechazo (`rechazarCandidatura()`), la bitácora de anotaciones queda sellada de forma irrevocable para garantizar la seguridad jurídica del proceso selectivo.

---

## 🔗 Referencias

* [Modelo del Dominio: `Candidato`, `Entrevista`, `Gestor`](/RUP/00-modelo-del-dominio/README.md)
* [Diagrama de Contexto Gestor](/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoGestor.puml)
* [Caso de Uso: `abrirPerfilCandidato()`](/RUP/01-requisitos/03-detalle-casos-uso/abrirPerfilCandidato/README.md)
* [Caso de Uso: `agendarEntrevistaGoogleMeet()`](/RUP/01-requisitos/03-detalle-casos-uso/agendarEntrevistaGoogleMeet/README.md)
* [ADR-007: Admisión continua y batería de 3 tests diagnósticos](/RUP/BITACORA.md#adr-007-admisi%C3%B3n-continua-por-ciclos-acad%C3%A9micos-bater%C3%ADa-de-3-tests-e-inclusi%C3%B3n-de-entrevista)
* [ADR-009: Centralización del perfil de candidato y entrevista en el Gestor](/RUP/BITACORA.md#adr-009-centralizaci%C3%B3n-del-perfil-del-candidato-y-gesti%C3%B3n-de-entrevistas-en-el-gestor-profer)
---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
