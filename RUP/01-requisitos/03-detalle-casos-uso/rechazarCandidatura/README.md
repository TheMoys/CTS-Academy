<div align=right>

<sub>[Al inicio](/README.md) / [Bitácora RUP](/RUP/BITACORA.md) / [Modelo del dominio](/RUP/00-modelo-del-dominio/README.md) / [Actores y casos de uso](/RUP/01-requisitos/01-actores-casos-uso/README.md) / [Detalle de casos de uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) / **rechazarCandidatura()**</sub>

</div>

# Caso de Uso: `rechazarCandidatura()`

> | [Inicio](/README.md) | [Diagrama de Contexto Gestor](/images/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoGestor.svg) | [Perfil del Candidato](/RUP/01-requisitos/03-detalle-casos-uso/abrirPerfilCandidato/README.md) | **Detalle** | [Análisis](/RUP/02-analisis/README.md) | [Diseño](/RUP/03-diseño/README.md) |
> | :-: | :-: | :-: | :-: | :-: | :-: |

<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/rechazarCandidatura/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/rechazarCandidatura/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## 📋 Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `Gestor` (`GestorProfer`) |
| **Objetivo** | Formalizar la resolución negativa de no admisión de una candidatura, registrando el motivo tipificado del rechazo, archivando el expediente en estado `RECHAZADO` y despachando la comunicación institucional correspondiente al aspirante y a su sede remitente |
| **Tipo** | Secundario, soporte de resolución de admisiones |
| **Nivel** | Objetivo de usuario |
| **Precondición** | El Gestor debe encontrarse autenticado y en el expediente del aspirante (`PERFIL_CANDIDATO_ABIERTO`); la candidatura debe estar en estado pendiente de resolución y no haber sido previamente admitida formalmente |
| **Postcondición Éxito** | Entidad `Candidatura` transiciona a `RECHAZADO` con motivo justificado; credenciales de acceso temporal para tests revocadas; notificación oficial enviada al aspirante y a la sede de origen; el contexto transiciona a `PANEL_ADMISIONES_ABIERTO` |
| **Postcondición Bloqueo** | Si el expediente ya contaba con resolución definitiva previa, el sistema impide la alteración y mantiene la visualización del perfil en modo solo lectura |

</div>

---

## 📑 Reglas de Negocio Asociadas

1. **RN-RECH-01 — Motivación Obligatoria del Dictamen**:
   * Ninguna candidatura puede ser archivada en estado negativo sin la selección de un motivo tipificado institucional (incompatibilidad on-site, inasistencia a entrevista, desajuste competencial, etc.) y una justificación cualitativa interna que fundamente la decisión para fines de auditoría académica.
2. **RN-RECH-02 — Comunicación Institucional Constructiva**:
   * La notificación despachada al aspirante utiliza plantillas institucionales con recomendaciones formativas, agradeciendo su postulación y preservando las relaciones académicas internacionales con las sedes remitentes.
3. **RN-RECH-03 — Revocación de Credenciales de Examen**:
   * Al formalizar el rechazo, el subsistema de acceso revoca de inmediato cualquier token o credencial de evaluación del aspirante, impidiendo nuevos accesos al panel de postulación.

---

## 🔗 Referencias

* [Modelo del Dominio: `Candidato`, `Convocatoria`, `Gestor`](/RUP/00-modelo-del-dominio/README.md)
* [Diagrama de Estados de Candidatura (`EN_EVALUACION` → `RECHAZADO`)](/RUP/00-modelo-del-dominio/estados-entidades/candidatura-estados.puml)
* [Diagrama de Contexto Gestor](/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoGestor.puml)
* [Caso de Uso: `abrirPerfilCandidato()`](/RUP/01-requisitos/03-detalle-casos-uso/abrirPerfilCandidato/README.md)
* [ADR-007: Admisión continua y batería de 3 tests diagnósticos](/RUP/BITACORA.md#adr-007-admisi%C3%B3n-continua-por-ciclos-acad%C3%A9micos-bater%C3%ADa-de-3-tests-e-inclusi%C3%B3n-de-entrevista)
