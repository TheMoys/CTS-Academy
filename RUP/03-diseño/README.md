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

## Catálogo de Artefactos de Diseño

<div align=center>

| Artefacto de Diseño | Alcance / Componentes | Especificación Técnica | Estado |
| :--- | :--- | :---: | :---: |
| **Modelo de Datos Relacional (DER)** | 29 tablas, 3 esquemas PostgreSQL (`equipos`, `evaluacion`, `formacion`), UUID v4, JSONB, auditoría e índices | [Ver DER y Diccionario](modelo-datos/README.md) | Completado |
| **Arquitectura de Despliegue Físico** | Topología Docker Compose multi-stage, redes internas, volumen PostgreSQL y sandbox CI | [Ver Despliegue](despliegue/README.md) | En cola |
| **Contratos de Interfaces OpenAPI / REST** | Especificación formal de endpoints HTTP, payloads JSON, DTOs y cabeceras JWT | [Ver Contratos API](casos-uso/README.md) | En cola |
| **Diagramas de Secuencia de Diseño** | Interacción detallada controladores NestJS/Express, repositorios Prisma y APIs externas | [Ver Secuencias](casos-uso/README.md) | En cola |

</div>

---

## Estado de la Fase

> [!NOTE]
> **Hito Inicial Completado — Modelo de Datos Relacional**:
> Se ha formalizado el esquema relacional de persistencia PostgreSQL para los 3 microservicios del sistema ([ADR-006](/RUP/BITACORA.md#adr-006-descomposici%C3%B3n-arquitect%C3%B3nica-en-3-microservicios)) con sus 4 diagramas Entity-Relationship (`derGeneral`, `derMotorEquipos`, `derMotorEvaluacion`, `derMotorFormacion`) compilados vectorialmente en `/images/RUP/03-diseño/modelo-datos/`.

---

<div align="center">

[Fase 02: Análisis](/RUP/02-analisis/README.md) • [Fase 04: Desarrollo](/RUP/04-desarrollo/README.md)

</div>
