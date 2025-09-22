import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

from color_print import ColorPrint, Color

# Cargar variables de entorno desde el archivo .env
load_dotenv()

INSTRUCT_BASICO = """
    Responde basado en la siguiente información de pedidos de clientes en una tienda de comercio electrónico.
    {contexto}
"""

INSTRUCT_MEJORADO = """
    Actúa como un agente de servicio al cliente amable y servicial. Utiliza la siguiente información de pedidos de clientes en una tienda de comercio electrónico para responder a las consultas de los clientes. Si no sabes la respuesta, di que no lo sabes en lugar de inventar una respuesta. Incluye una estimación del tiempo de entrega si es relevante y un enlace de rastreo si el estado es enviado.
    {contexto}
    """

INSTRUCT_DEVOLUCION = """
    Eres un agente de servicio al cliente que maneja solicitudes de devolución.
    Si el pedido es elegible para devolución, proporciona las instrucciones necesarias. Si no es elegible, explica amablemente el motivo.
    ## Política de devoluciones:
    - Los pedidos pueden devolverse dentro de los 30 días posteriores a la entrega.
    - Los artículos deben estar en su estado original y sin usar.
    - Los artículos en oferta no son elegibles para devolución.
    - Los reembolsos se procesan dentro de los 5-7 días hábiles posteriores a la recepción del artículo devuelto.
    - Los artículos personalizados no son elegibles para devolución.
    - Los productos perecederos o de higiene no son elegibles para devolución.
"""


def init_client():
    """Inicializa el cliente de Azure OpenAI.

    Returns:
        ChatCompletionsClient: Cliente de Azure OpenAI.
    """
    endpoint = "https://models.github.ai/inference"
    token = os.environ["GITHUB_TOKEN"]
    print(token)
    return ChatCompletionsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(token),
    )


def obtener_respuesta(client, model: str, messages: list[SystemMessage | UserMessage]):
    """Obtiene una respuesta del modelo de lenguaje.

    Args:
        client (ChatCompletionsClient): Cliente de Azure OpenAI.
        model (str): Nombre del modelo a utilizar.
        messages (list[SystemMessage | UserMessage]): Mensajes para enviar al modelo.

    Returns:
        str: Respuesta generada por el modelo.
    """
    response = client.complete(
        model=model,
        messages=messages,
        temperature=0.4,
        max_tokens=1000,
    )
    return response.choices[0].message.content


def mostrar_respuesta_basica(
    client, contexto: str, model: str = "mistral-ai/mistral-medium-2505"
):
    """Muestra una respuesta básica del modelo.

    Args:
        client (ChatCompletionsClient): Cliente de Azure OpenAI.
        contexto (str): Contexto para la consulta.
        model (str, optional): Nombre del modelo a utilizar. Defaults to "mistral-ai/mistral-medium-2505".
    """
    messages = [
        SystemMessage(content=INSTRUCT_BASICO.format(contexto=contexto)),
        UserMessage(content="Dame el estado del pedido PED001"),
    ]
    print(obtener_respuesta(client, model, messages))


def mostrar_respuesta_mejorada(
    client, contexto: str, model: str = "mistral-ai/mistral-medium-2505"
):
    """Muestra una respuesta mejorada del modelo.

    Args:
        client (ChatCompletionsClient): Cliente de Azure OpenAI.
        contexto (str): Contexto para la consulta.
        model (str, optional): Nombre del modelo a utilizar. Defaults to "mistral-ai/mistral-medium-2505".
    """
    messages = [
        SystemMessage(content=INSTRUCT_MEJORADO.format(contexto=contexto)),
        UserMessage(
            content="proporciona el estado actual del pedido con el número de seguimiento PED001"
        ),
    ]
    print(obtener_respuesta(client, model, messages))


def mostrar_respuesta_mejorada_envio(
    client, contexto: str, model: str = "mistral-ai/mistral-medium-2505"
):
    """Muestra una respuesta mejorada del modelo.

    Args:
        client (ChatCompletionsClient): Cliente de Azure OpenAI.
        contexto (str): Contexto para la consulta.
        model (str, optional): Nombre del modelo a utilizar. Defaults to "mistral-ai/mistral-medium-2505".
    """
    messages = [
        SystemMessage(content=INSTRUCT_MEJORADO.format(contexto=contexto)),
        UserMessage(content="¿cual es el estado del pedido PED003?"),
    ]
    print(obtener_respuesta(client, model, messages))


def mostrar_respuesta_devolucion_producto_no_elegible(
    client, model: str = "mistral-ai/mistral-medium-2505"
):
    """Muestra una respuesta del modelo para un producto no elegible para devolución.

    Args:
        client (ChatCompletionsClient): Cliente de Azure OpenAI.
        model (str, optional): Nombre del modelo a utilizar. Defaults to "mistral-ai/mistral-medium-2505".
    """
    messages = [
        SystemMessage(content=INSTRUCT_DEVOLUCION),
        UserMessage(
            content="Las galletas que me mandaron tienen maní y soy alérgico ¿Como puedo devolver el producto?"
        ),
    ]
    print(obtener_respuesta(client, model, messages))


def mostrar_respuesta_devolucion_producto_elegible(
    client, model: str = "mistral-ai/mistral-medium-2505"
):
    """Muestra una respuesta del modelo para un producto elegible para devolución.

    Args:
        client (ChatCompletionsClient): Cliente de Azure OpenAI.
        model (str, optional): Nombre del modelo a utilizar. Defaults to "mistral-ai/mistral-medium-2505".
    """
    messages = [
        SystemMessage(content=INSTRUCT_DEVOLUCION),
        UserMessage(
            content="El carro de juguete está dañado, ¿Como puedo devolver el producto?"
        ),
    ]
    print(obtener_respuesta(client, model, messages))


def mostrar_respuesta_devolucion_productos(
    client, model: str = "mistral-ai/mistral-medium-2505"
):
    """Muestra una respuesta del modelo para productos elegibles y no elegibles para devolución.

    Args:
        client (ChatCompletionsClient): Cliente de Azure OpenAI.
        model (str, optional): Nombre del modelo a utilizar. Defaults to "mistral-ai/mistral-medium-2505".
    """
    messages = [
        SystemMessage(content=INSTRUCT_DEVOLUCION),
        UserMessage(
            content="Ya no quiero los productos que pedí, la crema dental contiene alcohol, el cepillo tienen cerdas duras, las camisas son muy grandes, el frijol es rojo y pense que era verde, el detergente es muy fuerte, la leche no es descremada. ¿Como puedo devolver los productos?"
        ),
    ]
    print(obtener_respuesta(client, model, messages))


def leer_pedidos():
    """
    Lee el archivo pedidos.txt y devuelve su contenido como string
    """
    try:
        with open("pedidos.txt", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "Error: No se encontró el archivo pedidos.txt"
    except Exception as e:
        return f"Error al leer el archivo: {str(e)}"


def main():
    model = "mistral-ai/mistral-medium-2505"
    contenido_pedidos = leer_pedidos()
    client = init_client()
    ColorPrint.print_colored("Respuesta del prompt básico:", Color.GREEN)
    mostrar_respuesta_basica(client, contenido_pedidos, model)
    ColorPrint.print_colored("Respuesta del prompt mejorado:", Color.BLUE)
    mostrar_respuesta_mejorada(client, contenido_pedidos, model)
    ColorPrint.print_colored(
        "Respuesta del prompt mejorado con pedido en envío:", Color.CYAN
    )
    mostrar_respuesta_mejorada_envio(client, contenido_pedidos, model)
    ColorPrint.print_colored(
        "Respuesta de devolución de producto no elegible:", Color.RED
    )
    mostrar_respuesta_devolucion_producto_no_elegible(client, model)
    ColorPrint.print_colored(
        "Respuesta de devolución de producto elegible:", Color.YELLOW
    )
    mostrar_respuesta_devolucion_producto_elegible(client, model)
    ColorPrint.print_colored("Respuesta de devolución de productos:", Color.MAGENTA)
    mostrar_respuesta_devolucion_productos(client, model)


if __name__ == "__main__":
    main()
