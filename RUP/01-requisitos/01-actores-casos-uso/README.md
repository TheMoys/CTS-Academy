<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [Bitácora ADR](/RUP/BITACORA.md) | [00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [01 Requisitos](/RUP/01-requisitos/README.md) | [02 Análisis](/RUP/02-analisis/README.md) | [03 Diseño](/RUP/03-diseño/README.md) | [04 Desarrollo](/RUP/04-desarrollo/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|

**Fase 01 Requisitos:** **Actores y Contexto** • [Catálogo y Detalle de Casos de Uso (35)](/RUP/01-requisitos/03-detalle-casos-uso/README.md)

</div>

# Actores y Casos de Uso — Fase 01: Requisitos

En esta fase se formalizan los actores que interactúan con **CTS Academy & Evaluator** y el catálogo completo de casos de uso del sistema estructurados en sus 3 microservicios (`MotorEquipos`, `MotorEvaluacion`, `MotorFormacion`), garantizando la trazabilidad entre el dominio conceptual y la futura implementación.

> [!NOTE]
> **Mecanismo Canónico de Acceso (`UsuarioNoLogueado` y Extensión a Paneles de Rol)**:
> Aunque el sistema es un entorno cerrado sin portal público de auto-registro (los aspirantes son canalizados por las sedes internacionales y registrados por el Gestor), se modela formalmente al actor **`UsuarioNoLogueado`** como la entidad no autenticada en `SESION_CERRADA` que invoca exclusivamente `iniciarSesion()`.
>
> Los roles institucionales específicos (**`Candidato`**, **`Alumno`**, **`LiderEquipo`**, **`Gestor`**) se materializan formalmente tras validar con éxito las credenciales. Cada uno extiende `iniciarSesion()` mediante su caso de uso de apertura de panel (`abrirPanelPostulacion()`, `abrirPanelAlumno()`, `abrirPanelLider()`, `abrirPanelAdmisiones()`) bajo la condición `rol == <Rol>`, y son dichos roles identificados quienes invocan `cerrarSesion()`.

---

## Catálogo de Actores y Casos de Uso

<div align=center>

| Candidato — Batería de Tests Diagnósticos | Alumno PROFER — LMS On-Site y Prácticas |
| :---: | :---: |
| ![](/images/RUP/01-requisitos/01-actores-casos-uso/actoresCasosUsoCandidato.svg) | ![](/images/RUP/01-requisitos/01-actores-casos-uso/actoresCasosUsoAlumno.svg) |
| <sup><i>[Código fuente PlantUML](actoresCasosUsoCandidato.puml)</i></sup> | <sup><i>[Código fuente PlantUML](actoresCasosUsoAlumno.puml)</i></sup> |

| LiderEquipo (TL) — Módulos y Code Reviews | Gestor PROFER — Admisiones y Asignación |
| :---: | :---: |
| ![](/images/RUP/01-requisitos/01-actores-casos-uso/actoresCasosUsoLiderEquipo.svg) | ![](/images/RUP/01-requisitos/01-actores-casos-uso/actoresCasosUsoGestor.svg) |
| <sup><i>[Código fuente PlantUML](actoresCasosUsoLiderEquipo.puml)</i></sup> | <sup><i>[Código fuente PlantUML](actoresCasosUsoGestor.puml)</i></sup> |

</div>

---

## Diagramas de Contexto por Actor

Se define un diagrama de contexto por cada actor del sistema. 

Los estados en estos diagramas **no deben verse simplemente como pantallas**, sino como **contextos de disponibilidad de casos de uso** (qué acciones son invocables en cada momento con independencia del canal o framework frontend). Cada transición lleva el **nombre literal del caso de uso** ya catalogado, sirviendo como mecanismo de verificación formal para detectar callejones sin salida y casos de uso faltantes antes de detallar flujos.

---

### 1. Diagrama de Contexto: `Candidato`

Modela la navegación del aspirante desde su acceso mediante las credenciales generadas por el Gestor hasta la culminación de su batería de tests:

<div align=center>

![](/images/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoCandidato.svg)
<sup><i>[Código fuente PlantUML](diagramaContextoCandidato.puml)</i></sup>

</div>

* **Panel de Postulación**: Acceso a su panel (`abrirPanelPostulacion()`) donde visualiza el estado de disponibilidad de sus 3 tests diagnósticos (`Actitud`, `Aptitud`, `Tecnico`).
* **Ejecución de Tests**: El candidato rinde cualquiera de los 3 tests (`iniciarTest()`), respondiendo preguntas conceptuales (`responderPreguntaTeorica()`) o retos prácticos de código (`entregarPreguntaPractica()`). El cronómetro corre en el backend y el test se entrega manualmente o se autoentrega por expiración con `finalizarTest()`.
* **Opacidad de Resultados y Agenda**: El candidato **no** consulta informes de resultados (los indicadores son de uso exclusivo del Gestor) y **no** agenda ni visualiza entrevistas en su interfaz (la convocatoria y enlace de Google Meet son coordinados enteramente por el Gestor).

---

### 2. Diagrama de Contexto: `Alumno` (`AlumnoProfer`)

Gobierna la interacción diaria del becario dentro de su equipo de trabajo asignado en CTS:

<div align=center>

![](/images/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoAlumno.svg)
<sup><i>[Código fuente PlantUML](diagramaContextoAlumno.puml)</i></sup>

</div>

* **Itinerario Formativo**: Desde `INICIO_ALUMNO_ABIERTO` accede a su capacitación y a los módulos configurados por el TL de su equipo.
* **Ciclo de Entrega de Prácticas**: El alumno registra la URL del Pull Request (`enviarEntregable()`) y consulta los comentarios de revisión del TL (`consultarFeedbackEntregable()`).
* **Tests de Nivelación**: En el cierre de módulo rinde reactivos técnicos transversales reutilizando el motor de evaluación.

---

### 3. Diagrama de Contexto: `LiderEquipo` (`TechLeader` - TL)

Modela el gobierno formativo y técnico ejercido por el TL sobre los alumnos, módulos y entregables de su propio equipo asignado:

<div align=center>

![](/images/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoLiderEquipo.svg)
<sup><i>[Código fuente PlantUML](diagramaContextoLiderEquipo.puml)</i></sup>

</div>

* **Configuración de Módulos**: Gestión de materiales didácticos de su área (`crearMaterial()`, `editarMaterial()`, `eliminarMaterial()`).
* **Banco de Conocimiento Técnico**: Alta y afinado de preguntas teóricas y retos de código vinculados a su módulo (`crearPregunta()`, `editarPregunta()`, `eliminarPregunta()`), que alimentan tanto los tests de fin de módulo como el test técnico de admisión.
* **Code Reviews de Alumnos**: El TL inspecciona los Pull Requests pendientes de los alumnos de su equipo (`abrirEntregablesPendientes()`, `revisarEntregable()`), solicitando correcciones (`solicitarCambiosEntregable()`) o aprobando la entrega (`aprobarEntregable()`).
* **Evaluación Integral**: Calificación de la capacitación del alumno al completar el ciclo (`evaluarCapacitacionAlumno()`).
* **Aislamiento de Candidatos**: El TL **no** tiene acceso a la cartera global de candidatos (acotado estrictamente a su equipo).

---

### 4. Diagrama de Contexto: `Gestor` (`GestorProfer`)

Gobierna la admisión continua, la recepción desde las sedes internacionales, la evaluación en el perfil del candidato y la gobernanza académica:

<div align=center>

![](/images/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoGestor.svg)
<sup><i>[Código fuente PlantUML](diagramaContextoGestor.puml)</i></sup>

</div>

* **Recepción desde Sedes**: Alta individual (`registrarCandidato()`) o importación masiva (`importarCandidatosSede()`) de los aspirantes recopilados por las sedes de cada país.
* **Perfil Unificado del Candidato**: Centro operativo (`abrirPerfilCandidato()`) donde el Gestor examina directamente los resultados de la batería de tests (radares de aptitud, actitud y habilidades técnicas).
* **Entrevistas Google Meet y Anotaciones**: El Gestor agenda la reunión virtual (`agendarEntrevistaGoogleMeet()`) tras constatar los tests (o anticipadamente a su criterio) y registra sus notas cualitativas e impresiones (`registrarAnotacionesEntrevista()`) directamente en el perfil.
* **Dictamen de Admisión**: Formaliza la beca PROFER asignando al aspirante a uno de los 6 equipos y fijando su rol técnico (`admitirAlumnoProfer()`), o descarta la postulación (`rechazarCandidatura()`).
* **Gobernanza Académica**: Apertura de nuevos periodos anuales (`abrirPeriodoIngreso()`) y ejecución de cortes semestrales para consolidar cohortes (`cerrarCorteSemestral()`).

---

## Convenciones de Nomenclatura y Granularidad

1. **Convención `verboEntidad()`**:
   * Todos los casos de uso siguen el formato formal de método `verboEntidad()` con el sustantivo tomado literalmente de `modeloDominio.puml`.
2. **Granularidad Fina**:
   * Se define un caso de uso independiente por cada alta, baja, actualización o transición distinguible, evitando casos de uso monolíticos ambiguos.
3. **Desacoplamiento de Roles**:
   * El `Candidato` y el `Alumno` tienen espacios de trabajo y casos de uso totalmente separados; la transición de uno a otro se produce únicamente tras la acción `admitirAlumnoProfer()` del `Gestor`.

---

<div align="center">

[Volver a Hub de Requisitos](/RUP/01-requisitos/README.md) • [Catálogo y Detalle de Casos de Uso (35)](/RUP/01-requisitos/03-detalle-casos-uso/README.md)

</div>
