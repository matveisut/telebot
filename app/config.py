from dotenv import load_dotenv
import os

load_dotenv()  # Загружает переменные из .env

BOT_TOKEN = os.getenv("BOT_TOKEN")
gemini_api = os.getenv("gemini_api")
DATABASE_URL = os.getenv("DATABASE_URL")
print(DATABASE_URL)