<div align=right>

<sub>[Al inicio](/README.md) / [Bitácora RUP](/RUP/BITACORA.md) / [Modelo del dominio](/RUP/00-modelo-del-dominio/README.md) / [Actores y casos de uso](/RUP/01-requisitos/01-actores-casos-uso/README.md) / [Detalle de casos de uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) / **cerrarSesion()**</sub>

</div>

# Caso de Uso: `cerrarSesion()`

> | [Inicio](/README.md) | [Diagrama de Contexto Candidato](/images/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoCandidato.svg) | [Diagrama de Contexto Alumno](/images/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoAlumno.svg) | [Diagrama de Contexto TL](/images/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoLiderEquipo.svg) | [Diagrama de Contexto Gestor](/images/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoGestor.svg) | **Detalle** | [Análisis](/RUP/02-analisis/README.md) | [Diseño](/RUP/03-diseño/README.md) |
> | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |

<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/cerrarSesion/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/cerrarSesion/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## 📋 Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | Común a los 4 actores (`Candidato`, `Alumno`, `LiderEquipo`, `Gestor`) |
| **Objetivo** | Finalizar e invalidar de forma segura la sesión activa del usuario autenticado, revocando sus tokens criptográficos en el servidor (Refresh Token y lista negra de Access Token JTI), purgando las cookies `HttpOnly` y retornando a la interfaz de acceso general (`SESION_CERRADA`) |
| **Tipo** | Secundario, soporte de seguridad |
| **Nivel** | Objetivo de usuario |
| **Precondición** | El usuario debe encontrarse previamente autenticado en cualquiera de los paneles principales (`PANEL_POSTULACION_ABIERTO`, `INICIO_ALUMNO_ABIERTO`, `PANEL_LIDER_ABIERTO`, `PANEL_ADMISIONES_ABIERTO`) |
| **Postcondición Éxito** | Tokens invalidados en backend; cabecera `Clear-Site-Data` y cookies `HttpOnly` eliminadas; almacenamiento volátil del cliente purgado; contexto transiciona a `SESION_CERRADA` con la pantalla de acceso |
| **Postcondición Cancelación** | Si el usuario cancela en el diálogo de advertencia de procesos activos (`-[#blue]->`), permanece en su panel de origen sin alteración de credenciales |

</div>

---

## 📑 Reglas de Negocio Asociadas

1. **RN-ACC-03 — Revocación Server-Side y Blacklist en Redis**:
   * La invalidación de sesión no delega la seguridad en el cliente. El backend revoca formalmente el `refresh_token` en base de datos e incorpora el identificador único `jti` del `access_token` en una lista negra en memoria caché (Redis) con un TTL equivalente al tiempo remanente de expiración del token.
2. **RN-ACC-04 — Fail-Secure Client-Side**:
   * Si ocurre una interrupción de red o fallo en el microservicio de autenticación al procesar la revocación, el cliente web actúa bajo la directiva *fail-secure*: purga de inmediato el almacenamiento local de credenciales, elimina cookies y fuerza la redirección a `SESION_CERRADA` registrando una advertencia técnica en auditoría.
3. **RN-ACC-05 — Advertencia de Procesos y Tests Activos**:
   * Si un `Candidato` o `Alumno` solicita cerrar sesión con una evaluación en estado `EN_CURSO`, el sistema presenta una advertencia modal informando que el cronómetro del examen continuará su curso en el servidor (inmutabilidad temporal ADR-007) y exigiendo confirmación consciente antes de abandonar.

---

## 🔗 Referencias

* [Diagrama de Contexto Candidato](/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoCandidato.puml)
* [Diagrama de Contexto Alumno](/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoAlumno.puml)
* [Diagrama de Contexto LiderEquipo](/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoLiderEquipo.puml)
* [Diagrama de Contexto Gestor](/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoGestor.puml)
* [Caso de Uso: `iniciarSesion()`](/RUP/01-requisitos/03-detalle-casos-uso/iniciarSesion/README.md)
* [ADR-007: Admisión continua y batería de 3 tests diagnósticos](/RUP/BITACORA.md#adr-007-admisi%C3%B3n-continua-por-ciclos-acad%C3%A9micos-bater%C3%ADa-de-3-tests-e-inclusi%C3%B3n-de-entrevista)
