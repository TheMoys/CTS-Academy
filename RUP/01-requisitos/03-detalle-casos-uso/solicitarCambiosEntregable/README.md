<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

<sub>**Fase 01 Requisitos** › **Detalle de Caso de Uso** › `solicitarCambiosEntregable()`</sub>

</div>

# Caso de Uso: `solicitarCambiosEntregable()`


## 1. Identificación y Metadatos

| Atributo | Detalle |
| :--- | :--- |
| **Identificador** | `CU-LEAD-10` |
| **Nombre** | `solicitarCambiosEntregable()` |
| **Paquete** | `PK03 - MotorFormacion` |
| **Actores** | `LiderEquipo` |
| **Tipo de Flujo** | Solicitud de Corrección / Feedback de Code Review |
| **Prioridad** | Crítica (Alta) |
| **Estado** | Especificado |

---

## 2. Descripción General
Permite al Tech Leader solicitar correcciones o refactorizaciones sobre un laboratorio práctico entregado por un alumno cuando el código no cumple con los estándares de calidad, presenta fallos en los tests del sandbox o carece de buenas prácticas arquitectónicas. Al registrarse, el estado del entregable cambia a `CAMBIOS_SOLICITADOS`, permitiendo al estudiante subsanar las observaciones y reenviar su Pull Request.

---

## 3. Precondiciones y Postcondiciones

### 3.1. Precondiciones
1. El usuario debe estar autenticado con rol `LiderEquipo`.
2. El entregable debe encontrarse en estado `PENDIENTE_REVISION`.

### 3.2. Postcondiciones
1. El entregable pasa a estado `CAMBIOS_SOLICITADOS`.
2. Se registra el desglose de observaciones técnicas en la bitácora del entregable.
3. El alumno recibe notificación inmediata y se le habilita la opción de reenvío de la entrega corregida.

---

## 4. Diagramas de Especificación

### 4.1. Diagrama de Estados del Caso de Uso (RUP)
![Especificación solicitarCambiosEntregable](/images/RUP/01-requisitos/03-detalle-casos-uso/solicitarCambiosEntregable/especificacion.svg)

### 4.2. Wireframe / Prototipo de Interfaz
![Wireframe solicitarCambiosEntregable](/images/RUP/01-requisitos/03-detalle-casos-uso/solicitarCambiosEntregable/wireframes.svg)

---

## 5. Flujo de Eventos

### 5.1. Flujo Básico (Exitoso)
1. El **LiderEquipo** solicita requerir cambios tras inspeccionar el entregable del alumno.
2. El **Sistema** presenta el formulario para consignar los motivos de rechazo y las observaciones técnicas.
3. El **LiderEquipo** introduce las razones y las instrucciones detalladas de corrección.
4. El **LiderEquipo** solicita registrar la solicitud de cambios.
5. El **Sistema** valida que las observaciones técnicas contengan justificación explícita.
6. El **Sistema** actualiza el estado a `CAMBIOS_SOLICITADOS` y envía notificación al estudiante.
7. El **Sistema** retorna a la bandeja de entregables pendientes.

### 5.2. Flujo Alternativo: Justificación Insuficiente
- En el paso 5, si el campo de observaciones técnicas está vacío o carece de justificación mínima, el **Sistema** presenta un mensaje de validación impidiendo registrar la solicitud sin feedback pedagógico.

---

## 6. Reglas de Negocio Vinculadas
- **RN-LEAD-10 (Obligatoriedad de Feedback Constructivo):** Es mandatorio que toda solicitud de cambios incluya una explicación técnica detallada orientada a guiar al alumno en la subsanación de las deficiencias detectadas.
---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
