<div align=right>

<sub>[Al inicio](/README.md) / [Bitácora RUP](/RUP/BITACORA.md) / [Modelo del dominio](/RUP/00-modelo-del-dominio/README.md) / [Actores y casos de uso](/RUP/01-requisitos/01-actores-casos-uso/README.md) / [Detalle de casos de uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) / **abrirPanelAdmisiones()**</sub>

</div>

# Caso de Uso: `abrirPanelAdmisiones()`

> | [Inicio](/README.md) | [Diagrama de Contexto Gestor](/images/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoGestor.svg) | [Perfil del Candidato](/RUP/01-requisitos/03-detalle-casos-uso/abrirPerfilCandidato/README.md) | **Detalle** | [Análisis](/RUP/02-analisis/README.md) | [Diseño](/RUP/03-diseño/README.md) |
> | :-: | :-: | :-: | :-: | :-: | :-: |

<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/abrirPanelAdmisiones/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/abrirPanelAdmisiones/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## 📋 Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `Gestor` (`GestorProfer`) |
| **Objetivo** | Proveer al Gestor PROFER el cuadro de mando integral de admisiones, presentando las métricas consolidadas de la convocatoria, la disponibilidad de plazas en los 6 equipos de CTS y la tabla interactiva de aspirantes con opciones de filtrado y acceso a expedientes |
| **Tipo** | Primario, concentrador del rol Gestor |
| **Nivel** | Objetivo de usuario |
| **Precondición** | El actor debe encontrarse autenticado con rol `Gestor` (`SESION_CERRADA` $\rightarrow$ `PANEL_ADMISIONES_ABIERTO`) |
| **Postcondición Éxito** | Dashboard de admisiones operativo con KPIs en tiempo real, listado paginado y acciones de alta, importación y gestión de ciclos habilitadas |

</div>

---

## 📑 Reglas de Negocio Asociadas

1. **RN-ADM-DASH-01 — Visión Agregada de Plazas**:
   * El panel calcula en tiempo real la tasa de ocupación de becarios en cada uno de los 6 equipos de desarrollo de CTS (Team 01 a Team 06) respecto a sus cupos máximos autorizados.
2. **RN-ADM-DASH-02 — Centralización de Candidaturas (ADR-009)**:
   * A diferencia de los Tech Leaders (cuyo alcance se circunscribe a su propio equipo), el Gestor posee visión holística de todos los aspirantes de todas las sedes internacionales y convocatorias activas.

---

## 🔗 Referencias

* [Modelo del Dominio: `Gestor`, `Convocatoria`, `Equipo`](/RUP/00-modelo-del-dominio/README.md)
* [Diagrama de Contexto Gestor](/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoGestor.puml)
* [Caso de Uso: `abrirPerfilCandidato()`](/RUP/01-requisitos/03-detalle-casos-uso/abrirPerfilCandidato/README.md)
