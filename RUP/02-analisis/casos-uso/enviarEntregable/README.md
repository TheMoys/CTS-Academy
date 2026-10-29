<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [Fase 01: Requisitos](/RUP/01-requisitos/README.md) | [Fase 02: Análisis](/RUP/02-analisis/README.md) |
|:---:|:---:|:---:|:---:|

</div>

# Realización de Análisis: `enviarEntregable()`

Este documento formaliza la colaboración de análisis entre clases estereotipadas Boundary-Control-Entity (BCE) que realiza el caso de uso `enviarEntregable()`, permitiendo al estudiante becario remitir la solución técnica de un laboratorio práctico mediante un Pull Request en el repositorio de control de versiones de la organización para su posterior revisión de código (*Code Review*).

---

## 1. Diagrama de Clases de Análisis (VOPC)

El diagrama de clases participantes delimita las responsabilidades de captura, validación externa con el servicio Git y persistencia del estado del entregable.

<div align="center">

![Diagrama de Clases de Análisis](clasesAnalisis.svg)
*Figura 1: Clases de análisis participantes en `enviarEntregable()`.*

</div>

### Participantes y Estereotipos

| Clase | Estereotipo | Responsabilidad |
| :--- | :---: | :--- |
| **`Alumno`** | `<<actor>>` | Estudiante becario autenticado que remite su solución de código. |
| **`FormularioEntrega`** | `<<boundary>>` | Interfaz de usuario para ingresar la URL del Pull Request y notas descriptivas. |
| **`ServicioGitRepository`** | `<<boundary>>` | Adaptador perimetral que valida el estado del Pull Request y su pertenencia al repositorio institucional. |
| **`GestorFormacion`** | `<<control>>` | Controlador de lógica de negocio que orquesta la validación, la persistencia de la entrega y el encolado de alertas. |
| **`Alumno`** | `<<entity>>` | Expediente del alumno que valida su pertenencia al equipo correspondiente. |
| **`Laboratorio`** | `<<entity>>` | Consigna práctica que define los criterios técnicos de entrega. |
| **`EntregaLaboratorio`** | `<<entity>>` | Entidad central que registra los intentos de entrega y transiciona su estado a `PENDIENTE_REVISION`. |
| **`Notificacion`** | `<<entity>>` | Alerta interna encolada para el Tech Leader responsable del equipo. |

---

## 2. Diagrama de Realización de Análisis (Secuencia BCE)

La interacción formaliza el flujo de remisión y el manejo del ciclo iterativo de revisión técnica.

<div align="center">

![Diagrama de Realización de Análisis](realizacionAnalisis.svg)
*Figura 2: Secuencia de mensajes BCE para `enviarEntregable()`.*

</div>

### Flujo de Colaboración

1. El actor `Alumno` solicita abrir el formulario de entrega para un laboratorio determinado.
2. `FormularioEntrega` consulta a `GestorFormacion` la existencia de intentos previos (por ejemplo, si el laboratorio se encuentra en estado `REQUIERE_CAMBIOS`).
3. El alumno introduce la URL de su Pull Request en GitHub/GitLab junto con comentarios explicativos y ejecuta el envío.
4. `FormularioEntrega` delega en `GestorFormacion` la remisión (`remitirEntregaLaboratorio(...)`).
5. En cumplimiento de **ADR-003**, `GestorFormacion` invoca a `ServicioGitRepository` para verificar que la URL corresponda a un Pull Request abierto y pertenezca a la organización institucional autorizada.
6. Si la validación falla, se notifica el rechazo al formulario permaneciendo en el contexto de edición.
7. Si el PR es válido:
   - Si existía una entrega previa en `REQUIERE_CAMBIOS`, se registra un nuevo intento y se transiciona a `PENDIENTE_REVISION`.
   - Si es la primera remisión, se crea la nueva instancia `EntregaLaboratorio` en estado `PENDIENTE_REVISION`.
8. Se genera una `Notificacion` encolada para el `TechLeader` del equipo CTS para su posterior revisión en la bandeja técnica (`abrirEntregablesPendientes()`).
9. Se confirma el éxito de la operación al estudiante.

---

## 3. Trazabilidad con Decisiones Arquitectónicas y Reglas

- **ADR-003 (Flujo Ágil Basado en Pull Requests):** Los entregables se gestionan exclusivamente mediante Pull Requests en ramas de control de versiones, prohibiendo la carga de archivos binarios o comprimidos estáticos.
- **Ciclo de Revisión Interactiva:** Si un laboratorio requirió correcciones, el estudiante reutiliza el flujo de entrega incrementando el número de intento sin perder la trazabilidad de revisiones previas.

---

<div align="center">

[Volver al Índice de la Fase 02: Análisis](/RUP/02-analisis/README.md)

</div>
