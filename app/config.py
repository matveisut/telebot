from dotenv import load_dotenv
import os

load_dotenv()  # Загружает переменные из .env

BOT_TOKEN = os.getenv("BOT_TOKEN")
gemini_api = os.getenv("gemini_api")
PG_LINK = os.getenv("PG_LINK")
ROOT_PASS = os.getenv("ROOT_PASS")
