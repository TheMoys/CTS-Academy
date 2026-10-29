<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [01 Requisitos](/RUP/01-requisitos/README.md) | [02 Análisis](/RUP/02-analisis/README.md) | [Catálogo Requisitos](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

<sub>**Fase 02 Análisis** › **Realización de Casos de Uso** › `registrarAnotacionesEntrevista()`</sub>

</div>

# Realización de Caso de Uso: `registrarAnotacionesEntrevista()`

Esta especificación describe la realización de análisis del caso de uso `registrarAnotacionesEntrevista()` mediante clases BCE, formalizando la evaluación tipificada en rúbrica de 4 dimensiones, el almacenamiento inmutable *append-only* en la bitácora cualitativa y el sellado de registros tras el dictamen final.

---

<div align=center>

| Diagrama de Clases de Análisis (VOPC) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/registrarAnotacionesEntrevista/clasesAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](clasesAnalisis.puml)</i></sup> |

| Diagrama de Realización de Análisis (Secuencia BCE) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/registrarAnotacionesEntrevista/realizacionAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](realizacionAnalisis.puml)</i></sup> |

</div>

---

## Clases de Análisis Participantes

<div align=center>

| Clase | Estereotipo | Tipo | Responsabilidad Principal |
| :--- | :---: | :---: | :--- |
| **`FormularioEntrevista`** | `<<boundary>>` | Frontera | Interfaz de captura de rúbrica cuantitativa/cualitativa, presentación cronológica de la bitácora de impresiones y bloqueo ante expedientes formalizados. |
| **`GestorAdmisiones`** | `<<control>>` | Control | Comprobación de que el expediente no cuenta con resolución definitiva (`RN-ANOT-03`), validación de dimensiones completas de rúbrica (`RN-ANOT-01`) e incorporación del evento. |
| **`Candidato`** | `<<entity>>` | Entidad | Aspirante evaluado; verifica si `estadoCandidatura` admite nuevas anotaciones (`estaAbiertoParaAnotaciones()`). |
| **`Entrevista`** | `<<entity>>` | Entidad | Registro de la sesión; actúa como raíz de agregación de la bitácora de eventos cualitativos. |
| **`Anotacion`** | `<<entity>>` | Entidad | Evento individual inmutable (*append-only*); almacena el momento de captura (`PRE_ENTREVISTA`, `EN_SESION`, `POST_DELIBERACION`), las puntuaciones de rúbrica (1 a 5), texto de evidencia y autor (`RN-ANOT-02`). |

</div>

---

## Flujo de Realización (Colaboración BCE)

### Flujo Principal: Registro de Valoración en Bitácora
1. El **`Gestor`** introduce sus observaciones cualitativas y califica las 4 dimensiones de la rúbrica en **`FormularioEntrevista`**.
2. **`FormularioEntrevista`** remite la información a **`GestorAdmisiones`** mediante `registrarAnotacion()`.
3. **Comprobación de Expediente Activo (RN-ANOT-03)**: **`GestorAdmisiones`** comprueba en **`Candidato`** que el expediente no se encuentre cerrado. Al estar en proceso, prosigue.
4. **Validación de Rúbrica Tipificada (RN-ANOT-01 / ADR-007)**: **`GestorAdmisiones`** verifica que se hayan puntuado las 4 dimensiones obligatorias (Comunicación, Fit Cultural, Actitud Profesional y Compromiso con régimen on-site).
5. **Persistencia Append-Only (RN-ANOT-02 / ADR-009)**:
   - Se crea una nueva instancia inmutable de **`Anotacion`** con timestamp, autor y momento de captura.
   - Se invoca `agregarAnotacionAppendOnly()` en **`Entrevista`**, incorporándola al final de la bitácora sin permitir modificaciones destructivas.
6. **`GestorAdmisiones`** confirma el registro exitoso a **`FormularioEntrevista`**, que actualiza el historial visible.

### Flujo Alternativo: Bloqueo por Expediente Resuelto (RN-ANOT-03)
1. Si el candidato ya cuenta con resolución formal cerrada (`ADMITIDO` o `RECHAZADO`):
   - **`Candidato`** devuelve `false` en `estaAbiertoParaAnotaciones()`.
   - **`GestorAdmisiones`** aborta la persistencia y emite un mensaje de bloqueo.
   - **`FormularioEntrevista`** muestra el expediente en modo de solo lectura, impidiendo nuevas entradas.

---

## Trazabilidad con la Fase de Requisitos

| Requisito / Artefacto Fase 01 | Realización en Fase 02 (Análisis) |
| :--- | :--- |
| **Caso de Uso `registrarAnotacionesEntrevista()`** | Coordinación en `GestorAdmisiones` asociando `FormularioEntrevista` con `Entrevista` y `Anotacion`. |
| **RN-ANOT-01 (Dimensiones de Rúbrica)** | Atributos específicos tipificados (`puntuacionComunicacion`, etc.) en la entidad `Anotacion`. |
| **RN-ANOT-02 (Bitácora Append-Only)** | Relación de agregación estricta y método acumulativo `agregarAnotacionAppendOnly()` en `Entrevista`. |
| **RN-ANOT-03 (Inmutabilidad Post-Dictamen)** | Validación previa mediante `estaAbiertoParaAnotaciones()` en la entidad `Candidato`. |

---

<div align="center">

[Volver a Fase 02: Análisis](/RUP/02-analisis/README.md) • [Ver Especificación de Requisitos (Fase 01)](/RUP/01-requisitos/03-detalle-casos-uso/registrarAnotacionesEntrevista/README.md)

</div>
