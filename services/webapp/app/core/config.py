import os

from fastapi.templating import Jinja2Templates

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "localhost")

DB_URL = os.getenv("DB_URL", "")

templates = Jinja2Templates(directory="app/templates")