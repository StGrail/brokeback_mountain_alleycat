import os

from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv('DEBUG', False)
TG_SECRET_KEY = os.getenv('TG_SECRET_KEY', '')
AUTH_USER = os.getenv('AUTH_USER', '')
AUTH_PASSWORD = os.getenv('AUTH_PASSWORD', '')
