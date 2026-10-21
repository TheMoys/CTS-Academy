<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

<sub>**Fase 01 Requisitos** › **Detalle de Caso de Uso** › `eliminarPregunta()`</sub>

</div>

# Caso de Uso: `eliminarPregunta()`


## 1. Identificación y Metadatos

| Atributo | Detalle |
| :--- | :--- |
| **Identificador** | `CU-LEAD-06` |
| **Nombre** | `eliminarPregunta()` |
| **Paquete** | `PK03 - MotorFormacion` |
| **Actores** | `LiderEquipo` |
| **Tipo de Flujo** | Desactivación de Reactivo Técnico |
| **Prioridad** | Media-Baja |
| **Estado** | Especificado |

---

## 2. Descripción General
Permite al Tech Leader dar de baja o desactivar una pregunta técnica del banco de evaluación de su especialidad. Para salvaguardar la coherencia estadística y la trazabilidad de los exámenes completados en el pasado, la eliminación se procesa como un borrado lógico (*soft delete*), cambiando el estado del reactivo a `INACTIVO`.

---

## 3. Precondiciones y Postcondiciones

### 3.1. Precondiciones
1. El usuario debe estar autenticado con rol `LiderEquipo`.
2. La pregunta técnica debe existir y encontrarse actualmente activa en el banco.

### 3.2. Postcondiciones
1. La pregunta técnica cambia su estado a `INACTIVO`.
2. Queda excluida de los algoritmos de generación y aleatorización de nuevos exámenes.
3. Se conservan todas las respuestas históricas asociadas a esta pregunta en evaluaciones ya cerradas.

---

## 4. Diagramas de Especificación

### 4.1. Diagrama de Estados del Caso de Uso (RUP)
![Especificación eliminarPregunta](/images/RUP/01-requisitos/03-detalle-casos-uso/eliminarPregunta/especificacion.svg)

### 4.2. Wireframe / Prototipo de Interfaz
![Wireframe eliminarPregunta](/images/RUP/01-requisitos/03-detalle-casos-uso/eliminarPregunta/wireframes.svg)

---

## 5. Flujo de Eventos

### 5.1. Flujo Básico (Exitoso)
1. El **LiderEquipo** selecciona una pregunta técnica del banco y solicita eliminarla.
2. El **Sistema** presenta un diálogo de confirmación informando la cantidad de exámenes históricos que contienen este reactivo.
3. El **LiderEquipo** solicita confirmar la desactivación.
4. El **Sistema** actualiza el estado del reactivo a `INACTIVO`.
5. El **Sistema** retorna al banco de preguntas mostrando el catálogo actualizado.

### 5.2. Flujo Alternativo: Cancelación Voluntaria
- En el paso 2, el **LiderEquipo** solicita cancelar la operación.
- El **Sistema** descarta la solicitud y vuelve a la vista del banco sin realizar cambios.

---

## 6. Reglas de Negocio Vinculadas
- **RN-LEAD-06 (No Eliminación Física de Reactivos):** Está estrictamente prohibido el borrado físico (`DELETE` relacional) de preguntas que hayan formado parte de al menos una evaluación ejecutada.
---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
