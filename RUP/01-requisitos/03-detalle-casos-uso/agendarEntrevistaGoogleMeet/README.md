<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|
</div>

# Caso de Uso: `agendarEntrevistaGoogleMeet()`


<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/agendarEntrevistaGoogleMeet/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/agendarEntrevistaGoogleMeet/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## 📋 Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `Gestor` (`GestorProfer`) |
| **Objetivo** | Programar y coordinar la entrevista diagnóstica cualitativa con el aspirante, integrándose con Google Calendar API para generar automáticamente la sala de Google Meet, sincronizar el evento en la agenda institucional y despachar la convocatoria transaccional por correo electrónico |
| **Precondición** | El Gestor debe encontrarse autenticado y en el expediente del aspirante (`PERFIL_CANDIDATO_ABIERTO`); el candidato debe encontrarse en estado admisible para entrevista; las credenciales de servicio de Google Workspace deben estar configuradas |
| **Postcondición Éxito** | Entrevista registrada en la entidad `Candidato.entrevista`; evento sincronizado en Google Calendar con enlace Meet persistido; notificación enviada al correo del candidato; el contexto permanece en `PERFIL_CANDIDATO_ABIERTO` con el enlace y estado actualizados |
| **Postcondición Fallo** | Si la integración con Google Calendar API falla persistentemente o se introducen fechas no válidas, el sistema emite un mensaje de error y mantiene el formulario abierto sin alterar el expediente |

</div>

---

## 📑 Reglas de Negocio Asociadas

1. **RN-ENTR-01 — Conciliación de Husos Horarios (Dual Timezone)**:
   * La interfaz calcula y presenta en tiempo real la equivalencia horaria entre la sede central (Santander, `Europe/Madrid`) y la sede internacional remitente del candidato (ej. `America/Bogota`), emitiendo una advertencia si la hora fijada coincide con horario nocturno o inhábil en el país de origen del aspirante.
2. **RN-ENTR-02 — Resiliencia y Fallback de Google Workspace**:
   * Ante fallos de red o errores 5xx de Google Calendar API, la operación no bloquea el expediente; el sistema permite el reintento automático o la conmutación a enlace de contingencia manual introducido por el Gestor.
3. **RN-ENTR-03 — Idempotencia en Reagendación**:
   * Si el candidato ya posee una cita previa, la reprogramación no duplica eventos huérfanos en Google Calendar, sino que ejecuta una actualización `PATCH` del evento existente, exigiendo un motivo de reagendación que se incrusta en el cuerpo de la notificación al candidato.
4. **RN-ENTR-04 — Centralización y Opacidad del Canal (ADR-009)**:
   * El enlace de Google Meet se despacha por correo electrónico oficial y no se expone como botón de acceso libre en el panel web del candidato, preservando el control de asistencia y gobernanza en el Gestor.

---

## 🔗 Referencias

* [Modelo del Dominio: `Candidato`, `Entrevista`, `Gestor`](/RUP/00-modelo-del-dominio/README.md)
* [Diagrama de Contexto Gestor](/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoGestor.puml)
* [Caso de Uso: `abrirPerfilCandidato()`](/RUP/01-requisitos/03-detalle-casos-uso/abrirPerfilCandidato/README.md)
* [ADR-007: Admisión continua y batería de 3 tests diagnósticos](/RUP/BITACORA.md#adr-007-admisi%C3%B3n-continua-por-ciclos-acad%C3%A9micos-bater%C3%ADa-de-3-tests-e-inclusi%C3%B3n-de-entrevista)
* [ADR-009: Centralización del perfil de candidato y entrevista en el Gestor](/RUP/BITACORA.md#adr-009-centralizaci%C3%B3n-del-perfil-del-candidato-y-gesti%C3%B3n-de-entrevistas-en-el-gestor-profer)
---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
