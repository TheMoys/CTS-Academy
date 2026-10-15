<div align=right>

<sub>[Al inicio](/README.md) / [Bitácora RUP](/RUP/BITACORA.md) / [Modelo del dominio](/RUP/00-modelo-del-dominio/README.md) / [Actores y casos de uso](/RUP/01-requisitos/01-actores-casos-uso/README.md) / [Detalle de casos de uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) / **iniciarTest()**</sub>

</div>

# Caso de Uso: `iniciarTest()`

> | [Inicio](/README.md) | [Diagrama de Contexto Candidato](/images/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoCandidato.svg) | **Detalle** | [Análisis](/RUP/02-analisis/README.md) | [Diseño](/RUP/03-diseño/README.md) |
> | :-: | :-: | :-: | :-: | :-: |

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
| **Objetivo** | Iniciar formalmente la ejecución de un test diagnóstico (`TestActitud`, `TestAptitud` o `TestTecnico`), activando el cronómetro inmutable en servidor y habilitando el panel de preguntas |
| **Tipo** | Primario, esencial |
| **Nivel** | Objetivo de usuario |
| **Precondición** | El actor debe estar autenticado; el test seleccionado debe estar en estado `PENDIENTE` dentro de la convocatoria activa |
| **Postcondición Éxito** | Test en estado `EN_CURSO`; cronómetro backend iniciado; primer ítem presentado; navegación en `TEST_EN_EJECUCION` |
| **Postcondición Fallo** | Si el test ya fue entregado (`COMPLETADO`) o expiró, el sistema bloquea el acceso mostrando mensaje informativo y permanece en `PANEL_POSTULACION_ABIERTO` |

</div>

---

## 📑 Reglas de Negocio Asociadas

1. **Inmutabilidad del Tiempo de Prueba**:
   * El cronómetro se calcula y valida en el servidor (`MotorEvaluacion`). Cerrar la ventana o refrescar el navegador no pausa el tiempo restante.
2. **Nutrición Multidisciplinar (`TestTecnico`)**:
   * En el caso del `TestTecnico`, el motor de evaluación selecciona aleatoriamente preguntas aportadas por los 6 equipos de CTS (`TestTecnico ... Pregunta`) para evaluar la afinidad del candidato a las diferentes disciplinas.
3. **Sin Nota de Corte Eliminatoria (ADR-007)**:
   * El test no tiene nota eliminatoria; su propósito es emitir indicadores de perfil para el `Gestor`.

---

## 🔗 Referencias

* [Diagrama de Estados de Test](/RUP/00-modelo-del-dominio/estados-entidades/test-estados.puml)
* [ADR-007: Admisión continua y batería de 3 tests](/RUP/BITACORA.md#adr-007-admisi%C3%B3n-continua-por-ciclos-acad%C3%A9micos-bater%C3%ADa-de-3-tests-e-inclusi%C3%B3n-de-entrevista)
