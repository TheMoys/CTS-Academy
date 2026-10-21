# Caso de Uso: `abrirEntregablesPendientes()`

## 1. Identificación y Metadatos

| Atributo | Detalle |
| :--- | :--- |
| **Identificador** | `CU-LEAD-07` |
| **Nombre** | `abrirEntregablesPendientes()` |
| **Paquete** | `PK03 - MotorFormacion` |
| **Actores** | `LiderEquipo` |
| **Tipo de Flujo** | Consulta de Cola de Revisiones Técnicas |
| **Prioridad** | Crítica (Alta) |
| **Estado** | Especificado |

---

## 2. Descripción General
Permite al Tech Leader abrir y gestionar la bandeja centralizada de entregables de código (Pull Requests de GitHub) enviados por los alumnos de su equipo técnico CTS que se encuentran pendientes de evaluación. Presenta el estado de ejecución automática del pipeline de integración continua (*CI Sandbox*), la fecha de entrega y el tiempo transcurrido para asegurar el cumplimiento del acuerdo de nivel de servicio (SLA) de retroalimentación.

---

## 3. Precondiciones y Postcondiciones

### 3.1. Precondiciones
1. El usuario debe estar autenticado con rol `LiderEquipo`.
2. El Tech Leader debe tener alumnos asignados a su equipo CTS.

### 3.2. Postcondiciones
1. El sistema realiza la transición hacia el estado `REVISION_ENTREGABLES_ABIERTO`.
2. Se presenta la cola ordenada de entregables priorizada por antigüedad de envío.
3. Se habilita la selección individual para proceder a la revisión técnica detallada.

---

## 4. Diagramas de Especificación

### 4.1. Diagrama de Estados del Caso de Uso (RUP)
![Especificación abrirEntregablesPendientes](/images/RUP/01-requisitos/03-detalle-casos-uso/abrirEntregablesPendientes/especificacion.svg)

### 4.2. Wireframe / Prototipo de Interfaz
![Wireframe abrirEntregablesPendientes](/images/RUP/01-requisitos/03-detalle-casos-uso/abrirEntregablesPendientes/wireframes.svg)

---

## 5. Flujo de Eventos

### 5.1. Flujo Básico (Exitoso)
1. El **LiderEquipo** solicita abrir los entregables pendientes desde el panel de líder o menú principal.
2. El **Sistema** consulta las entregas en estado `PENDIENTE_REVISION` de los alumnos del equipo tutorado.
3. El **Sistema** recupera el resultado de la batería de pruebas automatizadas ejecutadas en el contenedor sandbox.
4. El **Sistema** presenta la lista priorizada con los enlaces directos a los Pull Requests de GitHub.
5. El **Sistema** permite seleccionar cualquier entregable para proceder a la revisión de código (*Code Review*).
6. El **Sistema** permite solicitar el retorno al panel de gestión del líder.

---

## 6. Reglas de Negocio Vinculadas
- **RN-LEAD-07 (SLA de Code Review):** Todo entregable de alumno debe ser revisado y dictaminado por su Tech Leader en un plazo máximo no superior a 48 horas hábiles tras su envío.
