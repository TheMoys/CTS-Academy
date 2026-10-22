<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

</div>

# Caso de Uso: `abrirPanelAlumno()`

<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/abrirPanelAlumno/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/abrirPanelAlumno/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## 📋 Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `Alumno` (estudiante/becario admitido asignado a un equipo CTS) |
| **Objetivo** | Permite al alumno becario visualizar su cuadro de mando formativo integral tras iniciar sesión en el sistema. Presenta información de su equipo CTS asignado, su Tech Leader responsable, el avance consolidado en la hoja de ruta de capacitación, el estado del módulo formativo activo, las notificaciones de revisiones de código realizadas por el Tech Leader y los plazos de entrega inmediatos. |
| **Precondición** | El alumno debe estar autenticado con credenciales válidas en la plataforma (estado de sesión activa con rol `Alumno`). El alumno debe estar formalmente admitido y asignado a un equipo técnico CTS (Equipos 1 a 6) con un itinerario formativo activo. |
| **Postcondición Éxito** | El sistema presenta el panel principal del alumno con los indicadores actualizados en tiempo real. Se habilitan los enlaces de navegación directa hacia el módulo en curso, la hoja de ruta de capacitación y la bandeja de retroalimentación de entregables. |

</div>

---

## 📑 Reglas de Negocio Asociadas

- **RN-FORM-01 (Itinerario Secuencial):** Los módulos formativos se desbloquean en estricto orden secuencial conforme se aprueban los laboratorios y el test de nivelación del módulo predecesor.
- **RN-FORM-02 (Tutelaje Exclusivo):** Cada alumno reporta exclusivamente al Tech Leader asignado a su equipo técnico CTS.

---

## 🔗 Referencias

* [Modelo del Dominio: MotorFormacion](/RUP/00-modelo-del-dominio/README.md)
* [Diagramas de Contexto por Actor](/RUP/01-requisitos/01-actores-casos-uso/README.md)
* [Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md)

---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
