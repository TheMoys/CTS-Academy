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

|Paquete|Caso de uso|Actor Principal|Requisito|Análisis|Diseño|Desarrollo|
|:-|:-|:-:|:-:|:-:|:-:|:-:|
|**PK01 - Sesión**|`iniciarSesion()`|`UsuarioNoLogueado`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/iniciarSesion/README.md)|—|—|—|
|**PK01 - Sesión**|`cerrarSesion()`|`Usuario`|—|—|—|—|
|**PK02 - Admisión**|`iniciarPruebaTecnica()`|`Candidato`|[📃](/RUP/01-requisitos/03-detalle-casos-uso/iniciarPruebaTecnica/README.md)|—|—|—|
|**PK02 - Admisión**|`responderReactivoTeorico()`|`Candidato`|—|—|—|—|
|**PK02 - Admisión**|`entregarEjercicioPractico()`|`Candidato`|—|—|—|—|
|**PK02 - Admisión**|`ejecutarCodigoSandbox()`|`Candidato` / `TestRunner`|—|—|—|—|
|**PK02 - Admisión**|`finalizarPruebaTecnica()`|`Candidato`|—|—|—|—|
|**PK02 - Admisión**|`calificarPruebaManual()`|`TechLeader`|—|—|—|—|
|**PK02 - Admisión**|`emitirDictamenCandidato()`|`TechLeader` / `GestorProfer`|—|—|—|—|
|**PK03 - Academy**|`abrirRutaAprendizaje()`|`AlumnoProfer`|—|—|—|—|
|**PK03 - Academy**|`entregarLaboratorioOnSite()`|`AlumnoProfer`|—|—|—|—|
|**PK03 - Academy**|`revisarCodigoLaboratorio()`|`TechLeader`|—|—|—|—|
|**PK03 - Academy**|`registrarSeguimientoSemanal()`|`TechLeader`|—|—|—|—|
|**PK04 - Convocatorias**|`crearConvocatoria()`|`GestorProfer`|—|—|—|—|
|**PK04 - Convocatorias**|`matricularCandidato()`|`GestorProfer`|—|—|—|—|
|**PK04 - Convocatorias**|`asignarTLAlumnoProfer()`|`GestorProfer`|—|—|—|—|
|**PK05 - Reactivos**|`crearReactivoTeorico()`|`TechLeader`|—|—|—|—|
|**PK05 - Reactivos**|`crearEjercicioPractico()`|`TechLeader`|—|—|—|—|
|**PK05 - Reactivos**|`configurarRubricaEvaluacion()`|`TechLeader`|—|—|—|—|

</div>
