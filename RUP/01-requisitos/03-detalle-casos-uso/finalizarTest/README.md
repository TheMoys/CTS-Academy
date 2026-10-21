<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

<sub>**Fase 01 Requisitos** › **Detalle de Caso de Uso** › `finalizarTest()`</sub>

</div>

# Caso de Uso: `finalizarTest()`


<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/finalizarTest/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/finalizarTest/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## 📋 Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `Candidato` (admisión en `Actitud`, `Aptitud` o `Tecnico`), `Alumno` (evaluación continua o test de nivelación técnica en `MotorFormacion`) |
| **Objetivo** | Formalizar el cierre y entrega definitiva de una evaluación diagnóstica o de módulo formativo, ya sea por confirmación voluntaria del evaluado o por autoentrega forzada al expirar el cronómetro en el servidor, congelando atómicamente todos los reactivos y transitando el expediente hacia la fase de procesamiento |
| **Tipo** | Primario, esencial |
| **Nivel** | Objetivo de usuario |
| **Precondición** | El actor debe estar autenticado; el test evaluado debe encontrarse en estado `EN_CURSO` (`TEST_EN_EJECUCION` para Candidato o `TEST_NIVELACION_EN_EJECUCION` para Alumno) |
| **Postcondición Éxito** | La entidad `Test` transiciona a `ENTREGADO` (cierre manual en tiempo) o `EXPIRADO` (autoentrega por cronómetro de backend); las respuestas y el código del sandbox quedan sellados e inmutables; se revoca la sesión del test; el actor retorna a `PANEL_POSTULACION_ABIERTO` (Candidato) o `INICIO_ALUMNO_ABIERTO` (Alumno) |
| **Postcondición Cancelación** | Si el evaluado cancela la acción en el diálogo de balance antes de confirmar (`-[#blue]->`), el sistema reanuda la interacción en `TEST_EN_EJECUCION` sin alterar datos |

</div>

---

## 📑 Reglas de Negocio Asociadas

1. **RN-EVAL-FIN-01 — Opacidad Absoluta de Resultados (ADR-007)**:
   * Al formalizar la entrega, el sistema **no revela** puntuaciones, porcentajes de acierto ni correcciones. El aspirante recibe un acuse de recibo aséptico indicando que su evaluación ha sido registrada y será analizada por el equipo evaluador. Los indicadores y afinidades disciplinarias son de acceso exclusivo para el `Gestor`.
2. **RN-EVAL-FIN-02 — Congelamiento Atómico y Bloqueo Pesimista Post-Cierre**:
   * En el backend (`MotorEvaluacion`), el cambio de estado se ejecuta con bloqueo pesimista a nivel transaccional. Una vez que la entidad alcanza `ENTREGADO` o `EXPIRADO`, cualquier petición HTTP posterior para alterar opciones o enviar código es rechazada atómicamente con error de conflicto (`TestYaCerradoException`).
3. **RN-EVAL-FIN-03 — Autoentrega Forzada por Servidor (Reloj UTC Authoritative)**:
   * El cronómetro se rige de manera estricta por el reloj del servidor. Si el temporizador llega a cero mientras el evaluado está completando reactivos o leyendo el diálogo de confirmación, el sistema ejecuta una autoentrega inmediata con las respuestas consolidadas en el último snapshot, forzando la transición a `EXPIRADO`.
4. **RN-EVAL-FIN-04 — Balance Cuantitativo de Entrega y Confirmación Segura**:
   * En la finalización manual voluntaria, la plataforma presenta un resumen cuantitativo con el desglose de preguntas teóricas y retos de código respondidos versus pendientes. Si existen ítems sin contestar, se exige confirmación explícita con advertencia antes de sellar la entrega.

---

## 🔗 Referencias

* [Modelo del Dominio: `Test`, `Resultado`, `Convocatoria`](/RUP/00-modelo-del-dominio/README.md)
* [Diagrama de Estados de Test (`EN_CURSO` → `ENTREGADO` / `EXPIRADO` → `EN_PROCESAMIENTO`)](/RUP/00-modelo-del-dominio/estados-entidades/test-estados.puml)
* [Diagrama de Contexto Candidato](/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoCandidato.puml)
* [Diagrama de Contexto Alumno](/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoAlumno.puml)
* [ADR-007: Admisión continua y batería de 3 tests diagnósticos](/RUP/BITACORA.md#adr-007-admisi%C3%B3n-continua-por-ciclos-acad%C3%A9micos-bater%C3%ADa-de-3-tests-e-inclusi%C3%B3n-de-entrevista)
---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
