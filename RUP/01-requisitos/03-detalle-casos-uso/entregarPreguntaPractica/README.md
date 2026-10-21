<div align="center">

| [🏠 Inicio](/README.md) | [📖 RUP Hub](/RUP/README.md) | [🏛️ 00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [📋 01 Requisitos](/RUP/01-requisitos/README.md) | [👥 Actores y Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md) | [📋 Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

<sub>**Fase 01 Requisitos** › **Detalle de Caso de Uso** › `entregarPreguntaPractica()`</sub>

</div>

# Caso de Uso: `entregarPreguntaPractica()`


<div align=center>

| Especificación del Caso de Uso |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/entregarPreguntaPractica/especificacion.svg) |
| <sup><i>[Código fuente PlantUML](especificacion.puml)</i></sup> |

| Wireframe de la Interfaz |
| :---: |
| ![](/images/RUP/01-requisitos/03-detalle-casos-uso/entregarPreguntaPractica/wireframes.svg) |
| <sup><i>[Código fuente PlantUML](wireframes.puml)</i></sup> |

</div>

---

## 📋 Información del Caso de Uso

<div align=center>

| Atributo | Valor |
| :--- | :--- |
| **Actores** | `Candidato` (admisión en `Tecnico`), `Alumno` (evaluación continua o test de nivelación técnica en `MotorFormacion`) |
| **Objetivo** | Formalizar la entrega de la solución de código a un reto práctico (`Practica`), permitiendo ejecuciones de validación en contenedor seguro Docker (`TestRunner`) y persistiendo versiones consolidadas para la evaluación cualitativa por rúbrica del Tech Leader |
| **Tipo** | Primario, esencial |
| **Nivel** | Objetivo de usuario |
| **Precondición** | El actor debe estar autenticado; el test técnico debe encontrarse en estado `EN_CURSO` (`TEST_EN_EJECUCION`); el cronómetro en servidor debe tener tiempo disponible (`tiempoRestante > 0`); el reactivo seleccionado debe ser de tipo práctico |
| **Postcondición Éxito** | La solución de código queda persistida con identificador de versión, marcas temporales y telemetría; si hay cuota de sandbox disponible se ejecuta la suite automatizada en `TestRunner` y se presentan los resultados; la sesión permanece en `TEST_EN_EJECUCION` |
| **Postcondición Fallo** | - Si el cronómetro en servidor expiró sin ventana de gracia, el sistema rechaza la nueva entrega, consolida automáticamente el último borrador guardado en segundo plano y notifica el fin de la prueba.<br>- Si el código introducido coincide al 100% con la plantilla inicial o está vacío, el sistema emite una advertencia de contenido no modificado y mantiene la edición. |

</div>

---

## 📑 Reglas de Negocio Asociadas

1. **RN-EVAL-PRACT-01 — Editor Integrado y Autoguardado Silencioso**:
   * La vía canónica de resolución es el editor web multi-archivo integrado. Para prevenir pérdidas de trabajo ante desconexiones fortuitas o refrescos de página, el cliente realiza un autoguardado en segundo plano (*background draft*) cada 30 segundos, manteniendo un snapshot sincronizado en servidor.
2. **RN-EVAL-PRACT-02 — Cuota y Cooldown de Sandbox Docker (`TestRunner`)**:
   * Para evitar saturación o ataques de denegación de servicio (DoS) contra los workers de Docker, cada candidato dispone de un cupo máximo de **5 ejecuciones automatizadas de prueba** por reto práctico (o un cooldown de 90 segundos entre ejecuciones). Al agotar la cuota, el candidato puede seguir entregando versiones, pero estas se evaluarán directamente en diferido mediante la rúbrica del `LiderEquipo`.
3. **RN-EVAL-PRACT-03 — Versionado de Intentos y Mutabilidad en Tiempo de Examen**:
   * Mientras el test se encuentre en `TEST_EN_EJECUCION` y con tiempo remanente, el evaluado puede entregar nuevas versiones de su código. Cada entrega genera un nuevo registro versionado (`version 1`, `version 2`...), siendo la última versión entregada la que se consolida al cerrar la evaluación.
4. **RN-EVAL-PRACT-04 — Tolerancia de Red y Ventana de Gracia**:
   * Se concede una tolerancia técnica de 60 segundos tras el vencimiento formal del temporizador exclusivamente para completar peticiones HTTP de entrega que se hayan originado antes de llegar al segundo cero.

---

## 🔗 Referencias

* [Modelo del Dominio: `Tecnico`, `Practica`, `Modulo`](/RUP/00-modelo-del-dominio/README.md)
* [Diagrama de Estados de Test (`EN_CURSO` → `ENTREGADO` / `EXPIRADO`)](/RUP/00-modelo-del-dominio/estados-entidades/test-estados.puml)
* [Diagrama de Contexto Candidato](/RUP/01-requisitos/01-actores-casos-uso/diagramaContextoCandidato.puml)
* [ADR-007: Admisión continua y batería de 3 tests diagnósticos](/RUP/BITACORA.md#adr-007-admisi%C3%B3n-continua-por-ciclos-acad%C3%A9micos-bater%C3%ADa-de-3-tests-e-inclusi%C3%B3n-de-entrevista)
---

<div align="center">

[⬅️ Volver al Catálogo de Casos de Uso](/RUP/01-requisitos/03-detalle-casos-uso/README.md) • [👥 Ver Diagramas de Contexto](/RUP/01-requisitos/01-actores-casos-uso/README.md)

</div>
