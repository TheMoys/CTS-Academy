<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [01 Requisitos](/RUP/01-requisitos/README.md) | [02 Análisis](/RUP/02-analisis/README.md) | [Catálogo Requisitos](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

<sub>**Fase 02 Análisis** › **Realización de Casos de Uso** › `finalizarTest()`</sub>

</div>

# Realización de Caso de Uso: `finalizarTest()`

Esta especificación modela la realización de análisis del caso de uso `finalizarTest()` mediante clases BCE, describiendo el balance cuantitativo previo a la entrega, el sellado pesimista post-cierre, la autoentrega forzada por temporizador UTC authoritative y la opacidad absoluta de resultados diagnósticos.

---

<div align=center>

| Diagrama de Clases de Análisis (VOPC) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/finalizarTest/clasesAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](clasesAnalisis.puml)</i></sup> |

| Diagrama de Realización de Análisis (Secuencia BCE) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/finalizarTest/realizacionAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](realizacionAnalisis.puml)</i></sup> |

</div>

---

## Clases de Análisis Participantes

<div align=center>

| Clase | Estereotipo | Tipo | Responsabilidad Principal |
| :--- | :---: | :---: | :--- |
| **`DialogoFinalizarTest`** | `<<boundary>>` | Frontera | Presentación del resumen cuantitativo de ítems contestados vs. pendientes (`RN-EVAL-FIN-04`), captura de confirmación final consciente, despliegue del acuse de recibo aséptico y redirección al panel de origen. |
| **`GestorEvaluacion`** | `<<control>>` | Control | Cálculo del balance de prueba, orquestación del cierre voluntario o forzado por servidor (`RN-EVAL-FIN-03`), ejecución del bloqueo pesimista y creación del registro opaco de resultados. |
| **`Test`** | `<<entity>>` | Entidad | Instrumento evaluativo; transiciona de `EN_CURSO` a `ENTREGADO` (voluntario) o `EXPIRADO` (autoentrega), fija la `horaCierreReal` y congela atómicamente sus reactivos (`RN-EVAL-FIN-02`). |
| **`Resultado`** | `<<entity>>` | Entidad | Consolidación diagnóstica; almacena las métricas cuantitativas e indicadores de afinidad procesados de forma diferida, con acceso estrictamente restringido al `Gestor` (`RN-EVAL-FIN-01` / `ADR-007`). |
| **`SesionEvaluacion`** | `<<entity>>` | Entidad | Contexto volátil de examen; es revocado inmediatamente tras el cierre impidiendo cualquier posterior mutación de respuestas. |

</div>

---

## Flujo de Realización (Colaboración BCE)

### Escenario 1: Cierre Voluntario con Balance de Respuestas (RN-EVAL-FIN-04)
1. El **`ActorEvaluado`** solicita finalizar la prueba en **`DialogoFinalizarTest`**.
2. **`DialogoFinalizarTest`** solicita a **`GestorEvaluacion`** el balance cuantitativo actual.
3. **`GestorEvaluacion`** consulta a la entidad **`Test`** y devuelve el número de reactivos contestados y pendientes.
4. **`DialogoFinalizarTest`** presenta el resumen en pantalla:
   - Si existen preguntas sin responder, muestra una advertencia visual destacada.
   - Si el evaluado **cancela**, regresa a `TEST_EN_EJECUCION` sin alterar datos.
   - Si el evaluado **confirma la entrega definitiva**, remite la orden formal de cierre a **`GestorEvaluacion`**.
5. **Sellado Atómico y Bloqueo Pesimista (RN-EVAL-FIN-02)**: **`GestorEvaluacion`** invoca `congelarAtómicamente()` en **`Test`**, transicionando a `ENTREGADO` y rechazando cualquier futura mutación.
6. **Generación de Resultado Opaco (RN-EVAL-FIN-01 / ADR-007)**: Se instancia la entidad **`Resultado`** con los datos crudos para procesamiento en diferido.
7. Se revoca la **`SesionEvaluacion`**.
8. **`DialogoFinalizarTest`** presenta un acuse de recibo aséptico (sin notas ni correcciones) y redirige al panel de origen (`PANEL_POSTULACION_ABIERTO` o `INICIO_ALUMNO_ABIERTO`).

### Escenario 2: Autoentrega Forzada por Servidor (RN-EVAL-FIN-03)
1. El reloj UTC authoritative en el backend detecta que `horaLimiteServidor` ha vencido.
2. **`GestorEvaluacion`** invoca directamente `finalizar(TIEMPO_AGOTADO)` en la entidad **`Test`**, forzando la transición a `EXPIRADO` con el último snapshot consolidado.
3. Se revoca la **`SesionEvaluacion`**.
4. **`GestorEvaluacion`** instruye a **`DialogoFinalizarTest`** a emitir la notificación de tiempo agotado y redirigir inmediatamente al panel principal.

---

## Trazabilidad con la Fase de Requisitos

| Requisito / Artefacto Fase 01 | Realización en Fase 02 (Análisis) |
| :--- | :--- |
| **Caso de Uso `finalizarTest()`** | Orquestación mediante `GestorEvaluacion` con transición de estados en `Test`. |
| **RN-EVAL-FIN-01 (Opacidad de Resultados)** | La entidad `Resultado` se crea de forma desacoplada y la frontera omite cualquier puntuación. |
| **RN-EVAL-FIN-02 (Congelamiento Atómico)** | Invocación de `congelarAtómicamente()` con bloqueo pesimista en la entidad `Test`. |
| **RN-EVAL-FIN-03 (Autoentrega Forzada Servidor)** | Cierre autónomo disparado por el vencimiento de `horaLimiteServidor` en backend. |
| **RN-EVAL-FIN-04 (Balance Cuantitativo)** | Diálogo modal en `DialogoFinalizarTest` con conteo previo de ítems pendientes. |

---

<div align="center">

[Volver a Fase 02: Análisis](/RUP/02-analisis/README.md) • [Ver Especificación de Requisitos (Fase 01)](/RUP/01-requisitos/03-detalle-casos-uso/finalizarTest/README.md)

</div>
