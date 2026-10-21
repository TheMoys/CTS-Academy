<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [📜 Bitácora ADR](/RUP/BITACORA.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [🔍 02 Análisis](/RUP/02-analisis/README.md) | [🎨 03 Diseño](/RUP/03-diseño/README.md) | **💻 04 Desarrollo** |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|

</div>

# Fase 04: Desarrollo — CTS Academy & Evaluator

Bienvenido a la **Fase 04: Desarrollo / Implementación** de **CTS Academy & Evaluator** bajo la metodología RUP (Rational Unified Process).

---

## 🎯 Propósito del Modelo de Desarrollo

Esta fase alberga el código fuente del sistema y la matriz de correspondencia directa entre los artefactos de modelado RUP y los componentes de software implementados.

En esta fase se formalizan:
1. **Mapeo de Casos de Uso a Código**: Trazabilidad directa entre cada caso de uso y sus respectivos controladores, casos de uso de aplicación, componentes frontend y tests.
2. **Estructura del Código Fuente**:
   * **Backend**: Arquitectura limpia / hexagonal organizada por bounded contexts (`MotorEquipos`, `MotorEvaluacion`, `MotorFormacion`).
   * **Frontend**: Single Page Application (SPA) con interfaces reactivas basadas en los prototipos Salt especificados en la Fase 01.
   * **Sandbox**: Aisladores Docker para la ejecución segura de retos de código y tests automatizados.
3. **Batería de Pruebas**: Tests unitarios, tests de integración y validaciones end-to-end.

---

## 📋 Estado de la Fase

> [!NOTE]
> **Trazabilidad Garantizada**:
> Todo el desarrollo posterior se sustentará rigurosamente sobre los 35 casos de uso ya especificados en [Fase 01: Requisitos](/RUP/01-requisitos/README.md).

---

<div align="center">

[⬅️ Fase 03: Diseño](/RUP/03-diseño/README.md) • [Volver al Inicio del Proyecto 🏠](/README.md)

</div>
