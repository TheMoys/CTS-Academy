<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [01 Requisitos](/RUP/01-requisitos/README.md) | [02 Análisis](/RUP/02-analisis/README.md) | [Catálogo Requisitos](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

<sub>**Fase 02 Análisis** › **Realización de Casos de Uso** › `iniciarTest()`</sub>

</div>

# Realización de Caso de Uso: `iniciarTest()`

Esta especificación modela la realización de análisis del caso de uso `iniciarTest()` mediante el patrón BCE, formalizando la transición irreversible a estado en ejecución, el arranque del cronómetro inmutable en servidor y la entrega del primer reactivo evaluativo.

---

<div align=center>

| Diagrama de Clases de Análisis (VOPC) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/iniciarTest/clasesAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](clasesAnalisis.puml)</i></sup> |

| Diagrama de Realización de Análisis (Secuencia BCE) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/iniciarTest/realizacionAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](realizacionAnalisis.puml)</i></sup> |

</div>

---

## Clases de Análisis Participantes

<div align=center>

| Clase | Estereotipo | Tipo | Responsabilidad Principal |
| :--- | :---: | :---: | :--- |
| **`InterfazTest`** | `<<boundary>>` | Frontera | Presentación de las instrucciones previas de la prueba, diálogo modal de confirmación irreversible, renderizado del entorno de examen y despliegue del cronómetro regresivo sincronizado. |
| **`GestorEvaluacion`** | `<<control>>` | Control | Verificación de elegibilidad de la prueba (`PENDIENTE`), fijación del reloj de inicio en el servidor, orquestación de la carga de reactivos y emisión del token temporal de sesión de prueba. |
| **`Test`** | `<<entity>>` | Entidad | Instancia evaluativa concreta (`Actitud`, `Aptitud`, `Tecnico`); custodia el estado transicional (`PENDIENTE` $\rightarrow$ `EN_CURSO`), la duración asignada y la `horaLimiteServidor` inmutable. |
| **`Pregunta`** | `<<entity>>` | Entidad | Banco de reactivos; en el test técnico incorpora preguntas multidisciplinares aportadas por los 6 equipos de CTS para medir afinidades y competencias base. |
| **`SesionEvaluacion`** | `<<entity>>` | Entidad | Contexto volátil de examen en curso; asocia el token de prueba y garantiza la sincronización estricta frente a desconexiones de red. |

</div>

---

## Flujo de Realización (Colaboración BCE)

### Flujo Principal: Inicio Exitoso de la Evaluación
1. El **`ActorEvaluado`** (`Candidato` o `Alumno`) lee las instrucciones y confirma el inicio voluntario de la prueba en **`InterfazTest`**.
2. **`InterfazTest`** invoca `iniciarTest(idTest, idUsuario)` en **`GestorEvaluacion`**.
3. **`GestorEvaluacion`** consulta a la entidad **`Test`** verificando `estaPendiente()`.
4. Al confirmarse la disponibilidad, **`GestorEvaluacion`** invoca `iniciar(horaActualServidor)` en **`Test`**:
   - **`Test`** transiciona su estado a `EN_CURSO`.
   - Se fija la `horaLimiteServidor` (hora actual + `duracionMinutos`), estableciendo la fuente de verdad temporal autoritativa.
5. **`GestorEvaluacion`** recupera la lista de reactivos asociados a la prueba y selecciona el primer ítem.
6. **`GestorEvaluacion`** instancia una **`SesionEvaluacion`** activa con su token criptográfico correspondiente.
7. **`GestorEvaluacion`** retorna el primer reactivo y la duración en segundos a **`InterfazTest`**.
8. **`InterfazTest`** presenta la pantalla de examen (`TEST_EN_EJECUCION`) e inicia el cronómetro regresivo visual.

### Flujo Alternativo: Test No Disponible
1. Si el test ya ha sido entregado (`COMPLETADO`) o su plazo expiró (`EXPIRADO`):
   - **`GestorEvaluacion`** rechaza la petición sin alterar registros.
   - **`InterfazTest`** muestra un mensaje informativo de rechazo y retorna al actor a su panel de origen.

---

## Trazabilidad con la Fase de Requisitos

| Requisito / Artefacto Fase 01 | Realización en Fase 02 (Análisis) |
| :--- | :--- |
| **Caso de Uso `iniciarTest()`** | Realización coordinada por `GestorEvaluacion` mediando entre `InterfazTest` y `Test`. |
| **Regla de Inmutabilidad Temporal** | Asignación de `horaLimiteServidor` inalterable en la entidad `Test` al transicionar a `EN_CURSO`. |
| **Nutrición Multidisciplinar (`Tecnico`)** | Carga de reactivos de `Pregunta` vinculados transversalmente a los módulos de los equipos CTS. |
| **Opacidad Diagnóstica (ADR-007)** | La sesión de evaluación omite notas de corte o ponderaciones, centrándose exclusivamente en la ejecución. |

---

<div align="center">

[Volver a Fase 02: Análisis](/RUP/02-analisis/README.md) • [Ver Especificación de Requisitos (Fase 01)](/RUP/01-requisitos/03-detalle-casos-uso/iniciarTest/README.md)

</div>
