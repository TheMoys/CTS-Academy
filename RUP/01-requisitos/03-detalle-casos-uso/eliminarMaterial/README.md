# Caso de Uso: `eliminarMaterial()`

## 1. Identificación y Metadatos

| Atributo | Detalle |
| :--- | :--- |
| **Identificador** | `CU-LEAD-03` |
| **Nombre** | `eliminarMaterial()` |
| **Paquete** | `PK03 - MotorFormacion` |
| **Actores** | `LiderEquipo` |
| **Tipo de Flujo** | Eliminación / Despublicación de Recurso Didáctico |
| **Prioridad** | Media-Baja |
| **Estado** | Especificado |

---

## 2. Descripción General
Permite al Tech Leader despublicar o eliminar lógicamente un recurso didáctico de un módulo formativo bajo su tutela. Requiere confirmación explícita para evitar supresiones accidentales y preserva la auditoría histórica de lecturas previas.

---

## 3. Precondiciones y Postcondiciones

### 3.1. Precondiciones
1. El usuario debe estar autenticado con rol `LiderEquipo`.
2. El recurso didáctico debe existir en el módulo correspondiente.

### 3.2. Postcondiciones
1. El recurso didáctico se marca como inactivo / eliminado lógicamente en la base de datos.
2. Deja de mostrarse en el temario accesible por los alumnos del equipo.
3. Se reindexa el orden secuencial de los materiales restantes del módulo.

---

## 4. Diagramas de Especificación

### 4.1. Diagrama de Estados del Caso de Uso (RUP)
![Especificación eliminarMaterial](/images/RUP/01-requisitos/03-detalle-casos-uso/eliminarMaterial/especificacion.svg)

### 4.2. Wireframe / Prototipo de Interfaz
![Wireframe eliminarMaterial](/images/RUP/01-requisitos/03-detalle-casos-uso/eliminarMaterial/wireframes.svg)

---

## 5. Flujo de Eventos

### 5.1. Flujo Básico (Exitoso)
1. El **LiderEquipo** selecciona un recurso didáctico y solicita eliminarlo.
2. El **Sistema** presenta un diálogo de confirmación indicando el título del material y las consecuencias de la baja.
3. El **LiderEquipo** solicita confirmar la eliminación.
4. El **Sistema** aplica un borrado lógico (*soft delete*) y reordena los materiales del módulo.
5. El **Sistema** retorna a la vista de configuración del módulo con la lista actualizada.

### 5.2. Flujo Alternativo: Cancelación Voluntaria
- En el paso 2, el **LiderEquipo** solicita cancelar la eliminación.
- El **Sistema** cierra el diálogo de confirmación y regresa al temario sin aplicar cambios.

---

## 6. Reglas de Negocio Vinculadas
- **RN-LEAD-03 (Baja No Destructiva):** La eliminación es siempre lógica para preservar el histórico de métricas de lectura de alumnos de cohortes previas.
