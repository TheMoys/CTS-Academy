<div align=right>

<sub>[Al inicio](/README.md) / [Bitácora RUP](/RUP/BITACORA.md) / **Modelo del dominio** / [Actores y casos de uso](/RUP/01-requisitos/01-actores-casos-uso/README.md) / [Detalle de casos de uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) / [Análisis](/RUP/02-analisis/README.md) / [Diseño](/RUP/03-diseño/README.md) / [Desarrollo](/RUP/04-desarrollo/README.md)</sub>

</div>

# Modelo del Dominio — Arquitectura en 3 Microservicios

El modelo del dominio formaliza los conceptos, entidades y relaciones del sistema organizados en **3 microservicios/subsistemas independientes** (*Bounded Contexts*), garantizando una separación estricta de responsabilidades entre la gobernanza de equipos, el motor de exámenes y la plataforma de capacitación formativa.

---

## 🏗️ Los 3 Microservicios del Sistema

| Microservicio | Propósito y Responsabilidad | Entidades Propias |
| :--- | :--- | :--- |
| **`MotorEquipos`** | **Estructura Organizativa y Gobernanza**<br>Controla los programas, los equipos del centro tecnológico, los alumnos que los integran, el liderazgo técnico y la coordinación general. | `Programa`, `Equipo`, `Alumno`, `LiderEquipo`, `Gestor` |
| **`MotorEvaluacion`** | **Admisión Continua, Batería de Tests y Entrevistas**<br>Canaliza las postulaciones abiertas todo el año, la división por cursos académicos y semestres, la ejecución de la batería de 3 tests (actitud, aptitud y técnico) como indicadores competenciales, y la agenda de entrevistas con el gestor. | `Convocatoria`, `CursoAcademico`, `Semestre`, `Candidato`, `Test`, `TestActitud`, `TestAptitud`, `TestTecnico`, `Resultado`, `Entrevista` |
| **`MotorFormacion`** | **Academy On-Site y Banco de Conocimiento**<br>LMS interno donde se crean capacitaciones divididas en módulos, material de estudio, entregables prácticos y reactivos (teóricos y prácticos). | `Capacitacion`, `Modulo`, `Material`, `Entregable`, `Pregunta`, `PreguntaTeorica`, `PreguntaPractica` |

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
  * **`TestActitud`**: Mide competencias blandas, compromiso, motivación, proactividad y encaje en cultura de equipo.
  * **`TestAptitud`**: Mide razonamiento lógico, agilidad analítica y capacidad de resolución de problemas.
  * **`TestTecnico`**: Mide conocimientos técnicos aplicados, nutriéndose de preguntas de los módulos de los 6 equipos de CTS.
* **`Resultado`**: Informe diagnóstico y métricas de afinidad técnica/actitudinal emitidas tras la realización de los tests (sin notas de corte excluyentes).
* **`Entrevista`**: Sesión personal conducida por el `Gestor` a la que todo candidato tiene derecho al completar la batería (o por dispensa excepcional), donde se decide la admisión definitiva.

### 3. `MotorFormacion`
* **`Capacitacion`**: Itinerario formativo on-site cursado por el alumno y evaluado por el líder de su equipo.
* **`Modulo`**: Unidad temático-práctica dentro de una capacitación, configurada por el líder técnico.
* **`Material`**: Recursos didácticos (documentación, vídeos, guías técnicas, repositorios de referencia).
* **`Entregable`**: Práctica o ticket en código fuente enviado por el alumno (rama de Git / Pull Request).
* **`Pregunta`**: Reactivo de evaluación del banco de conocimiento. Especializado en:
  * **`PreguntaTeorica`**: Cuestión conceptual objetiva (HTML, CSS, JS, Git, SQL).
  * **`PreguntaPractica`**: Reto de código o maquetación con plantilla base y criterios de corrección.

---

## Invariantes y Reglas del Dominio

1. **Desacoplamiento de Servicios**:
   * Cada motor es autónomo en su persistencia y lógica de negocio. La comunicación entre `MotorEvaluacion` y `MotorFormacion` (para componer el `TestTecnico` a partir de preguntas de los módulos de los 6 equipos) se produce a través de contratos de API REST interna.
2. **Canalización por Sedes Internacionales y Admisión Continua**:
   * No existe registro público anónimo ni auto-postulación en la plataforma. La captación y recepción de solicitudes es responsabilidad de las sedes en cada país, que recopilan los aspirantes y los remiten al `GestorProfer`. El gestor los da de alta en el sistema (`registrarCandidato()`), agrupándolos en el `CursoAcademico` (ej. 2024-2025) y `Semestre` activo para coordinar las pruebas y los cortes semestrales.
3. **Batería de Tests como Indicadores (Sin Nota de Corte)**:
   * Los 3 tests (`TestActitud`, `TestAptitud`, `TestTecnico`) no actúan como guillotina o filtro eliminatorio por nota mínima. Producen un mapa de indicadores competenciales y de afinidad de equipo para orientar la decisión.
4. **Derecho a Entrevista y Vía Excepcional**:
   * Completar la batería de tests otorga automáticamente al candidato el derecho a agendar su entrevista personal. Excepcionalmente, el `Gestor` puede autorizar la agenda con algún test pendiente.
5. **Decisión de Admisión y Asignación de Plazas**:
   * La decisión definitiva de admisión a la beca PROFER la toma el `Gestor` en la `Entrevista`, contrastando la entrevista con el informe de indicadores de los tests, formalizando la reducción de matrícula y asignando al alumno a uno de los 6 equipos con su rol específico.
6. **El Alumno se Capacita en su Equipo**:
   * No existe vínculo directo entre la entidad `Equipo` y `Capacitacion`; la capacitación es una actividad propia del `Alumno` dentro del equipo, supervisada y evaluada por el `LiderEquipo`.
7. **Evaluación Integral por el Líder Técnico**:
   * Al configurar el `Modulo` y evaluar la `Capacitacion`, el `LiderEquipo` evalúa implícitamente tanto los `Entregable`s de código como los tests técnicos de nivelación rendidos por los alumnos de su equipo.

---

## 🔄 Ciclos de Vida y Máquinas de Estados del Dominio

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
* **Acceso a Entrevista**: Concedido por derecho al finalizar todos los tests, o por dispensa expresa del Gestor si queda alguno pendiente.
* **Dictamen Final**: La entrevista personal con el `Gestor` concluye en admisión (con asignación a equipo y rol) o no admisión.

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
