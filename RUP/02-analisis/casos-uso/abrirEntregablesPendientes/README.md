<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [Fase 01: Requisitos](/RUP/01-requisitos/README.md) | [Fase 02: Análisis](/RUP/02-analisis/README.md) |
|:---:|:---:|:---:|:---:|

</div>

# Realización de Análisis: `abrirEntregablesPendientes()`

Este documento formaliza la colaboración de análisis entre clases estereotipadas Boundary-Control-Entity (BCE) que realiza el caso de uso `abrirEntregablesPendientes()`, permitiendo al Tech Leader abrir y gestionar la bandeja centralizada de entregables prácticos (Pull Requests) remitidos por los alumnos becarios de su equipo CTS pendientes de evaluación técnica.

---

## 1. Diagrama de Clases de Análisis (VOPC)

El diagrama de clases participantes delimita las responsabilidades para compilar y ordenar la cola de entregables tutelados.

<div align="center">

![Diagrama de Clases de Análisis](clasesAnalisis.svg)
*Figura 1: Clases de análisis participantes en `abrirEntregablesPendientes()`.*

</div>

### Participantes y Estereotipos

| Clase | Estereotipo | Responsabilidad |
| :--- | :---: | :--- |
| **`LiderEquipo`** | `<<actor>>` | Docente / Líder técnico responsable del equipo CTS que inspecciona las entregas pendientes. |
| **`BandejaRevisiones`** | `<<boundary>>` | Interfaz interactiva que presenta la cola de entregables, filtros por módulo y alertas de SLA. |
| **`GestorRevisiones`** | `<<control>>` | Controlador de lógica de negocio que orquesta la consulta de entregas de los alumnos tutelados y calcula los tiempos de espera. |
| **`TechLeader`** | `<<entity>>` | Perfil del líder técnico autenticado. |
| **`Equipo`** | `<<entity>>` | Squad técnico CTS tutelado; relaciona al líder con sus alumnos activos. |
| **`Alumno`** | `<<entity>>` | Estudiante becario autor de la solución práctica. |
| **`Laboratorio`** | `<<entity>>` | Ejercicio práctico al que corresponde la entrega. |
| **`EntregaLaboratorio`** | `<<entity>>` | Solución enviada en estado `PENDIENTE_REVISION`. |

---

## 2. Diagrama de Realización de Análisis (Secuencia BCE)

La interacción formaliza la extracción de datos curriculares y el cálculo de alertas SLA.

<div align="center">

![Diagrama de Realización de Análisis](realizacionAnalisis.svg)
*Figura 2: Secuencia de mensajes BCE para `abrirEntregablesPendientes()`.*

</div>

### Flujo de Colaboración

1. El actor `LiderEquipo` solicita acceder a su bandeja de revisiones desde `BandejaRevisiones`.
2. `BandejaRevisiones` delega en `GestorRevisiones` (`obtenerColaEntregablesPendientes(idLider)`).
3. `GestorRevisiones` consulta a `TechLeader` para identificar el equipo técnico asignado y luego recupera en `Equipo` la lista de alumnos activos tutelados.
4. Con base en esa lista, se interroga a `EntregaLaboratorio` para obtener todas las entregas en estado `PENDIENTE_REVISION`.
5. Para cada entrega recuperada:
   - Se obtienen los datos de identidad del `Alumno` y la consigna del `Laboratorio`.
   - Se calcula el tiempo transcurrido desde `fechaEnvio`.
   - En virtud de **RN-LEAD-07**, se evalúa si el entregable se aproxima o supera el umbral límite del SLA de 48 horas hábiles.
6. La colección se ordena por estricta antigüedad de envío para priorizar los tickets más antiguos.
7. Se retorna el DTO compilado y `BandejaRevisiones` renderiza la tabla interactiva destacando visualmente los ítems en riesgo de SLA.

---

## 3. Trazabilidad con Reglas de Negocio

- **RN-LEAD-07 (SLA de Code Review):** Todo entregable debe ser dictaminado por su Tech Leader en un plazo máximo no superior a 48 horas hábiles tras su envío, resaltando visualmente aquellos que requieran atención inmediata.

---

<div align="center">

[Volver al Índice de la Fase 02: Análisis](/RUP/02-analisis/README.md)

</div>
