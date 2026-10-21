# Caso de Uso: `crearMaterial()`

## 1. Identificación y Metadatos

| Atributo | Detalle |
| :--- | :--- |
| **Identificador** | `CU-LEAD-01` |
| **Nombre** | `crearMaterial()` |
| **Paquete** | `PK03 - MotorFormacion` |
| **Actores** | `LiderEquipo` (Tech Leader de equipo técnico CTS) |
| **Tipo de Flujo** | Creación de Contenido Didáctico |
| **Prioridad** | Media-Alta |
| **Estado** | Especificado |

---

## 2. Descripción General
Permite al Tech Leader diseñar y publicar un nuevo recurso didáctico (guía técnica en Markdown, diagrama arquitectónico, especificación de laboratorio o recurso de referencia) dentro de un módulo formativo bajo su tutela. El material creado queda inmediatamente accesible para los alumnos asignados al equipo.

---

## 3. Precondiciones y Postcondiciones

### 3.1. Precondiciones
1. El usuario debe estar autenticado con rol `LiderEquipo`.
2. El Tech Leader debe tener permisos sobre el módulo seleccionado dentro de su equipo CTS asignado.

### 3.2. Postcondiciones
1. El nuevo recurso didáctico queda almacenado en la base de datos vinculado al módulo y orden de lectura establecido.
2. Los alumnos del equipo pueden consultar el nuevo material en su temario.

---

## 4. Diagramas de Especificación

### 4.1. Diagrama de Estados del Caso de Uso (RUP)
![Especificación crearMaterial](/images/RUP/01-requisitos/03-detalle-casos-uso/crearMaterial/especificacion.svg)

### 4.2. Wireframe / Prototipo de Interfaz
![Wireframe crearMaterial](/images/RUP/01-requisitos/03-detalle-casos-uso/crearMaterial/wireframes.svg)

---

## 5. Flujo de Eventos

### 5.1. Flujo Básico (Exitoso)
1. El **LiderEquipo** solicita crear un nuevo material didáctico desde la pantalla de configuración del módulo.
2. El **Sistema** presenta el formulario de alta con los campos requeridos (título, tipología, tiempo estimado, obligatoriedad y cuerpo del recurso).
3. El **LiderEquipo** introduce los metadatos y el contenido en formato Markdown.
4. El **LiderEquipo** solicita guardar el material.
5. El **Sistema** valida que el título no esté vacío y que el contenido cumpla con los estándares mínimos de longitud.
6. El **Sistema** registra el material y actualiza el temario formativo.
7. El **Sistema** retorna a la configuración del módulo mostrando el nuevo ítem listado.

### 5.2. Flujo Alternativo: Campos Incompletos
- En el paso 5, si el título está vacío o el contenido no contiene texto válido, el **Sistema** presenta un mensaje de validación destacando los campos obligatorios pendientes y mantiene los datos introducidos para su corrección.

---

## 6. Reglas de Negocio Vinculadas
- **RN-LEAD-01 (Propiedad de Módulos):** Un Tech Leader solo puede dar de alta o modificar materiales en los módulos asociados a su equipo técnico CTS.
