from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext, filters
from aiogram.types import CallbackQuery

from api_requests.geo_points import (
    get_all_geo_points,
    get_intermediate_start_point_data,
    get_start_geo_points,
    get_finish_geo_point,
)
from api_requests.race_requests import (
    create_race_instance_in_db,
    get_race_instance_in_db,
    get_geo_points_exclude,
    patch_race_instance_in_db,
    get_race_data,
)
from config.utils import dp
from keyboards.geo_points import GeoPointsKeyboards


from services.race_services import check_geo_position
from states.race_states import RaceStates


@dp.callback_query_handler(text='ready_to_race')
async def start_race(call: CallbackQuery, state: FSMContext) -> None:
    tg_chat_id = int(call.from_user.id)

    await call.answer(cache_time=1)
    await state.reset_state(with_data=True)

    race_data = await get_race_data()
    time_of_start = race_data[0].get('time_of_start')

    await create_race_instance_in_db(participant=tg_chat_id, time_of_start=time_of_start)
    await call.message.edit_text(
        'Давай проверим, что ты действительно на старте. Пришли свою локацию 🗺',
    )
    await RaceStates.check_you_are_on_the_start.set()


# прием локации на основном старте
@dp.message_handler(
    state=RaceStates.check_you_are_on_the_start, content_types=types.ContentType.LOCATION
)
async def check_location_on_the_start_point(message: types.Message):
    on_point_answer = 'Ты на месте!\nДля подтверждения, отправь селфи 📷'

    tg_chat_id = message.from_user.id
    user_latitude = float(f'{message.location["latitude"]:.5f}')
    user_longitude = float(f'{message.location["longitude"]:.5f}')

    point_data = await get_start_geo_points()
    finish_longitude = float(point_data.get('longitude_start'))
    finish_latitude = float(point_data.get('latitude_start'))
    point_id = point_data.get('id')

    on_point = check_geo_position(
        user_latitude=float(f'{user_latitude:.5f}'),
        user_longitude=float(f'{user_longitude:.5f}'),
        point_longitude=float(f'{finish_longitude:.5f}'),
        point_latitude=float(f'{finish_latitude:.5f}'),
    )
    if on_point:
        await message.answer(on_point_answer)

        await patch_race_instance_in_db(
            tg_chat_id=tg_chat_id, participant=tg_chat_id, points=[point_id]
        )
        await RaceStates.choose_all_points.set()
    else:
        # Запрашиваю локацию еще раз
        await message.answer(
            'Далеко от точки, попробуй еще раз', reply_markup=GeoPointsKeyboards.location_button()
        )


# выбор всех точек на стартовой локации, после получения фото
@dp.message_handler(state=RaceStates.choose_all_points, content_types=types.ContentType.PHOTO)
async def choose_all_points(message: types.Message, state: FSMContext):
    points = await get_all_geo_points()
    point_names_text = '\n'.join([point.get('name') for point in points])
    await message.answer(
        f'И так, всего у нас {len(points)} точек:\n\n{point_names_text}\n\n'
        f'Выбери, куда поедешь сначала ⬇️',
        reply_markup=GeoPointsKeyboards(kb_data=points).point_kb(),
    )
    await state.reset_state(with_data=True)
    await RaceStates.choose_next_point.set()


@dp.callback_query_handler(state=RaceStates.choose_next_point, regexp=r'[0-9]')
async def to_intermediate_start_point(call: types.CallbackQuery, state: FSMContext) -> None:

    point_id = int(call.data)

    intermediate_start_point_data = await get_intermediate_start_point_data(point_id=call.data)
    start_longitude = intermediate_start_point_data.get('longitude_start')
    start_latitude = intermediate_start_point_data.get('latitude_start')
    await call.message.edit_text(
        f'Старт участка расположен по этим координатам <code>{start_longitude},{start_latitude}</code>.\n\n'
        f'Нажми на кнопку, когда будешь на месте',
        reply_markup=GeoPointsKeyboards.get_start_point(),
    )
    await RaceStates.intermediate_start.set()
    await state.set_data(data={'point_id': point_id})


# запрос локации на промежуточном старте
@dp.callback_query_handler(state=RaceStates.intermediate_start, text='got_the_start_point')
async def on_intermediate_start_point(call: types.CallbackQuery) -> None:
    """Проверяем, что участник действительно на промежуточном старте, запрос локации и проверка"""

    await call.answer(cache_time=1)
    await call.message.delete_reply_markup()

    await call.message.answer(
        'Отправь своё местоположение 🗺',
        reply_markup=GeoPointsKeyboards.location_button(),
    )


@dp.message_handler(state=RaceStates.intermediate_start, content_types=types.ContentType.LOCATION)
async def on_intermediate_start_point_get_location(
    message: types.Message, state: FSMContext
) -> None:
    """Проверяем, что участник действительно на промежуточном старте, проверка локации и запрос фото"""

    on_point_message = 'Ты на месте!\nДля подтверждения, отправь селфи 📷'
    user_latitude = float(f'{message.location["latitude"]:.5f}')
    user_longitude = float(f'{message.location["longitude"]:.5f}')
    state_data = await state.get_data()
    point_id = int(state_data.get('point_id'))

    intermediate_start_point_data = await get_intermediate_start_point_data(point_id=point_id)

    finish_longitude = float(intermediate_start_point_data.get('longitude_start'))
    finish_latitude = float(intermediate_start_point_data.get('latitude_start'))
    point_id = intermediate_start_point_data.get('id')

    on_point = check_geo_position(
        user_latitude=float(f'{user_latitude:.5f}'),
        user_longitude=float(f'{user_longitude:.5f}'),
        point_longitude=float(f'{finish_longitude:.5f}'),
        point_latitude=float(f'{finish_latitude:.5f}'),
    )

    if on_point:
        await message.answer(on_point_message)
        await RaceStates.intermediate_start.set()
        await state.set_data({'point_id': point_id})

    else:
        # Запрашиваю локацию еще раз
        await message.answer(
            'Далеко от точки, попробуй еще раз', reply_markup=GeoPointsKeyboards.location_button()
        )


# Получаем фото на промежуточно старте и отдаём локацию промежуточного финиша
@dp.message_handler(state=RaceStates.intermediate_start, content_types=types.ContentType.PHOTO)
async def on_intermediate_start_point_get_photo(message: types.Message, state: FSMContext):

    state_data = await state.get_data()
    point_id = state_data.get('point_id')

    intermediate_start_point_data = await get_intermediate_start_point_data(point_id=point_id)
    start_longitude = intermediate_start_point_data.get('longitude_start')
    start_latitude = intermediate_start_point_data.get('latitude_start')
    await message.answer(
        f'Финиш участка расположен по этим координатам <code>{start_longitude},{start_latitude}</code>.\n\n'
        f'Нажми на кнопку, когда будешь на месте',
        reply_markup=GeoPointsKeyboards.get_finish_point(),
    )
    await RaceStates.intermediate_finish.set()
    await state.set_data(data={'point_id': point_id})


@dp.callback_query_handler(state=RaceStates.intermediate_finish, text='got_the_finish_point')
async def get_intermediate_finish_point(call: types.CallbackQuery) -> None:

    await call.answer(cache_time=1)
    await call.message.delete_reply_markup()

    await call.message.answer(
        'Отправь своё местоположение 🗺',
        reply_markup=GeoPointsKeyboards.location_button(),
    )


@dp.message_handler(state=RaceStates.intermediate_finish, content_types=types.ContentType.LOCATION)
async def on_intermediate_finish_point_get_location(
    message: types.Message, state: FSMContext
) -> None:
    """Проверяем, что участник действительно на промежуточном финише, проверка локации и запрос фото"""

    on_point = 'Ты на месте!\nДля подтверждения, отправь селфи 📷'

    tg_chat_id = message.from_user.id
    user_latitude = float(f'{message.location["latitude"]:.5f}')
    user_longitude = float(f'{message.location["longitude"]:.5f}')
    state_data = await state.get_data()
    point_id = state_data.get('point_id')

    intermediate_start_point_data = await get_intermediate_start_point_data(point_id=point_id)

    start_longitude = float(intermediate_start_point_data.get('longitude_finish'))
    start_latitude = float(intermediate_start_point_data.get('latitude_finish'))

    if check_geo_position(
        user_latitude=user_latitude,
        user_longitude=user_longitude,
        point_latitude=start_latitude,
        point_longitude=start_longitude,
    ):

        data_from_db = await get_race_instance_in_db(tg_chat_id=tg_chat_id)
        points = data_from_db.get('points')
        points.append(int(point_id))
        await patch_race_instance_in_db(tg_chat_id=tg_chat_id, points=points)
        print('патс on_intermediate_finish_point_get_location')
        await message.answer(on_point)
        await state.reset_data()
    else:
        # Запрашиваю локацию еще раз
        await message.answer(
            'Далеко от точки, попробуй еще раз', reply_markup=GeoPointsKeyboards.location_button()
        )


# Получаем фото на промежуточно финише и отдаём следуюзие точки
@dp.message_handler(
    state=RaceStates.intermediate_finish, content_types=types.ContentType.PHOTO
)
async def on_intermediate_finish_point_get_photo(message: types.Message, state: FSMContext):

    await state.reset_state(with_data=True)
    tg_chat_id = message.from_user.id

    user_race_data = await get_race_instance_in_db(tg_chat_id=tg_chat_id)
    user_points = user_race_data.get('points')
    any_points_for_user = await get_geo_points_exclude(points_list=user_points)
    total_points = await get_all_geo_points()

    if len(user_points) == len(total_points) + 1:
        await message.answer(
            'Отлично, все точки закончились, гони на финиш, пришли локацию, когда доедешь',
            reply_markup=GeoPointsKeyboards.location_button(),
        )
        await state.reset_state(with_data=True)
        await RaceStates.check_you_are_on_the_finish.set()
    else:
        points = any_points_for_user
        point_names_text = '\n'.join([point.get('name') for point in points])
        await message.answer(
            f'Еще {len(points)} точек:\n\n{point_names_text}\n\n' f'Выбери, куда поедешь',
            reply_markup=GeoPointsKeyboards(kb_data=points).point_kb(),
        )
        await state.reset_state(with_data=True)
        await state.reset_data()
        await RaceStates.choose_next_point.set()


# прием локации на основном финише
@dp.message_handler(
    state=RaceStates.check_you_are_on_the_finish, content_types=types.ContentType.LOCATION
)
async def check_location_on_the_finish_point(message: types.Message):
    on_point_message = 'Ты на месте!\nДля подтверждения, отправь селфи 📷'
    user_latitude = float(f'{message.location["latitude"]:.5f}')
    user_longitude = float(f'{message.location["longitude"]:.5f}')

    point_data = await get_finish_geo_point()
    finish_longitude = point_data.get('longitude_start')
    finish_latitude = point_data.get('latitude_start')

    on_point = check_geo_position(
        user_latitude=user_latitude,
        user_longitude=user_longitude,
        point_longitude=float(f'{finish_longitude:.5f}'),
        point_latitude=float(f'{finish_latitude:.5f}f'),
    )
    if on_point:
        await message.answer(on_point_message)
    else:
        # Запрашиваю локацию еще раз
        await message.answer(
            'Далеко от точки, попробуй еще раз', reply_markup=GeoPointsKeyboards.location_button()
        )


# прием фото на основном финише
@dp.message_handler(
    state=RaceStates.check_you_are_on_the_finish, content_types=types.ContentType.PHOTO
)
async def check_location_on_the_finish_point(message: types.Message, state: FSMContext):
    end_race = 'Поздравляю, ты на финише. Выпей пивка, ковбой.'

    tg_chat_id = message.from_user.id
    user_race_data = await get_race_instance_in_db(tg_chat_id=tg_chat_id)
    user_points = user_race_data.get('points')
    point_data = await get_start_geo_points()
    finish_longitude = point_data.get('longitude_start')
    finish_latitude = point_data.get('latitude_start')
    point_id = point_data.get('id')

    time_finish = datetime.now()
    race_data = await get_race_data()
    time_start = race_data[0].get('time_of_start')

    total_time_delta = time_finish - datetime.strptime(time_start, "%Y-%m-%dT%H:%M:%S.%f+03:00")
    total_time = datetime.strptime(str(total_time_delta), "%H:%M:%S.%f")

    await message.answer(end_race)
    data = {
        'is_finished': True,
        'time_of_finish': time_finish,
        'time_of_race': total_time,
        'points': user_points.append(int(point_id)),
    }
    await patch_race_instance_in_db(tg_chat_id=tg_chat_id, participant=tg_chat_id, data=data)
    await state.reset_state(with_data=True)
