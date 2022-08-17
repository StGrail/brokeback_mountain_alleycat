import os

from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv('DEBUG', False)
BOT_TOKEN = os.getenv('BOT_TOKEN', 'BOT_TOKEN_DEV')
API_URL = os.getenv('API_URL', '') if not DEBUG else 'http://127.0.0.1:8000/api/'
API_AUTH_USER = os.getenv('API_AUTH_USER', '')
API_AUTH_PASSWORD = os.getenv('API_AUTH_PASSWORD', '')

MY_TG_ID = os.getenv('MY_TG_ID')
