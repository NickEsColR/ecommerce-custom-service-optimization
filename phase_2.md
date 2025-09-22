# Evaluación de Fortalezas, Limitaciones y Riesgos Éticos

## 🦾 Fortalezas

- Disponibilidad 24/7
- Reducción del tiempo de respuesta
- Manejo de las consultas repetitivas (aprox. 80%)
- Mejora en la experiencia de usuario
- Aumento en la retención de usuarios
- Posible aumento en las ventas

## ⛔ Limitaciones

- No responder preguntas complejas o que requieren empatía (aprox 20%)
- Dar respuestas limitadas como estado exacto del pedido si no se puede obtener información
- No responder preguntas sobre inventario de productos
- Estar desactualizado en las últimas reseñas de un producto
- Respuestas incorrectas si la recuperación falla o la base de datos tiene información incorrecta

## ✳️ Riesgos Éticos

### 💡 Alucionaciones

Con el uso de **RAG** es poco probable que se presenten alucinaciones. Sin embargo, es posible que sucedan en casos donde no encuentre documentos relacionados o mal interprete el contexto adicional que se proporciona. Es vital no depender exclusivamente de las respuestas del modelo, en especial en casos complejos que requieran una intervención humana. También se deben considerar ataques de inyección de prompts que puedan generar respuestas falsas.

### ⋆⭒˚.⋆ Sesgo

En un principio no se esperan problemas de sesgo considerando que los datos proporcionados son únicamente sobre los productos ofrecidos y documentación sobre el proceso de venta, atención y envió. A pesar de esto, se debe mantener un monitoreo frecuente frente a todo tipo de preguntas; por ejemplo, preguntar por productos cuidado capilar resalte productos femeninos sin conocer información adicional del cliente.

Dado que se implementa una arquitectura **RAG** no que preocuparse por sesgar el entrenamiento, solo garantizar que las descripciones de los productos u otros datos sean generales y claros. Ademmás, de validar que las instrucciones del modelo ayuden a evitar casos extremos donde una sobre carga de un tipo de producto para un público especifico genere respuestas sesgadas. 

### 🔒 Privacidad de datos

- Garantizar que el modelo proveido por un tercero no use los datos para su entrenamiento. 
- Asegurarse de omitir información sensible o innecesaria del cliente como parte del contexto.
- Ofuscar datos de los clientes al guardar conversaciones para monitoreo.
- Garantizar que el modelo no pueda mostrar información de ningún cliente en las conversaciones.

### 🧍 Impacto laboral

La intención es permitir atender un mayor número de casos en menos tiempo, enfocandose en casos complejos en lugar de preguntas sencillas. De esta forma los agentes de servicio al cliente pueden poner su esfuerzo en problemas que requieran un toque humano. Con esto se reduce la carga a los agentes a la vez que se mejora la percepción del servicio al cliente de la empresa. Por tanto, el sistema no remplazaria a los agentes existentes, los empoderaría.
