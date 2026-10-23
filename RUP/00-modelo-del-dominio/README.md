<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [Bitácora ADR](/RUP/BITACORA.md) | **00 Dominio** | [01 Requisitos](/RUP/01-requisitos/README.md) | [02 Análisis](/RUP/02-analisis/README.md) | [03 Diseño](/RUP/03-diseño/README.md) | [04 Desarrollo](/RUP/04-desarrollo/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|

</div>

# Modelo del Dominio — Arquitectura en 3 Microservicios

El modelo del dominio formaliza los conceptos, entidades y relaciones del sistema organizados en **3 microservicios/subsistemas independientes** (*Bounded Contexts*), garantizando una separación estricta de responsabilidades entre la gobernanza de equipos, el motor de exámenes y la plataforma de capacitación formativa.

---

## Microservicios del Sistema

| Microservicio | Propósito y Responsabilidad | Entidades Propias |
| :--- | :--- | :--- |
| **`MotorEquipos`** | **Estructura Organizativa y Gobernanza**<br>Controla los programas, los equipos del centro tecnológico, los alumnos que los integran, el liderazgo técnico y la coordinación general. | `Programa`, `Equipo`, `Alumno`, `LiderEquipo`, `Gestor` |
| **`MotorEvaluacion`** | **Admisión Continua, Batería de Tests y Entrevistas**<br>Canaliza las postulaciones abiertas todo el año, la división por cursos académicos y semestres, la ejecución de la batería de 3 tests (actitud, aptitud y técnico) como indicadores competenciales, y la agenda de entrevistas con el gestor. | `Convocatoria`, `CursoAcademico`, `Semestre`, `Candidato`, `Test`, `Actitud`, `Aptitud`, `Tecnico`, `Resultado`, `Entrevista` |
| **`MotorFormacion`** | **Academy On-Site y Banco de Conocimiento**<br>LMS interno donde se crean capacitaciones divididas en módulos, material de estudio, entregables prácticos y reactivos (teóricos y prácticos). | `Capacitacion`, `Modulo`, `Material`, `Entregable`, `Pregunta`, `Teorica`, `Practica` |

---

## Diagrama Conceptual del Dominio

<div align=center>

![](/images/RUP/00-modelo-del-dominio/modeloDominio.svg)
<sup><i>[Código fuente PlantUML](modeloDominio.puml)</i></sup>

</div>

---

## Glosario de Entidades por Microservicio

### 1. `MotorEquipos`
* **`Programa`**: Marco institucional (Programa PROFER) que gestiona y alberga los equipos del centro tecnológico en convenio con la universidad.
* **`Equipo`**: Una de las unidades técnicas de trabajo de CTS donde los alumnos desarrollan proyectos reales.
* **`Alumno`**: Estudiante incorporado formalmente a un equipo dentro del programa PROFER.
* **`LiderEquipo` (TL)**: Ingeniero senior responsable de liderar un equipo, configurar sus módulos formativos y evaluar la capacitación de sus alumnos.
* **`Gestor`**: Coordinador institucional del programa que organiza las admisiones, conduce las entrevistas y asigna alumnos a los equipos.

### 2. `MotorEvaluacion`
* **`Convocatoria`**: Canal de postulación continua (abierto los 365 días del año) que recibe y gestiona los aspirantes.
* **`CursoAcademico`**: Marco anual (ej. *2024-2025*, *2025-2026*) que organiza la admisión e incorporaciones a los equipos.
* **`Semestre`**: Periodo semestral (*Semestre 1* / *Semestre 2*) en el que se estructuran los cortes de ingreso y formalización de becas.
* **`Candidato`**: Aspirante que postula al programa en cualquier momento del año y rinde la batería diagnóstica de tests.
* **`Test`**: Evaluación objetiva y estructurada de indicadores de desempeño. Se especializa en:
  * **`Actitud`**: Mide competencias blandas, compromiso, motivación, proactividad y encaje en cultura de equipo.
  * **`Aptitud`**: Mide razonamiento lógico, agilidad analítica y capacidad de resolución de problemas.
  * **`Tecnico`**: Reto y preguntas técnicas de especialidad para admisión o nivelación de alumnos.
* **`Resultado`**: Informe diagnóstico y métricas de afinidad técnica/actitudinal emitidas tras la realización de los tests (sin notas de corte excluyentes), consultables de forma exclusiva por el `Gestor`.
* **`Entrevista`**: Sesión en Google Meet agendada y registrada por el `Gestor` desde el perfil del candidato una vez completada la batería de tests (o a su discreción con tests en curso), donde se registran notas cualitativas y se formaliza el dictamen de admisión.

### 3. `MotorFormacion`
* **`Capacitacion`**: Itinerario formativo on-site cursado por el alumno, que concentra y agrega el acervo de materiales técnicos (`Capacitacion o-- Material`).
* **`Modulo`**: Unidad temático-práctica configurada por el líder técnico en la que se agrupan los materiales didácticos (`Modulo <- Material : se agrupa en`) y los entregables de laboratorio (`Modulo o-- Entregable`).
* **`Material`**: Recursos didácticos (guías técnicas en Markdown, diagramas de arquitectura, documentación) que generan los reactivos de evaluación (`Material --> Pregunta : genera`).
* **`Entregable`**: Práctica o ticket en código fuente enviado por el alumno (rama de Git / Pull Request) para revisión de código por el TL.
* **`Pregunta`**: Reactivo de evaluación generado a partir de los contenidos de los materiales. Especializado en:
  * **`Teorica`**: Cuestión conceptual objetiva (HTML, CSS, JS, Git, SQL).
  * **`Practica`**: Reto de código o maquetación con plantilla base y criterios de corrección.

---

## Invariantes y Reglas del Dominio

1. **Desacoplamiento de Servicios y Nutrición de Tests**:
   * Cada motor es autónomo en su persistencia y lógica de negocio. La comunicación entre `MotorEvaluacion` y `MotorFormacion` (donde los tests se nutren de preguntas del banco formativo: `Test ... Pregunta`, y el alumno realiza el test técnico: `Alumno ---> Tecnico : realiza`) se produce a través de contratos de API REST interna.
2. **Transición Formal de Candidato a Alumno (`Candidato -- Alumno : > Cuando se acepta`)**:
   * La relación entre el aspirante y el estudiante no es anónima ni automática; el `Candidato` transiciona a `Alumno` únicamente cuando el `Gestor` formaliza el dictamen favorable de admisión (`admitirAlumnoProfer()`).
3. **Agregación de Alumno a Equipo (`Equipo o-- Alumno`)**:
   * Los alumnos pertenecen a los equipos de CTS por agregación (`o--`), posibilitando la reasignación técnica entre squads o rotaciones interdisciplinares sin destruir el expediente formativo del estudiante.
4. **Composición Estricta de la Entrevista (`Candidato *-- Entrevista`)**:
   * La entrevista personal de admisión pertenece indisolublemente al expediente del candidato (`*--`); no pueden existir entrevistas huérfanas sin una postulación formal activa.
5. **Generación de Preguntas desde Materiales (`Material --> Pregunta : genera`)**:
   * En `MotorFormacion`, el acervo de materiales didácticos es la fuente generadora directa de los reactivos (`Pregunta`), los cuales se agrupan temáticamente en los módulos formativos (`Modulo <- Material : se agrupa en`).
6. **Canalización por Sedes Internacionales y Admisión Continua**:
   * No existe registro público anónimo ni auto-postulación en la plataforma. La captación y recepción de solicitudes es responsabilidad de las sedes en cada país, que recopilan los aspirantes y los remiten al `GestorProfer`. El gestor los da de alta en el sistema (`registrarCandidato()`), agrupándolos en el `CursoAcademico` (ej. 2024-2025) y `Semestre` activo para coordinar las pruebas y los cortes semestrales.
7. **Batería de Tests como Indicadores (Sin Nota de Corte)**:
   * Los 3 tests (`Actitud`, `Aptitud`, `Tecnico`) no actúan como guillotina o filtro eliminatorio por nota mínima. Producen un mapa de indicadores competenciales y de afinidad de equipo para orientar la decisión. Los resultados son estrictamente de consumo interno para el `Gestor` y no se publican al candidato.
8. **Gestión de Entrevistas vía Google Meet y Anotaciones**:
   * El candidato no agenda ni visualiza entrevistas en el sistema. Es el `Gestor` quien, desde el perfil unificado del aspirante, agenda el enlace de Google Meet al verificar los indicadores de los tests (o anticipadamente a su criterio). Tras celebrar la reunión, el Gestor vuelca sus impresiones y anotaciones directamente en el perfil.
9. **Decisión de Admisión y Asignación de Plazas**:
   * La decisión definitiva de admisión a la beca PROFER la formaliza el `Gestor` en el perfil del candidato (`admitirAlumnoProfer()`), contrastando las anotaciones de la entrevista con los indicadores de los tests, asignando al alumno a uno de los 6 equipos con su rol técnico específico, o dictaminando el descarte (`rechazarCandidatura()`).
10. **El Alumno se Capacita en su Equipo**:
    * No existe vínculo directo entre la entidad `Equipo` y `Capacitacion`; la capacitación es una actividad propia del `Alumno` dentro del equipo, supervisada y evaluada por el `LiderEquipo`.
11. **Evaluación Integral por el Líder Técnico**:
    * Al configurar el `Modulo` y evaluar la `Capacitacion`, el `LiderEquipo` evalúa implícitamente tanto los `Entregable`s de código como los tests técnicos de nivelación rendidos por los alumnos de su equipo.

---

## Ciclos de Vida y Estados del Dominio

Las entidades puramente estructurales (`Programa`, `Equipo`, `Material`, `Pregunta`) se gestionan mediante operaciones CRUD sin transiciones de estado complejas. Sin embargo, la lógica de negocio y la dinámica temporal del sistema están gobernadas por **4 máquinas de estados críticas**:

---

### 1. Candidatura — Admisión Continua, Batería de Tests y Entrevista

Representa la evolución del aspirante desde su alta en el sistema tras ser remitido por las sedes hasta su eventual admisión como alumno becario en uno de los 6 equipos:

<div align=center>

![](/images/RUP/00-modelo-del-dominio/estados-entidades/candidatura-estados.svg)
<sup><i>[Código fuente PlantUML](estados-entidades/candidatura-estados.puml)</i></sup>

</div>

* **Remisión por Sedes Internacionales**: El candidato es dado de alta en la plataforma por el Gestor PROFER a partir de las listas remitidas por las sedes de cada país, vinculado al curso académico y semestre activo.
* **Batería de 3 Tests**: Habilita la realización de los tests de Actitud, Aptitud y Técnico, consolidando el perfil de indicadores.
* **Agenda de Google Meet y Anotaciones**: El Gestor agenda la reunión de Google Meet al verificar la finalización de los tests (o anticipadamente a su criterio) y registra sus notas y observaciones en el perfil del aspirante.
* **Dictamen Final**: La evaluación culmina en admisión formal a la beca PROFER (`admitirAlumnoProfer()`), asignando equipo y rol, o en no admisión (`rechazarCandidatura()`).

---

### 2. Test — Ciclo de Ejecución y Consolidación de Indicadores

Controla la ejecución de cualquiera de los tests (actitudinal, aptitudinal o técnico) garantizando la inmutabilidad temporal y la consolidación de métricas:

<div align=center>

![](/images/RUP/00-modelo-del-dominio/estados-entidades/test-estados.svg)
<sup><i>[Código fuente PlantUML](estados-entidades/test-estados.puml)</i></sup>

</div>

* **Control de tiempo inmutable**: El cronómetro corre en el backend. Al llegar a cero, el test se autoentrega y se congelan las respuestas.
* **Procesamiento de resultados**: Baremación automatizada para actitud/aptitud; ejecución en sandbox Docker (`TestRunner`) y rúbrica del TL para el reto técnico.
* **Generación de indicadores**: Emite métricas de afinidad y desempeño sin emitir notas de corte excluyentes.

---

### 3. EntregaLaboratorio — Formación Continua y Code Reviews

Modela el flujo de trabajo ágil dentro del equipo formativo entre el `Alumno` y su `LiderEquipo`:

<div align=center>

![](/images/RUP/00-modelo-del-dominio/estados-entidades/entregaLaboratorio-estados.svg)
<sup><i>[Código fuente PlantUML](estados-entidades/entregaLaboratorio-estados.puml)</i></sup>

</div>

* **Ciclo de Code Review**: El alumno clona el repositorio del ejercicio, abre rama y somete su Pull Request. El TL revisa el código e interactúa hasta la aprobación formal.

---

### 4. Convocatoria — Admisión Continua 365 Días y Cortes Semestrales

Gobierna el marco de admisión permanente y los hitos de corte periódico:

<div align=center>

![](/images/RUP/00-modelo-del-dominio/estados-entidades/convocatoria-estados.svg)
<sup><i>[Código fuente PlantUML](estados-entidades/convocatoria-estados.puml)</i></sup>

</div>

* **Admisión activa permanente**: No existen cancelaciones ni plazos fatales de postulación; las recepciones se mantienen vivas todo el año.
* **Corte semestral**: En cada cambio de semestre se consolidan los alumnos que se incorporan a los 6 equipos de CTS y se da paso al siguiente semestre lectivo.

---

<div align="center">

[Bitácora ADR](/RUP/BITACORA.md) • [Fase 01: Requisitos](/RUP/01-requisitos/README.md)

</div>
