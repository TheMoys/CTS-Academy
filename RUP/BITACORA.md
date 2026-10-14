<div align=right>

<sub>[Al inicio](/README.md) / [RUP Principal](/RUP/README.md) / [Modelo del dominio](/RUP/00-modelo-del-dominio/README.md) / [Requisitos](/RUP/01-requisitos/01-actores-casos-uso/README.md)</sub>

</div>

# Bitácora de Decisiones Arquitectónicas y Evolución RUP

Registro formal y cronológico de decisiones de diseño, acuerdos de modelado y evolución del proyecto **CTS Academy & Evaluator** bajo la metodología RUP (Rational Unified Process).

> [!NOTE]
> 🤡 **Hall of Fame de Cagadas y Redundancias**: Para consultar el registro informal, autocrítico y sin filtros de todas las pifias, incoherencias y fiascos de modelado rectificados sobre la marcha, visita la discusión oficial: [💬 Discussion #9: El Muro de los Despropósitos](https://github.com/TheMoys/CTS-Academy/discussions/9).

---

## 📋 Índice de Decisiones (ADR - Architectural Decision Records)

| ID | Fecha | Título | Estado | Discusión Consolidada en GitHub |
| :---: | :---: | :--- | :---: | :--- |
| **[ADR-001](#adr-001-adopción-de-la-metodología-rup-estándar-uneatlantico)** | 2026-10-09 | Adopción de la metodología RUP estándar UNEATLANTICO | Aprobado | [📋 Sesión 2026-10-09 (#7)](https://github.com/TheMoys/CTS-Academy/discussions/7) |
| **[ADR-002](#adr-002-diagramas-conceptuales-limpios-sin-atributos)** | 2026-10-09 | Diagramas conceptuales limpios sin atributos de entidad | Aprobado | [📋 Sesión 2026-10-09 (#7)](https://github.com/TheMoys/CTS-Academy/discussions/7) |
| **[ADR-003](#adr-003-adopción-de-nomenclatura-institucional-programa-profer)** | 2026-10-09 | Adopción de nomenclatura institucional del Programa PROFER | Aprobado | [📋 Sesión 2026-10-09 (#7)](https://github.com/TheMoys/CTS-Academy/discussions/7) |
| **[ADR-004](#adr-004-embudo-en-2-fases-y-asignación-a-los-6-equipos-de-cts)** | 2026-10-09 | Embudo de admisión en 2 fases y asignación a los 6 equipos de CTS | Aprobado | [📋 Sesión 2026-10-09 (#7)](https://github.com/TheMoys/CTS-Academy/discussions/7) |
| **[ADR-005](#adr-005-gobernanza-institucional-convenio-programa-profer--universidad)** | 2026-10-09 | Gobernanza institucional: convenio Programa PROFER – Universidad | Aprobado | [📋 Sesión 2026-10-09 (#7)](https://github.com/TheMoys/CTS-Academy/discussions/7) |
| **[ADR-006](#adr-006-descomposición-arquitectónica-en-3-microservicios)** | 2026-10-13 | Descomposición arquitectónica en 3 microservicios independientes | Aprobado | [🧩 Sesión 2026-10-13 (#8)](https://github.com/TheMoys/CTS-Academy/discussions/8) |
| **[ADR-007](#adr-007-admisión-continua-por-ciclos-académicos-batería-de-3-tests-e-inclusión-de-entrevista)** | 2026-10-14 | Admisión continua por ciclos académicos, batería de 3 tests e inclusión de entrevista | Aprobado | [🧩 Sesión 2026-10-13 (#8)](https://github.com/TheMoys/CTS-Academy/discussions/8) |
| **[ADR-008](#adr-008-canalización-de-candidatos-por-sedes-internacionales-y-eliminación-de-usuarionologueado)** | 2026-10-14 | Canalización de candidatos por sedes internacionales y eliminación de UsuarioNoLogueado | Aprobado | [🧩 Sesión 2026-10-13 (#8)](https://github.com/TheMoys/CTS-Academy/discussions/8) |

---

### ADR-001: Adopción de la metodología RUP estándar UNEATLANTICO
* **Fecha**: 2026-10-09
* **Contexto**: Se requiere planificar y documentar exhaustivamente la plataforma de evaluación técnica de aspirantes y formación de becarios de CTS antes de iniciar el desarrollo, evitando deuda técnica y refactorizaciones ciegas.
* **Decisión**: Adoptar la metodología RUP canónica basada en los repositorios de referencia (*DOCUTRACE*, *pySigHor*, *pyCelda*). Estructurar el proyecto en fases secuenciales: `00-modelo-del-dominio`, `01-requisitos`, `02-analisis`, `03-diseño` y `04-desarrollo`, utilizando PlantUML (`.puml`) y Markdown para una trazabilidad integral versionada en Git.
* **Artefactos afectados**: Estructura de carpetas `/RUP` y concentradores `README.md`.

---

### ADR-002: Diagramas conceptuales limpios sin atributos
* **Fecha**: 2026-10-09
* **Contexto**: El primer borrador del modelo de dominio incluía tipos de datos y atributos que saturaban visualmente el diagrama de clases conceptual.
* **Decisión**: Eliminar los atributos de las entidades en la Fase 00 (`hide empty members`, `hide circles`). El diagrama conceptual debe reflejar con máxima claridad exclusivamente los paquetes, las entidades y las relaciones estructurales entre ellas.
* **Artefactos afectados**: `RUP/00-modelo-del-dominio/modeloDominio.puml` y diagrama Mermaid en `README.md`.

---

### ADR-003: Adopción de nomenclatura institucional Programa PROFER
* **Fecha**: 2026-10-09
* **Contexto**: Alinear la terminología genérica con la realidad institucional de CTS y el programa de becas de formación y empleo.
* **Decisión**:
  * Sustituir `Becario` por **`AlumnoProfer`**.
  * Sustituir `TutorSenior` por **`TechLeader` (TL)**.
  * Sustituir `CoordinadorAdmin` por **`GestorProfer`**.
* **Artefactos afectados**: Todas las especificaciones de dominio y máquinas de estados.

---

### ADR-004: Embudo en 2 fases y asignación a los 6 equipos de CTS
* **Fecha**: 2026-10-09
* **Contexto**: El centro tecnológico se organiza de forma permanente en 6 equipos con diferentes responsabilidades y stacks tecnológicos. La admisión a la beca requiere un filtro en dos fases: prueba técnica y entrevista.
* **Decisión**:
  * **Filtro 1 (`PruebaTecnica`)**: Núcleo digital de la plataforma. Evalúa teoría y práctica generando un `PerfilAptitudes` diagnóstico.
  * **Filtro 2 (`Entrevista`)**: Conducida exclusivamente por el `GestorProfer`. El `TechLeader` no interviene en la entrevista; su rol en selección es evaluar ejercicios prácticos y consultar perfiles y repositorios.
  * Los candidatos aptos son asignados a **1 de los 6 Equipos** con un **Rol de equipo** específico.
* **Artefactos afectados**: `modeloDominio.puml`, `estados-entidades/candidatura-estados.puml`, `00-modelo-del-dominio/README.md`.

---

### ADR-005: Gobernanza institucional: convenio Programa PROFER – Universidad
* **Fecha**: 2026-10-09
* **Contexto**: Esclarecer la relación jurídica e institucional entre la Universidad y el Centro Tecnológico.
* **Decisión**: Incorporar las entidades `ProgramaProfer` y `GerenciaUniversidad`. La Universidad no convoca becas directamente; el `ProgramaProfer` mantiene convenio con la Universidad (supervisado por su Gerencia), gestiona y opera el `CentroTecnologico` y abre las `ConvocatoriaProfer`.
* **Artefactos afectados**: `modeloDominio.puml`, `00-modelo-del-dominio/README.md`.

---

### ADR-006: Descomposición arquitectónica en 3 microservicios
* **Fecha**: 2026-10-13
* **Contexto**: El alcance del sistema abarca tres dominios claramente diferenciados: estructura organizativa, exámenes y plataforma LMS de capacitación. Mantener un monolito generaría acoplamiento excesivo.
* **Decisión**:
  * Descomponer el sistema en **3 microservicios/subsistemas independientes**:
    1. **`MotorEquipos`**: Gobierna `Programa`, `Equipo`, `Alumno`, `LiderEquipo` y `Gestor`.
    2. **`MotorEvaluacion`**: Gobierna `Convocatoria`, `Candidato`, `Test` y `Resultado`.
    3. **`MotorFormacion`**: Gobierna `Capacitacion`, `Modulo`, `Material`, `Entregable`, `Pregunta`, `PreguntaTeorica` y `PreguntaPractica`.
  * **Regla de negocio sobre capacitación**: No existe relación `Equipo --> Capacitacion`; la capacitación es una acción del alumno dentro del equipo (`Alumno --> Capacitacion : realiza`).
  * **Responsabilidad del Tech Leader**: `LiderEquipo --> Capacitacion : evalua`, comprendiendo por herencia y jerarquía la configuración de módulos, la revisión de entregables de código y la calificación de tests de fin de módulo de los alumnos de su equipo.
  * **Test transversal**: El `Test` de `MotorEvaluacion` es agnóstico y es ejecutado tanto por el `Candidato` (admisión) como por el `Alumno` (nivelación o cierre de módulo formativo).
  * La composición de `Test` a partir de `Pregunta` se realiza mediante API REST inter-servicios (`Test ... Pregunta`).
* **Artefactos afectados**: `RUP/00-modelo-del-dominio/modeloDominio.puml`, `RUP/00-modelo-del-dominio/README.md`, `RUP/README.md`.

---

### ADR-007: Admisión continua por ciclos académicos, batería de 3 tests e inclusión de entrevista
* **Fecha**: 2026-10-14
* **Contexto**: El proceso de selección real de los Alumnos PROFER no sigue un calendario rígido con convocatorias que expiran ni aplica una nota de corte eliminatoria sobre un único examen técnico. La captación de talento está abierta todo el año y se estructura para alimentar a los 6 equipos de CTS de forma continua.
* **Decisión**:
  * **Temporalidad y Postulación Continua**: Incorporar las entidades `CursoAcademico` y `Semestre`. La postulación no se cierra (365 días al año); las candidaturas se canalizan y agrupan según el `(CursoAcademico, Semestre)` activo para los cortes de asignación.
  * **Especialización de Tests como Indicadores**: Especializar `Test` en `TestActitud` (competencias blandas y compromiso), `TestAptitud` (lógica y resolución) y `TestTecnico` (habilidades prácticas nutriéndose de reactivos de los módulos de los 6 equipos: `TestTecnico ... Pregunta`). Los tests no eliminan por nota de corte, sino que consolidan un perfil de indicadores y afinidades competenciales.
  * **Formalización de `Entrevista`**: Incorporar la entidad `Entrevista` en `MotorEvaluacion`.
  * **Reglas de Acceso a Entrevista**:
    * *Por derecho*: Todo candidato que completa la batería de 3 tests adquiere el derecho a agendar su entrevista personal.
    * *Por excepción*: El `Gestor` puede autorizar manualmente la agenda a un candidato con algún test pendiente o incompleto.
  * **Dictamen Final**: La entrevista personal con el `GestorProfer` es el hito resolutorio donde se decide la admisión definitiva y la asignación a uno de los 6 equipos con su rol de equipo.
* **Artefactos afectados**: `RUP/00-modelo-del-dominio/modeloDominio.puml`, `estados-entidades/candidatura-estados.puml`, `estados-entidades/test-estados.puml`, `estados-entidades/convocatoria-estados.puml`, `RUP/00-modelo-del-dominio/README.md`.

---

### ADR-008: Canalización de candidatos por sedes internacionales y eliminación de UsuarioNoLogueado
* **Fecha**: 2026-10-14
* **Contexto**: Se había asumido inicialmente que la plataforma contaba con un portal público de auto-registro donde cualquier persona anónima postulaba desde internet. La realidad operativa es que las sedes de la universidad/fundación en cada país son las encargadas de recepcionar, cribar y recopilar las solicitudes de los alumnos interesados, remitiéndolas por lotes al Gestor del programa.
* **Decisión**:
  * **Eliminación del Actor `UsuarioNoLogueado`**: El sistema no expone casos de uso para usuarios anónimos ni registro libre en la web.
  * **Ingreso Controlado por el Gestor**: El `GestorProfer` da de alta o importa a los candidatos remitidos por las sedes de cada país (`registrarCandidato()`), lo que genera sus credenciales/enlace de acceso.
  * **Los 4 Actores Autenticados**: El alcance de actores del sistema queda estrictamente delimitado a 4 perfiles autenticados: `Candidato`, `Alumno`, `LiderEquipo` y `Gestor`.
* **Artefactos afectados**: `estados-entidades/candidatura-estados.puml`, `estados-entidades/convocatoria-estados.puml`, `RUP/00-modelo-del-dominio/README.md`, catálogo de actores en `RUP/01-requisitos/01-actores-casos-uso/`.


