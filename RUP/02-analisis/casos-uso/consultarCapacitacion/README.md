<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [Fase 01: Requisitos](/RUP/01-requisitos/README.md) | [Fase 02: Análisis](/RUP/02-analisis/README.md) |
|:---:|:---:|:---:|:---:|

</div>

# Realización de Análisis: `consultarCapacitacion()`

Este documento formaliza la colaboración de análisis entre clases estereotipadas Boundary-Control-Entity (BCE) que realiza el caso de uso `consultarCapacitacion()`, permitiendo al estudiante becario inspeccionar la hoja de ruta curricular completa vinculada a su escuadrón técnico CTS.

---

## 1. Diagrama de Clases de Análisis (VOPC)

El diagrama de clases participantes delimita las responsabilidades para determinar el estado de avance y el acceso a cada módulo del itinerario.

<div align="center">

![Diagrama de Clases de Análisis](clasesAnalisis.svg)
*Figura 1: Clases de análisis participantes en `consultarCapacitacion()`.*

</div>

### Participantes y Estereotipos

| Clase | Estereotipo | Responsabilidad |
| :--- | :---: | :--- |
| **`Alumno`** | `<<actor>>` | Estudiante autenticado que consulta su plan formativo. |
| **`VistaCapacitacion`** | `<<boundary>>` | Interfaz gráfica que proyecta el mapa de ruta modular y visualiza los bloqueos correlativos. |
| **`GestorFormacion`** | `<<control>>` | Controlador de lógica de negocio que evalúa la secuencialidad de módulos y calcula los porcentajes de avance. |
| **`Alumno`** | `<<entity>>` | Entidad con el rol técnico asignado (e.g. Backend, Frontend, DevOps). |
| **`Capacitacion`** | `<<entity>>` | Agregado curricular del track de especialización correspondiente. |
| **`Modulo`** | `<<entity>>` | Unidad pedagógica secuencial que contiene recursos teóricos y laboratorios prácticos. |
| **`Laboratorio`** | `<<entity>>` | Ejercicio práctico de programación sujeto a aprobación obligatoria. |

---

## 2. Diagrama de Realización de Análisis (Secuencia BCE)

La interacción formaliza el algoritmo de desbloqueo correlativo sin exponer detalles técnicos de persistencia.

<div align="center">

![Diagrama de Realización de Análisis](realizacionAnalisis.svg)
*Figura 2: Secuencia de mensajes BCE para `consultarCapacitacion()`.*

</div>

### Flujo de Colaboración

1. El actor `Alumno` solicita visualizar el itinerario completo desde la interfaz `VistaCapacitacion`.
2. `VistaCapacitacion` delega en `GestorFormacion` la consulta (`obtenerItinerarioCapacitacion(idAlumno)`).
3. `GestorFormacion` interroga a `Alumno` para determinar su track de especialización técnica.
4. Con base en dicho track, se consulta a `Capacitacion` para obtener la lista ordenada de módulos curriculares en cumplimiento de **RN-FORM-01**.
5. Para cada módulo de la colección:
   - Se consulta el estado del alumno frente a dicha unidad temática (`APROBADO`, `EN_CURSO` o `BLOQUEADO`).
   - Aplicando **RN-FORM-03**, si el módulo predecesor no cuenta con aprobación formal por parte del Tech Leader, la unidad queda marcada como bloqueada impidiendo cualquier acceso a sus consignas o evaluaciones.
6. Se compila el DTO del itinerario consolidado y `VistaCapacitacion` renderiza la hoja de ruta con sus respectivos bloqueos e indicadores de avance.

---

## 3. Trazabilidad con Reglas de Negocio

- **RN-FORM-01 (Itinerario Secuencial):** Los módulos se organizan de forma lineal y no se permite la alteración de su orden de ejecución formativa.
- **RN-FORM-03 (Bloqueo de Módulos Futuros):** Los módulos en estado `BLOQUEADO` permanecen estrictamente inaccesibles hasta la aprobación formal del módulo anterior.

---

<div align="center">

[Volver al Índice de la Fase 02: Análisis](/RUP/02-analisis/README.md)

</div>
