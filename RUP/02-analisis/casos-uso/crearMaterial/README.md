<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [Fase 01: Requisitos](/RUP/01-requisitos/README.md) | [Fase 02: Análisis](/RUP/02-analisis/README.md) |
|:---:|:---:|:---:|:---:|

</div>

# Realización de Análisis: `crearMaterial()`

Este documento formaliza la colaboración de análisis entre clases estereotipadas Boundary-Control-Entity (BCE) que realiza el caso de uso `crearMaterial()`, permitiendo al Tech Leader incorporar un nuevo recurso formativo (guía técnica en Markdown, esquemas de diseño o recursos externos) en un módulo bajo su tutela directa.

---

## 1. Diagrama de Clases de Análisis (VOPC)

El diagrama de clases participantes delimita las responsabilidades para verificar la pertenencia del módulo y persistir el nuevo recurso didáctico.

<div align="center">

![Diagrama de Clases de Análisis](clasesAnalisis.svg)
*Figura 1: Clases de análisis participantes en `crearMaterial()`.*

</div>

### Participantes y Estereotipos

| Clase | Estereotipo | Responsabilidad |
| :--- | :---: | :--- |
| **`LiderEquipo`** | `<<actor>>` | Tech Leader que diseña y publica el recurso pedagógico. |
| **`EditorMaterial`** | `<<boundary>>` | Interfaz gráfica interactiva para redactar el contenido Markdown y fijar atributos (obligatoriedad, enlaces). |
| **`GestorContenidos`** | `<<control>>` | Controlador de lógica de negocio que valida la pertenencia del módulo al equipo y asigna el orden correlativo de lectura. |
| **`TechLeader`** | `<<entity>>` | Perfil del líder técnico autenticado. |
| **`Modulo`** | `<<entity>>` | Unidad temática formativa receptora del material. |
| **`Material`** | `<<entity>>` | Recurso didáctico dado de alta en estado activo. |

---

## 2. Diagrama de Realización de Análisis (Secuencia BCE)

La interacción formaliza el control de acceso departamental y la indexación secuencial del recurso.

<div align="center">

![Diagrama de Realización de Análisis](realizacionAnalisis.svg)
*Figura 2: Secuencia de mensajes BCE para `crearMaterial()`.*

</div>

### Flujo de Colaboración

1. El actor `LiderEquipo` abre el editor de contenidos para un módulo específico desde `EditorMaterial`.
2. Se capturan los datos didácticos del recurso y el Tech Leader confirma la publicación.
3. `EditorMaterial` invoca al controlador `GestorContenidos` (`crearMaterialEnModulo(...)`).
4. `GestorContenidos` consulta a `TechLeader` y a `Modulo` para validar en virtud de **RN-LEAD-01** que el módulo pertenezca al equipo asignado al líder.
5. Si el módulo pertenece a otro squad, se deniega la operación.
6. Habiendo superado la validación de propiedad, `Modulo` calcula el siguiente número de orden de lectura disponible.
7. Se crea la entidad `Material` inicializada en estado activo.
8. Se confirma la publicación exitosa al Tech Leader y el material queda disponible de inmediato para los alumnos del equipo.

---

## 3. Trazabilidad con Reglas de Negocio

- **RN-LEAD-01 (Propiedad de Módulos):** Un Tech Leader solo puede dar de alta o modificar materiales en los módulos asociados a su equipo técnico CTS.

---

<div align="center">

[Volver al Índice de la Fase 02: Análisis](/RUP/02-analisis/README.md)

</div>
