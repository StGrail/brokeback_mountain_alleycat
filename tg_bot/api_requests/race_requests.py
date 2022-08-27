from typing import Union

import aiohttp
from aiohttp import BasicAuth
from rest_framework import status

from config.settings import API_URL, API_AUTH_USER, API_AUTH_PASSWORD


async def create_race_instance_in_db(**kwargs) -> bool:
    """
    POST запрос в API для создания инстанса "гонки" с участником и записи времени старта.
    :return: bool создан или нет
    """
    url = API_URL + 'race/'
    data = kwargs

    async with aiohttp.ClientSession() as session:
        async with session.post(
            url,
            data=data,
            auth=BasicAuth(API_AUTH_USER, API_AUTH_PASSWORD),
        ) as resp:
            resp_status = resp.status
            if resp_status == status.HTTP_200_OK:
                return True
            return False


async def get_race_instance_in_db(tg_chat_id: int) -> Union[dict, None]:
    """
    GET запрос в API для детального вида инстанса гонки по участнику.
    :return: dict c информацией по гонке
    """
    url = API_URL + f'race/{tg_chat_id}/'
    async with aiohttp.ClientSession() as session:
        async with session.get(url, auth=BasicAuth(API_AUTH_USER, API_AUTH_PASSWORD)) as resp:
            resp_status = resp.status
            if resp_status == status.HTTP_200_OK:
                data = await resp.json()
                return data
            return None


async def get_geo_points_exclude(tg_chat_id: int) -> Union[dict, None]:
    """
    GET запрос в API для детального вида инстанса гонки по участнику.
    :return: dict c информацией по гонке
    """
    url = API_URL + f'exclude/?tg_chat_id={tg_chat_id}'
    async with aiohttp.ClientSession() as session:
        async with session.get(
            url, auth=BasicAuth(API_AUTH_USER, API_AUTH_PASSWORD)
        ) as resp:
            resp_status = resp.status
            if resp_status == status.HTTP_200_OK:
                data = await resp.json()
                return data
            return None


async def post_race_instance_in_db(**kwargs) -> bool:
    """
    POST запрос в API для обновления точки у пользователя.
    :return: bool создан или нет
    """
    url = API_URL + 'race/'
    data = {**kwargs}
    async with aiohttp.ClientSession() as session:
        async with session.post(
            url, data=data, auth=BasicAuth(API_AUTH_USER, API_AUTH_PASSWORD)
        ) as resp:
            resp_status = resp.status
            if resp_status == status.HTTP_200_OK:
                return True
            return False


async def patch_race_instance_in_db(tg_chat_id: int, **kwargs) -> bool:
    """
    POST запрос в API для обновления точки у пользователя.
    :return: bool создан или нет
    """
    url = API_URL + f'race/{tg_chat_id}/'
    data = {**kwargs}
    async with aiohttp.ClientSession() as session:
        async with session.patch(
            url, data=data, auth=BasicAuth(API_AUTH_USER, API_AUTH_PASSWORD)
        ) as resp:
            resp_status = resp.status
            if resp_status == status.HTTP_200_OK:
                return True
            return False


async def get_race_data() -> Union[dict, None]:
    """
    GET запрос в API для получения данных о старте гонки и времени старта.
    :returns: данные по настройкам гонки / None
    """

    url = API_URL + 'race_data/'
    async with aiohttp.ClientSession() as session:
        async with session.get(url, auth=BasicAuth(API_AUTH_USER, API_AUTH_PASSWORD)) as resp:
            resp_status = resp.status
            if resp_status == status.HTTP_200_OK:
                data = await resp.json()
                return data
            return None
