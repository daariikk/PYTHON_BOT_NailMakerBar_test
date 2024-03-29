import os

from dotenv import load_dotenv, find_dotenv
if not find_dotenv():
    exit("Переменные окружения не загружены, так как отсутствует файл .env")
else:
    load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_KEY = os.getenv("API_KEY")
DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("low", "Найти дешёвые услуги"),
    ('high', "Найти дорогие услуги"),
    ('custom', "Найти услугу по диапазону"),
    ('history', "Посмотреть историю запросов")
)