<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [📜 Bitácora ADR](/RUP/BITACORA.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [🔍 02 Análisis](/RUP/02-analisis/README.md) | [🎨 03 Diseño](/RUP/03-diseño/README.md) | [💻 04 Desarrollo](/RUP/04-desarrollo/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|

**Fase 01 Requisitos:** [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) • **📋 Catálogo y Detalle de Casos de Uso (35)**

</div>

# Detalle de Casos de Uso — Fase 01: Requisitos

En esta sección se especifica formalmente el comportamiento interactivo, las máquinas de estados de control y los prototipos de interfaz de los **35 casos de uso** del sistema **CTS Academy & Evaluator**, siguiendo con rigor el estándar de ingeniería de software de UNEATLANTICO (*pyCelda* / Dr. Manuel Masías).

---

## 🧭 Acceso Rápido por Paquete Funcional

<div align="center">

| [🔐 PK01 — Acceso (2 CUs)](#-pk01--acceso-2-casos-de-uso) | [🎯 PK02 — MotorEvaluacion (12 CUs)](#-pk02--motorevaluacion-12-casos-de-uso) | [📚 PK03 — MotorFormacion (17 CUs)](#-pk03--motorformacion-17-casos-de-uso) | [👥 PK04 — MotorEquipos (4 CUs)](#-pk04--motorequipos-4-casos-de-uso) |
|:---:|:---:|:---:|:---:|

</div>

---

## 📐 Estructura Canónica de Cada Caso de Uso

Cada caso de uso cuenta con su propio subdirectorio (`iniciarSesion/`, `iniciarTest/`, `crearMaterial/`, etc.) compuesto invariablemente por **tres ficheros**:

1. **`especificacion.puml`** — **Statechart de Interacción (Fuente de Verdad)**:
   * Statechart PlantUML (`skinparam linetype polyline`) con un estado compuesto nombrado exactamente como el caso de uso (`state iniciarTest as "iniciarTest()"`).
   * Estados internos anónimos (`state " " as Paso1`) para evitar redundancias visuales con las notas de transición.
   * Entradas y salidas explícitas que coinciden textualmente con los estados de los [Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md#%F0%9F%94%84-diagramas-de-contexto-por-actor).
   * **Bifurcaciones de Control (`<<choice>>`)**: Evaluación de precondiciones y reglas de negocio antes de transicionar.
   * **Colores semánticos de transición**:
     * `-[#green]->`: Flujo principal de éxito (*Happy path*).
     * `-[#red]->`: Fallo de validación o bloqueo de precondición (retorna con mensaje del sistema).
     * `-[#blue]->`: Cancelación voluntaria del actor (únicamente permitida si el sistema planteó una confirmación previa explícita).

2. **`wireframes.puml`** — **Prototipos de Interfaz en PlantUML Salt**:
   * Maqueta esquemática (`@startsalt`) representativa de los formularios, paneles o visores correspondientes al caso de uso.
   * Correspondencia 1:1 estricta con la especificación (sin controles huérfanos fuera del modelo).

3. **`README.md`** — **Ficha de Requisitos**:
   * Ficha técnica tabular (Actor, Objetivo, Tipo, Prioridad, Estado).
   * Inclusión de los dos diagramas vectoriales compilados en SVG desde `/images/RUP/01-requisitos/03-detalle-casos-uso/<casoUso>/`.
   * Descripción de precondiciones, reglas de negocio e invariantes del dominio aplicables.

---

## 🔒 Vocabulario Cerrado en Notas de Transición (Regla UNEATLANTICO)

Las notas (`note on link`) utilizan **exclusivamente** el vocabulario canónico:

<div align=center>

| Actor | Sistema |
| :--- | :--- |
| `introduce` | `permite introducir` |
| `solicita introducir` | `permite solicitar` |
| `solicita` | `presenta` / `muestra` / `visualiza` |
| `selecciona` | `presenta selección de` |

</div>

---

## 🔐 PK01 — Acceso (2 Casos de Uso)

Mecanismos transversales de autenticación multifuncional, control de credenciales y revocación segura de sesiones para los 4 actores.

<div align=center>

| Caso de Uso | Actor Principal | Especificación PUML | Wireframe Salt | Ficha RUP |
| :--- | :---: | :---: | :---: | :---: |
| `iniciarSesion()` | Común (4 Actores) | [especificacion.puml](iniciarSesion/especificacion.puml) | [wireframes.puml](iniciarSesion/wireframes.puml) | [Detalle 📃](iniciarSesion/README.md) |
| `cerrarSesion()` | Común (4 Actores) | [especificacion.puml](cerrarSesion/especificacion.puml) | [wireframes.puml](cerrarSesion/wireframes.puml) | [Detalle 📃](cerrarSesion/README.md) |

</div>

---

## 🎯 PK02 — MotorEvaluacion (12 Casos de Uso)

Proceso integral de admisión técnica continua: batería de 3 tests diagnósticos, cronometraje en servidor, expedientes de aspirantes, agenda de entrevistas Google Meet y resoluciones de ingreso.

<div align=center>

| Caso de Uso | Actor Principal | Especificación PUML | Wireframe Salt | Ficha RUP |
| :--- | :---: | :---: | :---: | :---: |
| `abrirPanelPostulacion()` | `Candidato` | [especificacion.puml](abrirPanelPostulacion/especificacion.puml) | [wireframes.puml](abrirPanelPostulacion/wireframes.puml) | [Detalle 📃](abrirPanelPostulacion/README.md) |
| `iniciarTest()` | `Candidato` / `Alumno` | [especificacion.puml](iniciarTest/especificacion.puml) | [wireframes.puml](iniciarTest/wireframes.puml) | [Detalle 📃](iniciarTest/README.md) |
| `responderPreguntaTeorica()` | `Candidato` / `Alumno` | [especificacion.puml](responderPreguntaTeorica/especificacion.puml) | [wireframes.puml](responderPreguntaTeorica/wireframes.puml) | [Detalle 📃](responderPreguntaTeorica/README.md) |
| `entregarPreguntaPractica()` | `Candidato` / `Alumno` | [especificacion.puml](entregarPreguntaPractica/especificacion.puml) | [wireframes.puml](entregarPreguntaPractica/wireframes.puml) | [Detalle 📃](entregarPreguntaPractica/README.md) |
| `finalizarTest()` | `Candidato` / `Alumno` | [especificacion.puml](finalizarTest/especificacion.puml) | [wireframes.puml](finalizarTest/wireframes.puml) | [Detalle 📃](finalizarTest/README.md) |
| `abrirPerfilCandidato()` | `Gestor` | [especificacion.puml](abrirPerfilCandidato/especificacion.puml) | [wireframes.puml](abrirPerfilCandidato/wireframes.puml) | [Detalle 📃](abrirPerfilCandidato/README.md) |
| `agendarEntrevistaGoogleMeet()` | `Gestor` | [especificacion.puml](agendarEntrevistaGoogleMeet/especificacion.puml) | [wireframes.puml](agendarEntrevistaGoogleMeet/wireframes.puml) | [Detalle 📃](agendarEntrevistaGoogleMeet/README.md) |
| `registrarAnotacionesEntrevista()` | `Gestor` | [especificacion.puml](registrarAnotacionesEntrevista/especificacion.puml) | [wireframes.puml](registrarAnotacionesEntrevista/wireframes.puml) | [Detalle 📃](registrarAnotacionesEntrevista/README.md) |
| `admitirAlumnoProfer()` | `Gestor` | [especificacion.puml](admitirAlumnoProfer/especificacion.puml) | [wireframes.puml](admitirAlumnoProfer/wireframes.puml) | [Detalle 📃](admitirAlumnoProfer/README.md) |
| `rechazarCandidatura()` | `Gestor` | [especificacion.puml](rechazarCandidatura/especificacion.puml) | [wireframes.puml](rechazarCandidatura/wireframes.puml) | [Detalle 📃](rechazarCandidatura/README.md) |
| `registrarCandidato()` | `Gestor` | [especificacion.puml](registrarCandidato/especificacion.puml) | [wireframes.puml](registrarCandidato/wireframes.puml) | [Detalle 📃](registrarCandidato/README.md) |
| `importarCandidatosSede()` | `Gestor` | [especificacion.puml](importarCandidatosSede/especificacion.puml) | [wireframes.puml](importarCandidatosSede/wireframes.puml) | [Detalle 📃](importarCandidatosSede/README.md) |

</div>

---

## 📚 PK03 — MotorFormacion (17 Casos de Uso)

Plataforma formativa interna (LMS On-Site): itinerarios de capacitación por equipos CTS, material didáctico, banco de reactivos, entregables prácticos (Pull Requests), revisiones de código (*Code Reviews*) y evaluación sumativa de competencias.

<div align=center>

| Caso de Uso | Actor Principal | Especificación PUML | Wireframe Salt | Ficha RUP |
| :--- | :---: | :---: | :---: | :---: |
| `abrirPanelAlumno()` | `Alumno` | [especificacion.puml](abrirPanelAlumno/especificacion.puml) | [wireframes.puml](abrirPanelAlumno/wireframes.puml) | [Detalle 📃](abrirPanelAlumno/README.md) |
| `consultarCapacitacion()` | `Alumno` | [especificacion.puml](consultarCapacitacion/especificacion.puml) | [wireframes.puml](consultarCapacitacion/wireframes.puml) | [Detalle 📃](consultarCapacitacion/README.md) |
| `consultarModulo()` | `Alumno` | [especificacion.puml](consultarModulo/especificacion.puml) | [wireframes.puml](consultarModulo/wireframes.puml) | [Detalle 📃](consultarModulo/README.md) |
| `consultarMaterial()` | `Alumno` | [especificacion.puml](consultarMaterial/especificacion.puml) | [wireframes.puml](consultarMaterial/wireframes.puml) | [Detalle 📃](consultarMaterial/README.md) |
| `enviarEntregable()` | `Alumno` | [especificacion.puml](enviarEntregable/especificacion.puml) | [wireframes.puml](enviarEntregable/wireframes.puml) | [Detalle 📃](enviarEntregable/README.md) |
| `consultarFeedbackEntregable()` | `Alumno` | [especificacion.puml](consultarFeedbackEntregable/especificacion.puml) | [wireframes.puml](consultarFeedbackEntregable/wireframes.puml) | [Detalle 📃](consultarFeedbackEntregable/README.md) |
| `crearMaterial()` | `LiderEquipo` | [especificacion.puml](crearMaterial/especificacion.puml) | [wireframes.puml](crearMaterial/wireframes.puml) | [Detalle 📃](crearMaterial/README.md) |
| `editarMaterial()` | `LiderEquipo` | [especificacion.puml](editarMaterial/especificacion.puml) | [wireframes.puml](editarMaterial/wireframes.puml) | [Detalle 📃](editarMaterial/README.md) |
| `eliminarMaterial()` | `LiderEquipo` | [especificacion.puml](eliminarMaterial/especificacion.puml) | [wireframes.puml](eliminarMaterial/wireframes.puml) | [Detalle 📃](eliminarMaterial/README.md) |
| `crearPregunta()` | `LiderEquipo` | [especificacion.puml](crearPregunta/especificacion.puml) | [wireframes.puml](crearPregunta/wireframes.puml) | [Detalle 📃](crearPregunta/README.md) |
| `editarPregunta()` | `LiderEquipo` | [especificacion.puml](editarPregunta/especificacion.puml) | [wireframes.puml](editarPregunta/wireframes.puml) | [Detalle 📃](editarPregunta/README.md) |
| `eliminarPregunta()` | `LiderEquipo` | [especificacion.puml](eliminarPregunta/especificacion.puml) | [wireframes.puml](eliminarPregunta/wireframes.puml) | [Detalle 📃](eliminarPregunta/README.md) |
| `abrirEntregablesPendientes()` | `LiderEquipo` | [especificacion.puml](abrirEntregablesPendientes/especificacion.puml) | [wireframes.puml](abrirEntregablesPendientes/wireframes.puml) | [Detalle 📃](abrirEntregablesPendientes/README.md) |
| `revisarEntregable()` | `LiderEquipo` | [especificacion.puml](revisarEntregable/especificacion.puml) | [wireframes.puml](revisarEntregable/wireframes.puml) | [Detalle 📃](revisarEntregable/README.md) |
| `aprobarEntregable()` | `LiderEquipo` | [especificacion.puml](aprobarEntregable/especificacion.puml) | [wireframes.puml](aprobarEntregable/wireframes.puml) | [Detalle 📃](aprobarEntregable/README.md) |
| `solicitarCambiosEntregable()` | `LiderEquipo` | [especificacion.puml](solicitarCambiosEntregable/especificacion.puml) | [wireframes.puml](solicitarCambiosEntregable/wireframes.puml) | [Detalle 📃](solicitarCambiosEntregable/README.md) |
| `evaluarCapacitacionAlumno()` | `LiderEquipo` | [especificacion.puml](evaluarCapacitacionAlumno/especificacion.puml) | [wireframes.puml](evaluarCapacitacionAlumno/wireframes.puml) | [Detalle 📃](evaluarCapacitacionAlumno/README.md) |

</div>

---

## 👥 PK04 — MotorEquipos (4 Casos de Uso)

Gobernanza institucional: administración de periodos anuales, cohortes semestrales y cuadros de mando de liderazgo técnico y admisiones.

<div align=center>

| Caso de Uso | Actor Principal | Especificación PUML | Wireframe Salt | Ficha RUP |
| :--- | :---: | :---: | :---: | :---: |
| `abrirPanelAdmisiones()` | `Gestor` | [especificacion.puml](abrirPanelAdmisiones/especificacion.puml) | [wireframes.puml](abrirPanelAdmisiones/wireframes.puml) | [Detalle 📃](abrirPanelAdmisiones/README.md) |
| `abrirPeriodoIngreso()` | `Gestor` | [especificacion.puml](abrirPeriodoIngreso/especificacion.puml) | [wireframes.puml](abrirPeriodoIngreso/wireframes.puml) | [Detalle 📃](abrirPeriodoIngreso/README.md) |
| `cerrarCorteSemestral()` | `Gestor` | [especificacion.puml](cerrarCorteSemestral/especificacion.puml) | [wireframes.puml](cerrarCorteSemestral/wireframes.puml) | [Detalle 📃](cerrarCorteSemestral/README.md) |
| `abrirPanelLider()` | `LiderEquipo` | [especificacion.puml](abrirPanelLider/especificacion.puml) | [wireframes.puml](abrirPanelLider/wireframes.puml) | [Detalle 📃](abrirPanelLider/README.md) |

</div>

---

<div align="center">

[⬅️ Volver a Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) • [Fase 02: Análisis ➡️](/RUP/02-analisis/README.md)

</div>
