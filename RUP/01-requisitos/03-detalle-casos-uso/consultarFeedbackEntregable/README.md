# Caso de Uso: `consultarFeedbackEntregable()`

## 1. Identificación y Metadatos

| Atributo | Detalle |
| :--- | :--- |
| **Identificador** | `CU-FORM-05` |
| **Nombre** | `consultarFeedbackEntregable()` |
| **Paquete** | `PK03 - MotorFormacion` |
| **Actores** | `Alumno` |
| **Tipo de Flujo** | Consulta de Retroalimentación de Código |
| **Prioridad** | Alta |
| **Estado** | Especificado |

---

## 2. Descripción General
Permite al alumno revisar el veredicto formal y las anotaciones técnicas emitidas por el Tech Leader tras la revisión de código (*Code Review*) de un laboratorio práctico entregado. Presenta la calificación asignada, el estado final (`APROBADO` o `CAMBIOS_SOLICITADOS`) y las observaciones detalladas sobre la calidad, arquitectura y cobertura de pruebas del Pull Request. Si se requieren cambios, habilita la opción de corrección y reenvío.

---

## 3. Precondiciones y Postcondiciones

### 3.1. Precondiciones
1. El alumno debe estar autenticado en la plataforma.
2. El laboratorio práctico debe haber sido previamente entregado y evaluado por el Tech Leader.

### 3.2. Postcondiciones
1. El alumno toma conocimiento formal del estado y comentarios de su entrega de código.
2. Si el dictamen es `CAMBIOS_SOLICITADOS`, se habilita el reenvío de la entrega con las correcciones implementadas.
3. Si el dictamen es `APROBADO`, el laboratorio computa como aprobado para los requisitos del módulo.

---

## 4. Diagramas de Especificación

### 4.1. Diagrama de Estados del Caso de Uso (RUP)
![Especificación consultarFeedbackEntregable](/images/RUP/01-requisitos/03-detalle-casos-uso/consultarFeedbackEntregable/especificacion.svg)

### 4.2. Wireframe / Prototipo de Interfaz
![Wireframe consultarFeedbackEntregable](/images/RUP/01-requisitos/03-detalle-casos-uso/consultarFeedbackEntregable/wireframes.svg)

---

## 5. Flujo de Eventos

### 5.1. Flujo Básico (Exitoso)
1. El **Alumno** selecciona un entregable evaluado y solicita consultar su retroalimentación.
2. El **Sistema** recupera la ficha de entrega, la rama, el enlace de GitHub y la evaluación registrada por el Tech Leader.
3. El **Sistema** presenta el dictamen formal (`APROBADO` o `CAMBIOS_SOLICITADOS`).
4. El **Sistema** presenta la calificación numérica y la rúbrica técnica de evaluación.
5. El **Sistema** presenta las observaciones cualitativas y requerimientos de cambio emitidos por el revisor.
6. Si el estado es `CAMBIOS_SOLICITADOS`, el **Sistema** permite solicitar el reenvío del entregable corregido.
7. El **Sistema** permite solicitar el retorno al detalle del módulo formativo.

---

## 6. Reglas de Negocio Vinculadas
- **RN-FORM-06 (Revisión Obligatoria para Avance):** Ningún laboratorio puede considerarse superado sin la aprobación expresa (`APROBADO`) y calificación numérica superior o igual a 7.0/10.0 por parte del Tech Leader.
