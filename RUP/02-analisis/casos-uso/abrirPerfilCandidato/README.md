<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [01 Requisitos](/RUP/01-requisitos/README.md) | [02 Análisis](/RUP/02-analisis/README.md) | [Catálogo Requisitos](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

<sub>**Fase 02 Análisis** › **Realización de Casos de Uso** › `abrirPerfilCandidato()`</sub>

</div>

# Realización de Caso de Uso: `abrirPerfilCandidato()`

Esta especificación describe la realización de análisis del caso de uso `abrirPerfilCandidato()` mediante clases BCE, detallando la consolidación centralizada del expediente del aspirante, el cálculo del radar de afinidades disciplinarias hacia los 6 equipos de CTS y la habilitación de acciones resolutorias (ADR-009).

---

<div align=center>

| Diagrama de Clases de Análisis (VOPC) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/abrirPerfilCandidato/clasesAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](clasesAnalisis.puml)</i></sup> |

| Diagrama de Realización de Análisis (Secuencia BCE) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/abrirPerfilCandidato/realizacionAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](realizacionAnalisis.puml)</i></sup> |

</div>

---

## Clases de Análisis Participantes

<div align=center>

| Clase | Estereotipo | Tipo | Responsabilidad Principal |
| :--- | :---: | :---: | :--- |
| **`PerfilCandidato`** | `<<boundary>>` | Frontera | Interfaz unificada del expediente de admisión; renderizado de radares diagnósticos de aptitud/actitud, estado del enlace Google Meet, bitácora cualitativa y botones de resolución. |
| **`GestorAdmisiones`** | `<<control>>` | Control | Orquestación de la carga de expediente, agregación de resultados de la batería de tests, cálculo de afinidades hacia los 6 equipos CTS y recuperación del estado de la entrevista. |
| **`Candidato`** | `<<entity>>` | Entidad | Aspirante internacional; custodia el identificador de expediente, sede remitente, estado procesal y relaciones hacia tests y entrevista personal. |
| **`Resultado`** | `<<entity>>` | Entidad | Métricas diagnósticas calculadas; expone indicadores de rendimiento por áreas disciplinarias para calcular la idoneidad técnica. |
| **`Entrevista`** | `<<entity>>` | Entidad | Registro de la sesión personal; custodia la fecha programada, enlace Meet sincronizado y bitácora de anotaciones cualitativas. |

</div>

---

## Flujo de Realización (Colaboración BCE)

### Flujo Principal: Apertura y Consolidación del Expediente
1. El **`Gestor`** selecciona un aspirante desde el panel general de admisiones.
2. **`PerfilCandidato`** solicita a **`GestorAdmisiones`** la carga completa del expediente mediante `abrirPerfilCandidato(idCandidato)`.
3. **`GestorAdmisiones`** recupera la entidad **`Candidato`** desde la persistencia.
4. **`GestorAdmisiones`** recupera las instancias de **`Resultado`** de los tests completados (`Actitud`, `Aptitud`, `Tecnico`).
5. **Cálculo de Afinidades por Equipos (ADR-009)**: **`GestorAdmisiones`** procesa los reactivos técnicos multidisciplinares, ponderando la afinidad porcentual hacia cada uno de los 6 squads técnicos de CTS.
6. **`GestorAdmisiones`** consulta la entidad **`Entrevista`** asociada para conocer si la sesión en Google Meet está pendiente, agendada o finalizada.
7. Se emite el expediente unificado hacia **`PerfilCandidato`**, que despliega los radares de competencias y habilita las acciones de contextuales (`agendarEntrevistaGoogleMeet`, `registrarAnotacionesEntrevista`, `admitirAlumnoProfer` o `rechazarCandidatura`).

### Flujo Alternativo: Expediente Inexistente
1. Si el identificador del candidato no se encuentra registrado, **`GestorAdmisiones`** retorna un error de entidad no encontrada y la frontera redirige al Gestor al listado general de admisiones.

---

## Trazabilidad con la Fase de Requisitos

| Requisito / Artefacto Fase 01 | Realización en Fase 02 (Análisis) |
| :--- | :--- |
| **Caso de Uso `abrirPerfilCandidato()`** | Coordinación en `GestorAdmisiones` unificando `PerfilCandidato` con `Candidato`, `Resultado` y `Entrevista`. |
| **Centralización en el Perfil (ADR-009)** | La frontera `PerfilCandidato` agrupa diagnósticos, Meet y resoluciones en un único punto focal. |
| **Recomendación por Equipos** | Algoritmo `calcularAfinidadEquipos()` en `GestorAdmisiones` ponderando reactivos por equipo. |

---

<div align="center">

[Volver a Fase 02: Análisis](/RUP/02-analisis/README.md) • [Ver Especificación de Requisitos (Fase 01)](/RUP/01-requisitos/03-detalle-casos-uso/abrirPerfilCandidato/README.md)

</div>
