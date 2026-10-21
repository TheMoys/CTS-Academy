# Caso de Uso: `editarMaterial()`

## 1. Identificación y Metadatos

| Atributo | Detalle |
| :--- | :--- |
| **Identificador** | `CU-LEAD-02` |
| **Nombre** | `editarMaterial()` |
| **Paquete** | `PK03 - MotorFormacion` |
| **Actores** | `LiderEquipo` |
| **Tipo de Flujo** | Modificación de Contenido Didáctico |
| **Prioridad** | Media |
| **Estado** | Especificado |

---

## 2. Descripción General
Permite al Tech Leader actualizar el contenido pedagógico, los metadatos o los archivos adjuntos de un recurso didáctico existente dentro de los módulos asignados a su equipo. Los cambios surten efecto de manera inmediata para los estudiantes.

---

## 3. Precondiciones y Postcondiciones

### 3.1. Precondiciones
1. El usuario debe estar autenticado con rol `LiderEquipo`.
2. El recurso didáctico a editar debe existir y pertenecer a un módulo del equipo del Tech Leader.

### 3.2. Postcondiciones
1. El recurso didáctico se actualiza con la nueva versión del contenido.
2. Los alumnos que abran el recurso accederán a la versión modificada sin alterar su registro de lecturas históricas.

---

## 4. Diagramas de Especificación

### 4.1. Diagrama de Estados del Caso de Uso (RUP)
![Especificación editarMaterial](/images/RUP/01-requisitos/03-detalle-casos-uso/editarMaterial/especificacion.svg)

### 4.2. Wireframe / Prototipo de Interfaz
![Wireframe editarMaterial](/images/RUP/01-requisitos/03-detalle-casos-uso/editarMaterial/wireframes.svg)

---

## 5. Flujo de Eventos

### 5.1. Flujo Básico (Exitoso)
1. El **LiderEquipo** selecciona un recurso didáctico y solicita editar su información.
2. El **Sistema** precarga el formulario con los valores vigentes (título, tipo, orden, Markdown y adjuntos).
3. El **LiderEquipo** modifica el contenido o los parámetros deseados.
4. El **LiderEquipo** solicita guardar los cambios.
5. El **Sistema** valida que el título no esté vacío y que el contenido mantenga integridad formal.
6. El **Sistema** persiste las modificaciones y actualiza el temario.
7. El **Sistema** retorna a la configuración del módulo mostrando el recurso actualizado.

### 5.2. Flujo Alternativo: Cancelación Voluntaria
- En cualquier momento antes de guardar, el **LiderEquipo** solicita cancelar la edición.
- El **Sistema** descarta las modificaciones no guardadas y retorna al listado sin alterar el recurso.

---

## 6. Reglas de Negocio Vinculadas
- **RN-LEAD-02 (Preservación de Trazabilidad):** Las modificaciones a guías formativas no invalidan las lecturas ya completadas por los alumnos que las leyeron previamente.
