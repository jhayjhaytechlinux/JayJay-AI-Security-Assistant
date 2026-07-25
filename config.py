import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Telegram
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
AUTHORIZED_USERS = os.getenv("AUTHORIZED_USERS", "").split(",")

# AI Provider
AI_PROVIDER = os.getenv("AI_PROVIDER", "ollama").lower()

# OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Ollama
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "phi3:mini")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434")
ENABLE_LIVE_CVE_LOOKUP = True
