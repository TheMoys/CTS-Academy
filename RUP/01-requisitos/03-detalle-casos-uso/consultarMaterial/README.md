<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

<sub>**Fase 01 Requisitos** › **Detalle de Caso de Uso** › `consultarMaterial()`</sub>

</div>

# Caso de Uso: `consultarMaterial()`


## 1. Identificación y Metadatos

| Atributo | Detalle |
| :--- | :--- |
| **Identificador** | `CU-FORM-04` |
| **Nombre** | `consultarMaterial()` |
| **Paquete** | `PK03 - MotorFormacion` |
| **Actores** | `Alumno` |
| **Tipo de Flujo** | Consulta de Contenido Didáctico |
| **Prioridad** | Media-Alta |
| **Estado** | Especificado |

---

## 2. Descripción General
Permite al alumno abrir y leer un material didáctico (guía técnica en Markdown, diagrama de arquitectura de sistemas, recurso interactivo o enlace a repositorio de referencia) perteneciente a un módulo formativo activo. Al finalizar la lectura, el sistema registra el evento para computar el porcentaje de avance del alumno en los recursos teóricos del módulo.

---

## 3. Precondiciones y Postcondiciones

### 3.1. Precondiciones
1. El alumno debe estar autenticado en la plataforma.
2. El módulo formativo al que pertenece el material debe estar habilitado (`EN_CURSO` o `APROBADO`).

### 3.2. Postcondiciones
1. El material queda marcado como leído en el expediente formativo del alumno.
2. Se recalculan los indicadores de avance del módulo.
3. El sistema retorna al estado `MODULO_ABIERTO`.

---

## 4. Diagramas de Especificación

### 4.1. Diagrama de Estados del Caso de Uso (RUP)
![Especificación consultarMaterial](/images/RUP/01-requisitos/03-detalle-casos-uso/consultarMaterial/especificacion.svg)

### 4.2. Wireframe / Prototipo de Interfaz
![Wireframe consultarMaterial](/images/RUP/01-requisitos/03-detalle-casos-uso/consultarMaterial/wireframes.svg)

---

## 5. Flujo de Eventos

### 5.1. Flujo Básico (Exitoso)
1. El **Alumno** selecciona un material didáctico dentro de la lista del módulo y solicita consultar su contenido.
2. El **Sistema** recupera el contenido enriquecido del material (texto formateado, diagramas embebidos, adjuntos descargables).
3. El **Sistema** presenta el visor de contenido didáctico y documentación técnica.
4. El **Sistema** registra la lectura del material y actualiza el progreso en el módulo formativo.
5. El **Sistema** permite solicitar la descarga de archivos adjuntos (guías PDF, repositorios base).
6. El **Alumno** solicita cerrar el visor de material didáctico.
7. El **Sistema** retorna al detalle del módulo con el estado de lectura actualizado.

---

## 6. Reglas de Negocio Vinculadas
- **RN-FORM-05 (Computo de Lectura Requerida):** Para considerar un módulo listo para evaluación de fin de módulo, el alumno debe haber registrado la lectura del 100% de los materiales catalogados como obligatorios por el Tech Leader.
---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
