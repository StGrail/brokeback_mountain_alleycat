import aiohttp
from aiohttp import BasicAuth
from rest_framework import status

from config.settings import API_URL, API_AUTH_USER, API_AUTH_PASSWORD


async def get_welcome_message_from_db() -> str:
    """
    GET запрос в API на получение welcome message для регистрации в боте
    :return: текст welcome message
    """

    url = API_URL + f'bot_settings/'
    async with aiohttp.ClientSession() as session:
        async with session.get(url, auth=BasicAuth(API_AUTH_USER, API_AUTH_PASSWORD)) as resp:
            resp_status = resp.status
            if resp_status == status.HTTP_200_OK:
                data = await resp.json()
                welcome_message = data[0].get('welcome_message', 'Нет welcome message')
                return welcome_message
            return 'Нет welcome message'


async def get_disclaimer_from_db() -> str:
    """
    GET запрос в API на получение дисклеймера для регистрации в боте
    :return: текст дисклеймера
    """

    url = API_URL + f'bot_settings/'
    async with aiohttp.ClientSession() as session:
        async with session.get(url, auth=BasicAuth(API_AUTH_USER, API_AUTH_PASSWORD)) as resp:
            resp_status = resp.status
            if resp_status == status.HTTP_200_OK:
                data = await resp.json()
                race_disclaimer = data[0].get('race_disclaimer', 'Нет дисклеймера')
                return race_disclaimer
            return 'Нет дисклеймера'


async def get_message_after_registration_from_db() -> str:
    """
    GET запрос в API на получение сообщения после регистрации в боте
    :return: текст сообщения после регистрации в боте
    """

    url = API_URL + f'bot_settings/'
    async with aiohttp.ClientSession() as session:
        async with session.get(url, auth=BasicAuth(API_AUTH_USER, API_AUTH_PASSWORD)) as resp:
            resp_status = resp.status
            if resp_status == status.HTTP_200_OK:
                data = await resp.json()
                after_reg_message = data[0].get(
                    'after_reg_message', 'Нет сообщения после регистрации в боте'
                )
                return after_reg_message
            return 'Нет сообщения после регистрации в боте'
