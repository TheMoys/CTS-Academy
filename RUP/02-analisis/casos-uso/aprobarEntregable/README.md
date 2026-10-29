<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [Fase 01: Requisitos](/RUP/01-requisitos/README.md) | [Fase 02: Análisis](/RUP/02-analisis/README.md) |
|:---:|:---:|:---:|:---:|

</div>

# Realización de Análisis: `aprobarEntregable()`

Este documento formaliza la colaboración de análisis entre clases estereotipadas Boundary-Control-Entity (BCE) que realiza el caso de uso `aprobarEntregable()`, permitiendo al Tech Leader emitir el dictamen formal de superación sobre un laboratorio práctico, asignando una calificación numérica aprobatoria y habilitando condicionalmente el test técnico del módulo formativo.

---

## 1. Diagrama de Clases de Análisis (VOPC)

El diagrama de clases participantes delimita las responsabilidades de captura del veredicto, validación del umbral aprobatorio y desbloqueo de hitos curriculares.

<div align="center">

![Diagrama de Clases de Análisis](clasesAnalisis.svg)
*Figura 1: Clases de análisis participantes en `aprobarEntregable()`.*

</div>

### Participantes y Estereotipos

| Clase | Estereotipo | Responsabilidad |
| :--- | :---: | :--- |
| **`LiderEquipo`** | `<<actor>>` | Tech Leader que califica y aprueba formalmente la práctica. |
| **`DialogoAprobacionRevision`** | `<<boundary>>` | Formulario modal para ingresar calificación numérica, rúbrica sumativa y feedback cualitativo. |
| **`GestorRevisiones`** | `<<control>>` | Controlador de lógica de negocio que valida la nota mínima, actualiza el estado de la entrega y comprueba requisitos para desbloquear el test de nivelación. |
| **`EntregaLaboratorio`** | `<<entity>>` | Instancia de la solución enviada cuya máquina de estados transiciona a `APROBADO`. |
| **`RevisionCodigo`** | `<<entity>>` | Registro de auditoría con la calificación final y el veredicto formal emitido por el docente. |
| **`Modulo`** | `<<entity>>` | Contenedor curricular que evalúa si todos sus laboratorios obligatorios han sido superados por el alumno. |
| **`Test`** | `<<entity>>` | Evaluación técnica sumativa del módulo formativo. |
| **`Notificacion`** | `<<entity>>` | Alerta interna encolada para el alumno informando su calificación. |

---

## 2. Diagrama de Realización de Análisis (Secuencia BCE)

La interacción formaliza la verificación del umbral numérico y la compuerta lógica de desbloqueo evaluativo.

<div align="center">

![Diagrama de Realización de Análisis](realizacionAnalisis.svg)
*Figura 2: Secuencia de mensajes BCE para `aprobarEntregable()`.*

</div>

### Flujo de Colaboración

1. El actor `LiderEquipo` abre el diálogo de aprobación desde `DialogoAprobacionRevision`.
2. El Tech Leader ingresa la nota numérica, desglose de rúbrica y observaciones finales, confirmando la acción.
3. `DialogoAprobacionRevision` invoca a `GestorRevisiones` (`emitirDictamenAprobado(...)`).
4. En virtud de **RN-LEAD-09**, `GestorRevisiones` verifica que la calificación asignada sea estrictamente mayor o igual a 7.0/10.0. Si la nota es inferior, se rechaza la aprobación forzando al usuario a subsanar el valor o solicitar cambios.
5. Se persiste la aprobación en `RevisionCodigo` con veredicto `APROBADO`.
6. La entidad `EntregaLaboratorio` transiciona formalmente su estado a `APROBADO` registrando la nota definitiva.
7. Se interroga a `Modulo` para comprobar si todos los ejercicios prácticos obligatorios del módulo formativo han sido aprobados por el alumno.
8. En caso afirmativo, se habilita la instancia de `Test` de fin de módulo para el estudiante.
9. Se encola una `Notificacion` para el alumno informando el veredicto y se confirma la operación al Tech Leader.

---

## 3. Trazabilidad con Reglas de Negocio

- **RN-LEAD-09 (Umbral Aprobatorio):** La nota mínima requerida para certificar un laboratorio práctico como `APROBADO` es de 7.0 puntos sobre 10.0.
- **RN-FORM-04 (Habilitación del Test de Nivelación):** El test técnico del módulo permanece bloqueado hasta que el 100% de los laboratorios del módulo alcancen el estado `APROBADO`.

---

<div align="center">

[Volver al Índice de la Fase 02: Análisis](/RUP/02-analisis/README.md)

</div>
