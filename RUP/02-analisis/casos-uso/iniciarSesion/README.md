<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [01 Requisitos](/RUP/01-requisitos/README.md) | [02 Análisis](/RUP/02-analisis/README.md) | [Catálogo Requisitos](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

<sub>**Fase 02 Análisis** › **Realización de Casos de Uso** › `iniciarSesion()`</sub>

</div>

# Realización de Caso de Uso: `iniciarSesion()`

Esta especificación describe la realización de análisis del caso de uso `iniciarSesion()` mediante la colaboración de clases estereotipadas Boundary-Control-Entity (BCE), estableciendo la arquitectura lógica previa al diseño tecnológico concreto.

---

<div align=center>

| Diagrama de Clases de Análisis (VOPC) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/iniciarSesion/clasesAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](clasesAnalisis.puml)</i></sup> |

| Diagrama de Realización de Análisis (Secuencia BCE) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/iniciarSesion/realizacionAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](realizacionAnalisis.puml)</i></sup> |

</div>

---

## Clases de Análisis Participantes

<div align=center>

| Clase | Estereotipo | Tipo | Responsabilidad Principal |
| :--- | :---: | :---: | :--- |
| **`FormularioLogin`** | `<<boundary>>` | Frontera | Interfaz de captura de credenciales (`email`, `contraseña`), renderizado de advertencias de error/bloqueo y redirección dinámica hacia el panel correspondiente según el rol del usuario validado. |
| **`GestorAutenticacion`** | `<<control>>` | Control | Orquestación del flujo de autenticación, verificación de políticas de bloqueo temporal por intentos fallidos, invocación de comprobación de credenciales y coordinación de emisión de la nueva sesión. |
| **`Usuario`** | `<<entity>>` | Entidad | Representación de la identidad persistente, validación de contraseñas mediante hash seguro, control de estado de cuenta (`Activo`, `BloqueadoTemporalmente`) y conteo de intentos fallidos. |
| **`Sesion`** | `<<entity>>` | Entidad | Entidad representativa del contexto autenticado activo, custodia del token criptográfico, control de expiración por inactividad y vida absoluta. |

</div>

---

## Flujo de Realización (Colaboración BCE)

### Flujo Principal: Autenticación Exitosa
1. El **`UsuarioNoLogueado`** interactúa con **`FormularioLogin`** introduciendo su correo y contraseña.
2. **`FormularioLogin`** delega la petición invocando `iniciarSesion(email, contraseña)` en **`GestorAutenticacion`**.
3. **`GestorAutenticacion`** localiza la entidad **`Usuario`** correspondiente por su identificador unívoco (email).
4. **`GestorAutenticacion`** comprueba el estado de la cuenta invocando `estaBloqueado()` en **`Usuario`**. Al encontrarse la cuenta activa, prosigue.
5. **`GestorAutenticacion`** solicita la comprobación de credenciales a **`Usuario`** mediante `verificarPassword(contraseña)`.
6. Al ser el hash coincidente:
   - **`GestorAutenticacion`** invoca `reiniciarIntentosFallidos()` en **`Usuario`**.
   - **`GestorAutenticacion`** crea una nueva instancia de **`Sesion`** vinculada al usuario.
   - **`GestorAutenticacion`** retorna el resultado de éxito con el rol asignado y el token de sesión a **`FormularioLogin`**.
7. **`FormularioLogin`** ejecuta la extensión condicional (`<<extend>>` ADR-011) redirigiendo al panel del actor según su rol (`abrirPanelPostulacion`, `abrirPanelAlumno`, `abrirPanelLider` o `abrirPanelAdmisiones`).

### Flujos Alternativos: Errores y Bloqueos
* **Usuario inexistente o contraseña inválida**:
  - Si el usuario no existe, o si `verificarPassword()` devuelve `false`, **`GestorAutenticacion`** invoca `incrementarIntentosFallidos()` en **`Usuario`**.
  - Si el contador alcanza el límite configurado (5 intentos), la cuenta transiciona a `BloqueadoTemporalmente` por 15 minutos.
  - **`GestorAutenticacion`** retorna un error genérico (prevención de enumeración de usuarios) a **`FormularioLogin`**, que lo visualiza en pantalla.
* **Intento de acceso a cuenta bloqueada**:
  - Al evaluar `estaBloqueado()`, si el periodo de bloqueo no ha expirado, **`GestorAutenticacion`** aborta la verificación de contraseña y retorna advertencia de bloqueo a **`FormularioLogin`** indicando los minutos restantes.

---

## Trazabilidad con la Fase de Requisitos

| Requisito / Artefacto Fase 01 | Realización en Fase 02 (Análisis) |
| :--- | :--- |
| **Caso de Uso `iniciarSesion()`** | Realización orquestada por `GestorAutenticacion` mediando entre `FormularioLogin` y `Usuario`. |
| **Actor `UsuarioNoLogueado`** | Actor externo conectado exclusivamente a la frontera `FormularioLogin`. |
| **Extensión `<<extend>>` por rol (ADR-011)** | La frontera `FormularioLogin` inspecciona `rol` en el resultado y bifurca hacia el panel respectivo. |
| **Regla de Bloqueo tras 5 intentos** | Encapsulada en los métodos `estaBloqueado()` e `incrementarIntentosFallidos()` de la entidad `Usuario`. |

---

<div align="center">

[Volver a Fase 02: Análisis](/RUP/02-analisis/README.md) • [Ver Especificación de Requisitos (Fase 01)](/RUP/01-requisitos/03-detalle-casos-uso/iniciarSesion/README.md)

</div>
