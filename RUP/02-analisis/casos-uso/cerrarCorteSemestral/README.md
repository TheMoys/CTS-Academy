<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [Fase 01: Requisitos](/RUP/01-requisitos/README.md) | [Fase 02: Análisis](/RUP/02-analisis/README.md) |
|:---:|:---:|:---:|:---:|

</div>

# Realización de Análisis: `cerrarCorteSemestral()`

Este documento formaliza la colaboración de análisis entre clases estereotipadas Boundary-Control-Entity (BCE) que realiza el caso de uso `cerrarCorteSemestral()`, permitiendo al Gestor formalizar la clausura administrativa de una convocatoria de admisión, congelando las evaluaciones activas, archivando por abandono las candidaturas inconclusas y consolidando el informe inmutable de métricas del ciclo.

---

## 1. Diagrama de Clases de Análisis (VOPC)

El diagrama de clases participantes (View of Participating Classes) delimita las fronteras de confirmación y generación de informes, el controlador de ciclo y las entidades afectadas por la congelación transaccional.

<div align="center">

| Diagrama de Clases de Análisis (VOPC) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/cerrarCorteSemestral/clasesAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](clasesAnalisis.puml)</i></sup> |

</div>

### Participantes y Estereotipos

| Clase | Estereotipo | Responsabilidad |
| :--- | :---: | :--- |
| **`Gestor`** | `<<actor>>` | Coordinador de admisiones autorizado para clausurar formalmente convocatorias. |
| **`DialogoCierreConvocatoria`** | `<<boundary>>` | Interfaz gráfica que muestra el balance preliminar y solicita la confirmación de clausura irrevocable. |
| **`GeneradorReportes`** | `<<boundary>>` | Componente de interfaz de salida encargado de emitir el documento PDF con el consolidado del ciclo. |
| **`GestorCiclosAcademicos`** | `<<control>>` | Controlador de lógica de negocio que orquesta la transición de estado, el bloqueo de pruebas y la generación del consolidado. |
| **`Gestor`** | `<<entity>>` | Perfil del usuario autenticado que autoriza la clausura. |
| **`Convocatoria`** | `<<entity>>` | Entidad del ciclo que transiciona de estado `ABIERTO` a `CERRADO`. |
| **`Candidato`** | `<<entity>>` | Expedientes de la cohorte evaluados o pendientes de conclusión. |
| **`Test`** | `<<entity>>` | Batería de pruebas diagnósticas que deben ser bloqueadas para evitar respuestas extemporáneas. |
| **`InformeCorte`** | `<<entity>>` | Registro estadístico consolidado e inmutable con las cifras finales de la convocatoria. |

---

## 2. Diagrama de Realización de Análisis (Secuencia BCE)

La interacción formaliza la comprobación de estado, el balance previo, la confirmación y la cascada de congelación de expedientes.

<div align="center">

| Diagrama de Realización de Análisis (Secuencia BCE) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/cerrarCorteSemestral/realizacionAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](realizacionAnalisis.puml)</i></sup> |

</div>

### Flujo de Colaboración

1. El actor `Gestor` solicita el cierre de un corte semestral indicando la convocatoria de referencia.
2. `DialogoCierreConvocatoria` solicita a `GestorCiclosAcademicos` el balance preliminar de la cohorte.
3. El controlador comprueba con `Convocatoria` si el proceso continúa en estado `ABIERTO`. Si ya estuviera cerrada, aborta notificando el error correspondiente.
4. Con la convocatoria abierta, `GestorCiclosAcademicos` consulta a `Candidato` para computar postulantes evaluados, admitidos y pendientes, entregando el `BalanceCorteDTO`.
5. El diálogo presenta las cifras al Gestor y requiere confirmación explícita para el cierre irreversible.
6. Al confirmar la clausura, `GestorCiclosAcademicos` actualiza el estado de `Convocatoria` a `CERRADO` registrando el timestamp UTC exacto.
7. En estricto cumplimiento de **RN-CORTE-01**, el controlador envía la orden de bloqueo forzoso a las instancias de `Test` asociadas a candidatos de esa convocatoria que aún permanezcan en curso o no iniciadas.
8. Siguiendo **RN-CORTE-02**, el controlador identifica los expedientes en `Candidato` con etapas inconclusas y los actualiza al estado de archivo por abandono o vencimiento de plazo.
9. En aplicación de **RN-CORTE-03**, se calcula el consolidado final y se persiste la entidad inmutable `InformeCorte` con la tasa de ocupación de los 6 equipos de desarrollo CTS y la procedencia de los aspirantes.
10. Se presenta la confirmación del corte clausurado y se habilita la exportación del informe en formato PDF a través de `GeneradorReportes`.

---

## 3. Trazabilidad con Reglas de Negocio

- **RN-CORTE-01 (Bloqueo Definitivo de Tests de Admisión):** Al clausurar la convocatoria, se invalida de forma inmediata cualquier intento de inicio o envío de respuestas en la batería diagnóstica para toda la cohorte.
- **RN-CORTE-02 (Archivo Automático por Abandono):** Las postulaciones que no hubiesen concluido todas sus fases evaluativas o entrevistas al momento de ejecutarse el cierre formal son transicionadas a causal de abandono.
- **RN-CORTE-03 (Consolidación de Métricas Anuales):** El sistema genera un registro agregado inmutable (`InformeCorte`) con las estadísticas definitivas de admisión por equipo y sede para la memoria académica anual.

---

<div align="center">

[Volver al Índice de la Fase 02: Análisis](/RUP/02-analisis/README.md)

</div>
