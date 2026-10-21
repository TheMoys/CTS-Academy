<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

<sub>**Fase 01 Requisitos** › **Detalle de Caso de Uso** › `abrirPerfilCandidato()`</sub>

</div>

# Caso de Uso: `abrirPerfilCandidato()`


<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/abrirPerfilCandidato/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/abrirPerfilCandidato/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## 📋 Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actor Principal** | `Gestor` (`GestorProfer`) |
| **Objetivo** | Abrir el expediente consolidado del candidato para inspeccionar sus resultados diagnósticos de tests, agendar o consultar la sesión en Google Meet, registrar impresiones cualitativas y formalizar la admisión o descarte |
| **Tipo** | Primario, esencial |
| **Nivel** | Objetivo de usuario / Centro neurálgico de admisiones |
| **Precondición** | El Gestor está autenticado; el aspirante fue previamente registrado a través de las listas canalizadas por las sedes |
| **Postcondición Éxito** | Expediente unificado visible en `PERFIL_CANDIDATO_ABIERTO` con todas las acciones contextuales operativas (`agendarEntrevistaGoogleMeet`, `registrarAnotacionesEntrevista`, `admitirAlumnoProfer`, `rechazarCandidatura`) |
| **Postcondición Fallo** | Si el identificador del candidato es inexistente, el sistema muestra error y permanece en `PANEL_ADMISIONES_ABIERTO` |

</div>

---

## 📑 Reglas de Negocio Asociadas

1. **Centralización Operativa en el Perfil (ADR-009)**:
   * En lugar de dispersar la selección en múltiples pantallas desarticuladas, el perfil unificado consolida:
     - Los indicadores diagnósticos (radares de aptitud, actitud y habilidades técnicas multidisciplinares).
     - La integración directa con Google Meet para la entrevista personal.
     - El registro continuo de anotaciones y feedback del evaluador.
2. **Recomendación de Afinidad por Equipos**:
   * A partir de los reactivos de los 6 equipos integrados en el `TestTecnico`, el perfil calcula un índice de afinidad para recomendar en qué equipo encaja con mayor naturalidad el aspirante.
3. **Formalización de Beca y Transición a Alumno**:
   * Al pulsar `[Admitir como Alumno PROFER]`, se asocia al estudiante a uno de los 6 equipos de CTS y se fija su rol técnico inicial, completando la transición de la entidad `Candidato` a `Alumno` en `MotorEquipos`.

---

## 🔗 Referencias

* [Diagrama de Estados de Candidatura](/RUP/00-modelo-del-dominio/estados-entidades/candidatura-estados.puml)
* [ADR-009: Entrevistas Google Meet en el Perfil por el Gestor](/RUP/BITACORA.md#adr-009-delimitaci%C3%B3n-de-actores-opacidad-de-tests-para-el-candidato-entrevistas-google-meet-en-el-perfil-por-el-gestor-y-aislamiento-del-tl)
---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
