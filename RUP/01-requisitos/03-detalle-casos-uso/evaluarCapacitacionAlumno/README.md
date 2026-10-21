# Caso de Uso: `evaluarCapacitacionAlumno()`

## 1. Identificación y Metadatos

| Atributo | Detalle |
| :--- | :--- |
| **Identificador** | `CU-LEAD-11` |
| **Nombre** | `evaluarCapacitacionAlumno()` |
| **Paquete** | `PK03 - MotorFormacion` |
| **Actores** | `LiderEquipo` |
| **Tipo de Flujo** | Evaluación Final / Certificación de Onboarding |
| **Prioridad** | Crítica (Alta) |
| **Estado** | Especificado |

---

## 2. Descripción General
Permite al Tech Leader emitir el informe final de desempeño y certificación de un alumno que ha completado la totalidad de los módulos formativos de su itinerario en el equipo técnico CTS. Evalúa competencias clave (arquitectura, calidad de software, autonomía y trabajo colaborativo) y emite el dictamen formal sobre su aptitud para integrarse a proyectos productivos reales de la organización.

---

## 3. Precondiciones y Postcondiciones

### 3.1. Precondiciones
1. El usuario debe estar autenticado con rol `LiderEquipo`.
2. El alumno tutelado debe haber completado el 100% de los módulos formativos y laboratorios exigidos en su itinerario.

### 3.2. Postcondiciones
1. Se genera y archiva el acta formal de evaluación final de capacitación.
2. El estado del alumno pasa a `CAPACITACION_CONCLUIDA`.
3. Se notifica automáticamente al Gestor de Admisiones y al Alumno con el informe de competencias.

---

## 4. Diagramas de Especificación

### 4.1. Diagrama de Estados del Caso de Uso (RUP)
![Especificación evaluarCapacitacionAlumno](/images/RUP/01-requisitos/03-detalle-casos-uso/evaluarCapacitacionAlumno/especificacion.svg)

### 4.2. Wireframe / Prototipo de Interfaz
![Wireframe evaluarCapacitacionAlumno](/images/RUP/01-requisitos/03-detalle-casos-uso/evaluarCapacitacionAlumno/wireframes.svg)

---

## 5. Flujo de Eventos

### 5.1. Flujo Básico (Exitoso)
1. El **LiderEquipo** selecciona un alumno con itinerario formativo completado y solicita evaluar su capacitación.
2. El **Sistema** consolida las métricas globales del alumno (promedio de entregables, pruebas superadas y asistencias).
3. El **Sistema** presenta la rúbrica de evaluación final por competencias.
4. El **LiderEquipo** asigna el nivel para cada competencia e introduce el dictamen final (`APTO_PRODUCCION` o `REFUERZO`).
5. El **LiderEquipo** solicita registrar la evaluación final.
6. El **Sistema** valida que todos los criterios obligatorios estén ponderados.
7. El **Sistema** expide el acta de certificación y actualiza el expediente del estudiante.
8. El **Sistema** retorna a la vista de gestión del equipo propio.

### 5.2. Flujo Alternativo: Criterios Incompletos
- En el paso 6, si alguna competencia no fue valorada o falta la conclusión técnica del Tech Leader, el **Sistema** presenta un mensaje de validación impidiendo la expedición del acta.

---

## 6. Reglas de Negocio Vinculadas
- **RN-LEAD-11 (Requisito de Completitud Curricular):** No es posible iniciar la evaluación final de capacitación si el alumno mantiene algún laboratorio en estado no aprobado o módulos pendientes de cursar.
