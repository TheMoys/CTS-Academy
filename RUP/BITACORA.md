<div align=right>

<sub>[Al inicio](/README.md) / [RUP Principal](/RUP/README.md) / [Modelo del dominio](/RUP/00-modelo-del-dominio/README.md) / [Requisitos](/RUP/01-requisitos/01-actores-casos-uso/README.md)</sub>

</div>

# Bitácora de Decisiones Arquitectónicas y Evolución RUP

Registro formal y cronológico de decisiones de diseño, acuerdos de modelado y evolución del proyecto **CTS Academy & Evaluator** bajo la metodología RUP (Rational Unified Process).

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
