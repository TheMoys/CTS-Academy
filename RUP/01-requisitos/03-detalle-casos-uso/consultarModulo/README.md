<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

<sub>**Fase 01 Requisitos** › **Detalle de Caso de Uso** › `consultarModulo()`</sub>

</div>

# Caso de Uso: `consultarModulo()`


## 1. Identificación y Metadatos

| Atributo | Detalle |
| :--- | :--- |
| **Identificador** | `CU-FORM-03` |
| **Nombre** | `consultarModulo()` |
| **Paquete** | `PK03 - MotorFormacion` |
| **Actores** | `Alumno` |
| **Tipo de Flujo** | Consulta de Unidad de Aprendizaje |
| **Prioridad** | Alta |
| **Estado** | Especificado |

---

## 2. Descripción General
Permite al alumno acceder al contenido detallado de un módulo formativo que se encuentre habilitado en su itinerario. Presenta las guías didácticas, los diagramas de arquitectura, las consignas de laboratorios prácticos, el estado de las entregas y revisiones de código, y el acceso al test técnico de fin de módulo cuando todos los requisitos prácticos previos hayan sido completados y aprobados.

---

## 3. Precondiciones y Postcondiciones

### 3.1. Precondiciones
1. El alumno debe estar autenticado en la plataforma.
2. El módulo seleccionado debe estar en estado `EN_CURSO` o `APROBADO`.

### 3.2. Postcondiciones
1. El sistema realiza la transición hacia el estado `MODULO_ABIERTO`.
2. Se presenta la lista completa de recursos didácticos con opción de visualización.
3. Se presentan los laboratorios prácticos habilitando el envío o la consulta de retroalimentación según corresponda.
4. Se habilita el botón de inicio del test técnico únicamente si todos los laboratorios están aprobados.

---

## 4. Diagramas de Especificación

### 4.1. Diagrama de Estados del Caso de Uso (RUP)
![Especificación consultarModulo](/images/RUP/01-requisitos/03-detalle-casos-uso/consultarModulo/especificacion.svg)

### 4.2. Wireframe / Prototipo de Interfaz
![Wireframe consultarModulo](/images/RUP/01-requisitos/03-detalle-casos-uso/consultarModulo/wireframes.svg)

---

## 5. Flujo de Eventos

### 5.1. Flujo Básico (Exitoso)
1. El **Alumno** selecciona un módulo formativo habilitado y solicita consultar su detalle.
2. El **Sistema** recupera los materiales teóricos, laboratorios prácticos y el estado del test técnico del módulo.
3. El **Sistema** presenta los objetivos pedagógicos y recursos didácticos disponibles.
4. El **Sistema** presenta los laboratorios prácticos con el estado de revisión de cada entrega.
5. El **Sistema** evalúa si todos los laboratorios están aprobados para habilitar el test técnico de fin de módulo.
6. El **Sistema** permite seleccionar cualquier material didáctico para su consulta detallada.
7. El **Sistema** permite solicitar el envío de entregables o consultar la retroalimentación de entregas previas.
8. El **Sistema** permite solicitar volver al itinerario general de capacitación.

---

## 6. Reglas de Negocio Vinculadas
- **RN-FORM-04 (Habilitación del Test de Nivelación):** El test técnico de fin de módulo permanece estrictamente inactivo mientras existan laboratorios prácticos sin entregar o en estado distinto de `APROBADO`.
---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
