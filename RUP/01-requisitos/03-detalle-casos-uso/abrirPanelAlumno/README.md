# Caso de Uso: `abrirPanelAlumno()`

## 1. Identificación y Metadatos

| Atributo | Detalle |
| :--- | :--- |
| **Identificador** | `CU-FORM-01` |
| **Nombre** | `abrirPanelAlumno()` |
| **Paquete** | `PK03 - MotorFormacion` |
| **Actores** | `Alumno` (estudiante/becario admitido asignado a un equipo CTS) |
| **Tipo de Flujo** | Consulta / Dashboard de Operaciones Formativas |
| **Prioridad** | Crítica (Alta) |
| **Estado** | Especificado |

---

## 2. Descripción General
Permite al alumno becario visualizar su cuadro de mando formativo integral tras iniciar sesión en el sistema. Presenta información de su equipo CTS asignado, su Tech Leader responsable, el avance consolidado en la hoja de ruta de capacitación, el estado del módulo formativo activo, las notificaciones de revisiones de código realizadas por el Tech Leader y los plazos de entrega inmediatos.

---

## 3. Precondiciones y Postcondiciones

### 3.1. Precondiciones
1. El alumno debe estar autenticado con credenciales válidas en la plataforma (estado de sesión activa con rol `Alumno`).
2. El alumno debe estar formalmente admitido y asignado a un equipo técnico CTS (Equipos 1 a 6) con un itinerario formativo activo.

### 3.2. Postcondiciones
1. El sistema presenta el panel principal del alumno con los indicadores actualizados en tiempo real.
2. Se habilitan los enlaces de navegación directa hacia el módulo en curso, la hoja de ruta de capacitación y la bandeja de retroalimentación de entregables.

---

## 4. Diagramas de Especificación

### 4.1. Diagrama de Estados del Caso de Uso (RUP)
![Especificación abrirPanelAlumno](/images/RUP/01-requisitos/03-detalle-casos-uso/abrirPanelAlumno/especificacion.svg)

### 4.2. Wireframe / Prototipo de Interfaz
![Wireframe abrirPanelAlumno](/images/RUP/01-requisitos/03-detalle-casos-uso/abrirPanelAlumno/wireframes.svg)

---

## 5. Flujo de Eventos

### 5.1. Flujo Básico (Exitoso)
1. El **Alumno** solicita abrir el panel de formación desde la barra de navegación o tras autenticarse con éxito.
2. El **Sistema** recupera la asignación académica del alumno, el progreso en los módulos y los últimos eventos de code review.
3. El **Sistema** presenta los datos del alumno, su equipo técnico y su Tech Leader tutor.
4. El **Sistema** presenta el avance porcentual acumulado y el módulo activo.
5. El **Sistema** presenta las alertas de retroalimentación pendientes de lectura y las fechas límite de entrega.
6. El **Sistema** permite seleccionar cualquier módulo accesible para consultar su temario y recursos.
7. El **Sistema** permite solicitar la consulta de retroalimentación de entregables evaluados.

---

## 6. Reglas de Negocio Vinculadas
- **RN-FORM-01 (Itinerario Secuencial):** Los módulos formativos se desbloquean en estricto orden secuencial conforme se aprueban los laboratorios y el test de nivelación del módulo predecesor.
- **RN-FORM-02 (Tutelaje Exclusivo):** Cada alumno reporta exclusivamente al Tech Leader asignado a su equipo técnico CTS.
