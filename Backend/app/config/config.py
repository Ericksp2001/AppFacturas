import os

class Config:
    OLLAMA_URL = os.getenv("OLLAMA_URL")
    MODEL_NAME = os.getenv("DEEPSEEK_MODEL")
    HOST = os.getenv("HOST")
    PORT = int(os.getenv("PORT"))