<div align=right>

<sub>[Al inicio](/README.md) / [Bitácora RUP](/RUP/BITACORA.md) / [Modelo del dominio](/RUP/00-modelo-del-dominio/README.md) / [Actores y casos de uso](/RUP/01-requisitos/01-actores-casos-uso/README.md) / [Detalle de casos de uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) / **responderPreguntaTeorica()**</sub>

</div>

# Caso de Uso: `responderPreguntaTeorica()`

> | [Inicio](/README.md) | [Diagrama de Contexto Candidato](/images/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoCandidato.svg) | [Diagrama de Contexto Alumno](/images/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoAlumno.svg) | **Detalle** | [Análisis](/RUP/02-analisis/README.md) | [Diseño](/RUP/03-diseño/README.md) |
> | :-: | :-: | :-: | :-: | :-: | :-: |

<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/responderPreguntaTeorica/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/responderPreguntaTeorica/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## 📋 Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `Candidato` (admisión en `TestActitud`, `TestAptitud` o `TestTecnico`), `Alumno` (evaluación continua o test de nivelación de fin de módulo formativo) |
| **Objetivo** | Registrar la opción de respuesta seleccionada por el evaluado para un ítem teórico de opción múltiple, validando la vigencia del tiempo en el servidor y aplicando las restricciones de mutabilidad e integridad según la modalidad de prueba |
| **Tipo** | Primario, esencial |
| **Nivel** | Objetivo de usuario |
| **Precondición** | El actor debe estar autenticado; el test evaluado debe encontrarse en estado `EN_CURSO` (`TEST_EN_EJECUCION`); el cronómetro en servidor debe tener tiempo remanente (`tiempoRestante > 0`); el reactivo presentado debe pertenecer al test activo |
| **Postcondición Éxito** | La respuesta queda persistida atómicamente en servidor con timestamp y metadatos de auditoría; el estado del reactivo se actualiza a respondido; se presenta el siguiente reactivo disponible; la sesión permanece en `TEST_EN_EJECUCION` |
| **Postcondición Fallo** | - Si el cronómetro en servidor expiró (`tiempoRestante <= 0`), la respuesta es rechazada atómicamente y el sistema notifica la finalización del tiempo límite, requiriendo la consolidación del test (`finalizarTest()`).<br>- Si se intenta modificar un reactivo en un `TestActitud` (psicométrico Likert) previamente consolidado, el sistema bloquea la alteración emitiendo mensaje de inmutabilidad y mantiene la respuesta original. |

</div>

---

## 📑 Reglas de Negocio Asociadas

1. **RN-EVAL-01 — Cronómetro Servidor como Fuente de Verdad**:
   * El tiempo restante se calcula y audita exclusivamente en el servidor (`MotorEvaluacion`). Las marcas de tiempo del cliente frontend no se aceptan para validar la entrega. Si la petición de respuesta ingresa con el cronómetro de sesión agotado, se rechaza y no se computa.
2. **RN-EVAL-02 — Inmutabilidad Psicométrica (`TestActitud`)**:
   * Los tests de actitud (escalas Likert diagnósticas) operan con navegación lineal e irreversible. Una vez que el candidato selecciona y registra una respuesta, esta queda fijada como inmutable para evitar sesgos de deseabilidad social, sobre-racionalización o adulteración del perfil psicológico.
3. **RN-EVAL-03 — Navegación Libre y Guardado Atómico (`TestTecnico` y `TestAptitud`)**:
   * En evaluaciones técnicas y psicotécnicas/lógicas, el evaluado puede navegar libremente entre preguntas, dejar ítems temporalmente pendientes y modificar sus respuestas previas mientras la evaluación continúe activa y con tiempo disponible. Cada guardado es una transacción atómica inmediata que protege contra caídas de red o recargas involuntarias del navegador.
4. **RN-EVAL-04 — Telemetría y Detección de Fugas / Antifraude**:
   * Cada registro de respuesta consolida marcas temporales (latencia de resolución por reactivo y número de rectificaciones). Una tasa anómala de respuestas instantáneas o cambios erráticos es registrada como indicador de riesgo para la revisión cualitativa del `Gestor`.

---

## 🔗 Referencias

* [Modelo del Dominio: `Test`, `PreguntaTeorica`, `Resultado`](/RUP/00-modelo-del-dominio/README.md)
* [Diagrama de Estados de Test (`PENDIENTE` → `EN_CURSO` → `ENTREGADO` / `EXPIRADO`)](/RUP/00-modelo-del-dominio/estados-entidades/test-estados.puml)
* [Diagrama de Contexto Candidato](/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoCandidato.puml)
* [ADR-007: Admisión continua y batería de 3 tests diagnósticos](/RUP/BITACORA.md#adr-007-admisi%C3%B3n-continua-por-ciclos-acad%C3%A9micos-bater%C3%ADa-de-3-tests-e-inclusi%C3%B3n-de-entrevista)
