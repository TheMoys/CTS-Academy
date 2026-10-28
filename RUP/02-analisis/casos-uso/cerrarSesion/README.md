<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [01 Requisitos](/RUP/01-requisitos/README.md) | [02 Análisis](/RUP/02-analisis/README.md) | [Catálogo Requisitos](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

<sub>**Fase 02 Análisis** › **Realización de Casos de Uso** › `cerrarSesion()`</sub>

</div>

# Realización de Caso de Uso: `cerrarSesion()`

Esta especificación describe la realización de análisis del caso de uso `cerrarSesion()` mediante la colaboración de clases Boundary-Control-Entity (BCE), formalizando la revocación segura de credenciales en el servidor y la purga del contexto en el cliente.

---

<div align=center>

| Diagrama de Clases de Análisis (VOPC) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/cerrarSesion/clasesAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](clasesAnalisis.puml)</i></sup> |

| Diagrama de Realización de Análisis (Secuencia BCE) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/cerrarSesion/realizacionAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](realizacionAnalisis.puml)</i></sup> |

</div>

---

## Clases de Análisis Participantes

<div align=center>

| Clase | Estereotipo | Tipo | Responsabilidad Principal |
| :--- | :---: | :---: | :--- |
| **`BarraNavegacion`** | `<<boundary>>` | Frontera | Componente de interfaz presente en todos los paneles autenticados que expone la acción de cierre, presenta advertencias modales si existen evaluaciones activas y ejecuta la purga de credenciales locales. |
| **`GestorAutenticacion`** | `<<control>>` | Control | Orquestación de la invalidación formal de sesiones activas, consulta de procesos o pruebas en curso y registro del evento de cierre en la bitácora de auditoría de seguridad. |
| **`Usuario`** | `<<entity>>` | Entidad | Cuenta del actor autenticado; proporciona la trazabilidad de sus evaluaciones activas y su sesión actual. |
| **`Sesion`** | `<<entity>>` | Entidad | Instancia de la sesión que pasa de estado activa a revocada de forma inmediata e irreversible. |
| **`Test`** | `<<entity>>` | Entidad | Evaluación diagnóstica (o técnica); permite verificar si el estado es `EN_CURSO` para disparar la advertencia de inmutabilidad del cronómetro (RN-ACC-05 / ADR-007). |

</div>

---

## Flujo de Realización (Colaboración BCE)

### Flujo Principal: Cierre Estándar sin Evaluaciones Activas
1. El **`ActorAutenticado`** (`Candidato`, `Alumno`, `LiderEquipo` o `Gestor`) pulsa el botón de cierre en **`BarraNavegacion`**.
2. **`BarraNavegacion`** solicita a **`GestorAutenticacion`** verificar si el usuario tiene procesos en curso mediante `verificarProcesosActivos(idUsuario)`.
3. **`GestorAutenticacion`** consulta a la entidad **`Usuario`** y este a sus instancias de **`Test`** (`estaEnCurso()`). Al no existir exámenes activos, devuelve confirmación limpia.
4. **`BarraNavegacion`** invoca `cerrarSesion(tokenSesion, idUsuario)` en **`GestorAutenticacion`**.
5. **`GestorAutenticacion`** invoca `revocar()` en la entidad **`Sesion`**, marcándola como revocada de forma inmediata.
6. **`GestorAutenticacion`** registra el evento en auditoría y responde con éxito a **`BarraNavegacion`**.
7. **`BarraNavegacion`** purga el almacenamiento local (tokens volátiles, estado en memoria), elimina las cookies de sesión y redirige al usuario a `SESION_CERRADA`.

### Flujo Alternativo: Advertencia de Test en Curso (RN-ACC-05)
1. Si **`Usuario`** cuenta con un **`Test`** en estado `EN_CURSO`:
   - **`GestorAutenticacion`** devuelve una advertencia informando de que el examen continúa activo y su temporizador no se detendrá en el servidor.
   - **`BarraNavegacion`** presenta un diálogo modal de confirmación informando de la regla de inmutabilidad temporal.
   - Si el usuario **cancela**, el flujo se interrumpe y permanece en su contexto de trabajo sin modificar la sesión.
   - Si el usuario **confirma conscientemente**, **`BarraNavegacion`** procede con la invocación de `cerrarSesion()` y la purga correspondiente.

---

## Trazabilidad con la Fase de Requisitos

| Requisito / Artefacto Fase 01 | Realización en Fase 02 (Análisis) |
| :--- | :--- |
| **Caso de Uso `cerrarSesion()`** | Realización coordinada por `GestorAutenticacion` con invalidación de `Sesion`. |
| **Actores Autenticados (ADR-011)** | Vinculación transversal desde `BarraNavegacion` en los 4 espacios de trabajo. |
| **Regla RN-ACC-03 (Revocación Server-Side)** | Método `revocar()` sobre la entidad `Sesion` antes de notificar al cliente. |
| **Regla RN-ACC-04 (Fail-Secure Client-Side)** | La frontera `BarraNavegacion` purga el almacenamiento local independientemente del resultado de red. |
| **Regla RN-ACC-05 (Advertencia de Tests Activos)** | Inspección previa de la entidad `Test` y bifurcación modal de advertencia antes de revocar credenciales. |

---

<div align="center">

[Volver a Fase 02: Análisis](/RUP/02-analisis/README.md) • [Ver Especificación de Requisitos (Fase 01)](/RUP/01-requisitos/03-detalle-casos-uso/cerrarSesion/README.md)

</div>
