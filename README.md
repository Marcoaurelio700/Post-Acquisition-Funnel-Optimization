# Análisis de la Eficiencia Post-Adquisición y Lealtad

## Resumen Ejecutivo y Conclusiones de Negocio 

Este estudio del flujo post-adquisición es crítico, ya que revela que el valor potencial se fuga en **dos etapas críticas** que requieren acciones inmediatas y coordinadas entre Operaciones y Marketing.

1. **Alto Riesgo Operativo (Fuga por Cancelación):** Se identifica una **tasa de cancelación o fallo de pedidos del 16.5%**, lo que implica la pérdida de **3,654 pedidos** ($22,190 - 18,536$). Esto genera costos operacionales y una mala experiencia de cliente.
2. **Desafío de la Lealtad:** Solo el **15.35%** de los clientes con pedidos netos completados ($18,536$) regresan para una segunda compra. El **84.65%** restante son compradores de una sola vez, limitando drásticamente el Valor de Vida del Cliente (CLV).

[**Resumen Ejecutivo**]()

**Recomendación:** Se debe priorizar un plan de acción dual: **1) Auditar y reducir las fallas operativas** que causan cancelaciones para mejorar la eficiencia y **2) Enfocar la inversión de marketing en la retención** para aumentar la base de Clientes Leales ($2,845$).

## Objetivo y Pregunta de Negocio

El objetivo principal es el **Análisis de Embudo Post-Adquisición** para medir y optimizar la retención de valor de los clientes existentes. Se busca identificar y cuantificar las dos mayores fuentes de pérdida de valor: las fricciones operativas que llevan a la cancelación y la baja conversión a la recompra (lealtad).

## Hallazgos Clave y Recomendaciones Estratégicas

El análisis se basó en el recuento de eventos transaccionales, creando cuatro etapas lógicas para cuantificar la eficiencia. La **Tasa de Conversión Paso a Paso del 15.35%** a clientes leales es el indicador más bajo, señalando la baja eficiencia de la estrategia de retención.

| Área | Conclusión de Negocio | Acciones Recomendadas (ROI Alto) | KPI de Éxito (Objetivo) |
|:---|:---|:---|:---|
| **Eficiencia Operativa** | La **Tasa de Cancelación del 16.5%** es una pérdida de valor directo y afecta la experiencia del cliente. | **Auditoría de Pagos/Inventario:** Implementar validaciones de *stock* en tiempo real antes de finalizar el pedido. | Reducir la Tasa de Cancelación del **16.5% al 10%**. |
| **Lealtad y Retención** | Solo el **15.35%** de los clientes completados vuelven a comprar. Se requiere un esfuerzo para mover a los clientes de 'primera compra' a 'leales'. | **Campaña de Segundo Envío Gratis:** Secuencia automatizada de *email marketing* con un incentivo buscando aumentar la tasa de lealtad. | Aumentar la Tasa de Conversión a Clientes Leales del **15.35% al 25%** en el primer trimestre. |

## Metodología y Entregables Técnicos

| Etapa | Cantidad Actual | Tasa Conversión Paso a Paso | Tasa Conversión Global | Definición de Negocio |
|:---|:---:|:---:|:---:|:---|
| **1. Clientes Únicos** | 4,372 | 23.59% | 100.00% | Base total de compradores identificados. |
| **2. Total de Pedidos (Bruto)** | 22,190 | 119.71% | 507.55% | Total de transacciones generadas (incluye cancelaciones). |
| **3. Pedidos Netos (Completados)** | 18,536 | 100.00% | 423.97% | Transacciones completadas sin ser canceladas. **Punto de Mayor Fuga Operativa**. |
| **4. Clientes Leales (2+ Compras Netas)** | 2,845 | **15.35%** | 65.07% | Clientes que han realizado al menos una recompra neta. **Foco de Retención**. |

El dashboard fue construido en Power BI para comunicar de forma visual y numérica los hallazgos (Mostrando la tasa de conversión paso a paso).

![(**Dashboard:**)]()

## Instrucciones de Reproducción

1.  **Entorno:** Se requiere Power BI Desktop para la visualización de datos de conversión.
2.  **Modelado:** El análisis se basa en **Medidas DAX** (Tasa Conversión Paso a Paso, Tasa Conversión Global) calculadas sobre el recuento de eventos transaccionales.
3.  **Implementación:** La implementación debe ser coordinada por los equipos de Operaciones, Desarrollo y Marketing, siguiendo los KPIs de éxito establecidos en las recomendaciones.