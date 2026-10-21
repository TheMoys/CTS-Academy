<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

<sub>**Fase 01 Requisitos** › **Detalle de Caso de Uso** › `aprobarEntregable()`</sub>

</div>

# Caso de Uso: `aprobarEntregable()`


## 1. Identificación y Metadatos

| Atributo | Detalle |
| :--- | :--- |
| **Identificador** | `CU-LEAD-09` |
| **Nombre** | `aprobarEntregable()` |
| **Paquete** | `PK03 - MotorFormacion` |
| **Actores** | `LiderEquipo` |
| **Tipo de Flujo** | Aprobación y Certificación de Laboratorio Práctico |
| **Prioridad** | Crítica (Alta) |
| **Estado** | Especificado |

---

## 2. Descripción General
Permite al Tech Leader emitir el dictamen formal de aprobación (`APROBADO`) sobre un entregable práctico presentado por un alumno. El evaluador asigna una calificación numérica igual o superior a 7.0/10.0, completa la rúbrica multidimensional (diseño, código y pruebas) y redacta la retroalimentación cualitativa. Al registrarse, el sistema actualiza el avance curricular del alumno y evalúa si se desbloquea el siguiente hito formativo.

---

## 3. Precondiciones y Postcondiciones

### 3.1. Precondiciones
1. El usuario debe estar autenticado con rol `LiderEquipo`.
2. El entregable debe encontrarse en estado `PENDIENTE_REVISION`.

### 3.2. Postcondiciones
1. El entregable pasa a estado `APROBADO`.
2. Se registra la calificación y el feedback cualitativo en el expediente del alumno.
3. Se actualiza el avance porcentual del módulo correspondiente.
4. Si todos los laboratorios del módulo están aprobados, se habilita el acceso al test técnico de fin de módulo.

---

## 4. Diagramas de Especificación

### 4.1. Diagrama de Estados del Caso de Uso (RUP)
![Especificación aprobarEntregable](/images/RUP/01-requisitos/03-detalle-casos-uso/aprobarEntregable/especificacion.svg)

### 4.2. Wireframe / Prototipo de Interfaz
![Wireframe aprobarEntregable](/images/RUP/01-requisitos/03-detalle-casos-uso/aprobarEntregable/wireframes.svg)

---

## 5. Flujo de Eventos

### 5.1. Flujo Básico (Exitoso)
1. El **LiderEquipo** solicita aprobar el entregable tras inspeccionar el código.
2. El **Sistema** presenta el formulario de evaluación con la rúbrica y campos de calificación y feedback.
3. El **LiderEquipo** introduce la nota numérica (mínimo 7.0/10.0) y sus observaciones técnicas.
4. El **LiderEquipo** solicita registrar la aprobación.
5. El **Sistema** valida que la calificación sea suficiente para aprobación y los comentarios no estén vacíos.
6. El **Sistema** cambia el estado de la entrega a `APROBADO` y dispara notificación transaccional al alumno.
7. El **Sistema** retorna a la bandeja de entregables pendientes.

### 5.2. Flujo Alternativo: Nota Insuficiente para Aprobación
- En el paso 5, si el Tech Leader introduce una nota menor a 7.0, el **Sistema** advierte que una calificación inferior al umbral de suficiencia requiere utilizar el caso de uso `solicitarCambiosEntregable()`.

---

## 6. Reglas de Negocio Vinculadas
- **RN-LEAD-09 (Umbral Aprobatorio):** La nota mínima requerida para certificar un laboratorio práctico como `APROBADO` es de 7.0 puntos sobre 10.0.
---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
