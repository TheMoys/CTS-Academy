<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [01 Requisitos](/RUP/01-requisitos/README.md) | [02 Análisis](/RUP/02-analisis/README.md) | [Catálogo Requisitos](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

<sub>**Fase 02 Análisis** › **Realización de Casos de Uso** › `agendarEntrevistaGoogleMeet()`</sub>

</div>

# Realización de Caso de Uso: `agendarEntrevistaGoogleMeet()`

Esta especificación describe la realización de análisis del caso de uso `agendarEntrevistaGoogleMeet()` mediante clases BCE, detallando la conciliación dual de husos horarios, la integración resiliente con Google Calendar API, la idempotencia en reagendaciones y el despacho oficial por correo electrónico.

---

<div align=center>

| Diagrama de Clases de Análisis (VOPC) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/agendarEntrevistaGoogleMeet/clasesAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](clasesAnalisis.puml)</i></sup> |

| Diagrama de Realización de Análisis (Secuencia BCE) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/agendarEntrevistaGoogleMeet/realizacionAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](realizacionAnalisis.puml)</i></sup> |

</div>

---

## Clases de Análisis Participantes

<div align=center>

| Clase | Estereotipo | Tipo | Responsabilidad Principal |
| :--- | :---: | :---: | :--- |
| **`DialogoAgendarEntrevista`** | `<<boundary>>` | Frontera | Interfaz de selección de fecha, hora y duración; presentación de la equivalencia horaria dual y confirmación visual del enlace Meet generado. |
| **`GoogleCalendarService`** | `<<boundary>>` | Frontera (Externa) | Adaptador con Google Workspace API; solicita la creación o actualización idempotente de eventos con generación automática de videoconferencia Google Meet. |
| **`ServicioNotificacionesEmail`** | `<<boundary>>` | Frontera (Externa) | Adaptador transaccional de correo; remite la convocatoria oficial al aspirante con las referencias horarias y el enlace seguro de acceso (`RN-ENTR-04`). |
| **`GestorAdmisiones`** | `<<control>>` | Control | Orquestación de la cita, cálculo de diferencia horaria (`RN-ENTR-01`), gestión de fallos de API (`RN-ENTR-02`) y actualización del estado de la entrevista. |
| **`Candidato`** | `<<entity>>` | Entidad | Aspirante evaluado; proporciona el correo institucional, la sede de origen y la zona horaria remitente (ej. `America/Bogota`). |
| **`Entrevista`** | `<<entity>>` | Entidad | Registro de la cita; custodia el identificador del evento remoto (`idEventoGoogle`), fecha programada, enlace persistido y motivo de reagendación (`RN-ENTR-03`). |

</div>

---

## Flujo de Realización (Colaboración BCE)

### Flujo Principal: Agendación Exitosa con Sincronización Google Workspace
1. El **`Gestor`** pulsa "Agendar entrevista" desde el perfil del candidato.
2. **`DialogoAgendarEntrevista`** invoca `calcularDualTimezone()` en **`GestorAdmisiones`**, recuperando la zona horaria del **`Candidato`** y visualizando la equivalencia entre Santander (`Europe/Madrid`) y la sede internacional (**RN-ENTR-01**).
3. El evaluador confirma la fecha y hora seleccionadas.
4. **`GestorAdmisiones`** invoca `agendarOReagendarEvento()` en el adaptador **`GoogleCalendarService`**.
5. **`GoogleCalendarService`** interactúa con Google Calendar API y retorna el `idEventoGoogle` y la URL única de `enlaceMeet`.
6. **Gestión de Reagendaciones (RN-ENTR-03)**:
   - Si no existía cita previa, se invoca `agendar()` en **`Entrevista`**.
   - Si existía cita anterior, se invoca `reagendar()` actualizando la fecha y almacenando el motivo del cambio sin generar eventos huérfanos.
7. **Despacho Institucional (RN-ENTR-04)**: **`GestorAdmisiones`** ordena a **`ServicioNotificacionesEmail`** enviar la convocatoria formal por correo electrónico con ambos husos horarios.
8. **`DialogoAgendarEntrevista`** muestra el acuse con el enlace Meet persistido y el estado de la cita actualizado.

### Flujo Alternativo: Fallo de Integración Google API (RN-ENTR-02)
1. Si Google Calendar API devuelve un error 5xx o desconexión de red:
   - **`GoogleCalendarService`** notifica la contingencia a **`GestorAdmisiones`**.
   - **`DialogoAgendarEntrevista`** emite un aviso de error sin bloquear el expediente, ofreciendo la posibilidad de reintentar o ingresar manualmente un enlace alternativo de contingencia.

---

## Trazabilidad con la Fase de Requisitos

| Requisito / Artefacto Fase 01 | Realización en Fase 02 (Análisis) |
| :--- | :--- |
| **Caso de Uso `agendarEntrevistaGoogleMeet()`** | Orquestación mediante `GestorAdmisiones` mediando con `GoogleCalendarService` y `Entrevista`. |
| **RN-ENTR-01 (Dual Timezone)** | Método `calcularDualTimezone()` en el controlador coordinando la zona horaria de `Candidato`. |
| **RN-ENTR-02 (Resiliencia Google API)** | Manejo de excepciones en el adaptador `GoogleCalendarService` con opción de enlace manual. |
| **RN-ENTR-03 (Idempotencia en Reagendación)** | Métodos diferenciados `agendar()` y `reagendar()` en la entidad `Entrevista`. |
| **RN-ENTR-04 (Despacho por Correo Oficial)** | Adaptador `ServicioNotificacionesEmail` enviando los datos sin exponer botones libres al aspirante. |

---

<div align="center">

[Volver a Fase 02: Análisis](/RUP/02-analisis/README.md) • [Ver Especificación de Requisitos (Fase 01)](/RUP/01-requisitos/03-detalle-casos-uso/agendarEntrevistaGoogleMeet/README.md)

</div>
