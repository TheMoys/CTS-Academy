<div align=right>

<sub>[Al inicio](/README.md) / [Bitácora RUP](/RUP/BITACORA.md) / [Modelo del dominio](/RUP/00-modelo-del-dominio/README.md) / [Actores y casos de uso](/RUP/01-requisitos/01-actores-casos-uso/README.md) / [Detalle de casos de uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) / **cerrarCorteSemestral()**</sub>

</div>

# Caso de Uso: `cerrarCorteSemestral()`

> | [Inicio](/README.md) | [Diagrama de Contexto Gestor](/images/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoGestor.svg) | [Apertura de Periodo](/RUP/01-requisitos/03-detalle-casos-uso/abrirPeriodoIngreso/README.md) | **Detalle** | [Análisis](/RUP/02-analisis/README.md) | [Diseño](/RUP/03-diseño/README.md) |
> | :-: | :-: | :-: | :-: | :-: | :-: |

<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/cerrarCorteSemestral/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/cerrarCorteSemestral/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## 📋 Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `Gestor` (`GestorProfer`) |
| **Objetivo** | Formalizar la clausura administrativa de una convocatoria de admisión tras el vencimiento de su plazo o por decisión institucional, congelando las candidaturas de la cohorte, inhabilitando la realización de nuevos tests y consolidando el informe estadístico final del ciclo |
| **Tipo** | Secundario, soporte de gobernanza y cierre de ciclo |
| **Nivel** | Objetivo de usuario |
| **Precondición** | El actor debe encontrarse autenticado con rol `Gestor` en `GESTION_CICLOS_ABIERTO`; la convocatoria debe encontrarse en estado `ABIERTO` |
| **Postcondición Éxito** | La entidad `Convocatoria` transiciona a `CERRADO`; se congelan los accesos a tests de la cohorte; se genera el consolidado estadístico de admisiones; contexto permanece en `GESTION_CICLOS_ABIERTO` |
| **Postcondición Cancelación** | Si el Gestor cancela tras revisar el balance preliminar, la convocatoria continúa abierta |

</div>

---

## 📑 Reglas de Negocio Asociadas

1. **RN-CORTE-01 — Bloqueo Definitivo de Tests de Admisión**:
   * Al clausurar la convocatoria, ningún candidato perteneciente a dicha cohorte puede iniciar, reanudar ni enviar respuestas de la batería de tests diagnósticos.
2. **RN-CORTE-02 — Archivo Automático por Abandono**:
   * Los expedientes que no hayan completado sus tests o entrevistas en el momento del cierre son archivados automáticamente con causal de abandono o plazo vencido.
3. **RN-CORTE-03 — Consolidación de Métricas Anuales**:
   * El sistema genera un reporte agregado inmutable con la tasa de ocupación de plazas por equipo CTS y la procedencia de los aspirantes por sedes internacionales.

---

## 🔗 Referencias

* [Modelo del Dominio: `Convocatoria`, `CursoAcademico`, `Semestre`](/RUP/00-modelo-del-dominio/README.md)
* [Diagrama de Estados de Convocatoria (`ABIERTO` → `CERRADO`)](/RUP/00-modelo-del-dominio/estados-entidades/convocatoria-estados.puml)
* [Diagrama de Contexto Gestor](/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoGestor.puml)
* [Caso de Uso: `abrirPeriodoIngreso()`](/RUP/01-requisitos/03-detalle-casos-uso/abrirPeriodoIngreso/README.md)
* [ADR-007: Admisión continua y batería de 3 tests diagnósticos](/RUP/BITACORA.md#adr-007-admisi%C3%B3n-continua-por-ciclos-acad%C3%A9micos-bater%C3%ADa-de-3-tests-e-inclusi%C3%B3n-de-entrevista)
