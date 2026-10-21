<div align="center">

| [🏠 Inicio](/README.md) | **📖 RUP Hub** | [📜 Bitácora ADR](/RUP/BITACORA.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [🔍 02 Análisis](/RUP/02-analisis/README.md) | [🎨 03 Diseño](/RUP/03-diseño/README.md) | [💻 04 Desarrollo](/RUP/04-desarrollo/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|

</div>

# RUP — CTS Academy & Evaluator

Página concentradora de artefactos de ingeniería de software bajo la metodología RUP (Rational Unified Process) para la plataforma **CTS Academy & Evaluator**.

Desde aquí se accede a cada una de las fases del ciclo de desarrollo, al registro de decisiones arquitectónicas y a la matriz de trazabilidad integral caso por caso.

---

## Artefactos Concentradores

<div align=center>

|Seguimiento y Decisiones|Modelo del dominio|Requisitos|Análisis|Diseño|
|:-:|:-:|:-:|:-:|:-:|
|**[Bitácora RUP (ADR)](/RUP/BITACORA.md)**|[Modelo del dominio](/RUP/00-modelo-del-dominio/README.md)|[Hub de Requisitos](/RUP/01-requisitos/README.md)|[Fase 02: Análisis](/RUP/02-analisis/README.md)|[Fase 03: Diseño](/RUP/03-diseño/README.md)|
|Historial de refinamientos|[Glosario de entidades](/RUP/00-modelo-del-dominio/README.md#glosario-de-entidades-por-microservicio)|[Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)|Clases de análisis (BCE)|Diagrama Entidad-Relación|
|Registro de acuerdos RUP|[3 Microservicios](/RUP/00-modelo-del-dominio/README.md#1-los-3-microservicios-del-sistema)|[Detalle Casos de Uso (35)](/RUP/01-requisitos/03-detalle-casos-uso/README.md)|Colaboraciones de análisis|Despliegue Docker|

</div>

---

## Fases del Proceso Unificado

<div align=center>

|Fase|Directorio / Enlace|Propósito y Contenido Principal|
|:-|:-|:-|
|**00 - Dominio**|[Modelo del dominio](/RUP/00-modelo-del-dominio/README.md)|Vocabulario del negocio, modelo conceptual de entidades, estados del ciclo de vida y reglas invariantes.|
|**01 - Requisitos**|[Requisitos](/RUP/01-requisitos/README.md)|Catálogo de actores, diagramas de contexto, diagramas de casos de uso por paquete funcional, especificaciones formales con máquinas de estados y wireframes.|
|**02 - Análisis**|[Análisis](/RUP/02-analisis/README.md)|Clases de análisis (Frontera, Control, Entidad) y realizaciones de casos de uso independientes de la tecnología concreta.|
|**03 - Diseño**|[Diseño](/RUP/03-diseño/README.md)|Diagramas de secuencia de diseño, contratos de API REST/GraphQL, diseño relacional (DER), clases del stack tecnológico y despliegue físico con Docker.|
|**04 - Desarrollo**|[Desarrollo](/RUP/04-desarrollo/README.md)|Trazabilidad hacia el código fuente de backend y frontend, componentes y pruebas automatizadas.|

</div>

---

## Matriz Preliminar de Casos de Uso y Trazabilidad

`📃` enlaza la ficha de la fase; `—` indica que el caso de uso está pendiente de elaborar en esa fase.

<div align=center>

|Subsistema / Paquete|Caso de uso|Actor Principal|Requisito|Análisis|Diseño|Desarrollo|
|:-|:-|:-:|:-:|:-:|:-:|:-:|
|**PK01 - Acceso**|`iniciarSesion()`|`Candidato` / `Alumno` / `LiderEquipo` / `Gestor`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/iniciarSesion/README.md)|—|—|—|
|**PK01 - Acceso**|`cerrarSesion()`|`Candidato` / `Alumno` / `LiderEquipo` / `Gestor`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/cerrarSesion/README.md)|—|—|—|
|**PK02 - MotorEvaluacion**|`abrirPanelPostulacion()`|`Candidato`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/abrirPanelPostulacion/README.md)|—|—|—|
|**PK02 - MotorEvaluacion**|`iniciarTest()`|`Candidato` / `Alumno`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/iniciarTest/README.md)|—|—|—|
|**PK02 - MotorEvaluacion**|`responderPreguntaTeorica()`|`Candidato` / `Alumno`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/responderPreguntaTeorica/README.md)|—|—|—|
|**PK02 - MotorEvaluacion**|`entregarPreguntaPractica()`|`Candidato` / `Alumno`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/entregarPreguntaPractica/README.md)|—|—|—|
|**PK02 - MotorEvaluacion**|`finalizarTest()`|`Candidato` / `Alumno`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/finalizarTest/README.md)|—|—|—|
|**PK02 - MotorEvaluacion**|`abrirPerfilCandidato()`|`Gestor`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/abrirPerfilCandidato/README.md)|—|—|—|
|**PK02 - MotorEvaluacion**|`agendarEntrevistaGoogleMeet()`|`Gestor`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/agendarEntrevistaGoogleMeet/README.md)|—|—|—|
|**PK02 - MotorEvaluacion**|`registrarAnotacionesEntrevista()`|`Gestor`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/registrarAnotacionesEntrevista/README.md)|—|—|—|
|**PK02 - MotorEvaluacion**|`admitirAlumnoProfer()`|`Gestor`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/admitirAlumnoProfer/README.md)|—|—|—|
|**PK02 - MotorEvaluacion**|`rechazarCandidatura()`|`Gestor`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/rechazarCandidatura/README.md)|—|—|—|
|**PK02 - MotorEvaluacion**|`registrarCandidato()`|`Gestor`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/registrarCandidato/README.md)|—|—|—|
|**PK02 - MotorEvaluacion**|`importarCandidatosSede()`|`Gestor`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/importarCandidatosSede/README.md)|—|—|—|
|**PK03 - MotorFormacion**|`abrirPanelAlumno()`|`Alumno`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/abrirPanelAlumno/README.md)|—|—|—|
|**PK03 - MotorFormacion**|`consultarCapacitacion()`|`Alumno`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/consultarCapacitacion/README.md)|—|—|—|
|**PK03 - MotorFormacion**|`consultarModulo()`|`Alumno`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/consultarModulo/README.md)|—|—|—|
|**PK03 - MotorFormacion**|`consultarMaterial()`|`Alumno`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/consultarMaterial/README.md)|—|—|—|
|**PK03 - MotorFormacion**|`enviarEntregable()`|`Alumno`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/enviarEntregable/README.md)|—|—|—|
|**PK03 - MotorFormacion**|`consultarFeedbackEntregable()`|`Alumno`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/consultarFeedbackEntregable/README.md)|—|—|—|
|**PK03 - MotorFormacion**|`crearMaterial()`|`LiderEquipo`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/crearMaterial/README.md)|—|—|—|
|**PK03 - MotorFormacion**|`editarMaterial()`|`LiderEquipo`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/editarMaterial/README.md)|—|—|—|
|**PK03 - MotorFormacion**|`eliminarMaterial()`|`LiderEquipo`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/eliminarMaterial/README.md)|—|—|—|
|**PK03 - MotorFormacion**|`crearPregunta()`|`LiderEquipo`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/crearPregunta/README.md)|—|—|—|
|**PK03 - MotorFormacion**|`editarPregunta()`|`LiderEquipo`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/editarPregunta/README.md)|—|—|—|
|**PK03 - MotorFormacion**|`eliminarPregunta()`|`LiderEquipo`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/eliminarPregunta/README.md)|—|—|—|
|**PK03 - MotorFormacion**|`abrirEntregablesPendientes()`|`LiderEquipo`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/abrirEntregablesPendientes/README.md)|—|—|—|
|**PK03 - MotorFormacion**|`revisarEntregable()`|`LiderEquipo`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/revisarEntregable/README.md)|—|—|—|
|**PK03 - MotorFormacion**|`aprobarEntregable()`|`LiderEquipo`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/aprobarEntregable/README.md)|—|—|—|
|**PK03 - MotorFormacion**|`solicitarCambiosEntregable()`|`LiderEquipo`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/solicitarCambiosEntregable/README.md)|—|—|—|
|**PK03 - MotorFormacion**|`evaluarCapacitacionAlumno()`|`LiderEquipo`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/evaluarCapacitacionAlumno/README.md)|—|—|—|
|**PK04 - MotorEquipos**|`abrirPanelLider()`|`LiderEquipo`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/abrirPanelLider/README.md)|—|—|—|
|**PK04 - MotorEquipos**|`abrirPanelAdmisiones()`|`Gestor`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/abrirPanelAdmisiones/README.md)|—|—|—|
|**PK04 - MotorEquipos**|`abrirPeriodoIngreso()`|`Gestor`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/abrirPeriodoIngreso/README.md)|—|—|—|
|**PK04 - MotorEquipos**|`cerrarCorteSemestral()`|`Gestor`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/cerrarCorteSemestral/README.md)|—|—|—|

</div>
