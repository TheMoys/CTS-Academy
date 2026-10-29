<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [Fase 01: Requisitos](/RUP/01-requisitos/README.md) | [Fase 02: Análisis](/RUP/02-analisis/README.md) |
|:---:|:---:|:---:|:---:|

</div>

# Realización de Análisis: `abrirPanelAdmisiones()`

Este documento formaliza la colaboración de análisis entre clases estereotipadas Boundary-Control-Entity (BCE) que realiza el caso de uso `abrirPanelAdmisiones()`, proveyendo al Gestor PROFER el cuadro de mando centralizado de admisiones con visibilidad multisucursal, métricas del embudo de postulaciones y disponibilidad de cupos en tiempo real para los 6 equipos de desarrollo de CTS.

---

## 1. Diagrama de Clases de Análisis (VOPC)

El diagrama de clases participantes (View of Participating Classes) delimita las responsabilidades de agregación estadística, control de acceso de gobernanza y visualización holística de expedientes.

<div align="center">

| Diagrama de Clases de Análisis (VOPC) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/abrirPanelAdmisiones/clasesAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](clasesAnalisis.puml)</i></sup> |

</div>

### Participantes y Estereotipos

| Clase | Estereotipo | Responsabilidad |
| :--- | :---: | :--- |
| **`Gestor`** | `<<actor>>` | Coordinador o responsable institucional de admisiones PROFER que monitorea la cohorte. |
| **`PanelAdmisiones`** | `<<boundary>>` | Interfaz gráfica interactiva que presenta los KPIs consolidados, gráficos de capacidad por equipo y tabla paginada de postulantes. |
| **`GestorAdmisiones`** | `<<control>>` | Controlador de lógica de negocio que consolida los datos globales de admisiones, calcula tasas de ocupación y aplica filtros dinámicos. |
| **`Gestor`** | `<<entity>>` | Perfil del usuario institucional con permisos de acceso holístico. |
| **`Convocatoria`** | `<<entity>>` | Proceso lectivo y temporal de captación de talento en estado abierto o en curso. |
| **`Equipo`** | `<<entity>>` | Unidades de trabajo técnico CTS (Team 01 a Team 06) cuyas capacidades y plazas son fiscalizadas. |
| **`Candidato`** | `<<entity>>` | Expedientes de postulantes de todas las sedes internacionales asociados a la convocatoria. |

---

## 2. Diagrama de Realización de Análisis (Secuencia BCE)

La interacción formaliza la consulta holística sin restricciones de squad y el cálculo en tiempo real de ocupación de plazas.

<div align="center">

| Diagrama de Realización de Análisis (Secuencia BCE) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/abrirPanelAdmisiones/realizacionAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](realizacionAnalisis.puml)</i></sup> |

</div>

### Flujo de Colaboración

1. El actor `Gestor` solicita la apertura del cuadro de mando de admisiones a través del límite `PanelAdmisiones`.
2. `PanelAdmisiones` solicita la consolidación ejecutiva a `GestorAdmisiones` (`obtenerResumenAdmisiones()`).
3. `GestorAdmisiones` valida los privilegios del rol administrativo en `Gestor`.
4. El controlador recupera la instancia vigente de `Convocatoria` (`obtenerConvocatoriaActiva()`).
5. En cumplimiento de **RN-ADM-DASH-01**, el controlador consulta a la entidad `Equipo` para obtener la lista de los 6 equipos de desarrollo de CTS y computar las plazas ocupadas vs. cupo máximo disponible de cada uno.
6. En virtud de **RN-ADM-DASH-02 (ADR-009)**, `GestorAdmisiones` interroga a `Candidato` para listar la totalidad de los expedientes de postulantes sin restricciones geográficas o departamentales (sedes Santander, México, Colombia, etc.).
7. Se computan las métricas agregadas del embudo de admisión (registrados, evaluados, entrevistados, admitidos y rechazados).
8. Se empaquetan los indicadores en `ResumenAdmisionesDTO` y `PanelAdmisiones` renderiza el cuadro de mando integral.

---

## 3. Trazabilidad con Reglas de Negocio

- **RN-ADM-DASH-01 (Visión Agregada de Plazas):** El panel calcula y visualiza en tiempo real la tasa de ocupación de becarios en cada uno de los 6 equipos técnicos de CTS respecto a sus cupos máximos autorizados, alertando sobre saturación o vacantes.
- **RN-ADM-DASH-02 (Centralización de Candidaturas - ADR-009):** A diferencia de los Tech Leaders (cuyo alcance se circunscribe estrictamente a su equipo titular), el Gestor posee visión holística y acceso sin restricciones a todos los aspirantes de todas las sedes y estados.

---

<div align="center">

[Volver al Índice de la Fase 02: Análisis](/RUP/02-analisis/README.md)

</div>
