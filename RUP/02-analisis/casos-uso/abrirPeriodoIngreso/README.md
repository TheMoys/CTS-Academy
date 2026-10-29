<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [Fase 01: Requisitos](/RUP/01-requisitos/README.md) | [Fase 02: Análisis](/RUP/02-analisis/README.md) |
|:---:|:---:|:---:|:---:|

</div>

# Realización de Análisis: `abrirPeriodoIngreso()`

Este documento formaliza la colaboración de análisis entre clases estereotipadas Boundary-Control-Entity (BCE) que realiza el caso de uso `abrirPeriodoIngreso()`, permitiendo al Gestor PROFER formalizar la creación y apertura temporal de una nueva convocatoria de ingreso vinculada a un curso académico y semestre, asignando los cupos obligatorios a los 6 equipos de desarrollo de CTS bajo el modelo de admisión continua.

---

## 1. Diagrama de Clases de Análisis (VOPC)

El diagrama de clases participantes (View of Participating Classes) delimita las responsabilidades para verificar la consistencia cronológica y parametrizar las capacidades departamentales del ciclo de selección.

<div align="center">

| Diagrama de Clases de Análisis (VOPC) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/abrirPeriodoIngreso/clasesAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](clasesAnalisis.puml)</i></sup> |

</div>

### Participantes y Estereotipos

| Clase | Estereotipo | Responsabilidad |
| :--- | :---: | :--- |
| **`Gestor`** | `<<actor>>` | Coordinador de admisiones autorizado para activar convocatorias institucionales. |
| **`DialogoAperturaConvocatoria`** | `<<boundary>>` | Ventana modal o formulario interactivo para capturar parámetros cronológicos y cupos por equipo. |
| **`GestorCiclosAcademicos`** | `<<control>>` | Controlador de lógica de negocio que valida coherencia de fechas UTC, integridad de cupos y orquesta la creación transaccional. |
| **`Gestor`** | `<<entity>>` | Perfil del usuario institucional con permisos de administración académica. |
| **`CursoAcademico`** | `<<entity>>` | Marco temporal anual del calendario universitario (ej. 2026/2027). |
| **`Semestre`** | `<<entity>>` | Período lectivo semestral asociado al curso académico (ej. Semestre 1 / Semestre 2). |
| **`Convocatoria`** | `<<entity>>` | Entidad central del proceso de admisión, dada de alta en estado `ABIERTO`. |
| **`Equipo`** | `<<entity>>` | Catálogo de squads técnicos de CTS (Team 01 a Team 06). |
| **`CupoEquipoConvocatoria`** | `<<entity>>` | Asociación que fija el número máximo de plazas de becarios asignables a cada equipo para la convocatoria específica. |

---

## 2. Diagrama de Realización de Análisis (Secuencia BCE)

La interacción formaliza las validaciones de cronograma y la asignación simultánea de cupos por escuadrón técnico.

<div align="center">

| Diagrama de Realización de Análisis (Secuencia BCE) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/abrirPeriodoIngreso/realizacionAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](realizacionAnalisis.puml)</i></sup> |

</div>

### Flujo de Colaboración

1. El actor `Gestor` solicita la apertura de un nuevo periodo desde el módulo de gestión de ciclos.
2. `DialogoAperturaConvocatoria` solicita a `GestorCiclosAcademicos` los catálogos vigentes (`obtenerCatalogosCiclos()`).
3. El controlador consulta a `CursoAcademico`, `Semestre` y `Equipo` para suministrar los cursos vigentes y los 6 equipos de desarrollo de CTS al formulario.
4. El `Gestor` diligencia la denominación de la convocatoria, rango de fechas de postulación y cupos máximos por escuadrón, enviando el formulario.
5. Siguiendo **RN-PER-01**, `GestorCiclosAcademicos` verifica que las fechas se encuentren en formato UTC y que la fecha de apertura sea anterior a la de cierre.
6. En virtud de **RN-PER-02**, el controlador verifica que se hayan asignado cupos válidos (mayores a cero) a la totalidad de los 6 equipos técnicos de CTS.
7. Si alguna validación falla, se notifica el error de validación al formulario sin crear registros.
8. Si los datos son conformes, en cumplimiento de **RN-PER-03 (ADR-007)**, se instancia `Convocatoria` en estado `ABIERTO` con modelo de admisión continua, y se persisten las cuotas para cada equipo mediante instancias de `CupoEquipoConvocatoria`.
9. Se presenta la confirmación de activación de la convocatoria al Gestor.

---

## 3. Trazabilidad con Reglas de Negocio

- **RN-PER-01 (Vinculación Temporal Estricta):** Toda convocatoria se vincula a un `CursoAcademico` y `Semestre` válidos, con fechas fijadas explícitamente bajo estándar horario UTC y validación de cronograma consistente (`fechaApertura < fechaCierre`).
- **RN-PER-02 (Cuotas Obligatorias por Equipo):** El sistema exige la fijación explícita de cupos máximos de becarios para cada uno de los 6 equipos CTS antes de admitir la activación de la convocatoria.
- **RN-PER-03 (Compatibilidad con Admisión Continua - ADR-007):** La convocatoria nace en estado `ABIERTO` habilitada para la recepción continua de expedientes a lo largo del periodo lectivo hasta su clausura formal.

---

<div align="center">

[Volver al Índice de la Fase 02: Análisis](/RUP/02-analisis/README.md)

</div>
