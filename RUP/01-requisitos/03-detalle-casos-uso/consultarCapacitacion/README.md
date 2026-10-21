<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

<sub>**Fase 01 Requisitos** › **Detalle de Caso de Uso** › `consultarCapacitacion()`</sub>

</div>

# Caso de Uso: `consultarCapacitacion()`


## 1. Identificación y Metadatos

| Atributo | Detalle |
| :--- | :--- |
| **Identificador** | `CU-FORM-02` |
| **Nombre** | `consultarCapacitacion()` |
| **Paquete** | `PK03 - MotorFormacion` |
| **Actores** | `Alumno` |
| **Tipo de Flujo** | Consulta de Itinerario de Aprendizaje |
| **Prioridad** | Alta |
| **Estado** | Especificado |

---

## 2. Descripción General
Permite al alumno consultar la hoja de ruta formativa completa (itinerario de especialización) vinculada a su equipo técnico CTS. Presenta la secuencia curricular de módulos, las competencias técnicas a desarrollar, las estimaciones horarias, los estados de desbloqueo de cada módulo y los requisitos necesarios para avanzar en el itinerario formativo.

---

## 3. Precondiciones y Postcondiciones

### 3.1. Precondiciones
1. El alumno debe estar autenticado en la plataforma.
2. El alumno debe tener asignado un rol técnico y un equipo CTS con un itinerario formativo activo.

### 3.2. Postcondiciones
1. El sistema realiza la transición hacia el estado `CAPACITACION_ABIERTO`.
2. Se presentan todos los módulos formativos con su estado correspondiente (`APROBADO`, `EN_CURSO` o `BLOQUEADO`).
3. Se permite acceder al detalle de los módulos que se encuentren activos o completados.

---

## 4. Diagramas de Especificación

### 4.1. Diagrama de Estados del Caso de Uso (RUP)
![Especificación consultarCapacitacion](/images/RUP/01-requisitos/03-detalle-casos-uso/consultarCapacitacion/especificacion.svg)

### 4.2. Wireframe / Prototipo de Interfaz
![Wireframe consultarCapacitacion](/images/RUP/01-requisitos/03-detalle-casos-uso/consultarCapacitacion/wireframes.svg)

---

## 5. Flujo de Eventos

### 5.1. Flujo Básico (Exitoso)
1. El **Alumno** solicita consultar la capacitación desde el menú de navegación o desde el panel de inicio.
2. El **Sistema** recupera la estructura curricular asignada al equipo del alumno.
3. El **Sistema** calcula el avance en cada módulo y determina los estados de desbloqueo.
4. El **Sistema** presenta el itinerario formativo completo y las competencias técnicas esperadas.
5. El **Sistema** presenta el listado de módulos ordenados y sus prerrequisitos de avance.
6. El **Sistema** permite seleccionar cualquier módulo habilitado para consultar su temario y recursos detallados.
7. El **Sistema** permite solicitar el retorno al panel principal de inicio.

---

## 6. Reglas de Negocio Vinculadas
- **RN-FORM-03 (Bloqueo de Módulos Futuros):** Un módulo en estado `BLOQUEADO` no permite el acceso a sus laboratorios ni al test técnico hasta que el módulo anterior sea formalmente aprobado por el Tech Leader.
---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
