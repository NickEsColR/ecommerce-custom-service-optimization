# Selección de Componentes Clave del Sistema RAG

## 1. Modelo de Embedding

### 1.1 Alternativas Consideradas

Se identificaron dos categorías principales de modelos:

- **Modelos de código abierto (open source)**

- **Modelos propietarios**

### 1.2 Criterios de Evaluación

#### 1.2.1 Privacidad de Datos

Para el caso del chatbot de servicio al cliente, la información es principalmente pública, por lo que ambas opciones (modelos open source y propietarios) son viables desde la perspectiva de privacidad.

#### 1.2.2 Análisis de Costos

- **Modelos propietarios:** El costo depende de los precios por millón de tokens del modelo.
- **Modelos open source:** El costo está determinado por el poder de cómputo necesario para su ejecución, dependiendo del tamaño del modelo.

Considerando el contexto de la empresa, las opciones viables son modelos ligeros abiertos o modelos propietarios económicos. Dado que la documentación y los detalles de productos no cambian con frecuencia, el uso de un modelo propietario no resultaría tan costoso a largo plazo, además de ser una opción inicial mientras se adquiere el equipo necesario para ejecutar localmente.

### 1.3 Modelos Evaluados

Los modelos propuestos fueron:

**Modelos propietarios:**

- OpenAI text-embedding-3-small
- Cohere embed-multilingual-v3.0

**Modelos abiertos:**

- Jina-embeddings-v2-base-es
- Paraphrase-Multilingual-MiniLM
- Granite-embedding-107m-multilingual

Todos los modelos evaluados manejan adecuadamente el idioma español. El modelo Granite-embedding-107m-multilingual presenta el menor rendimiento de todas las opciones inicialmente presentadas.

### 1.4 Comparativa Técnica

En términos de precisión, destacan:

| Modelo | MTEB Score | Dimensionalidad | Contexto |
|--------|------------|-----------------|----------|
| Jina-embeddings-v2-base-es | 65.2 | 768 | 8k tokens |
| OpenAI text-embedding-3-small | 62.3 | 1536 | 8k tokens |

Pesé a que una mayor dimensionalidad implica capturar relaciones más complejas, el modelo de Jina tiene un mejor puntaje pese a generar embeddings más pequeños. Esto es un beneficio adicional, dado que consume menor espacio de almacenamiento y hace los cálculos de similitud más ligeros.

**Nota:** [En este enlace](https://devblogs.microsoft.com/azure-sql/embedding-models-and-dimensions-optimizing-the-performance-resource-usage-ratio/) se prueba la reducción de la dimensionalidad en text embedding 3 small y large perdiendo entre 1 y 3 puntos de MTEB.

### 1.5 Análisis de Costos Finalistas

**OpenAI text-embedding-3-small:**

- $0.02 USD por millón de tokens
- $0.01 USD por millón de tokens en lote

**Jina-embeddings-v2-base-es:**

- $0.05 USD por millón de tokens (vía API)
- Ejecución local: requiere al menos 1GB de memoria

### 1.6 Decisión Final

**Modelo seleccionado:** Jina-embeddings-v2-base-es (ejecución local)

**Justificación:**

- No requiere una máquina potente para su ejecución
- No requiere estrictamente de GPU (aunque un mejor equipo resultaría en una generación más rápida)
- Mejor relación costo-beneficio a largo plazo
- Mayor independencia tecnológica

**Opción secundaria:** OpenAI text-embedding-3-small (si no es posible configurar la ejecución en local y se necesita una implementación más rápida)

**Recomendación:** Se recomienda el modelo de Jina a largo plazo por sus ventajas operativas y económicas.

---

## 2. Base de Datos Vectorial

### 2.1 Categorías de Bases de Datos Vectoriales

Se identificaron cuatro categorías de bases de datos vectoriales:

1. **Bases de datos vectoriales puras:** Pinecone, Milvus, Weaviate
2. **Extensiones de bases de datos existentes:** pgvector, MongoDB Vector
3. **Centradas en desarrollo:** Chroma, FAISS
4. **Administradas por proveedores de nube:** OpenSearch, Elastic Bean

### 2.2 Análisis por Categoría

#### 2.2.1 Bases de Datos Vectoriales Puras

**Características:**

- Diseñadas exclusivamente para alojar vectores
- Altamente escalables
- Facilidad de uso variable según la base de datos específica
- Costos variados

**Consideraciones:**

- La implementación local puede ser costosa
- Requiere alta inversión inicial para garantizar escalabilidad

#### 2.2.2 Extensiones de Bases de Datos Existentes

**Características:**

- Ideales si se cuenta con bases de datos como PostgreSQL o MongoDB para almacenar otros datos de la empresa
- Reducen la curva de aprendizaje de implementación
- Disminuyen la complejidad de la arquitectura
- Mantienen los datos en un solo lugar
- Altamente escalables

**Consideraciones:**

- Los costos dependen del proveedor o de los recursos de computación para uso local

#### 2.2.3 Centradas en Desarrollo

**Características:**

- Excelentes para prototipos rápidos
- Facilidad de uso ligada completamente al lenguaje de programación
- En su mayoría se guardan en memoria (almacenamiento volátil)

**Consideraciones:**

- No tienen buena escalabilidad
- No recomendadas para producción

#### 2.2.4 Proveedores de Nube (Database as a Service)

**Características:**

- Altamente escalables
- Costos dependientes completamente del proveedor

**Consideraciones:**

- Pueden resultar más complejos de usar, requieren conocimientos del proveedor específico
- Buena opción si la infraestructura de la empresa ya está en un proveedor de nube que cuenta con base de datos vectorial, para mantener la arquitectura simple

### 2.3 Evaluación para EcoMarket

Para el caso de EcoMarket, se determinó que la mejor opción es una **base de datos vectorial pura**.

#### 2.3.1 Finalistas

**Pinecone:**

- Enfoque plug and play
- Mayor facilidad de uso
- Costo aceptable en el corto plazo

**Weaviate:**

- Más económico a largo plazo
- Posibilidad de despliegue local si se cuenta con el cómputo necesario

Ambas opciones son altamente escalables

### 2.4 Decisión Final

**Base de datos seleccionada:** Pinecone

**Justificación:**

- Permite tener el chatbot operativo lo más rápido posible
- Facilidad de implementación
- Escalabilidad probada
- Costo aceptable en el corto plazo

**Recomendación a futuro:** Se recomienda considerar la migración a Weaviate o a la extensión de la base de datos donde se aloja la información de los productos cuando sea posible, para optimizar costos a largo plazo.
