<div align=right>

<sub>[Al inicio](/README.md) / [Bitácora RUP](/RUP/BITACORA.md) / [Modelo del dominio](/RUP/00-modelo-del-dominio/README.md) / [Actores y casos de uso](/RUP/01-requisitos/01-actores-casos-uso/README.md) / [Detalle de casos de uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) / **abrirPeriodoIngreso()**</sub>

</div>

# Caso de Uso: `abrirPeriodoIngreso()`

> | [Inicio](/README.md) | [Diagrama de Contexto Gestor](/images/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoGestor.svg) | [Panel de Admisiones](/RUP/01-requisitos/03-detalle-casos-uso/abrirPanelAdmisiones/README.md) | **Detalle** | [Análisis](/RUP/02-analisis/README.md) | [Diseño](/RUP/03-diseño/README.md) |
> | :-: | :-: | :-: | :-: | :-: | :-: |

<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/abrirPeriodoIngreso/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/abrirPeriodoIngreso/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## 📋 Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `Gestor` (`GestorProfer`) |
| **Objetivo** | Formalizar la apertura y configuración de una nueva convocatoria de ingreso dentro del curso académico y semestre correspondiente, fijando el cronograma de recepción de candidaturas y los cupos máximos de becarios autorizados para cada uno de los 6 equipos de desarrollo de CTS |
| **Tipo** | Secundario, soporte de gobernanza y planificación |
| **Nivel** | Objetivo de usuario |
| **Precondición** | El actor debe encontrarse autenticado con rol `Gestor` en `PANEL_ADMISIONES_ABIERTO`; el curso académico y semestre deben estar catalogados en el sistema |
| **Postcondición Éxito** | Se crea la entidad `Convocatoria` en estado `ABIERTO` vinculada al `CursoAcademico` y `Semestre`; se asignan las capacidades por equipo; contexto transiciona a `GESTION_CICLOS_ABIERTO` |
| **Postcondición Cancelación** | Si el Gestor cancela el formulario, permanece en `PANEL_ADMISIONES_ABIERTO` sin alterar la configuración previa |

</div>

---

## 📑 Reglas de Negocio Asociadas

1. **RN-PER-01 — Vinculación Temporal Estricta**:
   * Toda convocatoria debe estar suscrita a un `CursoAcademico` y un `Semestre` válidos, con fechas de apertura y cierre explícitas en huso horario UTC.
2. **RN-PER-02 — Cuotas Obligatorias por Equipo**:
   * No se permite activar una convocatoria sin definir el cupo máximo de becarios asignable a cada uno de los 6 equipos formadores de CTS.
3. **RN-PER-03 — Compatibilidad con Admisión Continua (ADR-007)**:
   * Las convocatorias operan bajo el modelo de admisión continua de 365 días con cortes periódicos, permitiendo recepcionar expedientes mientras la fecha límite se mantenga vigente.

---

## 🔗 Referencias

* [Modelo del Dominio: `Convocatoria`, `CursoAcademico`, `Semestre`, `Equipo`](/RUP/00-modelo-del-dominio/README.md)
* [Diagrama de Estados de Convocatoria (`PLANIFICADA` → `ABIERTO` → `CERRADO`)](/RUP/00-modelo-del-dominio/estados-entidades/convocatoria-estados.puml)
* [Diagrama de Contexto Gestor](/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoGestor.puml)
* [ADR-007: Admisión continua y batería de 3 tests diagnósticos](/RUP/BITACORA.md#adr-007-admisi%C3%B3n-continua-por-ciclos-acad%C3%A9micos-bater%C3%ADa-de-3-tests-e-inclusi%C3%B3n-de-entrevista)
