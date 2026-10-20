<div align=right>

<sub>[Al inicio](/README.md) / [Bitácora RUP](/RUP/BITACORA.md) / [Modelo del dominio](/RUP/00-modelo-del-dominio/README.md) / [Actores y casos de uso](/RUP/01-requisitos/01-actores-casos-uso/README.md) / **Detalle de casos de uso** / [Análisis](/RUP/02-analisis/README.md) / [Diseño](/RUP/03-diseño/README.md) / [Desarrollo](/RUP/04-desarrollo/README.md)</sub>

</div>

# Detalle de Casos de Uso — Fase 01: Requisitos

En esta sección se especifica formalmente el comportamiento interactivo y las interfaces de usuario de los casos de uso catalogados en [`01-actores-casos-uso`](/RUP/01-requisitos/01-actores-casos-uso/README.md), siguiendo con rigor metodológico el estándar de ingeniería de software de UNEATLANTICO (*pyCelda* / Dr. Manuel Masías).

---

## 📐 Estructura Canónica de Cada Caso de Uso

Cada caso de uso cuenta con su propio subdirectorio (`iniciarSesion/`, `iniciarTest/`, `abrirPerfilCandidato/`, etc.) compuesto invariablemente por **tres ficheros**:

1. **`especificacion.puml`** — **Statechart de Interacción (Fuente de Verdad)**:
   * Statechart PlantUML (`skinparam linetype polyline`) con un estado compuesto nombrado exactamente como el caso de uso (`state iniciarTest as "iniciarTest()"`).
   * Estados internos anónimos (`state " " as Paso1`) para evitar redundancias visuales con las notas de transición.
   * Entradas y salidas explícitas que coinciden textualmente con los estados de los [Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md#%F0%9F%94%84-diagramas-de-contexto-por-actor).
   * **Bifurcaciones de Control (`<<choice>>`)**: Evaluación de precondiciones y reglas de negocio antes de transicionar.
   * **Colores semánticos de transición**:
     * `-[#green]->`: Flujo principal de éxito (*Happy path*).
     * `-[#red]->`: Fallo de validación o bloqueo de precondición (retorna al estado origen o alternativo con mensaje del sistema).
     * `-[#blue]->`: Cancelación voluntaria del actor (únicamente permitida si el sistema planteó una confirmación previa explícita).

2. **`wireframes.puml`** — **Prototipos de Interfaz en PlantUML Salt**:
   * Maqueta esquemática (`@startsalt`) representativa de los formularios, paneles o visores correspondientes al caso de uso.
   * Correspondencia 1:1 estricta con la especificación (sin campos ni botones huérfanos que no estén modelados en el statechart).

3. **`README.md`** — **Ficha de Requisitos**:
   * Ficha técnica tabular (Actor, Objetivo, Tipo, Nivel).
   * Inclusión de los dos diagramas vectoriales compilados en SVG desde `/images/RUP/01-requisitos/03-detalle-casos-uso/<casoUso>/`.
   * Descripción de precondiciones, reglas de negocio e invariantes del dominio aplicables.
   * Trazabilidad hacia el modelo del dominio y diagramas de contexto.

---

## 🔒 Vocabulario Cerrado en Notas de Transición (Regla UNEATLANTICO)

Para evitar la ambigüedad del lenguaje natural y la intrusión prematura de diseño interno en requisitos, las notas (`note on link`) utilizan **exclusivamente** el siguiente vocabulario canónico:

<div align=center>

| Actor | Sistema |
| :--- | :--- |
| `introduce` | `permite introducir` |
| `solicita introducir` | `permite solicitar` |
| `solicita` | `presenta` / `muestra` / `visualiza` |
| `selecciona` | `presenta selección de` |

</div>

> [!CAUTION]
> **Prohibido en la especificación**:
> 1. Verbos cognitivos o subjetivos del actor (*"el candidato reflexiona..."*, *"decide..."*).
> 2. Verbos de cómputo interno o persistencia del sistema (*"guarda en base de datos"*, *"ejecuta consulta SQL"*, *"calcula hash"*); estos pertenecen a Análisis y Diseño.
> 3. Verbos de tecnología de interfaz gráfica (*"hace clic en el botón X"*, *"abre modal emergente"*); eso corresponde al wireframe.

---

## 🗂️ Índice de Casos de Uso Detallados

A continuación se indexan las especificaciones de los casos de uso nucleares estructurados por subsistema y actor principal:

<div align=center>

| Subsistema / Paquete | Caso de Uso | Actor Principal | Especificación | Wireframe | Ficha RUP |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **PK01 - Acceso** | `iniciarSesion()` | Común (4 Actores) | [especificacion.puml](iniciarSesion/especificacion.puml) | [wireframes.puml](iniciarSesion/wireframes.puml) | [Detalle](iniciarSesion/README.md) |
| **PK02 - MotorEvaluacion** | `abrirPanelPostulacion()` | `Candidato` | [especificacion.puml](abrirPanelPostulacion/especificacion.puml) | [wireframes.puml](abrirPanelPostulacion/wireframes.puml) | [Detalle](abrirPanelPostulacion/README.md) |
| **PK02 - MotorEvaluacion** | `iniciarTest()` | `Candidato` / `Alumno` | [especificacion.puml](iniciarTest/especificacion.puml) | [wireframes.puml](iniciarTest/wireframes.puml) | [Detalle](iniciarTest/README.md) |
| **PK02 - MotorEvaluacion** | `responderPreguntaTeorica()` | `Candidato` / `Alumno` | [especificacion.puml](responderPreguntaTeorica/especificacion.puml) | [wireframes.puml](responderPreguntaTeorica/wireframes.puml) | [Detalle](responderPreguntaTeorica/README.md) |
| **PK02 - MotorEvaluacion** | `entregarPreguntaPractica()` | `Candidato` / `Alumno` | [especificacion.puml](entregarPreguntaPractica/especificacion.puml) | [wireframes.puml](entregarPreguntaPractica/wireframes.puml) | [Detalle](entregarPreguntaPractica/README.md) |
| **PK02 - MotorEvaluacion** | `finalizarTest()` | `Candidato` / `Alumno` | [especificacion.puml](finalizarTest/especificacion.puml) | [wireframes.puml](finalizarTest/wireframes.puml) | [Detalle](finalizarTest/README.md) |
| **PK02 - MotorEvaluacion** | `abrirPerfilCandidato()` | `Gestor` | [especificacion.puml](abrirPerfilCandidato/especificacion.puml) | [wireframes.puml](abrirPerfilCandidato/wireframes.puml) | [Detalle](abrirPerfilCandidato/README.md) |
| **PK03 - MotorFormacion** | `enviarEntregable()` | `Alumno` | [especificacion.puml](enviarEntregable/especificacion.puml) | [wireframes.puml](enviarEntregable/wireframes.puml) | [Detalle](enviarEntregable/README.md) |

</div>
