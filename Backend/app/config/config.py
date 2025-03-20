import os

class config:
    MODEL_NAME = os.getenv("MODEL")
    HOST = os.getenv("HOST")
    PORT = int(os.getenv("PORT"))