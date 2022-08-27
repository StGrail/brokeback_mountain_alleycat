import os

from dotenv import load_dotenv

load_dotenv()

DEBUG = False
IS_DEV = os.getenv('IS_DEV', True)
BOT_TOKEN = os.getenv('BOT_TOKEN')
API_URL = os.getenv('API_URL', 'http://127.0.0.1:8000/api/')
API_AUTH_USER = os.getenv('API_AUTH_USER', '')
API_AUTH_PASSWORD = os.getenv('API_AUTH_PASSWORD', '')

MY_TG_ID = os.getenv('MY_TG_ID')
