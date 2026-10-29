<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [01 Requisitos](/RUP/01-requisitos/README.md) | [02 Análisis](/RUP/02-analisis/README.md) | [Catálogo Requisitos](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

<sub>**Fase 02 Análisis** › **Realización de Casos de Uso** › `importarCandidatosSede()`</sub>

</div>

# Realización de Caso de Uso: `importarCandidatosSede()`

Esta especificación describe la realización de análisis del caso de uso `importarCandidatosSede()` mediante clases BCE, detallando la validación previa no destructiva en memoria, la deduplicación automática de expedientes y el encolamiento asíncrono para la emisión de credenciales.

---

<div align=center>

| Diagrama de Clases de Análisis (VOPC) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/importarCandidatosSede/clasesAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](clasesAnalisis.puml)</i></sup> |

| Diagrama de Realización de Análisis (Secuencia BCE) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/importarCandidatosSede/realizacionAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](realizacionAnalisis.puml)</i></sup> |

</div>

---

## Clases de Análisis Participantes

<div align=center>

| Clase | Estereotipo | Tipo | Responsabilidad Principal |
| :--- | :---: | :---: | :--- |
| **`FormularioImportarSede`** | `<<boundary>>` | Frontera | Interfaz de subida de archivos estructurados (CSV/Excel); presentación del balance analítico previo (`RN-IMP-01`) y barra de progreso de importación masiva. |
| **`ColaNotificacionesAsincrona`** | `<<boundary>>` | Frontera (Externa) | Adaptador de cola de mensajería asíncrona (workers en background); encola la generación de credenciales y el despacho masivo de correos (`RN-IMP-03`). |
| **`GestorAdmisiones`** | `<<control>>` | Control | Orquestación del procesado del lote, filtrado de duplicados contra la base de datos (`RN-IMP-02`), persistencia atómica en bloque y despacho a la cola asíncrona. |
| **`LoteImportacion`** | `<<entity>>` | Entidad | Registro temporal del lote en memoria; cuantifica registros válidos, duplicados y con errores de formato antes de autorizar la persistencia. |
| **`Candidato`** | `<<entity>>` | Entidad | Aspirantes persistidos; cada registro válido genera una instancia en estado `REGISTRADO`. |
| **`Convocatoria`** | `<<entity>>` | Entidad | Convocatoria semestral; expone el conjunto de correos electrónicos previamente registrados en el ciclo activo. |
| **`Test`** | `<<entity>>` | Entidad | Instancias diagnósticas; se crean en bloque de 3 (`Actitud`, `Aptitud`, `Tecnico`) en estado `PENDIENTE` para cada aspirante importado (`ADR-007`). |

</div>

---

## Flujo de Realización (Colaboración BCE)

### Fase 1: Validación Previa No Destructiva (RN-IMP-01)
1. El **`Gestor`** carga un archivo estructurado (CSV/Excel) remitido por una sede internacional.
2. **`FormularioImportarSede`** remite el archivo a **`GestorAdmisiones`**.
3. **Deduplicación contra Convocatoria (RN-IMP-02)**: **`GestorAdmisiones`** solicita a **`Convocatoria`** el catálogo de correos activos en el periodo.
4. **`LoteImportacion`** procesa las filas en memoria y genera un informe analítico discriminando:
   - Filas válidas listas para importar.
   - Filas descartadas por correo duplicado.
   - Filas con errores sintácticos de formato.
5. **`FormularioImportarSede`** presenta el informe previo al Gestor sin haber alterado la base de datos.

### Fase 2: Confirmación y Persistencia Masiva con Encolamiento (RN-IMP-03)
1. El **`Gestor`** revisa el balance y confirma la importación definitiva de los registros válidos.
2. **`GestorAdmisiones`** recupera la lista limpia de **`LoteImportacion`**.
3. En una transacción por lotes:
   - Se crea cada entidad **`Candidato`**.
   - Se inicializan de forma indivisible las 3 pruebas diagnósticas (`Test`) en estado `PENDIENTE` (**RN-REG-01** / **ADR-007**).
4. **Despacho Asíncrono en Background (RN-IMP-03)**:
   - **`GestorAdmisiones`** remite los aspirantes a **`ColaNotificacionesAsincrona`** para la generación de credenciales temporales y envío de correos en diferido, preservando la respuesta inmediata de la interfaz.
5. **`FormularioImportarSede`** muestra el resumen de candidatos dados de alta satisfactoriamente.

---

## Trazabilidad con la Fase de Requisitos

| Requisito / Artefacto Fase 01 | Realización en Fase 02 (Análisis) |
| :--- | :--- |
| **Caso de Uso `importarCandidatosSede()`** | Coordinación en `GestorAdmisiones` conectando `FormularioImportarSede`, `LoteImportacion` y `ColaNotificacionesAsincrona`. |
| **RN-IMP-01 (Validación No Destructiva)** | Entidad temporal `LoteImportacion` procesando filas en memoria antes de persistir. |
| **RN-IMP-02 (Deduplicación Automática)** | Cruce contra `obtenerCorreosRegistrados()` de la entidad `Convocatoria`. |
| **RN-IMP-03 (Encolamiento Asíncrono)** | Desacoplamiento del despacho de credenciales mediante `ColaNotificacionesAsincrona`. |

---

<div align="center">

[Volver a Fase 02: Análisis](/RUP/02-analisis/README.md) • [Ver Especificación de Requisitos (Fase 01)](/RUP/01-requisitos/03-detalle-casos-uso/importarCandidatosSede/README.md)

</div>
