<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [Fase 01: Requisitos](/RUP/01-requisitos/README.md) | [Fase 02: Análisis](/RUP/02-analisis/README.md) |
|:---:|:---:|:---:|:---:|

</div>

# Realización de Análisis: `consultarMaterial()`

Este documento formaliza la colaboración de análisis entre clases estereotipadas Boundary-Control-Entity (BCE) que realiza el caso de uso `consultarMaterial()`, permitiendo al alumno becario visualizar un recurso didáctico (guía técnica, diagramas de arquitectura, referencias a repositorios) y registrar el evento de lectura para el cómputo de avance curricular.

---

## 1. Diagrama de Clases de Análisis (VOPC)

El diagrama de clases participantes delimita las responsabilidades de visualización, orquestación y persistencia de eventos de lectura.

<div align="center">

![Diagrama de Clases de Análisis](clasesAnalisis.svg)
*Figura 1: Clases de análisis participantes en `consultarMaterial()`.*

</div>

### Participantes y Estereotipos

| Clase | Estereotipo | Responsabilidad |
| :--- | :---: | :--- |
| **`Alumno`** | `<<actor>>` | Estudiante autenticado que lee el material didáctico. |
| **`VisorMaterial`** | `<<boundary>>` | Interfaz interactiva de lectura de documentos técnicos con soporte Markdown y recursos externos. |
| **`GestorFormacion`** | `<<control>>` | Controlador de lógica de negocio que valida accesos a módulos, expide contenidos y computa lecturas. |
| **`Alumno`** | `<<entity>>` | Expediente del estudiante. |
| **`Modulo`** | `<<entity>>` | Unidad pedagógica que valida si el recurso pertenece a un módulo en curso o superado. |
| **`Material`** | `<<entity>>` | Recurso didáctico con su contenido estructurado y carácter obligatorio u opcional. |
| **`LecturaMaterial`** | `<<entity>>` | Registro histórico que certifica la lectura completada por el estudiante. |

---

## 2. Diagrama de Realización de Análisis (Secuencia BCE)

La interacción formaliza la entrega del contenido y la posterior confirmación de lectura en estricto cumplimiento de los requisitos formativos.

<div align="center">

![Diagrama de Realización de Análisis](realizacionAnalisis.svg)
*Figura 2: Secuencia de mensajes BCE para `consultarMaterial()`.*

</div>

### Flujo de Colaboración

1. El actor `Alumno` solicita abrir un recurso didáctico a través de `VisorMaterial`.
2. `VisorMaterial` invoca al controlador `GestorFormacion` (`cargarContenidoMaterial(idAlumno, idMaterial)`).
3. `GestorFormacion` obtiene el identificador del módulo desde `Material` y verifica en `Modulo` si el alumno tiene acceso habilitado (`EN_CURSO` o `APROBADO`).
4. Si el módulo está activo, se extrae el contenido técnico de `Material` y se presenta en el límite interactivo `VisorMaterial`.
5. Una vez que el alumno completa la lectura técnica del recurso, se emite la acción de confirmación (`marcarLecturaCompletada()`).
6. `GestorFormacion` genera o actualiza la instancia `LecturaMaterial` marcando el estado como completado.
7. En cumplimiento de **RN-FORM-05**, se recalcula el porcentaje de avance teórico del módulo y se confirma la operación al usuario.

---

## 3. Trazabilidad con Reglas de Negocio

- **RN-FORM-05 (Cómputo de Lectura Requerida):** Para considerar un módulo listo para el test de nivelación, el sistema exige registrar la lectura del 100% de los materiales catalogados como obligatorios por el Tech Leader.

---

<div align="center">

[Volver al Índice de la Fase 02: Análisis](/RUP/02-analisis/README.md)

</div>
