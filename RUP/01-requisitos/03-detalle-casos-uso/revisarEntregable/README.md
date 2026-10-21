# Caso de Uso: `revisarEntregable()`

## 1. Identificación y Metadatos

| Atributo | Detalle |
| :--- | :--- |
| **Identificador** | `CU-LEAD-08` |
| **Nombre** | `revisarEntregable()` |
| **Paquete** | `PK03 - MotorFormacion` |
| **Actores** | `LiderEquipo` |
| **Tipo de Flujo** | Inspección y Auditoría de Código |
| **Prioridad** | Crítica (Alta) |
| **Estado** | Especificado |

---

## 2. Descripción General
Permite al Tech Leader inspeccionar detalladamente un entregable de laboratorio práctico presentado por un alumno. Presenta la información completa de la entrega: el enlace al Pull Request de GitHub, la rama de trabajo, las notas explicativas del estudiante, el informe del runner de pruebas automatizadas en contenedor Docker y los criterios de la rúbrica técnica de evaluación, habilitando la posterior emisión de dictamen de aprobación o solicitud de cambios.

---

## 3. Precondiciones y Postcondiciones

### 3.1. Precondiciones
1. El usuario debe estar autenticado con rol `LiderEquipo`.
2. El entregable debe encontrarse en estado `PENDIENTE_REVISION`.

### 3.2. Postcondiciones
1. El sistema presenta el expediente completo de la entrega de código.
2. Se habilita la selección de las acciones resolutivas: aprobar formalmente el entregable o requerir cambios técnicos.

---

## 4. Diagramas de Especificación

### 4.1. Diagrama de Estados del Caso de Uso (RUP)
![Especificación revisarEntregable](/images/RUP/01-requisitos/03-detalle-casos-uso/revisarEntregable/especificacion.svg)

### 4.2. Wireframe / Prototipo de Interfaz
![Wireframe revisarEntregable](/images/RUP/01-requisitos/03-detalle-casos-uso/revisarEntregable/wireframes.svg)

---

## 5. Flujo de Eventos

### 5.1. Flujo Básico (Exitoso)
1. El **LiderEquipo** selecciona un entregable de la bandeja y solicita revisarlo.
2. El **Sistema** recupera la ficha de entrega, los metadatos de Git, las notas del estudiante y los logs del sandbox.
3. El **Sistema** presenta el expediente con el enlace directo al repositorio y Pull Request.
4. El **Sistema** presenta los resultados de ejecución de tests unitarios y métricas de cobertura.
5. El **Sistema** habilita las opciones para emitir la evaluación (`aprobarEntregable()` o `solicitarCambiosEntregable()`).
6. El **Sistema** permite solicitar el retorno a la lista de entregables.

---

## 6. Reglas de Negocio Vinculadas
- **RN-LEAD-08 (Auditoría Integral):** La revisión debe contemplar tanto la aprobación sintáctica de los tests automáticos en el sandbox como la evaluación cualitativa de legibilidad, arquitectura y estándares de código por parte del Tech Leader.
