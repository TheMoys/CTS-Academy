<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [Fase 01: Requisitos](/RUP/01-requisitos/README.md) | [Fase 02: Análisis](/RUP/02-analisis/README.md) |
|:---:|:---:|:---:|:---:|

</div>

# Realización de Análisis: `editarMaterial()`

Este documento formaliza la colaboración de análisis entre clases estereotipadas Boundary-Control-Entity (BCE) que realiza el caso de uso `editarMaterial()`, permitiendo al Tech Leader actualizar el contenido didáctico, consignas o enlaces de un recurso existente sin invalidar el cómputo de lecturas completadas por estudiantes en cohortes pasadas o activas.

---

## 1. Diagrama de Clases de Análisis (VOPC)

El diagrama de clases participantes delimita las responsabilidades para verificar la autoridad de edición y versionar el recurso preservando la trazabilidad de los alumnos.

<div align="center">

![Diagrama de Clases de Análisis](clasesAnalisis.svg)
*Figura 1: Clases de análisis participantes en `editarMaterial()`.*

</div>

### Participantes y Estereotipos

| Clase | Estereotipo | Responsabilidad |
| :--- | :---: | :--- |
| **`LiderEquipo`** | `<<actor>>` | Tech Leader que modifica el material formativo. |
| **`EditorMaterial`** | `<<boundary>>` | Interfaz interactiva para la carga del contenido previo y la captura de las correcciones. |
| **`GestorContenidos`** | `<<control>>` | Controlador de lógica de negocio que valida permisos sobre el módulo, incrementa el versionado y resguarda el histórico. |
| **`TechLeader`** | `<<entity>>` | Perfil del líder técnico autenticado. |
| **`Modulo`** | `<<entity>>` | Unidad curricular contenedora. |
| **`Material`** | `<<entity>>` | Recurso formativo cuyo contenido y versión se actualizan. |
| **`LecturaMaterial`** | `<<entity>>` | Registros históricos de lecturas que se preservan inalterados. |

---

## 2. Diagrama de Realización de Análisis (Secuencia BCE)

La interacción formaliza el versionado del recurso y la protección de los eventos de lectura existentes.

<div align="center">

![Diagrama de Realización de Análisis](realizacionAnalisis.svg)
*Figura 2: Secuencia de mensajes BCE para `editarMaterial()`.*

</div>

### Flujo de Colaboración

1. El actor `LiderEquipo` solicita editar un material formativo desde `EditorMaterial`.
2. `EditorMaterial` invoca a `GestorContenidos` (`cargarMaterialParaEdicion(...)`).
3. `GestorContenidos` comprueba la vinculación del módulo al equipo del Tech Leader. Si pertenece a otro equipo, deniega la acción.
4. Si los permisos son válidos, se extrae el contenido actual y se presenta en el formulario interactivo.
5. El Tech Leader aplica las modificaciones requeridas y confirma la actualización.
6. `GestorContenidos` actualiza el cuerpo didáctico en `Material` e incrementa su contador de versión de contenido.
7. En cumplimiento de **RN-LEAD-02**, `GestorContenidos` garantiza que las instancias preexistentes de `LecturaMaterial` permanezcan intactas, evitando que los alumnos que ya estudiaron el documento pierdan su estado de avance.
8. Se confirma la actualización exitosa al usuario.

---

## 3. Trazabilidad con Reglas de Negocio

- **RN-LEAD-02 (Preservación de Trazabilidad):** Las modificaciones a guías formativas no invalidan las lecturas ya completadas por los alumnos que las leyeron previamente.

---

<div align="center">

[Volver al Índice de la Fase 02: Análisis](/RUP/02-analisis/README.md)

</div>
