<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [01 Requisitos](/RUP/01-requisitos/README.md) | [02 Análisis](/RUP/02-analisis/README.md) | [Catálogo Requisitos](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

<sub>**Fase 02 Análisis** › **Realización de Casos de Uso** › `registrarCandidato()`</sub>

</div>

# Realización de Caso de Uso: `registrarCandidato()`

Esta especificación describe la realización de análisis del caso de uso `registrarCandidato()` mediante clases BCE, detallando la inicialización automática indivisible de la batería de 3 tests diagnósticos, el control de unicidad de correo y el aprovisionamiento seguro de credenciales temporales.

---

<div align=center>

| Diagrama de Clases de Análisis (VOPC) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/registrarCandidato/clasesAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](clasesAnalisis.puml)</i></sup> |

| Diagrama de Realización de Análisis (Secuencia BCE) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/registrarCandidato/realizacionAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](realizacionAnalisis.puml)</i></sup> |

</div>

---

## Clases de Análisis Participantes

<div align=center>

| Clase | Estereotipo | Tipo | Responsabilidad Principal |
| :--- | :---: | :---: | :--- |
| **`FormularioRegistroCandidato`** | `<<boundary>>` | Frontera | Interfaz de alta individual; captura de datos personales, selector de sede de origen, validación de formato y aviso de confirmación con expediente. |
| **`ServicioAccesoAutenticacion`** | `<<boundary>>` | Frontera (Externa) | Interfaz con el subsistema de acceso (`PK01 - Acceso`); genera la cuenta de usuario temporal y el token criptográfico de activación (`RN-REG-03`). |
| **`ServicioNotificacionesEmail`** | `<<boundary>>` | Frontera (Externa) | Adaptador de mensajería; despacha el correo de bienvenida con las instrucciones para configurar contraseña y rendir las pruebas. |
| **`GestorAdmisiones`** | `<<control>>` | Control | Orquestación del alta, verificación de vigencia de convocatoria y unicidad de correo (`RN-REG-02`), e inicialización automática de la batería evaluativa (`RN-REG-01`). |
| **`Candidato`** | `<<entity>>` | Entidad | Nueva instancia de aspirante internacional; custodia el expediente unívoco, correo, sede remitente (`RN-REG-04`) y estado `REGISTRADO`. |
| **`Convocatoria`** | `<<entity>>` | Entidad | Convocatoria semestral activa; comprueba vigencia y previene la duplicidad de cuentas para un mismo ciclo lectivo. |
| **`Test`** | `<<entity>>` | Entidad | Instancias diagnósticas; se crean en bloque en estado `PENDIENTE` para `Actitud`, `Aptitud` y `Tecnico` (`ADR-007`). |

</div>

---

## Flujo de Realización (Colaboración BCE)

### Flujo Principal: Alta Individual Exitosa
1. El **`Gestor`** accede al formulario de registro individual de aspirante internacional.
2. Introduce nombre completo, correo institucional, sede remitente (**RN-REG-04**) y convocatoria.
3. **`FormularioRegistroCandidato`** remite la solicitud a **`GestorAdmisiones`**.
4. **Verificación de Convocatoria Activa y Unicidad (RN-REG-02)**: **`GestorAdmisiones`** valida en **`Convocatoria`** que el plazo esté abierto y que no exista otro aspirante con el mismo email en el ciclo académico.
5. **Creación del Aspirante**: Se instancia la entidad **`Candidato`** en estado `REGISTRADO`.
6. **Inicialización Automática de Batería (RN-REG-01 / ADR-007)**:
   - Se instancian en una transacción atómica las 3 pruebas diagnósticas (`Actitud`, `Aptitud`, `Tecnico`) en estado `PENDIENTE`.
   - Se vinculan indivisiblemente a la postulación del aspirante.
7. **Aprovisionamiento de Credenciales (RN-REG-03)**:
   - **`GestorAdmisiones`** solicita a **`ServicioAccesoAutenticacion`** generar el usuario con contraseña temporal y token de activación.
   - Se despacha el correo de bienvenida mediante **`ServicioNotificacionesEmail`**.
8. **`FormularioRegistroCandidato`** muestra la confirmación de alta con el número de expediente emitido.

### Flujo Alternativo: Correo Duplicado (RN-REG-02)
1. Si el correo electrónico ya cuenta con postulación previa en la convocatoria activa:
   - **`GestorAdmisiones`** aborta la persistencia y emite un mensaje de validación.
   - **`FormularioRegistroCandidato`** notifica la duplicidad, manteniendo los datos en el formulario para su corrección.

---

## Trazabilidad con la Fase de Requisitos

| Requisito / Artefacto Fase 01 | Realización en Fase 02 (Análisis) |
| :--- | :--- |
| **Caso de Uso `registrarCandidato()`** | Coordinación en `GestorAdmisiones` asociando `Candidato`, `Convocatoria`, `Test` y servicios externos. |
| **RN-REG-01 (Inicialización Batería)** | Creación en bloque de las 3 entidades `Test` en estado `PENDIENTE` en la misma transacción. |
| **RN-REG-02 (Unicidad de Correo)** | Comprobación mediante `existeAspiranteConEmail()` en la entidad `Convocatoria`. |
| **RN-REG-03 (Credenciales Seguras)** | Integración con `ServicioAccesoAutenticacion` emitiendo tokens de configuración única. |
| **RN-REG-04 (Trazabilidad de Sede)** | Atributo `sedeOrigen` obligatorio en la entidad `Candidato`. |

---

<div align="center">

[Volver a Fase 02: Análisis](/RUP/02-analisis/README.md) • [Ver Especificación de Requisitos (Fase 01)](/RUP/01-requisitos/03-detalle-casos-uso/registrarCandidato/README.md)

</div>
