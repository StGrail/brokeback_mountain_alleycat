from typing import Union

import aiohttp
from aiohttp import BasicAuth
from rest_framework import status

from config.settings import API_URL, API_AUTH_USER, API_AUTH_PASSWORD


async def create_participant_in_db(tg_chat_id: int) -> bool:
    """
    POST запрос в API на регистрацию участника
    :param tg_chat_id: tg id пользователя
    :return: bool статус регистрации
    """
    url = API_URL + 'participants/'
    data = {'tg_chat_id': tg_chat_id}
    async with aiohttp.ClientSession() as session:
        async with session.post(
            url, data=data, auth=BasicAuth(API_AUTH_USER, API_AUTH_PASSWORD)
        ) as resp:
            resp_status = resp.status
            if resp_status == status.HTTP_201_CREATED:
                return True
            return False


async def update_participant_in_db(tg_chat_id: int, user_data: dict) -> bool:
    """
    PATCH запрос в API на обновление участника
    :param tg_chat_id: tg id пользователя
    :param user_data: данные пользователя
    :return: статус обновления
    """
    url = API_URL + f'participants/{tg_chat_id}/'
    data = user_data
    async with aiohttp.ClientSession() as session:
        async with session.patch(
            url, data=data, auth=BasicAuth(API_AUTH_USER, API_AUTH_PASSWORD)
        ) as resp:
            resp_status = resp.status
            if resp_status == status.HTTP_200_OK:
                return True
            return False


async def get_participant_data_in_db(tg_chat_id: int) -> Union[dict, None]:
    """
    GET запрос в API на получение данных участника
    :param tg_chat_id: tg id пользователя
    :return: словарь с данными пользователя
    :return: None, если данных нет
    """
    url = API_URL + f'participants/{tg_chat_id}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url, auth=BasicAuth(API_AUTH_USER, API_AUTH_PASSWORD)) as resp:
            resp_status = resp.status
            if resp_status == status.HTTP_200_OK:
                user_data = await resp.json()
                return user_data
            return None
