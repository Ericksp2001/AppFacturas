import httpx
from config import Config

async def generate_text(prompt: str, max_tokens: int = 256):
    """
    Envía una solicitud a Ollama para generar texto con DeepSeek R1 14B.

    :param prompt: Texto de entrada para el modelo.
    :param max_tokens: Número máximo de tokens a generar.
    :return: Respuesta del modelo en formato JSON.
    """
    payload = {
        "model": Config.MODEL_NAME,
        "prompt": prompt,
        "options": {
            "temperature": 0.7,
            "max_tokens": max_tokens
        }
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(Config.OLLAMA_URL, json=payload)
        response.raise_for_status()
        return response.json()
