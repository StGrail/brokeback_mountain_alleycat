from api_requests.geo_points import get_all_geo_points
from api_requests.race_requests import get_race_instance_in_db
from constants import R


async def count_unfinished_points(tg_chat_id: int) -> int:
    total_points = await get_all_geo_points()
    user_finished_points = await get_race_instance_in_db(tg_chat_id=tg_chat_id)
    result = len(total_points) - len(user_finished_points.get('points'))
    return result


def check_geo_position(
    user_latitude: float, user_longitude: float, point_longitude: float, point_latitude: float
) -> bool:
    """Проверяем. что геоданные пользователя в радиусе 150м от точки"""

    if (user_latitude - point_longitude) ** 2 + (user_longitude - point_latitude) ** 2 <= R**2:
        return True
    return False
