<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

<sub>**Fase 01 Requisitos** › **Detalle de Caso de Uso** › `editarPregunta()`</sub>

</div>

# Caso de Uso: `editarPregunta()`


## 1. Identificación y Metadatos

| Atributo | Detalle |
| :--- | :--- |
| **Identificador** | `CU-LEAD-05` |
| **Nombre** | `editarPregunta()` |
| **Paquete** | `PK03 - MotorFormacion` |
| **Actores** | `LiderEquipo` |
| **Tipo de Flujo** | Modificación de Reactivo de Evaluación Técnica |
| **Prioridad** | Media |
| **Estado** | Especificado |

---

## 2. Descripción General
Permite al Tech Leader ajustar el enunciado, las opciones de respuesta, la opción correcta o los parámetros métricos (dificultad, puntaje, tiempo sugerido) de una pregunta técnica registrada en el banco de evaluación. Los cambios aplican a futuros tests generados sin afectar los exámenes ya completados ni los que se encuentren en curso.

---

## 3. Precondiciones y Postcondiciones

### 3.1. Precondiciones
1. El usuario debe estar autenticado con rol `LiderEquipo`.
2. La pregunta técnica debe existir en el banco del equipo.

### 3.2. Postcondiciones
1. El reactivo técnico se actualiza en el catálogo de evaluación.
2. Los nuevos tests técnicos generados a partir de ese momento utilizarán la versión actualizada del reactivo.

---

## 4. Diagramas de Especificación

### 4.1. Diagrama de Estados del Caso de Uso (RUP)
![Especificación editarPregunta](/images/RUP/01-requisitos/03-detalle-casos-uso/editarPregunta/especificacion.svg)

### 4.2. Wireframe / Prototipo de Interfaz
![Wireframe editarPregunta](/images/RUP/01-requisitos/03-detalle-casos-uso/editarPregunta/wireframes.svg)

---

## 5. Flujo de Eventos

### 5.1. Flujo Básico (Exitoso)
1. El **LiderEquipo** selecciona una pregunta técnica en el banco y solicita editarla.
2. El **Sistema** precarga el formulario con los datos vigentes del reactivo.
3. El **LiderEquipo** modifica el enunciado, alternativas o clave de corrección.
4. El **LiderEquipo** solicita actualizar la pregunta.
5. El **Sistema** valida que el reactivo modificado conserve coherencia y al menos una clave correcta.
6. El **Sistema** persiste la actualización.
7. El **Sistema** retorna al banco de preguntas con los cambios reflejados.

### 5.2. Flujo Alternativo: Cancelación Voluntaria
- En cualquier momento antes de guardar, el **LiderEquipo** solicita cancelar la edición.
- El **Sistema** retorna al banco de preguntas sin modificar los datos del reactivo.

---

## 6. Reglas de Negocio Vinculadas
- **RN-LEAD-05 (Inmutabilidad de Exámenes en Curso):** Si una pregunta está presente en un test que un candidato o alumno está respondiendo en ese instante, el examen en ejecución conserva una instantánea inmutable de la versión original.
---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
