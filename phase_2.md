# Creación de la Base de Conocimiento de Documentos

## 1. Identificación de Documentos

Se han identificado las siguientes fuentes de datos para el sistema:

### 1.1 Documentos PDF

Contienen información estructurada sobre:

- Políticas de devolución
- Políticas de envío
- Métodos de pago
- Garantías
- Información básica de productos

### 1.2 Base de Datos Relacional

Almacena:

- Información detallada de productos
- Inventario de productos
- Estado de pedidos

### 1.3 Archivos JSON

Incluyen:

- Preguntas frecuentes (FAQ)
- Estado de pedidos
- Conversaciones anteriores

### 1.4 Base de Datos NoSQL

Contiene:

- Historial de conversaciones con servicio al cliente

---

## 2. Estrategias de Segmentación

### 2.1 Segmentación Basada en Estructura del Documento

**Aplicable a:**

- Todos los documentos PDF
- Información e inventario de productos

**Justificación:**

Esta estrategia es ideal porque los documentos están altamente estructurados, lo que permite:

- Preservar la jerarquía del contenido
- Mantener la organización lógica de la información
- Generar contextos que cubren correctamente todas las opciones sin omitir información

**Ejemplos de aplicación:**

- Todos los métodos de pago
- Todas las políticas de devolución
- Especificaciones completas de productos

### 2.2 Segmentación por Contenido

**Aplicable a:**

- Preguntas frecuentes
- Histórico de conversaciones

#### 2.2.1 Estrategias consideradas

**Segmentación Dependiente del Contenido (Recomendada):**

- Asegura que cada pregunta y respuesta sea un contexto completo
- Mantiene la integridad de la información
- Facilita la recuperación precisa de información

**Segmentación por Párrafos:**

- Útil para separar cada pregunta
- Las preguntas generalmente no son muy largas
- Por lo general cubren diferentes temáticas

**Segmentación Semántica:**

- Aplicable cuando existen preguntas relacionadas entre sí
- Permite agrupar contenido temáticamente similar

**Consideración importante:**
Se debe validar que ninguna pregunta supere el límite de tokens del modelo de embedding seleccionado.

---

## 3. Proceso de Indexación

### 3.1 Pipeline de Indexación

El proceso de indexación sigue los siguientes pasos:

1. **Segmentación de documentos** utilizando las estrategias definidas en la sección 2, preservando la metadata de cada chunk (fuente, fecha, sección) y el contexto del documento original
2. **Generación de embeddings** mediante el modelo de embeddings seleccionado
3. **Carga en la base de datos vectorial** para su almacenamiento y posterior recuperación. Los vectores se actualizan si ya existen en la base de datos

### 3.2 Flujo de Trabajo

```text
Documentos → Segmentación → Modelo de Embeddings → Base de Datos Vectorial
```

Este proceso garantiza que toda la información esté correctamente procesada, vectorizada y disponible para consultas eficientes del sistema de chatbot.
