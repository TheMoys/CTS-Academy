<div align=right>

<sub>[Al inicio](/README.md) / [Bitácora RUP](/RUP/BITACORA.md) / [Modelo del dominio](/RUP/00-modelo-del-dominio/README.md) / [Actores y casos de uso](/RUP/01-requisitos/01-actores-casos-uso/README.md) / [Detalle](/RUP/01-requisitos/03-detalle-casos-uso/README.md) / [Análisis](/RUP/02-analisis/README.md) / [Diseño](/RUP/03-diseño/README.md) / [Desarrollo](/RUP/04-desarrollo/README.md)</sub>

</div>

# RUP — CTS Academy & Evaluator

Página concentradora de artefactos de ingeniería de software bajo la metodología RUP (Rational Unified Process) para la plataforma **CTS Academy & Evaluator**.

Desde aquí se accede a cada una de las fases del ciclo de desarrollo, al registro de decisiones arquitectónicas y a la matriz de trazabilidad integral caso por caso.

---

## Artefactos Concentradores

<div align=center>

|Seguimiento y Decisiones|Modelo del dominio|Requisitos|Análisis|Diseño|
|:-:|:-:|:-:|:-:|:-:|
|**[Bitácora RUP (ADR)](/RUP/BITACORA.md)**|[Modelo del dominio](/RUP/00-modelo-del-dominio/README.md)|[Actores y casos de uso](/RUP/01-requisitos/01-actores-casos-uso/README.md)|[Clases de análisis](/RUP/02-analisis/clases-analisis.puml)|[Clases de diseño](/RUP/03-diseño/clases-diseño.puml)|
|Historial de refinamientos|[Glosario de entidades](/RUP/00-modelo-del-dominio/README.md#glosario-de-entidades-por-microservicio)|[Detalle de casos de uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md)|[Colaboraciones de análisis](/RUP/02-analisis/casos-uso/README.md)|[Diagrama Entidad-Relación](/RUP/03-diseño/modelo-datos/README.md)|
|Registro de acuerdos RUP|[3 Microservicios](/RUP/00-modelo-del-dominio/README.md#1-los-3-microservicios-del-sistema)|Wireframes de interfaz||[Despliegue Docker](/RUP/03-diseño/despliegue/README.md)|

</div>

---

## Fases del Proceso Unificado

<div align=center>

|Fase|Directorio / Enlace|Propósito y Contenido Principal|
|:-|:-|:-|
|**00 - Dominio**|[Modelo del dominio](/RUP/00-modelo-del-dominio/README.md)|Vocabulario del negocio, modelo conceptual de entidades, estados del ciclo de vida y reglas invariantes.|
|**01 - Requisitos**|[Requisitos](/RUP/01-requisitos/01-actores-casos-uso/README.md)|Catálogo de actores, diagramas de contexto, diagramas de casos de uso por paquete funcional, especificaciones formales con máquinas de estados y wireframes.|
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
|**PK01 - Acceso**|`cerrarSesion()`|`Candidato` / `Alumno` / `LiderEquipo` / `Gestor`|—|—|—|—|
|**PK02 - MotorEvaluacion**|`abrirPanelPostulacion()`|`Candidato`|—|—|—|—|
|**PK02 - MotorEvaluacion**|`iniciarTest()`|`Candidato` / `Alumno`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/iniciarTest/README.md)|—|—|—|
|**PK02 - MotorEvaluacion**|`responderPreguntaTeorica()`|`Candidato`|—|—|—|—|
|**PK02 - MotorEvaluacion**|`entregarPreguntaPractica()`|`Candidato`|—|—|—|—|
|**PK02 - MotorEvaluacion**|`finalizarTest()`|`Candidato`|—|—|—|—|
|**PK02 - MotorEvaluacion**|`abrirPerfilCandidato()`|`Gestor`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/abrirPerfilCandidato/README.md)|—|—|—|
|**PK02 - MotorEvaluacion**|`agendarEntrevistaGoogleMeet()`|`Gestor`|—|—|—|—|
|**PK02 - MotorEvaluacion**|`registrarAnotacionesEntrevista()`|`Gestor`|—|—|—|—|
|**PK02 - MotorEvaluacion**|`admitirAlumnoProfer()`|`Gestor`|—|—|—|—|
|**PK02 - MotorEvaluacion**|`rechazarCandidatura()`|`Gestor`|—|—|—|—|
|**PK02 - MotorEvaluacion**|`registrarCandidato()`|`Gestor`|—|—|—|—|
|**PK02 - MotorEvaluacion**|`importarCandidatosSede()`|`Gestor`|—|—|—|—|
|**PK03 - MotorFormacion**|`abrirPanelAlumno()`|`Alumno`|—|—|—|—|
|**PK03 - MotorFormacion**|`consultarCapacitacion()`|`Alumno`|—|—|—|—|
|**PK03 - MotorFormacion**|`consultarModulo()`|`Alumno`|—|—|—|—|
|**PK03 - MotorFormacion**|`consultarMaterial()`|`Alumno`|—|—|—|—|
|**PK03 - MotorFormacion**|`enviarEntregable()`|`Alumno`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/enviarEntregable/README.md)|—|—|—|
|**PK03 - MotorFormacion**|`consultarFeedbackEntregable()`|`Alumno`|—|—|—|—|
|**PK03 - MotorFormacion**|`crearMaterial()`|`LiderEquipo`|—|—|—|—|
|**PK03 - MotorFormacion**|`editarMaterial()`|`LiderEquipo`|—|—|—|—|
|**PK03 - MotorFormacion**|`eliminarMaterial()`|`LiderEquipo`|—|—|—|—|
|**PK03 - MotorFormacion**|`crearPregunta()`|`LiderEquipo`|—|—|—|—|
|**PK03 - MotorFormacion**|`editarPregunta()`|`LiderEquipo`|—|—|—|—|
|**PK03 - MotorFormacion**|`eliminarPregunta()`|`LiderEquipo`|—|—|—|—|
|**PK03 - MotorFormacion**|`abrirEntregablesPendientes()`|`LiderEquipo`|—|—|—|—|
|**PK03 - MotorFormacion**|`revisarEntregable()`|`LiderEquipo`|—|—|—|—|
|**PK03 - MotorFormacion**|`aprobarEntregable()`|`LiderEquipo`|—|—|—|—|
|**PK03 - MotorFormacion**|`solicitarCambiosEntregable()`|`LiderEquipo`|—|—|—|—|
|**PK03 - MotorFormacion**|`evaluarCapacitacionAlumno()`|`LiderEquipo`|—|—|—|—|
|**PK04 - MotorEquipos**|`abrirPanelLider()`|`LiderEquipo`|—|—|—|—|
|**PK04 - MotorEquipos**|`abrirPanelAdmisiones()`|`Gestor`|—|—|—|—|
|**PK04 - MotorEquipos**|`abrirPeriodoIngreso()`|`Gestor`|—|—|—|—|
|**PK04 - MotorEquipos**|`cerrarCorteSemestral()`|`Gestor`|—|—|—|—|

</div>
