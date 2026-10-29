<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [Fase 01: Requisitos](/RUP/01-requisitos/README.md) | [Fase 02: Análisis](/RUP/02-analisis/README.md) |
|:---:|:---:|:---:|:---:|

</div>

# Realización de Análisis: `revisarEntregable()`

Este documento formaliza la colaboración de análisis entre clases estereotipadas Boundary-Control-Entity (BCE) que realiza el caso de uso `revisarEntregable()`, permitiendo al Tech Leader auditar integralmente el código fuente de una práctica, revisando tanto la ejecución automatizada de pruebas en el sandbox como la evaluación cualitativa sobre el diff de cambios.

---

## 1. Diagrama de Clases de Análisis (VOPC)

El diagrama de clases participantes delimita las responsabilidades para la inspección técnica del Pull Request y la incorporación de observaciones contextuales.

<div align="center">

![Diagrama de Clases de Análisis](clasesAnalisis.svg)
*Figura 1: Clases de análisis participantes en `revisarEntregable()`.*

</div>

### Participantes y Estereotipos

| Clase | Estereotipo | Responsabilidad |
| :--- | :---: | :--- |
| **`LiderEquipo`** | `<<actor>>` | Tech Leader que examina el código fuente y audita la calidad técnica de la solución. |
| **`EditorRevision`** | `<<boundary>>` | Interfaz interactiva para navegar por el diff de cambios, revisar logs del pipeline y emitir anotaciones por línea. |
| **`ServicioGitRepository`** | `<<boundary>>` | Perímetro externo que obtiene el parche unificado (diff) y la lista de archivos modificados en el PR. |
| **`GestorRevisiones`** | `<<control>>` | Controlador de lógica de negocio que orquesta la compilación del expediente de entrega y almacena las observaciones técnicas. |
| **`EntregaLaboratorio`** | `<<entity>>` | Instancia de la entrega sujeta a revisión, incluyendo metadatos de CI (logs, código de salida del contenedor Docker). |
| **`Laboratorio`** | `<<entity>>` | Consigna curricular con los criterios formales de la rúbrica de calidad. |
| **`RevisionCodigo`** | `<<entity>>` | Instancia en borrador de la evaluación del líder técnico. |
| **`ComentarioRevision`** | `<<entity>>` | Observación técnica específica ligada a una línea y archivo del código fuente. |

---

## 2. Diagrama de Realización de Análisis (Secuencia BCE)

La interacción formaliza la auditoría integral requerida antes de dictaminar la solución.

<div align="center">

![Diagrama de Realización de Análisis](realizacionAnalisis.svg)
*Figura 2: Secuencia de mensajes BCE para `revisarEntregable()`.*

</div>

### Flujo de Colaboración

1. El actor `LiderEquipo` selecciona un entregable de la cola de pendientes desde `EditorRevision`.
2. `EditorRevision` invoca al controlador `GestorRevisiones` (`cargarDetalleParaRevision(idEntrega)`).
3. `GestorRevisiones` recupera los datos de `EntregaLaboratorio` (URL del PR, logs de ejecución de tests y código de salida del runner Docker).
4. Se extrae la rúbrica de evaluación desde `Laboratorio`.
5. Se invoca a `ServicioGitRepository` para descargar el diff unificado del Pull Request.
6. Se inicia o recupera la entidad `RevisionCodigo` en estado borrador.
7. Conforme a **RN-LEAD-08**, se compila el expediente integral presentando tanto la auditoría sintáctica (sandbox CI) como el código fuente.
8. El Tech Leader agrega observaciones contextuales (`agregarObservacionLinea(...)`).
9. `GestorRevisiones` persiste las instancias de `ComentarioRevision` asociadas al borrador y habilita las acciones resolutivas para aprobar o solicitar cambios.

---

## 3. Trazabilidad con Reglas de Negocio

- **RN-LEAD-08 (Auditoría Integral):** La revisión exige evaluar la superación de los tests automáticos en el entorno aislado (sandbox CI) combinada con el análisis cualitativo de arquitectura, estilo y legibilidad del código.

---

<div align="center">

[Volver al Índice de la Fase 02: Análisis](/RUP/02-analisis/README.md)

</div>
