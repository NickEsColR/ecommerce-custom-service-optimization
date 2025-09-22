# Selección y Justificación del Modelo de IA

## 🎯 1. Descripción General y Objetivos Técnicos

Asistente de IA (chatbot) para el sitio web de EcoMarket.

- **Objetivo Principal:** Automatizar la respuesta a consultas frecuentes de clientes sobre productos, políticas y estado de pedidos.

- **Meta Técnica:** Desarrollar un servicio de backend robusto y de baja latencia que se conecte a un modelo de lenguaje grande (LLM) para generar respuestas precisas y contextualizadas.

## 🛠️ 2. Stack Tecnológico y Selección de Modelo

### Modelo de IA Generativa

**Modelo:** Gemini 2.5 Flash lite

**Proveedor:** Google (a través de la API de Vertex AI)

#### ¿Por qué este modelo?

- ⚡ **Velocidad:** Está optimizado para casos de uso de chat. El objetivo es una latencia de respuesta de extremo a extremo *< 2 segundos*.

- 💰 **Costo:** El modelo de pago por uso es ideal para el presupuesto operativo (OpEx) y evita grandes costos iniciales (CapEx). Dado que no se cuenta con servidores propios y los expertos necesarios para administrar un proveedor en la nube sobre el cual desplegar el modelo.

- 🧠 **Ventana de Contexto de 1M de Tokens:** Permite usar una arquitectura *RAG* de forma muy simple y potente, metiendo documentos enteros en el *prompt* en lugar de aplicar estrategias complejas de *chunking* (división de texto).

- 🔒 **Privacidad:** La política de Google para esta API garantiza que nuestros datos (consultas de clientes, info de productos) no se usarán para reentrenar sus modelos.

- ⚠️ **Decisión clave:** El **fine-tuning* es caro, lento y requiere un dataset masivo. Para garantizar un uso adecuado de los recursos de la empresa se dejara como un posible trabajo futuro en caso de ser requerido una mejora en la experiencia de uso. La arquitectura RAG con un modelo grande como *Gemini 2.5  flash lite* resulta más pertinente, dado en parte a que el modelo ya a sido previamente entrenado con una gran variaedad de casos, incluyendo el de preguntas y respuestas. Por lo tanto, es suficiente con darle el contexto y las instrucciones adecuadas para que responda de la forma adecuada.

## 🏗️ 3. Arquitectura del Sistema: Retrieval-Augmented Generation (RAG)

El cerebro de nuestro asistente es un flujo RAG. Esto asegura que el modelo responda basándose únicamente en la información de EcoMarket y no invente datos ("alucinaciones").

- 🗨️ **Preguntas básicas:** El usuario generalmente realiza preguntas básicas que pueden ser fácilmente respondidas con los documentos de la empresa. El sistema RAG permite encontrar la información adecuada para dar contexto al modelo y generar la respuesta apropiada.

- ℹ️ **Información del producto:** De la misma forma que las preguntas relacionadas a la operación del negocio, la información de los productos también deben hacer parte del espacio de búsqueda. De esta forma cualquier duda con respecto al producto en el que el cliente esta interesado se responderia rápidamente, asegurando en mayor medida una compra potencial.

- 📦 **Estado del pedido:** Se puede actualizar frecuentemente una base de datos con el estado de los pedidos, estos serían obtenidos en la recuperación para preguntas relacionadas. Sin embargo, pueden no estar completamente actualizados en todo momento, esto puede requierir un gran esfuerzo adicional, en especial si algún detalle en especifico se obtiene por un tercero (como la ubicación exacta si el envío lo realizza una empresa especializada)

## 📈 4. Escalabilidad

Al ser un servicio gestionado por Google, la infraestructura subyacente está diseñada para escalar automáticamente a niveles de demanda masivos. Las únicas limitaciones son los límites de tasa de la API (rate limits), que pueden ser aumentados según el plan contratado con el proveedor. La latencia se mantiene consistentemente baja incluso a gran escala. También es posible ampliar en un futuro el acceso a información de tiempo real del estado de un pedido por medio de *MCP*.

## 🧩 Facilidad de integración

Se integra a través de una API REST estándar, compatible con cualquier stack tecnológico moderno. Google proporciona robustos SDKs (Software Development Kits) para lenguajes populares como Python, Node.js y Go, junto con documentación extensa y herramientas como Google AI Studio para un prototipado rápido.
