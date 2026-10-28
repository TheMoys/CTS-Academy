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
    ├── PK02 - MotorEvaluacion (12 CUs)     ──► En cola de modelado
    ├── PK03 - MotorFormacion (17 CUs)      ──► En cola de modelado
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

| Caso de Uso | Actores Involucrados | Propósito de Análisis | Estado |
| :--- | :--- | :--- | :---: |
| `abrirPanelPostulacion()` | `Candidato` | Carga de estado de postulación y batería de 3 tests | Pendiente |
| `iniciarTest()` | `Candidato`, `Alumno` | Inicialización de intento y sincronización de cronómetro en servidor | Pendiente |
| `responderPreguntaTeorica()` | `Candidato`, `Alumno` | Persistencia de respuestas de opción múltiple / desarrollo | Pendiente |
| `entregarPreguntaPractica()` | `Candidato`, `Alumno` | Envío de soluciones de código a sandbox de evaluación | Pendiente |
| `finalizarTest()` | `Candidato`, `Alumno` | Cierre irreversible de examen y consolidación diagnóstica | Pendiente |
| `abrirPerfilCandidato()` | `Gestor` | Visualización agregada de indicadores de aptitud y tests | Pendiente |
| `agendarEntrevistaGoogleMeet()` | `Gestor` | Coordinación de cita virtual en expediente de admisión | Pendiente |
| `registrarAnotacionesEntrevista()` | `Gestor` | Registro cualitativo de competencias blandas en entrevista | Pendiente |
| `admitirAlumnoProfer()` | `Gestor` | Resolución favorable, asignación a equipo y rol de becario | Pendiente |
| `rechazarCandidatura()` | `Gestor` | Desestimación motivada del expediente de admisión | Pendiente |
| `registrarCandidato()` | `Gestor` | Alta manual controlada de aspirante internacional | Pendiente |
| `importarCandidatosSede()` | `Gestor` | Procesamiento por lotes de expedientes remitidos por sedes | Pendiente |

</div>

---

### PK03 — MotorFormacion (17 Casos de Uso)

<div align=center>

| Caso de Uso | Actores Involucrados | Propósito de Análisis | Estado |
| :--- | :--- | :--- | :---: |
| `abrirPanelAlumno()` | `Alumno` | Tablero de progreso formativo, módulos y entregables | Pendiente |
| `consultarCapacitacion()` | `Alumno` | Itinerario pedagógico de onboarding en el equipo | Pendiente |
| `consultarModulo()` | `Alumno` | Desglose de unidades temáticas y requisitos | Pendiente |
| `consultarMaterial()` | `Alumno` | Acceso a guías técnicas, documentación y referencias | Pendiente |
| `enviarEntregable()` | `Alumno` | Remisión de Pull Request / repositorio para Code Review | Pendiente |
| `consultarFeedbackEntregable()` | `Alumno` | Lectura de observaciones, cambios solicitados o aprobación | Pendiente |
| `abrirEntregablesPendientes()` | `LiderEquipo` | Cola de revisión de código de los alumnos del equipo | Pendiente |
| `revisarEntregable()` | `LiderEquipo` | Inspección técnica del PR y rúbrica de calidad | Pendiente |
| `aprobarEntregable()` | `LiderEquipo` | Validación positiva del ejercicio práctico de formación | Pendiente |
| `solicitarCambiosEntregable()` | `LiderEquipo` | Emisión de observaciones técnicas para iteración de código | Pendiente |
| `evaluarCapacitacionAlumno()` | `LiderEquipo` | Calificación global sumativa del itinerario del becario | Pendiente |
| `crearMaterial()` | `LiderEquipo` | Incorporación de nuevo recurso didáctico al banco | Pendiente |
| `editarMaterial()` | `LiderEquipo` | Actualización de contenido técnico de un material | Pendiente |
| `eliminarMaterial()` | `LiderEquipo` | Retirada lógica de recurso formativo | Pendiente |
| `crearPregunta()` | `LiderEquipo` | Creación de reactivo teórico o práctico | Pendiente |
| `editarPregunta()` | `LiderEquipo` | Modificación de enunciado o criterios de corrección | Pendiente |
| `eliminarPregunta()` | `LiderEquipo` | Desactivación de reactivo del banco de evaluación | Pendiente |

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
