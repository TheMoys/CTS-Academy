<div align=right>

<sub>[Al inicio](/README.md) / [Bitácora RUP](/RUP/BITACORA.md) / [Modelo del dominio](/RUP/00-modelo-del-dominio/README.md) / **Actores y casos de uso** / [Detalle de casos de uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) / [Análisis](/RUP/02-analisis/README.md) / [Diseño](/RUP/03-diseño/README.md) / [Desarrollo](/RUP/04-desarrollo/README.md)</sub>

</div>

# Actores y Casos de Uso — Fase 01: Requisitos

En esta fase se formalizan los actores que interactúan con **CTS Academy & Evaluator** y el catálogo completo de casos de uso del sistema estructurados en sus 3 microservicios (`MotorEquipos`, `MotorEvaluacion`, `MotorFormacion`), garantizando la trazabilidad entre el dominio conceptual y la futura implementación.

> [!IMPORTANT]
> **Canalización por Sedes Internacionales (Sin `UsuarioNoLogueado`)**:
> La captación y primera criba de aspirantes es realizada por las sedes de la institución en cada país. Las sedes remiten los expedientes recopilados al `GestorProfer`, quien realiza el alta en el sistema (`registrarCandidato()`). Por tanto, la plataforma es un entorno cerrado sin auto-registro anónimo público. El sistema opera exclusivamente con **4 actores autenticados**.

---

## 👥 Catálogo de Actores y Casos de Uso

<div align=center>

| Candidato — Batería de Tests y Agenda | Alumno PROFER — LMS On-Site y Prácticas |
| :---: | :---: |
| ![](/images/RUP/01-requisitos/01-actores-casos-uso/actoresCasosUsoCandidato.svg) | ![](/images/RUP/01-requisitos/01-actores-casos-uso/actoresCasosUsoAlumno.svg) |
| <sup><i>[Código fuente PlantUML](actoresCasosUsoCandidato.puml)</i></sup> | <sup><i>[Código fuente PlantUML](actoresCasosUsoAlumno.puml)</i></sup> |

| LiderEquipo (TL) — Módulos y Code Reviews | Gestor PROFER — Admisiones y Asignación |
| :---: | :---: |
| ![](/images/RUP/01-requisitos/01-actores-casos-uso/actoresCasosUsoLiderEquipo.svg) | ![](/images/RUP/01-requisitos/01-actores-casos-uso/actoresCasosUsoGestor.svg) |
| <sup><i>[Código fuente PlantUML](actoresCasosUsoLiderEquipo.puml)</i></sup> | <sup><i>[Código fuente PlantUML](actoresCasosUsoGestor.puml)</i></sup> |

</div>

---

## 🔄 Diagramas de Contexto por Actor

Siguiendo el estándar de ingeniería de software de UNEATLANTICO (*pyCelda* / Dr. Manuel Masías), se modela **un diagrama de contexto por cada actor**. 

Los estados en estos diagramas **no deben verse simplemente como pantallas**, sino como **contextos de disponibilidad de casos de uso** (qué acciones son invocables en cada momento con independencia del canal o framework frontend). Cada transición lleva el **nombre literal del caso de uso** ya catalogado, sirviendo como mecanismo de verificación formal para detectar callejones sin salida y casos de uso faltantes antes de detallar flujos.

---

### 1. Diagrama de Contexto: `Candidato`

Modela la navegación del aspirante desde su primer acceso hasta la culminación de la batería diagnóstica y la agenda de su entrevista:

<div align=center>

![](/images/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoCandidato.svg)
<sup><i>[Código fuente PlantUML](diagramaContextoCandidato.puml)</i></sup>

</div>

* **Ejecución de Tests**: El candidato rinde cualquiera de los 3 tests (`iniciarTest()`), respondiendo teoría o retos prácticos. El cronómetro corre en el backend y el test se entrega o autoentrega con `finalizarTest()`.
* **Derecho a Entrevista**: Al completar los 3 tests, la acción `agendarEntrevista()` queda disponible por derecho.
* **Vía Excepcional**: Si el `Gestor` otorga dispensa, `agendarEntrevista()` se habilita inmediatamente aunque existan tests pendientes.

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

Modela el gobierno formativo y técnico ejercido por el TL sobre los alumnos y módulos de su equipo:

<div align=center>

![](/images/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoLiderEquipo.svg)
<sup><i>[Código fuente PlantUML](diagramaContextoLiderEquipo.puml)</i></sup>

</div>

* **Configuración del Módulo**: Gestión de materiales didácticos (`crearMaterial()`, `editarMaterial()`, `eliminarMaterial()`).
* **Banco de Conocimiento**: Alta y afinado de preguntas teóricas y retos de código que alimentarán el motor de evaluación (`crearPregunta()`, `editarPregunta()`).
* **Code Reviews**: El TL inspecciona los PRs pendientes (`revisarEntregable()`), solicitando correcciones o aprobando la entrega.
* **Consulta de Aspirantes**: Inspecciona los repositorios, CVs e indicadores de candidatos para valorar su encaje en el equipo (sin intervenir en la entrevista).

---

### 4. Diagrama de Contexto: `Gestor` (`GestorProfer`)

Gobierna la admisión continua, la coordinación de las sedes internacionales y la asignación final de plazas:

<div align=center>

![](/images/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoGestor.svg)
<sup><i>[Código fuente PlantUML](diagramaContextoGestor.puml)</i></sup>

</div>

* **Recepción desde Sedes**: Alta individual o importación por lotes de los candidatos remitidos internacionalmente (`registrarCandidato()`, `importarCandidatosSede()`).
* **Monitoreo de Indicadores**: Consulta de radares de aptitud y actitud (`consultarIndicadoresCandidato()`) y concesión de dispensas para agendar entrevistas con tests incompletos.
* **Entrevista y Asignación**: El gestor conduce la entrevista personal (`realizarEntrevista()`) y dictamina la admisión a la beca formalizando la asignación a uno de los 6 equipos de CTS y su rol técnico (`admitirAlumnoProfer()`).
* **Corte Semestral**: Avanza administrativamente el periodo académico consolidando cohortes.

---

## 🏷️ Convenciones de Nomenclatura y Granularidad

1. **Convención `verboEntidad()`**:
   * Todos los casos de uso siguen el formato formal de método `verboEntidad()` con el sustantivo tomado literalmente de `modeloDominio.puml`.
2. **Granularidad Fina**:
   * Se define un caso de uso independiente por cada alta, baja, actualización o transición distinguible, evitando casos de uso monolíticos ambiguos.
3. **Desacoplamiento de Roles**:
   * El `Candidato` y el `Alumno` tienen espacios de trabajo y casos de uso totalmente separados; la transición de uno a otro se produce únicamente tras la acción `admitirAlumnoProfer()` del `Gestor`.
