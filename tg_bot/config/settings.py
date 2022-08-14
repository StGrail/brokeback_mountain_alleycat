import os

from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv('DEBUG', False)
TG_SECRET_KEY = os.getenv('TG_SECRET_KEY', '') if not DEBUG else os.getenv('TG_SECRET_KEY_DEV', '')
API_URL = os.getenv('API_URL', '') if not DEBUG else 'http://127.0.0.1:8000/api/'
API_AUTH_USER = os.getenv('API_AUTH_USER', '')
API_AUTH_PASSWORD = os.getenv('API_AUTH_PASSWORD', '')

MY_TG_ID = os.getenv('MY_TG_ID')
