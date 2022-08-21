from typing import Union

import aiohttp
from aiohttp import BasicAuth
from rest_framework import status

from config.settings import API_URL, API_AUTH_USER, API_AUTH_PASSWORD


async def get_all_geo_points() -> Union[dict, None]:
    """
    GET запрос в API на получение всех точек
    :return: словарь с данными пользователя
    :return: None, если данных нет
    """
    url = API_URL + 'all_get_points/'
    async with aiohttp.ClientSession() as session:
        async with session.get(url, auth=BasicAuth(API_AUTH_USER, API_AUTH_PASSWORD)) as resp:
            resp_status = resp.status
            if resp_status == status.HTTP_200_OK:
                points_data = await resp.json()
                return points_data
            return None


async def get_start_geo_points():
    url = API_URL + 'all_get_points/start/'
    async with aiohttp.ClientSession() as session:
        async with session.get(url, auth=BasicAuth(API_AUTH_USER, API_AUTH_PASSWORD)) as resp:
            resp_status = resp.status
            if resp_status == status.HTTP_200_OK:
                points_data = await resp.json()
                return points_data
            return None


async def get_finish_geo_point():
    url = API_URL + 'all_get_points/finish/'
    async with aiohttp.ClientSession() as session:
        async with session.get(url, auth=BasicAuth(API_AUTH_USER, API_AUTH_PASSWORD)) as resp:
            resp_status = resp.status
            if resp_status == status.HTTP_200_OK:
                points_data = await resp.json()
                return points_data
            return None


async def get_intermediate_start_point_data(point_id: int) -> Union[dict, None]:
    """
    GET запрос в API на получение детальной точки
    :return: словарь с данными точки
    """
    url = API_URL + f'all_get_points/{point_id}/'
    async with aiohttp.ClientSession() as session:
        async with session.get(url, auth=BasicAuth(API_AUTH_USER, API_AUTH_PASSWORD)) as resp:
            resp_status = resp.status
            if resp_status == status.HTTP_200_OK:
                point_data = await resp.json()
                return point_data
            return None
