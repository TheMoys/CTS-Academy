<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|
</div>

# Caso de Uso: `iniciarSesion()`


<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/iniciarSesion/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/iniciarSesion/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## 📋 Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `UsuarioNoLogueado` (extiende mediante `<<extend>>` condicional al caso de uso de apertura del panel correspondiente: `abrirPanelPostulacion()`, `abrirPanelAlumno()`, `abrirPanelLider()` o `abrirPanelAdmisiones()`) |
| **Objetivo** | Autenticar credenciales en `SESION_CERRADA` y dar paso al espacio de trabajo del actor según su rol institucional validado |
| **Precondición** | El usuario debe estar previamente registrado en la plataforma con credenciales activas (los candidatos son registrados por el Gestor tras la remisión de expedientes por las sedes) |
| **Postcondición Éxito** | Sesión establecida; token de sesión emitido y contexto del actor abierto (`PANEL_POSTULACION_ABIERTO`, `INICIO_ALUMNO_ABIERTO`, `PANEL_LIDER_ABIERTO` o `PANEL_ADMISIONES_ABIERTO`) |
| **Postcondición Fallo** | El sistema permanece en `SESION_CERRADA` visualizando mensaje de error de credenciales |

</div>

---

## 📑 Reglas de Negocio Asociadas

1. **Sin Auto-Registro Anónimo (ADR-008)**:
   * No existe opción de auto-registro en la interfaz. Todo acceso proviene de una cuenta previamente dada de alta por la administración o por el `Gestor` a partir de los listados de sedes.
2. **Enrutamiento por Rol Unívoco**:
   * Cada perfil autenticado accede exclusivamente a su área de trabajo. Un `Candidato` no puede navegar por las rutas del `Alumno` ni viceversa; la transición de rol solo se produce tras el caso de uso `admitirAlumnoProfer()`.
3. **Bloqueo por Intentos Fallidos**:
   * Tras 5 intentos erróneos consecutivos, la cuenta se bloquea temporalmente por 15 minutos, notificando al usuario en pantalla.

---

## 🔗 Referencias

* [Diagramas de Contexto por Actor](/RUP/01-requisitos/01-actores-casos-uso/README.md#%F0%9F%94%84-diagramas-de-contexto-por-actor)
* [ADR-008: Eliminación de UsuarioNoLogueado](/RUP/BITACORA.md#adr-008-canalizaci%C3%B3n-de-candidatos-por-sedes-internacionales-y-eliminaci%C3%B3n-de-usuarionologueado)
---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
