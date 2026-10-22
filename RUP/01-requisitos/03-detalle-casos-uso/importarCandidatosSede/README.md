<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|
</div>

# Caso de Uso: `importarCandidatosSede()`


<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/importarCandidatosSede/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/importarCandidatosSede/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## 📋 Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `Gestor` (`GestorProfer`) |
| **Objetivo** | Cargar masivamente un conjunto de aspirantes remitidos formalmente por una sede internacional mediante archivo estructurado (CSV/Excel), validando su integridad, deduplicando correos y generando en bloque sus candidaturas y credenciales de examen |
| **Precondición** | El Gestor debe encontrarse autenticado en `REGISTRO_CANDIDATO_ABIERTO`; debe existir al menos una convocatoria activa |
| **Postcondición Éxito** | Creación masiva de entidades `Candidato` y `Candidatura` para todos los registros válidos; baterías de 3 tests diagnósticos inicializadas; despacho de credenciales encolado en cola asíncrona; contexto permanece en `REGISTRO_CANDIDATO_ABIERTO` |
| **Postcondición Cancelación** | Si el Gestor cancela la operación tras visualizar el informe de validación previa (`-[#blue]->`), no se persiste ningún registro |

</div>

---

## 📑 Reglas de Negocio Asociadas

1. **RN-IMP-01 — Validación Previa no Destructiva**:
   * El sistema procesa el archivo en memoria y presenta un informe analítico discriminando filas válidas, duplicadas y con errores sintácticos antes de ejecutar cualquier transacción de base de datos.
2. **RN-IMP-02 — Deduplicación Automática**:
   * Los registros cuyo correo ya exista en la convocatoria activa son descartados automáticamente de la importación para evitar duplicidad de expedientes.
3. **RN-IMP-03 — Encolamiento Asíncrono de Notificaciones**:
   * Para lotes numerosos (ej. 50+ aspirantes por sede), la generación de tokens y el despacho de correos se procesa en segundo plano para garantizar la reactividad de la interfaz.

---

## 🔗 Referencias

* [Modelo del Dominio: `Candidato`, `Convocatoria`, `Test`](/RUP/00-modelo-del-dominio/README.md)
* [Diagrama de Contexto Gestor](/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoGestor.puml)
* [Caso de Uso: `registrarCandidato()`](/RUP/01-requisitos/03-detalle-casos-uso/registrarCandidato/README.md)
* [ADR-007: Admisión continua y batería de 3 tests diagnósticos](/RUP/BITACORA.md#adr-007-admisi%C3%B3n-continua-por-ciclos-acad%C3%A9micos-bater%C3%ADa-de-3-tests-e-inclusi%C3%B3n-de-entrevista)
---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
