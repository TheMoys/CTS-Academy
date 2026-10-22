<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|
</div>

# Caso de Uso: `enviarEntregable()`


<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/enviarEntregable/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/enviarEntregable/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## 📋 Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actor Principal** | `Alumno` (`AlumnoProfer`) |
| **Objetivo** | Enviar la solución en código fuente (Pull Request en repositorio Git) de una práctica de laboratorio o ticket asignado en un módulo formativo para su revisión técnica |
| **Precondición** | El Alumno está autenticado e integrado en un equipo de CTS; el módulo formativo está en curso y la práctica se encuentra en estado inicial o solicitada de cambios (`REQUIERE_CAMBIOS`) |
| **Postcondición Éxito** | Entregable registrado en estado `PENDIENTE_REVISION`; notificación encolada para el `LiderEquipo` (TL) en `abrirEntregablesPendientes()` |
| **Postcondición Fallo** | Si la URL del Pull Request no es válida o no pertenece al repositorio institucional, el sistema rechaza la entrega y permanece en el formulario |

</div>

---

## 📑 Reglas de Negocio Asociadas

1. **Flujo Ágil Basado en Pull Requests (ADR-003)**:
   * Los entregables no se suben como archivos comprimidos (ZIP) ni mediante formularios estáticos. El alumno trabaja con ramas de Git y envía el enlace a su Pull Request para permitir una revisión de código real.
2. **Ciclo de Revisión Interactiva con el TL**:
   * Tras la entrega, el Tech Leader del equipo puede ejecutar `aprobarEntregable()` o `solicitarCambiosEntregable()`. En este último caso, el alumno realiza nuevos commits sobre la misma rama y reitera `enviarEntregable()`.
3. **Pertenencia al Módulo del Equipo**:
   * Solo los alumnos pertenecientes al equipo correspondiente pueden someter entregables a los módulos configurados por el TL de ese equipo.

---

## 🔗 Referencias

* [Diagrama de Estados de Entrega de Laboratorio](/RUP/00-modelo-del-dominio/estados-entidades/entregaLaboratorio-estados.puml)
* [Diagrama de Contexto de Alumno](/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoAlumno.puml)
---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
