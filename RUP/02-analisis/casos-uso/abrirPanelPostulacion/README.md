<div align="center">

| [Inicio](/README.md) | [RUP Hub](/RUP/README.md) | [00 Dominio](/RUP/00-modelo-del-dominio/README.md) | [01 Requisitos](/RUP/01-requisitos/README.md) | [02 Análisis](/RUP/02-analisis/README.md) | [Catálogo Requisitos](/RUP/01-requisitos/03-detalle-casos-uso/README.md) |
|:---:|:---:|:---:|:---:|:---:|:---:|

<sub>**Fase 02 Análisis** › **Realización de Casos de Uso** › `abrirPanelPostulacion()`</sub>

</div>

# Realización de Caso de Uso: `abrirPanelPostulacion()`

Esta especificación formaliza la realización de análisis del caso de uso `abrirPanelPostulacion()` mediante clases Boundary-Control-Entity (BCE), estableciendo la reconciliación pasiva del reloj de servidor, la opacidad procesal de indicadores y el bloqueo cruzado de concurrencia.

---

<div align=center>

| Diagrama de Clases de Análisis (VOPC) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/abrirPanelPostulacion/clasesAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](clasesAnalisis.puml)</i></sup> |

| Diagrama de Realización de Análisis (Secuencia BCE) |
| :---: |
| ![](/images/RUP/02-analisis/casos-uso/abrirPanelPostulacion/realizacionAnalisis.svg) |
| <sup><i>[Código fuente PlantUML](realizacionAnalisis.puml)</i></sup> |

</div>

---

## Clases de Análisis Participantes

<div align=center>

| Clase | Estereotipo | Tipo | Responsabilidad Principal |
| :--- | :---: | :---: | :--- |
| **`PanelPostulacion`** | `<<boundary>>` | Frontera | Visualización del expediente del candidato, fechas de convocatoria, estado procesal de la batería de 3 tests y deshabilitación selectiva de controles ante concurrencia o vencimiento. |
| **`GestorPostulacion`** | `<<control>>` | Control | Orquestación de la carga del expediente, verificación de vigencia de convocatoria, reconciliación pasiva de temporizadores en backend y aplicación de la política de bloqueo concurrente. |
| **`Candidato`** | `<<entity>>` | Entidad | Identidad evaluada en proceso de admisión; vincula la convocatoria activa y las 3 instancias evaluativas (`Actitud`, `Aptitud`, `Tecnico`). |
| **`Convocatoria`** | `<<entity>>` | Entidad | Ciclo académico y periodo semestral de postulación; custodia las fechas límite de recepción de pruebas. |
| **`Test`** | `<<entity>>` | Entidad | Instrumento evaluativo individual; evalúa el tiempo restante en servidor (`calcularTiempoRestanteServidor()`) y transiciona a expirado si se consumió el plazo. |

</div>

---

## Flujo de Realización (Colaboración BCE)

### Flujo Principal: Acceso con Convocatoria Vigente y Tests Disponibles
1. El **`Candidato`** accede al panel principal de su postulación.
2. **`PanelPostulacion`** solicita la carga inicial a **`GestorPostulacion`**.
3. **`GestorPostulacion`** consulta la **`Convocatoria`** asociada al candidato y comprueba `estaVigente()`.
4. Al estar vigente, **`GestorPostulacion`** recupera la batería de tests del **`Candidato`**.
5. **Reconciliación pasiva de servidor (RN-POST-04)**: Por cada test en estado `EN_CURSO`, se recalcula el tiempo remanente en el servidor. Si el tiempo expiró (`tiempoRestante <= 0`), la entidad transiciona de forma autónoma a `EXPIRADO`.
6. **Validación de bloqueo concurrente (RN-POST-01)**:
   - Si algún test permanece `EN_CURSO`, **`GestorPostulacion`** lo marca como activo, habilitando únicamente su botón de reanudación y bloqueando los tests pendientes restantes.
   - Si no hay tests en ejecución, los tests en estado `PENDIENTE` se presentan habilitados con orden flexible de realización (RN-POST-03).
7. **`PanelPostulacion`** renderiza los estados procesales sin revelar métricas ni puntuaciones (RN-POST-02 / ADR-007).

### Flujo Alternativo: Convocatoria Fuera de Plazo
1. Si `estaVigente()` retorna `false` (fecha límite superada):
   - **`GestorPostulacion`** emite los datos del panel marcados como `modoSoloLectura = true`.
   - **`PanelPostulacion`** deshabilita todos los controles de inicio y reanudación, notificando el cierre del plazo formal de postulación.

---

## Trazabilidad con la Fase de Requisitos

| Requisito / Artefacto Fase 01 | Realización en Fase 02 (Análisis) |
| :--- | :--- |
| **Caso de Uso `abrirPanelPostulacion()`** | Realización coordinada por `GestorPostulacion` conectando `PanelPostulacion` y `Candidato`. |
| **RN-POST-01 (Bloqueo Concurrente)** | Lógica de exclusión en `GestorPostulacion` al detectar un `Test` en `EN_CURSO`. |
| **RN-POST-02 (Opacidad de Indicadores)** | La frontera `PanelPostulacion` solo expone estados procesales discretos (`Pendiente`, `En curso`, `Completado`, `Expirado`). |
| **RN-POST-04 (Reconciliación de Cronómetros)** | Invocación de `calcularTiempoRestanteServidor()` y `marcarExpiradoPorServidor()` en la entidad `Test`. |

---

<div align="center">

[Volver a Fase 02: Análisis](/RUP/02-analisis/README.md) • [Ver Especificación de Requisitos (Fase 01)](/RUP/01-requisitos/03-detalle-casos-uso/abrirPanelPostulacion/README.md)

</div>
