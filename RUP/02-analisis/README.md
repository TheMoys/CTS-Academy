<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [Bitácora ADR](/RUP/BITACORA.md) | [00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [01 Requisitos](/RUP/01-requisitos/README.md) | **02 Análisis** | [03 Diseño](/RUP/03-diseño/README.md) | [04 Desarrollo](/RUP/04-desarrollo/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|

</div>

# Fase 02: Análisis — CTS Academy & Evaluator

Esta fase formaliza las colaboraciones entre clases de análisis Boundary-Control-Entity (BCE) que realizan los 35 casos de uso del sistema de forma agnóstica a la tecnología concreta.

---

## Propósito del Modelo de Análisis

El modelo de análisis actúa como el puente formal entre la especificación de requisitos del usuario (Fase 01) y el diseño arquitectónico tecnológico (Fase 03). Su propósito es definir **cómo** el sistema responderá a las necesidades del negocio abstrayéndose de detalles técnicos particulares (bases de datos relacionales, frameworks web, protocolos de red).

En esta fase se formalizan:
1. **Clases de Análisis (Estereotipos RUP / BCE)**:
   * **Boundary (`<<boundary>>` / Frontera)**: Mediatizan la comunicación entre los actores externos y el interior del sistema.
   * **Control (`<<control>>` / Control)**: Encapsulan la lógica de coordinación, flujo de negocio y transacciones de cada caso de uso.
   * **Entity (`<<entity>>` / Entidad)**: Representan la información y el comportamiento duradero del dominio.
2. **Realizaciones de Casos de Uso (Análisis)**:
   * Diagramas de Clases de Análisis (VOPC - View of Participating Classes) con atributos y responsabilidades.
   * Diagramas de Realización de Análisis (Secuencia BCE) que modelan paso a paso los flujos principal y alternativo en estricta coherencia con las máquinas de estados de la Fase 01.

---

## Catálogo de Realizaciones por Paquete Funcional

```text
02-analisis/
└── casos-uso/
    ├── PK01 - Acceso (2 CUs)               ──► Completado (2/2)
    │   ├── iniciarSesion/
    │   └── cerrarSesion/
    ├── PK02 - MotorEvaluacion (12 CUs)     ──► Completado (12/12)
    │   ├── abrirPanelPostulacion/
    │   ├── iniciarTest/
    │   ├── responderPreguntaTeorica/
    │   ├── entregarPreguntaPractica/
    │   ├── finalizarTest/
    │   ├── abrirPerfilCandidato/
    │   ├── agendarEntrevistaGoogleMeet/
    │   ├── registrarAnotacionesEntrevista/
    │   ├── admitirAlumnoProfer/
    │   ├── rechazarCandidatura/
    │   ├── registrarCandidato/
    │   └── importarCandidatosSede/
    ├── PK03 - MotorFormacion (17 CUs)      ──► Completado (17/17)
    │   ├── abrirPanelAlumno/
    │   ├── consultarCapacitacion/
    │   ├── consultarModulo/
    │   ├── consultarMaterial/
    │   ├── enviarEntregable/
    │   ├── consultarFeedbackEntregable/
    │   ├── abrirEntregablesPendientes/
    │   ├── revisarEntregable/
    │   ├── aprobarEntregable/
    │   ├── solicitarCambiosEntregable/
    │   ├── evaluarCapacitacionAlumno/
    │   ├── crearMaterial/
    │   ├── editarMaterial/
    │   ├── eliminarMaterial/
    │   ├── crearPregunta/
    │   ├── editarPregunta/
    │   └── eliminarPregunta/
    └── PK04 - MotorEquipos (4 CUs)         ──► En cola de modelado
```

### PK01 — Acceso (2 Casos de Uso)

<div align=center>

| Caso de Uso | Frontera (`<<boundary>>`) | Control (`<<control>>`) | Entidades (`<<entity>>`) | Realización de Análisis | Estado |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **`iniciarSesion()`** | `FormularioLogin` | `GestorAutenticacion` | `Usuario`, `Sesion` | [Ver Análisis](casos-uso/iniciarSesion/README.md) | Completado |
| **`cerrarSesion()`** | `BarraNavegacion` | `GestorAutenticacion` | `Usuario`, `Sesion`, `Test` | [Ver Análisis](casos-uso/cerrarSesion/README.md) | Completado |

</div>

---

### PK02 — MotorEvaluacion (12 Casos de Uso)

<div align=center>

| Caso de Uso | Frontera (`<<boundary>>`) | Control (`<<control>>`) | Entidades (`<<entity>>`) | Realización de Análisis | Estado |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **`abrirPanelPostulacion()`** | `PanelPostulacion` | `GestorPostulacion` | `Candidato`, `Convocatoria`, `Test` | [Ver Análisis](casos-uso/abrirPanelPostulacion/README.md) | Completado |
| **`iniciarTest()`** | `InterfazTest` | `GestorEvaluacion` | `Test`, `Pregunta`, `SesionEvaluacion` | [Ver Análisis](casos-uso/iniciarTest/README.md) | Completado |
| **`responderPreguntaTeorica()`** | `PanelPreguntaTeorica` | `GestorEvaluacion` | `Test`, `Teorica`, `RespuestaTeorica` | [Ver Análisis](casos-uso/responderPreguntaTeorica/README.md) | Completado |
| **`entregarPreguntaPractica()`** | `EditorPractica`, `TestRunner` | `GestorEvaluacionPractica` | `Test`, `Practica`, `EntregaPractica` | [Ver Análisis](casos-uso/entregarPreguntaPractica/README.md) | Completado |
| **`finalizarTest()`** | `DialogoFinalizarTest` | `GestorEvaluacion` | `Test`, `Resultado`, `SesionEvaluacion` | [Ver Análisis](casos-uso/finalizarTest/README.md) | Completado |
| **`abrirPerfilCandidato()`** | `PerfilCandidato` | `GestorAdmisiones` | `Candidato`, `Resultado`, `Entrevista` | [Ver Análisis](casos-uso/abrirPerfilCandidato/README.md) | Completado |
| **`agendarEntrevistaGoogleMeet()`** | `DialogoAgendarEntrevista`, `GoogleCalendarService` | `GestorAdmisiones` | `Candidato`, `Entrevista` | [Ver Análisis](casos-uso/agendarEntrevistaGoogleMeet/README.md) | Completado |
| **`registrarAnotacionesEntrevista()`** | `FormularioEntrevista` | `GestorAdmisiones` | `Candidato`, `Entrevista`, `Anotacion` | [Ver Análisis](casos-uso/registrarAnotacionesEntrevista/README.md) | Completado |
| **`admitirAlumnoProfer()`** | `DialogoAdmision`, `ServicioNotificacionesEmail` | `GestorAdmisiones` | `Candidato`, `Equipo`, `Alumno`, `Capacitacion` | [Ver Análisis](casos-uso/admitirAlumnoProfer/README.md) | Completado |
| **`rechazarCandidatura()`** | `DialogoRechazo`, `ServicioAccesoAutenticacion` | `GestorAdmisiones` | `Candidato` | [Ver Análisis](casos-uso/rechazarCandidatura/README.md) | Completado |
| **`registrarCandidato()`** | `FormularioRegistroCandidato`, `ServicioAccesoAutenticacion` | `GestorAdmisiones` | `Candidato`, `Convocatoria`, `Test` | [Ver Análisis](casos-uso/registrarCandidato/README.md) | Completado |
| **`importarCandidatosSede()`** | `FormularioImportarSede`, `ColaNotificacionesAsincrona` | `GestorAdmisiones` | `Candidato`, `LoteImportacion`, `Convocatoria`, `Test` | [Ver Análisis](casos-uso/importarCandidatosSede/README.md) | Completado |

</div>

---

### PK03 — MotorFormacion (17 Casos de Uso)

<div align=center>

| Caso de Uso | Frontera (`<<boundary>>`) | Control (`<<control>>`) | Entidades (`<<entity>>`) | Realización de Análisis | Estado |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **`abrirPanelAlumno()`** | `PanelAlumno` | `GestorFormacion` | `Alumno`, `Equipo`, `TechLeader`, `Capacitacion`, `Modulo`, `EntregaLaboratorio` | [Ver Análisis](casos-uso/abrirPanelAlumno/README.md) | Completado |
| **`consultarCapacitacion()`** | `VistaCapacitacion` | `GestorFormacion` | `Alumno`, `Capacitacion`, `Modulo`, `Laboratorio` | [Ver Análisis](casos-uso/consultarCapacitacion/README.md) | Completado |
| **`consultarModulo()`** | `VistaModulo` | `GestorFormacion` | `Modulo`, `Material`, `Laboratorio`, `EntregaLaboratorio`, `Test` | [Ver Análisis](casos-uso/consultarModulo/README.md) | Completado |
| **`consultarMaterial()`** | `VisorMaterial` | `GestorFormacion` | `Alumno`, `Modulo`, `Material`, `LecturaMaterial` | [Ver Análisis](casos-uso/consultarMaterial/README.md) | Completado |
| **`enviarEntregable()`** | `FormularioEntrega`, `ServicioGitRepository` | `GestorFormacion` | `Alumno`, `Laboratorio`, `EntregaLaboratorio`, `Notificacion` | [Ver Análisis](casos-uso/enviarEntregable/README.md) | Completado |
| **`consultarFeedbackEntregable()`** | `VistaFeedbackEntrega` | `GestorFormacion` | `Alumno`, `Laboratorio`, `EntregaLaboratorio`, `RevisionCodigo`, `ComentarioRevision` | [Ver Análisis](casos-uso/consultarFeedbackEntregable/README.md) | Completado |
| **`abrirEntregablesPendientes()`** | `BandejaRevisiones` | `GestorRevisiones` | `TechLeader`, `Equipo`, `Alumno`, `Laboratorio`, `EntregaLaboratorio` | [Ver Análisis](casos-uso/abrirEntregablesPendientes/README.md) | Completado |
| **`revisarEntregable()`** | `EditorRevision`, `ServicioGitRepository` | `GestorRevisiones` | `EntregaLaboratorio`, `Laboratorio`, `RevisionCodigo`, `ComentarioRevision` | [Ver Análisis](casos-uso/revisarEntregable/README.md) | Completado |
| **`aprobarEntregable()`** | `DialogoAprobacionRevision` | `GestorRevisiones` | `EntregaLaboratorio`, `RevisionCodigo`, `Modulo`, `Test`, `Notificacion` | [Ver Análisis](casos-uso/aprobarEntregable/README.md) | Completado |
| **`solicitarCambiosEntregable()`** | `DialogoCambiosRevision` | `GestorRevisiones` | `EntregaLaboratorio`, `RevisionCodigo`, `ComentarioRevision`, `Notificacion` | [Ver Análisis](casos-uso/solicitarCambiosEntregable/README.md) | Completado |
| **`evaluarCapacitacionAlumno()`** | `FormularioEvaluacionGlobal`, `ServicioNotificacionesEmail` | `GestorRevisiones` | `TechLeader`, `Alumno`, `Capacitacion`, `EvaluacionSumativa` | [Ver Análisis](casos-uso/evaluarCapacitacionAlumno/README.md) | Completado |
| **`crearMaterial()`** | `EditorMaterial` | `GestorContenidos` | `TechLeader`, `Modulo`, `Material` | [Ver Análisis](casos-uso/crearMaterial/README.md) | Completado |
| **`editarMaterial()`** | `EditorMaterial` | `GestorContenidos` | `TechLeader`, `Modulo`, `Material`, `LecturaMaterial` | [Ver Análisis](casos-uso/editarMaterial/README.md) | Completado |
| **`eliminarMaterial()`** | `DialogoEliminacionMaterial` | `GestorContenidos` | `TechLeader`, `Modulo`, `Material` | [Ver Análisis](casos-uso/eliminarMaterial/README.md) | Completado |
| **`crearPregunta()`** | `EditorPregunta` | `GestorBancoPreguntas` | `TechLeader`, `Modulo`, `Pregunta`, `Opcion` | [Ver Análisis](casos-uso/crearPregunta/README.md) | Completado |
| **`editarPregunta()`** | `EditorPregunta` | `GestorBancoPreguntas` | `TechLeader`, `Pregunta`, `Opcion`, `Test` | [Ver Análisis](casos-uso/editarPregunta/README.md) | Completado |
| **`eliminarPregunta()`** | `DialogoEliminacionPregunta` | `GestorBancoPreguntas` | `TechLeader`, `Pregunta`, `RespuestaEvaluacion` | [Ver Análisis](casos-uso/eliminarPregunta/README.md) | Completado |

</div>

---

### PK04 — MotorEquipos (4 Casos de Uso)

<div align=center>

| Caso de Uso | Actores Involucrados | Propósito de Análisis | Estado |
| :--- | :--- | :--- | :---: |
| `abrirPanelLider()` | `LiderEquipo` | Cuadro de mando del squad técnico, métricas y becarios | Pendiente |
| `abrirPanelAdmisiones()` | `Gestor` | Embudo de postulaciones activas y filtros por cohortes | Pendiente |
| `abrirPeriodoIngreso()` | `Gestor` | Apertura de semestre lectivo para asignación de plazas | Pendiente |
| `cerrarCorteSemestral()` | `Gestor` | Consolidación y cierre de cohorte de incorporación | Pendiente |

</div>

---

<div align="center">

[Fase 01: Requisitos](/RUP/01-requisitos/README.md) • [Fase 03: Diseño](/RUP/03-diseño/README.md)

</div>
