<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [Bitácora ADR](/RUP/BITACORA.md) | [00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [01 Requisitos](/RUP/01-requisitos/README.md) | [02 Análisis](/RUP/02-analisis/README.md) | [03 Diseño](/RUP/03-diseño/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|

</div>

# Arquitectura y Despliegue Físico — Docker

Este documento formaliza la arquitectura de despliegue físico y topología de contenedores en **Docker** para **CTS Academy & Evaluator**, adaptando los requerimientos de seguridad, persistencia relacional ([ADR-012](/RUP/BITACORA.md#adr-012-elecci%C3%B3n-de-postgresql-16-para-persistencia-relacional-y-soporte-de-microservicios)) y ejecución aislada de código práctico mediante contenedores efímeros sin red.

---

## 1. Diagrama de Despliegue Físico UML

El siguiente diagrama modela la distribución de nodos, contenedores, redes virtuales, protocolos de comunicación y servicios cloud externos:

<div align="center">

| Diagrama de Despliegue Físico |
| :---: |
| ![](/images/RUP/03-diseño/despliegue/despliegue.svg) |
| <sup><i>[Código fuente PlantUML](despliegue.puml)</i></sup> |

</div>

---

## 2. Topología de Redes Aisladas (Zero-Trust)

Para garantizar la máxima seguridad en la ejecución de código no confiable entregado por aspirantes y becarios, el host Docker se segmenta en **4 redes virtuales internas tipo bridge**:

```text
Host Linux CTS (Docker Engine)
├── [cts_public_net]  ──► Exposición frontal hacia internet (Proxy Nginx y SPA estática).
├── [cts_app_net]     ──► Tráfico privado entre Proxy y Backend Node.js / NestJS.
├── [cts_data_net]    ──► Red de persistencia (PostgreSQL 16 y Redis 7).
└── [cts_sandbox_net] ──► Canal de control aislado para el runner de pruebas (Sin salida externa).
```

| Red Virtual | Nivel de Exposición | Contenedores Miembros | Propósito de Seguridad |
| :--- | :---: | :--- | :--- |
| **`cts_public_net`** | Pública (Puertos 80, 443) | `cts-proxy`, `cts-frontend` | Recepción de tráfico HTTPS de aspirantes, alumnos, Tech Leaders y gestores. |
| **`cts_app_net`** | Privada interna | `cts-proxy`, `cts-backend` | Enrutamiento de peticiones API REST y canales WebSocket protegidos. |
| **`cts_data_net`** | Aislada (Sin acceso web) | `cts-backend`, `cts-postgres`, `cts-redis` | Persistencia transaccional. La base de datos no expone puertos al exterior del host. |
| **`cts_sandbox_net`** | Estrictamente sellada | `cts-backend`, `cts-runner-daemon` | Orquestación de contenedores efímeros. `network_mode: none` en la ejecución de código. |

---

## 3. Inventario de Contenedores y Servicios

### 3.1 `cts-proxy` (Reverse Proxy & Gateway)
* **Imagen base:** `nginx:1.25-alpine`
* **Puertos anfitrión:** `80:80` (HTTP $\rightarrow$ Redirección 301), `443:443` (HTTPS / TLS 1.3).
* **Responsabilidades:**
  * Terminación SSL con certificados corporativos.
  * *Rate limiting* anti-DDoS en `/api/v1/evaluacion/` para proteger la prueba técnica.
  * Soporte de WebSocket (`Upgrade: websocket`) para el temporizador en tiempo real.
  * Compresión gzip de activos estáticos.

### 3.2 `cts-frontend` (SPA Client Application)
* **Imagen base:** `nginx:1.25-alpine` (multi-stage build desde Node.js 20).
* **Tecnología:** React 18, TypeScript, Tailwind CSS, Vite.
* **Puerto interno:** `80` (servido únicamente hacia `cts-proxy`).

### 3.3 `cts-backend` (API Monolito Modular de 3 Microservicios)
* **Imagen base:** `node:20-alpine` (NestJS Framework).
* **Puerto interno:** `3000`.
* **Módulos acoplados por arquitectura de esquemas ([ADR-006](/RUP/BITACORA.md#adr-006-descomposici%C3%B3n-arquitect%C3%B3nica-en-3-microservicios)):**
  1. `MotorEquipos`: Gobernanza, roles, asignación a squads (Team 01 a Team 06).
  2. `MotorEvaluacion`: Admisión continua, exámenes, temporizador y entrevistas Google Meet.
  3. `MotorFormacion`: LMS, material Markdown, revisiones de código y banco de reactivos.
* **Worker asíncrono:** Procesamiento de colas BullMQ para cálculo de métricas de admisión y envíos a sandboxes.

### 3.4 `cts-postgres` (Persistencia Relacional)
* **Imagen base:** `postgres:16-alpine`
* **Puerto interno:** `5432` (restringido a `cts_data_net`).
* **Volumen de datos:** `pgdata:/var/lib/postgresql/data`.
* **Inicialización:** Script `init-schemas.sql` que crea los 3 esquemas lógicos (`motor_equipos`, `motor_evaluacion`, `motor_formacion`) y habilita la extensión `pgcrypto` (`gen_random_uuid()`).

### 3.5 `cts-redis` (Cache & Mensajería en Memoria)
* **Imagen base:** `redis:7-alpine`
* **Puerto interno:** `6379` (restringido a `cts_data_net`).
* **Volumen:** `redisdata:/data`.
* **Uso:** Lista negra de tokens JWT invalidados tras `cerrarSesion()`, control de latidos contra desincronización horaria y colas de evaluación en segundo plano.

### 3.6 `cts-runner-daemon` & Contenedores Efímeros (Sandbox de Código)
* **Propósito:** Ejecutar retos prácticos de programación entregados por candidatos (Vanilla JS, lógica de algoritmos) y tests automatizados de Pull Requests de becarios sin comprometer el servidor anfitrión.
* **Políticas de confinamiento estricto:**
  * **Red:** `network_mode: none` (cero conectividad a internet o a la red local del host).
  * **CPU:** Límite máximo de `0.5 cores` por contenedor efímero.
  * **Memoria RAM:** Cap de `256 MB` con swap deshabilitado (`--memory-swap=256m`).
  * **Tiempo de ejecución (Timeout):** Matado forzoso a los `10 segundos` para abortar bucles infinitos.
  * **Sistema de archivos:** `read-only: true`, con únicamente `/tmp` montado en memoria RAM (`tmpfs`).

---

## 4. Especificación Canónica de `docker-compose.yml`

```yaml
version: '3.8'

networks:
  cts_public_net:
    driver: bridge
  cts_app_net:
    driver: bridge
  cts_data_net:
    internal: true
  cts_sandbox_net:
    internal: true

volumes:
  pgdata:
  redisdata:

services:
  cts-proxy:
    image: nginx:1.25-alpine
    container_name: cts-proxy
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - ./nginx/ssl:/etc/nginx/ssl:ro
    networks:
      - cts_public_net
      - cts_app_net
    depends_on:
      - cts-frontend
      - cts-backend

  cts-frontend:
    build:
      context: ../../
      dockerfile: docker/frontend/Dockerfile
    container_name: cts-frontend
    restart: unless-stopped
    networks:
      - cts_public_net

  cts-backend:
    build:
      context: ../../
      dockerfile: docker/backend/Dockerfile
    container_name: cts-backend
    restart: unless-stopped
    environment:
      - NODE_ENV=production
      - PORT=3000
      - DATABASE_URL=postgresql://${DB_USER}:${DB_PASS}@cts-postgres:5432/${DB_NAME}?schema=public
      - REDIS_URL=redis://cts-redis:6379
      - GOOGLE_CALENDAR_CLIENT_ID=${GOOGLE_CLIENT_ID}
      - GITHUB_TOKEN=${GITHUB_BOT_TOKEN}
    networks:
      - cts_app_net
      - cts_data_net
      - cts_sandbox_net
    depends_on:
      - cts-postgres
      - cts-redis

  cts-postgres:
    image: postgres:16-alpine
    container_name: cts-postgres
    restart: unless-stopped
    environment:
      POSTGRES_DB: ${DB_NAME:-cts_academy}
      POSTGRES_USER: ${DB_USER:-cts_admin}
      POSTGRES_PASSWORD: ${DB_PASS:-cts_secret_pass}
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ./scripts/init-schemas.sql:/docker-entrypoint-initdb.d/init-schemas.sql:ro
    networks:
      - cts_data_net

  cts-redis:
    image: redis:7-alpine
    container_name: cts-redis
    restart: unless-stopped
    command: redis-server --appendonly yes --requirepass ${REDIS_PASS:-redis_secret_pass}
    volumes:
      - redisdata:/data
    networks:
      - cts_data_net

  cts-runner-daemon:
    build:
      context: ../../
      dockerfile: docker/runner/Dockerfile
    container_name: cts-runner-daemon
    restart: unless-stopped
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    networks:
      - cts_sandbox_net
```

---

## 5. Trazabilidad con Decisiones de Arquitectura (ADR)

* **[ADR-006: Descomposición en 3 Microservicios](/RUP/BITACORA.md#adr-006-descomposici%C3%B3n-arquitect%C3%B3nica-en-3-microservicios)**: Reflejada en la separación de módulos de backend y en los tres esquemas PostgreSQL alojados en el mismo contenedor `cts-postgres`.
* **[ADR-009: Entrevistas en Google Meet](/RUP/BITACORA.md#adr-009-delimitaci%C3%B3n-de-actores-opacidad-de-tests-para-el-candidato-entrevistas-google-meet-en-el-perfil-por-el-gestor-y-aislamiento-del-tl)**: El contenedor `cts-backend` posee conexión saliente hacia `Google Calendar API` para emitir enlaces dinámicos de videoconferencia.
* **[ADR-012: Elección de PostgreSQL 16](/RUP/BITACORA.md#adr-012-elecci%C3%B3n-de-postgresql-16-para-persistencia-relacional-y-soporte-de-microservicios)**: Implementación de esquemas lógicos nativos, identificadores UUID v4 e índices GIN sobre campos JSONB.

---

<div align="center">

[Fase 02: Análisis](/RUP/02-analisis/README.md) • [Fase 03: Diseño](/RUP/03-diseño/README.md)

</div>
