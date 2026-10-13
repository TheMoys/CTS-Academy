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
| **`MotorEvaluacion`** | **Filtro de Admisión y Motor de Tests**<br>Gestiona las convocatorias de selección, el acceso de candidatos, la ejecución de tests cronometrados y la consolidación de resultados evaluados por el gestor. | `Convocatoria`, `Candidato`, `Test`, `Resultado` |
| **`MotorFormacion`** | **Academy On-Site y Banco de Conocimiento**<br>LMS interno donde se crean capacitaciones divididas en módulos, material de estudio, entregables prácticos y reactivos (teóricos y prácticos). | `Capacitacion`, `Modulo`, `Material`, `Entregable`, `Pregunta`, `PreguntaTeorica`, `PreguntaPractica` |

---

## Diagrama Conceptual del Dominio

<div align=center>

<sup><i>Código fuente: [modeloDominio.puml](modeloDominio.puml)</i></sup>

</div>

```mermaid
classDiagram
  direction LR

  namespace MotorEquipos {
    class Programa
    class Equipo 
    class Alumno
    class LiderEquipo
    class Gestor
  }

  namespace MotorEvaluacion {
    class Convocatoria
    class Candidato
    class Test
    class Resultado
  }

  namespace MotorFormacion {
    class Capacitacion
    class Modulo
    class Material
    class Entregable
    class Pregunta
    class PreguntaTeorica
    class PreguntaPractica
  }

  %% MotorEquipos
  Programa *-- Equipo
  Equipo *-- Alumno
  Equipo --> LiderEquipo : posee
  Programa --> Gestor : es organizado

  %% MotorEvaluacion
  Convocatoria o-- Candidato
  Candidato --> Test : realiza
  Test o-- Resultado

  %% MotorFormacion
  Pregunta <|-- PreguntaTeorica
  Pregunta <|-- PreguntaPractica
  Capacitacion o-- Modulo
  Modulo *-- Material
  Modulo o-- Entregable
  Modulo o-- Pregunta

  %% Relaciones Inter-Microservicios
  Programa --> Convocatoria : abre
  Gestor --> Resultado : evalua
  Test ..> Pregunta : compone reactivos de
  Alumno ---> Test : realiza
  Alumno --> Capacitacion : realiza
  LiderEquipo --> Modulo : configura
  LiderEquipo --> Capacitacion : evalua
```

---

## Glosario de Entidades por Microservicio

### 1. `MotorEquipos`
* **`Programa`**: Marco institucional (Programa PROFER) que gestiona y alberga los equipos del centro tecnológico en convenio con la universidad.
* **`Equipo`**: Una de las unidades técnicas de trabajo de CTS donde los alumnos desarrollan proyectos reales.
* **`Alumno`**: Estudiante incorporado formalmente a un equipo dentro del programa PROFER.
* **`LiderEquipo` (TL)**: Ingeniero senior responsable de liderar un equipo, configurar sus módulos formativos y evaluar la capacitación de sus alumnos.
* **`Gestor`**: Coordinador institucional del programa que organiza las convocatorias y evalúa los resultados de admisión.

### 2. `MotorEvaluacion`
* **`Convocatoria`**: Proceso formal y temporalizado de captación de talento abierto por el programa.
* **`Candidato`**: Aspirante que postula a una convocatoria y rinde la prueba técnica de ingreso (primer filtro).
* **`Test`**: Evaluación objetiva y práctica con temporizador en servidor. Puede ser ejecutado por un `Candidato` (admisión) o por un `Alumno` (evaluación periódica/fin de módulo).
* **`Resultado`**: Calificación e informe diagnóstico emitido tras la realización del test, evaluado por el gestor para la toma de decisiones.

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
   * Cada motor es autónomo en su persistencia y lógica de negocio. La comunicación entre `MotorEvaluacion` y `MotorFormacion` (para componer tests a partir de preguntas) se produce a través de contratos de API REST interna.
2. **Reutilización del Motor de Evaluación**:
   * El `Test` es agnóstico al rol de quien lo rinde: tanto un `Candidato` en fase de ingreso como un `Alumno` activo en formación pueden rendir tests.
3. **El Alumno se Capacita en su Equipo**:
   * No existe vínculo directo entre la entidad `Equipo` y `Capacitacion`; la capacitación es una actividad propia del `Alumno` dentro del equipo, supervisada y evaluada por el `LiderEquipo`.
4. **Evaluación Integral por el Líder Técnico**:
   * Al configurar el `Modulo` y evaluar la `Capacitacion`, el `LiderEquipo` evalúa implícitamente tanto los `Entregable`s de código como los tests de fin de módulo rendidos por los alumnos de su equipo.
5. **Decisión de Admisión**:
   * La evaluación del `Resultado` del test por parte del `Gestor` determina el paso del `Candidato` a `Alumno` y su asignación a un `Equipo`.
