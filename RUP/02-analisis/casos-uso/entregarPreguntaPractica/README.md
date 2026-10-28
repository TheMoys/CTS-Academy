<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [01 Requisitos](/RUP/01-requisitos/README.md) | [02 Análisis](/RUP/02-analisis/README.md) | [Catálogo Requisitos](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

<sub>**Fase 02 Análisis** › **Realización de Casos de Uso** › `entregarPreguntaPractica()`</sub>

</div>

# Realización de Caso de Uso: `entregarPreguntaPractica()`

Esta especificación describe la realización de análisis del caso de uso `entregarPreguntaPractica()` mediante clases BCE, detallando el autoguardado, el versionado continuo de soluciones prácticas, la gestión de cuota en el sandbox Docker (`TestRunner`) y la tolerancia de red por ventana de gracia.

---

<div align=center>

| Diagrama de Clases de Análisis (VOPC) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/entregarPreguntaPractica/clasesAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](clasesAnalisis.puml)</i></sup> |

| Diagrama de Realización de Análisis (Secuencia BCE) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/entregarPreguntaPractica/realizacionAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](realizacionAnalisis.puml)</i></sup> |

</div>

---

## Clases de Análisis Participantes

<div align=center>

| Clase | Estereotipo | Tipo | Responsabilidad Principal |
| :--- | :---: | :---: | :--- |
| **`EditorPractica`** | `<<boundary>>` | Frontera | Interfaz de edición multi-archivo de código, autoguardado pasivo en segundo plano (`RN-EVAL-PRACT-01`), botón de ejecución de suite de tests y formalización de entregas versionadas. |
| **`TestRunner`** | `<<boundary>>` | Frontera (Externa) | Adaptador de integración con los workers de ejecución aislada en Docker; recibe el árbol de ficheros del candidato y la suite de tests, devolviendo el log de ejecución y estado de aserciones. |
| **`GestorEvaluacionPractica`** | `<<control>>` | Control | Control de tiempo con ventana de gracia (`RN-EVAL-PRACT-04`), verificación del límite de cuota de ejecuciones sandbox (`RN-EVAL-PRACT-02`) y consolidación atómica de versiones de entrega. |
| **`Test`** | `<<entity>>` | Entidad | Evaluación técnica en curso; provee el método `tieneTiempoConVentanaGracia()` que concede 60 segundos extra para recepcionar paquetes en vuelo tras el segundo cero. |
| **`Practica`** | `<<entity>>` | Entidad | Reto de código práctico (hereda de `Pregunta`); custodia el enunciado, los archivos de la plantilla inicial, los tests unitarios automatizados y los criterios de rúbrica. |
| **`EntregaPractica`** | `<<entity>>` | Entidad | Registro de solución; mantiene el historial versionado (`v1`, `v2`...), contador de ejecuciones consumidas en sandbox y los resultados consolidados de validación. |

</div>

---

## Flujo de Realización (Colaboración BCE)

### Flujo A: Ejecución de Pruebas Automatizadas en Sandbox (RN-EVAL-PRACT-02)
1. El **`ActorEvaluado`** pulsa el botón "Ejecutar pruebas" en **`EditorPractica`**.
2. **`EditorPractica`** remite el árbol de código a **`GestorEvaluacionPractica`**.
3. **`GestorEvaluacionPractica`** valida que el temporizador del test continúe vigente en el servidor.
4. **`GestorEvaluacionPractica`** consulta `tieneCuotaDisponible()` a la entidad **`EntregaPractica`**:
   - Si ha superado el límite (5 ejecuciones por reto), rechaza la compilación remota y notifica a la frontera que el código solo podrá ser calificado en diferido por el Tech Leader.
   - Si cuenta con cuota, recupera la suite de tests de la entidad **`Practica`** e invoca `compilarYEjecutar()` en el adaptador **`TestRunner`**.
5. **`TestRunner`** ejecuta la suite en el contenedor Docker aislado y retorna los resultados (aserciones pasadas/fallidas y salida estándar).
6. **`GestorEvaluacionPractica`** actualiza el contador en **`EntregaPractica`** y emite la respuesta hacia **`EditorPractica`**, que visualiza los logs de consola y el cupo restante.

### Flujo B: Entrega Formal de Versión de Código (RN-EVAL-PRACT-03)
1. El evaluado pulsa "Entregar solución" en **`EditorPractica`**.
2. **`GestorEvaluacionPractica`** valida la vigencia en **`Test`** aplicando la ventana de gracia de 60 segundos (**RN-EVAL-PRACT-04**).
3. **`GestorEvaluacionPractica`** invoca `consolidarNuevaVersion(archivosCodigo)` en **`EntregaPractica`**, asignando un nuevo identificador secuencial de versión (`v1`, `v2`...).
4. **`EditorPractica`** presenta el acuse de versión guardada con éxito, permitiendo continuar iterando si resta tiempo.

---

## Trazabilidad con la Fase de Requisitos

| Requisito / Artefacto Fase 01 | Realización en Fase 02 (Análisis) |
| :--- | :--- |
| **Caso de Uso `entregarPreguntaPractica()`** | Orquestación mediante `GestorEvaluacionPractica` mediando con `EditorPractica` y `TestRunner`. |
| **RN-EVAL-PRACT-01 (Autoguardado Silencioso)** | Método `guardarBorradorCodigo()` en el controlador invocado periódicamente por la frontera. |
| **RN-EVAL-PRACT-02 (Cuota Sandbox Docker)** | Validación de `tieneCuotaDisponible()` y límite en `EntregaPractica` antes de invocar `TestRunner`. |
| **RN-EVAL-PRACT-03 (Versionado Continuo)** | Registro incremental mediante `consolidarNuevaVersion()` en la entidad `EntregaPractica`. |
| **RN-EVAL-PRACT-04 (Ventana de Gracia)** | Tolerancia técnica de 60s implementada en `tieneTiempoConVentanaGracia()` de la entidad `Test`. |

---

<div align="center">

[Volver a Fase 02: Análisis](/RUP/02-analisis/README.md) • [Ver Especificación de Requisitos (Fase 01)](/RUP/01-requisitos/03-detalle-casos-uso/entregarPreguntaPractica/README.md)

</div>
