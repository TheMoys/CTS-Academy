<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [Bitácora ADR](/RUP/BITACORA.md) | [00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [01 Requisitos](/RUP/01-requisitos/README.md) | [02 Análisis](/RUP/02-analisis/README.md) | **03 Diseño** | [04 Desarrollo](/RUP/04-desarrollo/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|

</div>

# Fase 03: Diseño — CTS Academy & Evaluator

Esta fase concreta las realizaciones de análisis en especificaciones técnicas de diseño: diagramas de secuencia, modelo relacional (PostgreSQL), contratos OpenAPI/REST y despliegue físico en contenedores Docker.

---

## Propósito del Modelo de Diseño

El modelo de diseño refina el análisis adaptándolo a la infraestructura, plataformas y limitaciones técnicas reales de **CTS Academy & Evaluator**. 

En esta fase se formalizan:
1. **Diseño de Datos (DER Relacional)**: Esquema de base de datos relacional (PostgreSQL), definición de tablas, llaves foráneas, índices de rendimiento y políticas de inmutabilidad (auditoría append-only y soft-delete).
2. **Diagramas de Secuencia de Diseño**: Interacciones temporales detalladas entre controladores, servicios de aplicación, repositorios, cache Redis y servicios externos (Google Calendar API, GitHub webhooks, runners Docker).
3. **Contratos de Interfaces de API (OpenAPI / REST)**: Definición formal de endpoints HTTP, payloads JSON, códigos de estado canónicos y encabezados de autenticación JWT.
4. **Arquitectura de Despliegue**: Especificación de contenedores Docker, redes internas, volúmenes de persistencia y balanceo de carga.

---

## Estado de la Fase

> [!NOTE]
> **Planificación de Artefactos**:
> Las decisiones arquitectónicas fundamentales que rigen este diseño se encuentran acordadas y documentadas formalmente en la [Bitácora ADR](/RUP/BITACORA.md).

---

<div align="center">

[Fase 02: Análisis](/RUP/02-analisis/README.md) • [Fase 04: Desarrollo](/RUP/04-desarrollo/README.md)

</div>
