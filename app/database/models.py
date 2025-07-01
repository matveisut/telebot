import sys
import os

# Получаем абсолютный путь к родительской папке
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Добавляем родительскую папку в sys.path
sys.path.append(parent_dir)

# Теперь можно импортировать модуль из родительской папки
import app.config as config
from asyncpg_lite import DatabaseManager

pg_manager = DatabaseManager(dsn=config.PG_LINK, deletion_password=config.ROOT_PASS)