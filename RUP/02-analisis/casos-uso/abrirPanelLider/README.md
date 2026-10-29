<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [Fase 01: Requisitos](/RUP/01-requisitos/README.md) | [Fase 02: Análisis](/RUP/02-analisis/README.md) |
|:---:|:---:|:---:|:---:|

</div>

# Realización de Análisis: `abrirPanelLider()`

Este documento formaliza la colaboración de análisis entre clases estereotipadas Boundary-Control-Entity (BCE) que realiza el caso de uso `abrirPanelLider()`, proporcionando al Tech Leader el tablero de mando para el seguimiento técnico de los alumnos de su equipo CTS asignado, las alertas tempranas de Pull Requests pendientes de revisión y el estado de sus módulos formativos.

---

## 1. Diagrama de Clases de Análisis (VOPC)

El diagrama de clases participantes (View of Participating Classes) delimita las responsabilidades de visualización, orquestación y entidades del dominio que intervienen en la carga del panel de gobierno técnico.

<div align="center">

| Diagrama de Clases de Análisis (VOPC) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/abrirPanelLider/clasesAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](clasesAnalisis.puml)</i></sup> |

</div>

### Participantes y Estereotipos

| Clase | Estereotipo | Responsabilidad |
| :--- | :---: | :--- |
| **`LiderEquipo`** | `<<actor>>` | Tech Leader titular de un squad de desarrollo de CTS que supervisa el rendimiento técnico de sus alumnos. |
| **`PanelLider`** | `<<boundary>>` | Superficie de interfaz gráfica que renderiza el cuadro de mando de liderazgo, alumnos tutelados y alertas de PRs. |
| **`GestorEquipos`** | `<<control>>` | Controlador de lógica de negocio que orquesta la carga de datos del squad, filtrando por el ámbito de asignación. |
| **`TechLeader`** | `<<entity>>` | Perfil del líder técnico autenticado con la identificación de su equipo adscrito. |
| **`Equipo`** | `<<entity>>` | Representa la unidad de trabajo técnico CTS (Team 01 a Team 06) con sus capacidades y cupos. |
| **`Alumno`** | `<<entity>>` | Becarios matriculados en el equipo, con su rol técnico y nivel de avance curricular. |
| **`Modulo`** | `<<entity>>` | Módulos formativos y de nivelación bajo la responsabilidad pedagógica del equipo. |
| **`EntregaLaboratorio`** | `<<entity>>` | Soluciones de laboratorio remitidas que demandan revisión de código por el Tech Leader. |

---

## 2. Diagrama de Realización de Análisis (Secuencia BCE)

La interacción formaliza el aislamiento de acceso al squad del Tech Leader y la priorización de revisiones pendientes.

<div align="center">

| Diagrama de Realización de Análisis (Secuencia BCE) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/abrirPanelLider/realizacionAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](realizacionAnalisis.puml)</i></sup> |

</div>

### Flujo de Colaboración

1. El actor `LiderEquipo` solicita acceder a su panel de gestión mediante el límite `PanelLider`.
2. `PanelLider` delega la obtención del resumen integral en el controlador `GestorEquipos` (`obtenerResumenLider(idLider)`).
3. `GestorEquipos` recupera el perfil del `TechLeader` para determinar el identificador del equipo adscrito (`obtenerEquipoAsignado()`).
4. En estricto cumplimiento de **RN-TL-01**, el controlador consulta a `Equipo` utilizando el identificador asignado, garantizando que el Tech Leader solo acceda a los datos de su propio escuadrón.
5. Se consultan las instancias de `Alumno` adscritas a dicho equipo (`listarAlumnosPorEquipo`).
6. Se consultan los `Modulo` formativos pertenecientes al equipo para verificar su estado de publicación.
7. Siguiendo **RN-TL-02**, `GestorEquipos` audita las instancias de `EntregaLaboratorio` para identificar las entregas en estado `PENDIENTE_REVISION` y calcular la antigüedad respecto al SLA formativo de 48 horas.
8. Se consolidan las métricas y alertas en un DTO (`ResumenLiderDTO`) y `PanelLider` renderiza el dashboard operativo.

---

## 3. Trazabilidad con Reglas de Negocio

- **RN-TL-01 (Aislamiento y Ámbito de Equipo):** El controlador `GestorEquipos` aísla los accesos estrictamente al `Equipo` del cual el `TechLeader` es titular, impidiendo la visualización cruzada de becarios de otros squads o la cartera global de admisiones.
- **RN-TL-02 (Alertas de Code Review):** Las entregas con estado `PENDIENTE_REVISION` se computan y priorizan en el dashboard principal para minimizar los tiempos de respuesta pedagógica al becario.

---

<div align="center">

[Volver al Índice de la Fase 02: Análisis](/RUP/02-analisis/README.md)

</div>
