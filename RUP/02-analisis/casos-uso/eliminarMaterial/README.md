<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [Fase 01: Requisitos](/RUP/01-requisitos/README.md) | [Fase 02: Análisis](/RUP/02-analisis/README.md) |
|:---:|:---:|:---:|:---:|

</div>

# Realización de Análisis: `eliminarMaterial()`

Este documento formaliza la colaboración de análisis entre clases estereotipadas Boundary-Control-Entity (BCE) que realiza el caso de uso `eliminarMaterial()`, permitiendo al Tech Leader dar de baja lógicamente un recurso didáctico de un módulo bajo su tutela sin comprometer la integridad histórica ni las métricas de alumnos de cohortes pasadas.

---

## 1. Diagrama de Clases de Análisis (VOPC)

El diagrama de clases participantes delimita las responsabilidades de verificación de permisos, transición de estado a inactivo y reindexación secuencial.

<div align="center">

![Diagrama de Clases de Análisis](clasesAnalisis.svg)
*Figura 1: Clases de análisis participantes en `eliminarMaterial()`.*

</div>

### Participantes y Estereotipos

| Clase | Estereotipo | Responsabilidad |
| :--- | :---: | :--- |
| **`LiderEquipo`** | `<<actor>>` | Tech Leader que solicita la despublicación o baja del recurso. |
| **`DialogoEliminacionMaterial`** | `<<boundary>>` | Ventana modal de confirmación explícita para evitar supresiones involuntarias. |
| **`GestorContenidos`** | `<<control>>` | Controlador de lógica de negocio que aplica el borrado lógico y ordena la reindexación del temario. |
| **`TechLeader`** | `<<entity>>` | Perfil del líder técnico tutor. |
| **`Modulo`** | `<<entity>>` | Unidad temática que reindexa su orden correlativo de lectura. |
| **`Material`** | `<<entity>>` | Recurso formativo cuyo estado transiciona a `INACTIVO`. |

---

## 2. Diagrama de Realización de Análisis (Secuencia BCE)

La interacción formaliza la baja no destructiva conforme a los estándares de auditoría del sistema.

<div align="center">

![Diagrama de Realización de Análisis](realizacionAnalisis.svg)
*Figura 2: Secuencia de mensajes BCE para `eliminarMaterial()`.*

</div>

### Flujo de Colaboración

1. El actor `LiderEquipo` solicita eliminar un material didáctico desde `DialogoEliminacionMaterial`.
2. `DialogoEliminacionMaterial` invoca a `GestorContenidos` para validar permisos (`verificarPermisoBaja(...)`).
3. `GestorContenidos` confirma que el módulo pertenezca al equipo administrado por el líder técnico.
4. Concedido el permiso, se solicita confirmación explícita al usuario en la interfaz.
5. El Tech Leader confirma la supresión del recurso.
6. En virtud de **RN-LEAD-03**, `GestorContenidos` marca la entidad `Material` con estado `INACTIVO` (borrado lógico), impidiendo su eliminación física de la base de datos.
7. Se notifica a `Modulo` para compactar y reindexar los números de orden de los materiales restantes que permanezcan activos.
8. Se confirma la baja lógica exitosa al usuario.

---

## 3. Trazabilidad con Reglas de Negocio

- **RN-LEAD-03 (Baja No Destructiva):** La eliminación es siempre lógica (`INACTIVO`) para preservar el histórico de lecturas y avance curricular de cohortes previas.

---

<div align="center">

[Volver al Índice de la Fase 02: Análisis](/RUP/02-analisis/README.md)

</div>
