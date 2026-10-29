<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [Fase 01: Requisitos](/RUP/01-requisitos/README.md) | [Fase 02: Análisis](/RUP/02-analisis/README.md) |
|:---:|:---:|:---:|:---:|

</div>

# Realización de Análisis: `consultarModulo()`

Este documento formaliza la colaboración de análisis entre clases estereotipadas Boundary-Control-Entity (BCE) que realiza el caso de uso `consultarModulo()`, permitiendo al alumno becario acceder al desglose detallado de recursos didácticos, consignas de laboratorios prácticos y la condición de habilitación del test de nivelación.

---

## 1. Diagrama de Clases de Análisis (VOPC)

El diagrama de clases participantes delimita las responsabilidades de consulta y validación del estado pedagógico de un módulo formativo.

<div align="center">

![Diagrama de Clases de Análisis](clasesAnalisis.svg)
*Figura 1: Clases de análisis participantes en `consultarModulo()`.*

</div>

### Participantes y Estereotipos

| Clase | Estereotipo | Responsabilidad |
| :--- | :---: | :--- |
| **`Alumno`** | `<<actor>>` | Estudiante autenticado que ingresa al módulo formativo. |
| **`VistaModulo`** | `<<boundary>>` | Superficie visual que lista materiales, laboratorios, estados de entrega y botón condicional del test técnico. |
| **`GestorFormacion`** | `<<control>>` | Controlador de lógica de negocio que valida accesibilidad, consolida estados prácticos y evalúa habilitación del test. |
| **`Alumno`** | `<<entity>>` | Entidad con el expediente del estudiante en formación. |
| **`Modulo`** | `<<entity>>` | Contenedor temático que valida si se encuentra habilitado para el estudiante. |
| **`Material`** | `<<entity>>` | Recurso de estudio (Markdown, esquemas de arquitectura, repositorios de referencia). |
| **`Laboratorio`** | `<<entity>>` | Ejercicio práctico con repositorio plantilla y consignas técnicas. |
| **`EntregaLaboratorio`** | `<<entity>>` | Registro de solución enviada por el estudiante con su estado y calificación asignada. |
| **`Test`** | `<<entity>>` | Reactivo evaluativo sumativo de fin de módulo. |

---

## 2. Diagrama de Realización de Análisis (Secuencia BCE)

La interacción formaliza el flujo de inspección y la evaluación de compuertas lógicas impuestas por las reglas de negocio.

<div align="center">

![Diagrama de Realización de Análisis](realizacionAnalisis.svg)
*Figura 2: Secuencia de mensajes BCE para `consultarModulo()`.*

</div>

### Flujo de Colaboración

1. El actor `Alumno` selecciona un módulo formativo para consultar su contenido en `VistaModulo`.
2. `VistaModulo` delega en `GestorFormacion` la consulta (`obtenerDetalleModulo(idAlumno, idModulo)`).
3. `GestorFormacion` valida si `Modulo` es accesible para el alumno (`esAccesiblePara(idAlumno)`). Si el módulo se encuentra bloqueado, se rechaza la navegación.
4. Si el módulo está en estado `EN_CURSO` o `APROBADO`, se listan sus recursos didácticos (`Material`) y ejercicios prácticos (`Laboratorio`).
5. Para cada laboratorio, se consulta la entidad `EntregaLaboratorio` correspondiente al alumno para determinar su estado (`PENDIENTE_REVISION`, `REQUIERE_CAMBIOS`, `APROBADO` o sin entregar).
6. En virtud de **RN-FORM-04**, `GestorFormacion` evalúa si **todos** los laboratorios obligatorios se encuentran formalmente aprobados y si se cumplió con la lectura obligatoria (**RN-FORM-05**).
7. Solo si la condición se cumple en su totalidad, se habilita la acción para iniciar el `Test` técnico de nivelación; en caso contrario, el test se mantiene bloqueado.
8. Se retorna el DTO compilado y `VistaModulo` renderiza las consignas y controles interactivos.

---

## 3. Trazabilidad con Reglas de Negocio

- **RN-FORM-04 (Habilitación del Test de Nivelación):** El test técnico de fin de módulo permanece estrictamente inactivo mientras existan laboratorios prácticos sin entregar o en estado distinto de `APROBADO`.
- **RN-FORM-05 (Cómputo de Lectura Requerida):** La consulta evalúa la finalización de los materiales obligatorios para habilitar el hito sumativo.

---

<div align="center">

[Volver al Índice de la Fase 02: Análisis](/RUP/02-analisis/README.md)

</div>
