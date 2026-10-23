<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [Bitácora ADR](/RUP/BITACORA.md) | [00 Dominio](/RUP/00-modelo-del-dominio/README.md) | **01 Requisitos** | [02 Análisis](/RUP/02-analisis/README.md) | [03 Diseño](/RUP/03-diseño/README.md) | [04 Desarrollo](/RUP/04-desarrollo/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|

**Sección 01 Requisitos:** [Actores y Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) • [Catálogo y Detalle de Casos de Uso (35)](/RUP/01-requisitos/03-detalle-casos-uso/README.md)

</div>

# Fase 01: Requisitos — CTS Academy & Evaluator

En esta fase se formalizan las interacciones de los actores con el sistema y se especifica el comportamiento exacto de los 35 casos de uso que componen la plataforma bajo la metodología RUP.

---

## Estructura de la Fase de Requisitos

Para navegar de forma ordenada, esta fase se divide en dos apartados secuenciales:

```text
01-requisitos/
├── 01-actores-casos-uso/     ──► 1. ¿Quién usa el sistema y en qué estados?
│   ├── Actores del Sistema (4 roles autenticados)
│   ├── Diagramas de Casos de Uso por Actor
│   └── Diagramas de Contexto Formales (Statecharts globales)
│
└── 03-detalle-casos-uso/     ──► 2. ¿Cómo funciona exactamente cada caso de uso?
    ├── PK01 - Acceso (2 CUs)
    ├── PK02 - MotorEvaluacion (12 CUs)
    ├── PK03 - MotorFormacion (17 CUs)
    └── PK04 - MotorEquipos (4 CUs)
```

---

## 1. [Actores y Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

Define los límites del sistema y las pantallas/contextos de disponibilidad operativa para cada uno de los **4 actores autenticados**:

| Actor | Rol en el Sistema | Diagrama de Contexto |
| :--- | :--- | :---: |
| **`Candidato`** | Aspirante internacional en proceso de admisión técnica | [Ver Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md#candidato) |
| **`Alumno`** | Becario on-site asignado a un equipo técnico CTS | [Ver Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md#alumno-profer) |
| **`LiderEquipo` (TL)** | Ingeniero tutor que lidera un equipo, revisa código y aporta reactivos | [Ver Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md#líderequipo-tech-leader) |
| **`Gestor`** | Coordinador general del programa PROFER, admisiones y asignaciones | [Ver Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md#gestor-profer) |

---

## 2. [Catálogo y Detalle de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md)

Contiene la especificación formal exhaustiva de los **35 casos de uso**, organizados en 4 paquetes funcionales alineados con la arquitectura en microservicios:

* **[PK01 — Acceso (2 Casos de Uso)](/RUP/01-requisitos/03-detalle-casos-uso/README.md#pk01--acceso-2-casos-de-uso)**: Autenticación multifactorial, sesiones seguras y revocación fail-secure.
* **[PK02 — MotorEvaluacion (12 Casos de Uso)](/RUP/01-requisitos/03-detalle-casos-uso/README.md#pk02--motorevaluacion-12-casos-de-uso)**: Batería de 3 tests diagnósticos, cronometraje en servidor, entrevistas Google Meet y admisiones.
* **[PK03 — MotorFormacion (17 Casos de Uso)](/RUP/01-requisitos/03-detalle-casos-uso/README.md#pk03--motorformacion-17-casos-de-uso)**: Itinerarios de onboarding on-site, temarios, banco de reactivos, Code Reviews de PRs y evaluación sumativa.
* **[PK04 — MotorEquipos (4 Casos de Uso)](/RUP/01-requisitos/03-detalle-casos-uso/README.md#pk04--motorequipos-4-casos-de-uso)**: Gobernanza de los 6 equipos CTS, cohortes semestrales y cuadros de mando de liderazgo.

Cada caso de uso cuenta estrictamente con:
1. `especificacion.puml`: Statechart de interacción con flujos alternativos y bifurcaciones de control.
2. `wireframes.puml`: Prototipo Salt esquemático de la interfaz.
3. `README.md`: Ficha técnica de requisitos con diagramas vectoriales SVG embebidos.

---

<div align="center">

[Fase 00: Modelo del Dominio](/RUP/00-modelo-del-dominio/README.md) • [Fase 01: Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
