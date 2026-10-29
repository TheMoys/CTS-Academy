<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [01 Requisitos](/RUP/01-requisitos/README.md) | [02 Análisis](/RUP/02-analisis/README.md) | [Catálogo Requisitos](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

<sub>**Fase 02 Análisis** › **Realización de Casos de Uso** › `admitirAlumnoProfer()`</sub>

</div>

# Realización de Caso de Uso: `admitirAlumnoProfer()`

Esta especificación describe la realización de análisis del caso de uso `admitirAlumnoProfer()` mediante clases BCE, detallando la transición de la entidad `Candidato` a `Alumno` (`AlumnoProfer`), la asignación obligatoria a uno de los 6 equipos de CTS con su rol técnico, el control de vacantes y la matriculación en el itinerario de capacitación.

---

<div align=center>

| Diagrama de Clases de Análisis (VOPC) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/admitirAlumnoProfer/clasesAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](clasesAnalisis.puml)</i></sup> |

| Diagrama de Realización de Análisis (Secuencia BCE) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/admitirAlumnoProfer/realizacionAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](realizacionAnalisis.puml)</i></sup> |

</div>

---

## Clases de Análisis Participantes

<div align=center>

| Clase | Estereotipo | Tipo | Responsabilidad Principal |
| :--- | :---: | :---: | :--- |
| **`DialogoAdmision`** | `<<boundary>>` | Frontera | Interfaz modal de selección de equipo (`Equipo 01` a `Equipo 06`), rol técnico junior y fecha de incorporación; advertencia de cupo saturado y confirmación. |
| **`ServicioNotificacionesEmail`** | `<<boundary>>` | Frontera (Externa) | Adaptador de mensajería; despacha la carta oficial de concesión de beca institucional al nuevo estudiante y a la sede remitente. |
| **`GestorAdmisiones`** | `<<control>>` | Control | Orquestación de la admisión, verificación de vacantes (`RN-ADM-02`), transición transaccional de rol (`RN-ADM-03`), matriculación en la capacitación y sellado del expediente (`RN-ADM-04`). |
| **`Candidato`** | `<<entity>>` | Entidad | Aspirante admitido; transiciona a estado `ADMITIDO` congelando su expediente en la convocatoria activa. |
| **`Equipo`** | `<<entity>>` | Entidad (MotorEquipos) | Squad de desarrollo receptor; verifica capacidad máxima y vincula al nuevo alumno a la tutela de su `LiderEquipo`. |
| **`Alumno`** | `<<entity>>` | Entidad (MotorEquipos) | Nueva instancia del becario (`AlumnoProfer`); custodia su squad, rol técnico asignado y fecha formal de incorporación. |
| **`Capacitacion`** | `<<entity>>` | Entidad (MotorFormacion) | Plan de formación técnica on-site del equipo; matricula al alumno para habilitar el acceso a los módulos y entregables. |

</div>

---

## Flujo de Realización (Colaboración BCE)

### Flujo Principal: Admisión y Promoción a Alumno PROFER
1. El **`Gestor`** pulsa "Admitir como Alumno PROFER" desde el perfil del aspirante.
2. **`DialogoAdmision`** consulta a **`GestorAdmisiones`** los equipos formadores que cuentan con plazas libres en el periodo lectivo.
3. El evaluador selecciona el equipo de destino, el rol técnico junior y la fecha prevista de inicio.
4. **`DialogoAdmision`** remite la orden formal a **`GestorAdmisiones`**.
5. **Validación de Elegibilidad e Inmutabilidad (RN-ADM-04)**: Se comprueba que el candidato esté en estado admisible y no cuente con resolución previa.
6. **Control de Capacidad por Equipo (RN-ADM-02)**: **`GestorAdmisiones`** invoca `tieneVacantes()` en la entidad **`Equipo`**. Al haber disponibilidad, prosigue.
7. **Transición y Promoción de Rol (RN-ADM-01 / RN-ADM-03)**:
   - Se invoca `marcarAdmitido()` en **`Candidato`**, cerrando su postulación en la convocatoria.
   - Se instancia la nueva entidad **`Alumno`** vinculada al equipo y rol técnico seleccionados.
   - La entidad **`Equipo`** incorpora al alumno (`incorporarAlumno()`).
   - La entidad **`Capacitacion`** matricula al alumno en el itinerario formativo correspondiente.
8. **Despacho Institucional**: **`GestorAdmisiones`** ordena a **`ServicioNotificacionesEmail`** emitir la carta formal de admisión.
9. **`DialogoAdmision`** muestra el acuse de admisión exitosa y transiciona al Gestor hacia el panel general de admisiones.

### Flujo Alternativo: Cupo Saturado (RN-ADM-02)
1. Si el equipo seleccionado no dispone de plazas vacantes al momento de la confirmación:
   - **`GestorAdmisiones`** rechaza la transacción y emite un mensaje de error.
   - **`DialogoAdmision`** advierte de la saturación del equipo, solicitando al Gestor reasignar al aspirante a otro squad con disponibilidad.

---

## Trazabilidad con la Fase de Requisitos

| Requisito / Artefacto Fase 01 | Realización en Fase 02 (Análisis) |
| :--- | :--- |
| **Caso de Uso `admitirAlumnoProfer()`** | Orquestación mediante `GestorAdmisiones` conectando `Candidato`, `Equipo`, `Alumno` y `Capacitacion`. |
| **RN-ADM-01 (Asignación Obligatoria)** | Atributos `idEquipo` y `rolTecnico` requeridos al instanciar la entidad `Alumno`. |
| **RN-ADM-02 (Control de Vacantes)** | Verificación de `tieneVacantes()` en `Equipo` antes de autorizar la creación de la instancia. |
| **RN-ADM-03 (Promoción de Rol)** | Creación de `Alumno` y actualización de credenciales del subsistema de acceso. |
| **RN-ADM-04 (Inmutabilidad del Dictamen)** | Invocación de `marcarAdmitido()` sellando la postulación en la entidad `Candidato`. |

---

<div align="center">

[Volver a Fase 02: Análisis](/RUP/02-analisis/README.md) • [Ver Especificación de Requisitos (Fase 01)](/RUP/01-requisitos/03-detalle-casos-uso/admitirAlumnoProfer/README.md)

</div>
