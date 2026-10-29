<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [Fase 01: Requisitos](/RUP/01-requisitos/README.md) | [Fase 02: Análisis](/RUP/02-analisis/README.md) |
|:---:|:---:|:---:|:---:|

</div>

# Realización de Análisis: `abrirPanelAlumno()`

Este documento formaliza la colaboración de análisis entre clases estereotipadas Boundary-Control-Entity (BCE) que realiza el caso de uso `abrirPanelAlumno()`, dando cumplimiento a los requisitos de consulta del tablero de mando de formación para estudiantes becarios admitidos en los equipos CTS.

---

## 1. Diagrama de Clases de Análisis (VOPC)

El diagrama de clases participantes (View of Participating Classes) delimita las responsabilidades de interfaz, orquestación y entidades del dominio que intervienen en la carga y presentación de las métricas formativas del alumno.

<div align="center">

![Diagrama de Clases de Análisis](clasesAnalisis.svg)
*Figura 1: Clases de análisis participantes en `abrirPanelAlumno()`.*

</div>

### Participantes y Estereotipos

| Clase | Estereotipo | Responsabilidad |
| :--- | :---: | :--- |
| **`Alumno`** | `<<actor>>` | Estudiante becario asignado a un equipo técnico CTS que consulta su estado formativo. |
| **`PanelAlumno`** | `<<boundary>>` | Superficie de interfaz gráfica que renderiza el cuadro de mando, indicadores de avance y enlaces de acción. |
| **`GestorFormacion`** | `<<control>>` | Controlador de lógica de negocio responsable de consolidar métricas curriculares, módulos activos y entregas. |
| **`Alumno`** | `<<entity>>` | Representa la identidad, historial de admisión, equipo y rol técnico del estudiante. |
| **`Equipo`** | `<<entity>>` | Representa el squad técnico CTS (Equipos 1 a 6) al cual se encuentra adscrito el becario. |
| **`TechLeader`** | `<<entity>>` | Docente / Líder técnico responsable exclusivo de la mentoría y evaluación del alumno. |
| **`Capacitacion`** | `<<entity>>` | Itinerario curricular y competencias especializadas asignadas a la especialidad del alumno. |
| **`Modulo`** | `<<entity>>` | Unidad temática formativa; determina cuál es el módulo activo en curso. |
| **`EntregaLaboratorio`** | `<<entity>>` | Historial de soluciones remitidas por el alumno para alertar sobre revisiones y retroalimentaciones pendientes. |

---

## 2. Diagrama de Realización de Análisis (Secuencia BCE)

La realización demuestra la orquestación de mensajes entre los componentes lógicos para sincronizar el panel principal sin exponer detalles de persistencia relacional.

<div align="center">

![Diagrama de Realización de Análisis](realizacionAnalisis.svg)
*Figura 2: Secuencia de mensajes BCE para `abrirPanelAlumno()`.*

</div>

### Flujo de Colaboración

1. El actor `Alumno` solicita el acceso a su cuadro de mando formativo a través del límite `PanelAlumno`.
2. `PanelAlumno` delega en `GestorFormacion` la consulta integral (`obtenerResumenAlumno(idAlumno)`).
3. `GestorFormacion` recupera los datos de adscripción de `Alumno` (equipo asignado y rol técnico).
4. En virtud de **RN-FORM-02**, `GestorFormacion` consulta a `Equipo` para obtener la información de tutela directa del `TechLeader`.
5. Siguiendo **RN-FORM-01**, se consulta a `Capacitacion` para validar el itinerario del track y se interroga a `Modulo` para identificar la unidad activa en curso.
6. `GestorFormacion` revisa las instancias de `EntregaLaboratorio` para listar aquellas con dictamen emitido por el Tech Leader pendientes de lectura o entregas requeridas de cambios.
7. Se consolidan las métricas curriculares en un DTO y `PanelAlumno` renderiza el tablero interactivo.

---

## 3. Trazabilidad con Reglas de Negocio

- **RN-FORM-01 (Itinerario Secuencial):** El controlador asegura que el módulo en curso respete la correlatividad curricular, no presentando módulos avanzados mientras los anteriores no se encuentren formalmente completados.
- **RN-FORM-02 (Tutelaje Exclusivo):** La entidad `Equipo` vincula al alumno directamente con el líder técnico único de su escuadrón para todas las notificaciones y revisiones.

---

<div align="center">

[Volver al Índice de la Fase 02: Análisis](/RUP/02-analisis/README.md)

</div>
