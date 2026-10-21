<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

<sub>**Fase 01 Requisitos** › **Detalle de Caso de Uso** › `registrarCandidato()`</sub>

</div>

# Caso de Uso: `registrarCandidato()`


<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/registrarCandidato/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/registrarCandidato/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## 📋 Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `Gestor` (`GestorProfer`) |
| **Objetivo** | Registrar individualmente en el sistema a un aspirante internacional remitido por una sede de origen, vinculándolo a la convocatoria vigente, inicializando automáticamente su batería de 3 tests diagnósticos y despachando sus credenciales de acceso |
| **Tipo** | Primario, entrada del flujo de admisiones |
| **Nivel** | Objetivo de usuario |
| **Precondición** | El Gestor debe encontrarse autenticado; debe existir al menos una convocatoria activa con plazo de postulación abierto |
| **Postcondición Éxito** | Se crea la entidad `Candidato` y la asociación `Candidatura`; se instancian los 3 tests (`TestActitud`, `TestAptitud`, `TestTecnico`) en estado `PENDIENTE`; se generan credenciales temporales y se despacha el correo de bienvenida; contexto transiciona a `REGISTRO_CANDIDATO_ABIERTO` |
| **Postcondición Fallo** | Si el email del candidato ya se encuentra registrado en la convocatoria activa o faltan campos obligatorios, el sistema emite un aviso de validación y mantiene el formulario editable |

</div>

---

## 📑 Reglas de Negocio Asociadas

1. **RN-REG-01 — Inicialización Automática de Batería (ADR-007)**:
   * Al registrar un nuevo candidato, el sistema crea de forma automática e indivisible las 3 instancias de test diagnósticos vinculadas a la candidatura en estado `PENDIENTE`.
2. **RN-REG-02 — Unicidad de Correo por Convocatoria**:
   * No se admiten dos candidaturas activas con el mismo correo electrónico dentro de un mismo ciclo académico o convocatoria vigente.
3. **RN-REG-03 — Generación Segura de Credenciales Temporales**:
   * El sistema genera una contraseña criptográfica temporal y un enlace con token de un solo uso para que el aspirante configure su acceso en `PK01 - Acceso`.
4. **RN-REG-04 — Trazabilidad de Sede Remitente**:
   * Toda postulación debe quedar inexcusablemente catalogada con su sede internacional de origen para fines de estadísticas institucionales y convenios PROFER.

---

## 🔗 Referencias

* [Modelo del Dominio: `Candidato`, `Convocatoria`, `Test`](/RUP/00-modelo-del-dominio/README.md)
* [Diagrama de Estados de Candidatura](/RUP/00-modelo-del-dominio/estados-entidades/candidatura-estados.puml)
* [Diagrama de Contexto Gestor](/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoGestor.puml)
* [ADR-007: Admisión continua y batería de 3 tests diagnósticos](/RUP/BITACORA.md#adr-007-admisi%C3%B3n-continua-por-ciclos-acad%C3%A9micos-bater%C3%ADa-de-3-tests-e-inclusi%C3%B3n-de-entrevista)
---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
