<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [01 Requisitos](/RUP/01-requisitos/README.md) | [02 Análisis](/RUP/02-analisis/README.md) | [Catálogo Requisitos](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

<sub>**Fase 02 Análisis** › **Realización de Casos de Uso** › `responderPreguntaTeorica()`</sub>

</div>

# Realización de Caso de Uso: `responderPreguntaTeorica()`

Esta especificación describe la realización de análisis del caso de uso `responderPreguntaTeorica()` mediante clases BCE, detallando la autoridad temporal del servidor, la inmutabilidad psicométrica en el test de actitud y la persistencia atómica con telemetría.

---

<div align=center>

| Diagrama de Clases de Análisis (VOPC) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/responderPreguntaTeorica/clasesAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](clasesAnalisis.puml)</i></sup> |

| Diagrama de Realización de Análisis (Secuencia BCE) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/responderPreguntaTeorica/realizacionAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](realizacionAnalisis.puml)</i></sup> |

</div>

---

## Clases de Análisis Participantes

<div align=center>

| Clase | Estereotipo | Tipo | Responsabilidad Principal |
| :--- | :---: | :---: | :--- |
| **`PanelPreguntaTeorica`** | `<<boundary>>` | Frontera | Interfaz de selección de opciones de respuesta, visualización del enunciado teórico, confirmación silenciosa de guardado y avisos de bloqueo o fin de tiempo. |
| **`GestorEvaluacion`** | `<<control>>` | Control | Verificación del tiempo autoritativo en servidor (`RN-EVAL-01`), aplicación de la política de inmutabilidad en escalas Likert (`RN-EVAL-02`) y coordinación del guardado atómico. |
| **`Test`** | `<<entity>>` | Entidad | Instancia evaluativa; valida si `horaLimiteServidor` sigue siendo posterior al instante actual (`tieneTiempoDisponible()`) y clasifica la modalidad de prueba. |
| **`Teorica`** | `<<entity>>` | Entidad | Reactivo teórico (hereda de `Pregunta`); custodia el enunciado, opciones de respuesta y la marca de obligatoriedad/inmutabilidad. |
| **`RespuestaTeorica`** | `<<entity>>` | Entidad | Registro de respuesta seleccionado por el aspirante; incluye timestamp, latencia de resolución en segundos y conteo de rectificaciones para telemetría antifraude (`RN-EVAL-04`). |

</div>

---

## Flujo de Realización (Colaboración BCE)

### Flujo Principal: Guardado Exitoso de Respuesta Teórica
1. El **`ActorEvaluado`** selecciona una opción de respuesta en **`PanelPreguntaTeorica`**.
2. **`PanelPreguntaTeorica`** recopila la selección y los metadatos de interacción (latencia), remitiendo `registrarRespuestaTeorica()` a **`GestorEvaluacion`**.
3. **Validación de Reloj Servidor (RN-EVAL-01)**: **`GestorEvaluacion`** consulta `tieneTiempoDisponible()` a la entidad **`Test`**. Al haber tiempo disponible, prosigue.
4. **Verificación de Inmutabilidad Psicométrica (RN-EVAL-02)**: **`GestorEvaluacion`** verifica si la prueba es de tipo `Actitud`. Si es de actitud y ya contaba con respuesta previa registrada, rechaza la modificación para prevenir sesgos de sobre-racionalización.
5. Si es la primera respuesta (o si se trata de un test de navegación libre `Tecnico` o `Aptitud`, **RN-EVAL-03**), **`GestorEvaluacion`** invoca el guardado atómico en **`RespuestaTeorica`**.
6. **`RespuestaTeorica`** confirma la persistencia inmediata.
7. **`GestorEvaluacion`** responde con éxito a **`PanelPreguntaTeorica`**, que actualiza visualmente el estado del reactivo como respondido.

### Flujos Alternativos: Rechazo por Tiempo o Inmutabilidad
* **Tiempo agotado en servidor (RN-EVAL-01)**:
  - Si el reloj autoritativo del backend alcanzó el límite, la respuesta es descartada inmediatamente.
  - **`GestorEvaluacion`** notifica la expiración y **`PanelPreguntaTeorica`** bloquea la interacción, exigiendo transicionar a `finalizarTest()`.
* **Intento de alteración en test de actitud (RN-EVAL-02)**:
  - **`GestorEvaluacion`** bloquea la sobreescritura y **`PanelPreguntaTeorica`** emite una advertencia de inmutabilidad, manteniendo la opción original.

---

## Trazabilidad con la Fase de Requisitos

| Requisito / Artefacto Fase 01 | Realización en Fase 02 (Análisis) |
| :--- | :--- |
| **Caso de Uso `responderPreguntaTeorica()`** | Orquestación en `GestorEvaluacion` conectando `PanelPreguntaTeorica` con `RespuestaTeorica`. |
| **RN-EVAL-01 (Cronómetro Servidor)** | Evaluación de `tieneTiempoDisponible()` en `Test` sin delegar en marcas de tiempo del cliente. |
| **RN-EVAL-02 (Inmutabilidad Psicométrica)** | Bifurcación condicional en `GestorEvaluacion` que bloquea actualizaciones en tests de `Actitud`. |
| **RN-EVAL-03 (Navegación Libre y Guardado Atómico)** | Persistencia individual inmediata en `RespuestaTeorica` sin esperar al cierre del examen. |
| **RN-EVAL-04 (Telemetría y Antifraude)** | Atributos `latenciaSegundos` y `rectificacionesCount` en la entidad `RespuestaTeorica`. |

---

<div align="center">

[Volver a Fase 02: Análisis](/RUP/02-analisis/README.md) • [Ver Especificación de Requisitos (Fase 01)](/RUP/01-requisitos/03-detalle-casos-uso/responderPreguntaTeorica/README.md)

</div>
