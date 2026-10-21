<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

<sub>**Fase 01 Requisitos** › **Detalle de Caso de Uso** › `crearPregunta()`</sub>

</div>

# Caso de Uso: `crearPregunta()`


## 1. Identificación y Metadatos

| Atributo | Detalle |
| :--- | :--- |
| **Identificador** | `CU-LEAD-04` |
| **Nombre** | `crearPregunta()` |
| **Paquete** | `PK03 - MotorFormacion` |
| **Actores** | `LiderEquipo` |
| **Tipo de Flujo** | Creación de Reactivo de Evaluación Técnica |
| **Prioridad** | Alta |
| **Estado** | Especificado |

---

## 2. Descripción General
Permite al Tech Leader incorporar nuevos reactivos de evaluación técnica al banco de preguntas del sistema (utilizado tanto para tests diagnósticos de candidatos como para evaluaciones técnicas de fin de módulo de los alumnos tutelados). Soporta preguntas teóricas de opción múltiple (MCQ) y retos prácticos con plantillas base.

---

## 3. Precondiciones y Postcondiciones

### 3.1. Precondiciones
1. El usuario debe estar autenticado con rol `LiderEquipo`.
2. El Tech Leader debe tener acceso al banco de preguntas de su especialidad técnica.

### 3.2. Postcondiciones
1. La nueva pregunta queda registrada en estado `ACTIVA` asociada al banco de reactivos.
2. Queda disponible para ser seleccionada aleatoriamente en la generación de tests técnicos.

---

## 4. Diagramas de Especificación

### 4.1. Diagrama de Estados del Caso de Uso (RUP)
![Especificación crearPregunta](/images/RUP/01-requisitos/03-detalle-casos-uso/crearPregunta/especificacion.svg)

### 4.2. Wireframe / Prototipo de Interfaz
![Wireframe crearPregunta](/images/RUP/01-requisitos/03-detalle-casos-uso/crearPregunta/wireframes.svg)

---

## 5. Flujo de Eventos

### 5.1. Flujo Básico (Exitoso)
1. El **LiderEquipo** solicita crear una nueva pregunta técnica desde el banco de reactivos.
2. El **Sistema** presenta el formulario de configuración (tipo de reactivo, categoría técnica, nivel de dificultad, puntos y tiempo sugerido).
3. El **LiderEquipo** introduce el enunciado técnico y las opciones de respuesta, marcando la opción correcta.
4. El **LiderEquipo** solicita guardar la pregunta.
5. El **Sistema** valida que el enunciado contenga texto, existan al menos 2 opciones de respuesta y exactamente una esté marcada como correcta (para MCQ).
6. El **Sistema** almacena la pregunta en la base de datos.
7. El **Sistema** retorna al banco de preguntas mostrando el nuevo reactivo en la lista.

### 5.2. Flujo Alternativo: Reactivo Incompleto
- En el paso 5, si no se marcó una opción correcta o faltan campos obligatorios, el **Sistema** presenta un mensaje de validación impidiendo el guardado hasta su subsanación.

---

## 6. Reglas de Negocio Vinculadas
- **RN-LEAD-04 (Composición de Banco):** Cada pregunta debe estar catalogada obligatoriamente por dificultad (`BÁSICO`, `INTERMEDIO`, `AVANZADO`) para permitir el balanceo automático del motor de tests.
---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
