# CTS Academy & Evaluator

> Plataforma integral para la evaluación técnica de admisión de becarios y la gestión formativa on-site del Centro Tecnológico de Desarrollo (CTS).

---

## 🎯 Propósito del Sistema

El proyecto moderniza y profesionaliza dos procesos neurálgicos de CTS:
1. **Evaluación de Admisión Técnica**: Sustituye las pruebas manuales (PDFs estáticos y carpetas de código desconectadas) por una plataforma interactiva con banco de reactivos teóricos objetivos, retos prácticos de código (Vanilla JS, CSS Grid/Flexbox, maquetación, APIs), temporizador en servidor, ejecución segura en sandbox (Docker) y rúbricas estandarizadas para los evaluadores senior.
2. **CTS Academy (Formación On-Site)**: Provee un entorno estructurado para los becarios admitidos durante su estancia presencial en CTS, con rutas de aprendizaje por perfiles (Frontend, Backend, Fullstack, DevOps), módulos temáticos, laboratorios prácticos basados en tickets/Pull Requests y acompañamiento tutorial con revisiones de código y seguimiento periódico.

---

## 📐 Metodología y Documentación (RUP)

Este proyecto sigue estrictamente la metodología **RUP (Rational Unified Process)** adaptada al estándar de ingeniería de software de UNEATLANTICO (referencias: *DOCUTRACE*, *pySigHor*, *pyCelda*), garantizando una especificación rigurosa antes de la implementación para evitar refactorizaciones innecesarias.

Toda la documentación arquitectónica y de requisitos se encuentra centralizada en el directorio [`/RUP`](/RUP/README.md):

* 📚 **[Fase 00: Modelo del Dominio](/RUP/00-modelo-del-dominio/README.md)** — Glosario, entidades conceptuales, diagramas de estados e invariantes de negocio.
* 📋 **[Fase 01: Requisitos](/RUP/01-requisitos/01-actores-casos-uso/README.md)** — Catálogo de actores, diagramas de contexto y especificación formal de casos de uso (máquinas de estados y wireframes).
* 🔍 **[Fase 02: Análisis](/RUP/02-analisis/README.md)** — Clases de análisis (Frontera, Control, Entidad) y realizaciones.
* 🎨 **[Fase 03: Diseño](/RUP/03-diseño/README.md)** — Diagramas de secuencia, DER, contratos de API REST y arquitectura de despliegue.
* 💻 **[Fase 04: Desarrollo](/RUP/04-desarrollo/README.md)** — Mapeo a código y matriz de trazabilidad.

---

## 🚀 Estructura del Repositorio

```text
cts-academy/
├── RUP/                          # Artefactos del Proceso Unificado
│   ├── 00-modelo-del-dominio/    # Entidades y reglas de negocio
│   │   ├── estados-entidades/    # Ciclos de vida en PlantUML
│   │   ├── modeloDominio.puml
│   │   └── README.md
│   ├── 01-requisitos/            # Requisitos, actores y casos de uso
│   ├── 02-analisis/              # Modelo y colaboraciones de análisis
│   ├── 03-diseño/                # Modelo de datos, secuencia y despliegue
│   └── 04-desarrollo/            # Trazabilidad a implementación
├── scripts/                      # Utilidades de compilación y validación
└── README.md                     # Entrada principal
```
