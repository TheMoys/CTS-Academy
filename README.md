<div align="center">

| **🏠 Inicio** | [📖 RUP Hub](/RUP/README.md) | [📜 Bitácora ADR](/RUP/BITACORA.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [🔍 02 Análisis](/RUP/02-analisis/README.md) | [🎨 03 Diseño](/RUP/03-diseño/README.md) | [💻 04 Desarrollo](/RUP/04-desarrollo/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|

</div>

# CTS Academy & Evaluator

> Plataforma integral para la evaluación técnica de admisión y la gestión formativa on-site de los Alumnos PROFER en el Centro Tecnológico de Desarrollo (CTS).

---

## 🎯 Propósito del Sistema

El proyecto moderniza y profesionaliza dos procesos neurálgicos de CTS y el programa PROFER:
1. **Evaluación de Admisión Técnica**: Sustituye las pruebas manuales (PDFs estáticos y carpetas de código desconectadas) por una plataforma interactiva con banco de reactivos teóricos objetivos, retos prácticos de código (Vanilla JS, CSS Grid/Flexbox, maquetación, APIs), temporizador en servidor, ejecución segura en sandbox (Docker) y rúbricas estandarizadas para los Tech Leaders (TL).
2. **CTS Academy (Formación On-Site)**: Provee un entorno estructurado para los Alumnos PROFER durante su estancia formativa on-site en CTS, con rutas de aprendizaje por perfiles (Frontend, Backend, Fullstack, DevOps), módulos temáticos, laboratorios prácticos basados en tickets/Pull Requests y acompañamiento de los Tech Leaders con revisiones de código y seguimiento periódico gestionado por el Gestor PROFER.

---

## 🧭 Guía de Navegación Lineal del Proyecto

Para explorar la documentación de forma secuencial sin tener que buscar manualmente en el explorador de archivos, sigue la ruta canónica del ciclo de ingeniería:

```text
[ 1. Bitácora ADR ] ──► [ 2. Modelo Dominio ] ──► [ 3. Requisitos ] ──► [ 4. Análisis / Diseño / Código ]
   /RUP/BITACORA.md       /00-modelo-del-dominio     /01-requisitos        /02-analisis /03-diseño /04-desarrollo
```

1. **[📜 Bitácora RUP (Registro de Decisiones - ADR)](/RUP/BITACORA.md)** — Decisiones arquitectónicas fundamentales, acuerdos de gobernanza y justificaciones de diseño.
2. **[🏛️ Fase 00: Modelo del Dominio](/RUP/00-modelo-del-dominio/README.md)** — Vocabulario de negocio, separación estricta en 3 microservicios (`MotorEquipos`, `MotorEvaluacion`, `MotorFormacion`) y ciclos de vida de entidades.
3. **[📋 Fase 01: Requisitos](/RUP/01-requisitos/README.md)** — Hub central de requisitos:
   * **[👥 01.1 Actores y Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)**: Los 4 actores autenticados y sus máquinas de estados operativas.
   * **[📋 01.2 Catálogo y Detalle de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md)**: Especificación formal exhaustiva de los 35 casos de uso con Statecharts, prototipos Salt y fichas RUP.
4. **[🔍 Fase 02: Análisis](/RUP/02-analisis/README.md)** — Clases de análisis Boundary-Control-Entity y colaboraciones preliminares.
5. **[🎨 Fase 03: Diseño](/RUP/03-diseño/README.md)** — Diagramas de secuencia, DER relacional PostgreSQL, contratos OpenAPI y despliegue Docker.
6. **[💻 Fase 04: Desarrollo](/RUP/04-desarrollo/README.md)** — Mapeo a código fuente, arquitectura hexagonal y testing automatizado.

---

## 📐 Metodología de Desarrollo

El proyecto aplica **RUP (Rational Unified Process)** con trazabilidad formal de requisitos, análisis, diseño y despliegue mediante especificaciones en PlantUML y Markdown.

Toda la documentación técnica se concentra y enlaza desde el concentrador central:
👉 **[Acceder al RUP Hub Central (`/RUP/README.md`)](/RUP/README.md)**

---

## 🚀 Estructura de Directorios del Repositorio

```text
cts-academy/
├── images/                       # Renderizado vectorial SVG de todos los diagramas PlantUML
├── RUP/                          # Artefactos del Proceso Unificado
│   ├── BITACORA.md               # Bitácora formal de decisiones (ADR)
│   ├── README.md                 # Hub concentrador RUP y matriz de trazabilidad
│   ├── 00-modelo-del-dominio/    # Entidades y reglas de negocio (3 microservicios)
│   │   ├── estados-entidades/    # Ciclos de vida de entidades en PlantUML
│   │   ├── modeloDominio.puml
│   │   └── README.md
│   ├── 01-requisitos/            # Requisitos, actores y casos de uso
│   │   ├── README.md             # Hub concentrador de la fase de requisitos
│   │   ├── 01-actores-casos-uso/ # Actores y diagramas de contexto formales
│   │   └── 03-detalle-casos-uso/ # Detalle de los 35 casos de uso (puml, salt, svg)
│   ├── 02-analisis/              # Modelo y colaboraciones de análisis (BCE)
│   ├── 03-diseño/                # Modelo de datos relacional, secuencia y despliegue
│   └── 04-desarrollo/            # Trazabilidad a implementación y código
├── scripts/                      # Utilidades de compilación (render_puml.py)
└── README.md                     # Entrada principal
```
