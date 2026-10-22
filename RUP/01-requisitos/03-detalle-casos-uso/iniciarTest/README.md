<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|
</div>

# Caso de Uso: `iniciarTest()`


<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/iniciarTest/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/iniciarTest/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## 📋 Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `Candidato` (admisión), `Alumno` (nivelación de fin de módulo formativo) |
| **Objetivo** | Iniciar formalmente la ejecución de un test diagnóstico (`Actitud`, `Aptitud` o `Tecnico`), activando el cronómetro inmutable en servidor y habilitando el panel de preguntas |
| **Precondición** | El actor debe estar autenticado; el test seleccionado debe estar en estado `PENDIENTE` dentro de la convocatoria activa |
| **Postcondición Éxito** | Test en estado `EN_CURSO`; cronómetro backend iniciado; primer ítem presentado; navegación en `TEST_EN_EJECUCION` |
| **Postcondición Fallo** | Si el test ya fue entregado (`COMPLETADO`) o expiró, el sistema bloquea el acceso mostrando mensaje informativo y permanece en `PANEL_POSTULACION_ABIERTO` |

</div>

---

## 📑 Reglas de Negocio Asociadas

1. **Inmutabilidad del Tiempo de Prueba**:
   * El cronómetro se calcula y valida en el servidor (`MotorEvaluacion`). Cerrar la ventana o refrescar el navegador no pausa el tiempo restante.
2. **Nutrición Multidisciplinar (`Tecnico`)**:
   * En el caso del test `Tecnico`, el motor de evaluación selecciona aleatoriamente preguntas aportadas por los 6 equipos de CTS (`Test ... Pregunta`) para evaluar la afinidad del candidato a las diferentes disciplinas.
3. **Sin Nota de Corte Eliminatoria (ADR-007)**:
   * El test no tiene nota eliminatoria; su propósito es emitir indicadores de perfil para el `Gestor`.

---

## 🔗 Referencias

* [Diagrama de Estados de Test](/RUP/00-modelo-del-dominio/estados-entidades/test-estados.puml)
* [ADR-007: Admisión continua y batería de 3 tests](/RUP/BITACORA.md#adr-007-admisi%C3%B3n-continua-por-ciclos-acad%C3%A9micos-bater%C3%ADa-de-3-tests-e-inclusi%C3%B3n-de-entrevista)
---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
