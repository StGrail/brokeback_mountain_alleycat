from aiogram import types, filters
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from api_requests.race_requests import get_race_data
from api_requests.text_messages import (
    get_disclaimer_from_db,
    get_welcome_message_from_db,
    get_message_after_registration_from_db,
)
from api_requests.registration import (
    create_participant_in_db,
    update_participant_in_db,
    get_participant_data_in_db,
)
from config.settings import DEBUG
from config.utils import dp
from constants import CategoriesEnums
from keyboards.registration import RegistrationKeyboards
from states.registration_states import RegistrationFormStates


@dp.message_handler(text='/start')
async def send_welcome(message: types.Message) -> None:
    """Создаю пользователя и задаю состояние для регистрации"""

    race_data = await get_race_data()
    is_race_start = race_data[0].get('is_started')
    if not is_race_start:

        tg_chat_id = message.from_user.id
        is_new = await create_participant_in_db(tg_chat_id=tg_chat_id)
        if is_new:
            welcome_message = (
                await get_welcome_message_from_db() if not DEBUG else 'WELCOME MESSAGE TEXT'
            )
            await message.reply(
                f'Добро пожаловать, {welcome_message}',
                reply_markup=RegistrationKeyboards.show_disclaimer,
            )
        else:
            user_data_from_db = await get_participant_data_in_db(tg_chat_id=tg_chat_id)
            name = user_data_from_db.get('name')
            category = CategoriesEnums.labels.value.get(user_data_from_db.get('category'))
            instagram = user_data_from_db.get('instagram')
            await message.answer(
                f'Вы уже зарегистрированы.\n'
                f'Проверьте, правильно ли записаны данные:\n\n'
                f'имя - {name}\n'
                f'категория - {category}\n'
                f'instagram - {instagram}',
                reply_markup=RegistrationKeyboards.is_data_correct,
            )
            await RegistrationFormStates.check_data.set()
    else:
        await message.reply('Гонка уже началась, регистрация закрыта')


@dp.callback_query_handler(text='disclaimer_message')
async def read_disclaimer(call: CallbackQuery) -> None:

    disclaimer_text = await get_disclaimer_from_db() if not DEBUG else 'DISCLAIMER TEXT'
    await call.message.delete()
    await call.message.answer(
        f'{disclaimer_text}', reply_markup=RegistrationKeyboards.start_registration
    )
    await RegistrationFormStates.start_registration.set()


@dp.callback_query_handler(state=RegistrationFormStates.start_registration)
async def start_registration(call: CallbackQuery) -> None:

    await call.answer(cache_time=1)
    await call.message.delete_reply_markup()
    await call.message.answer(text=f'Напишите своё имя')
    await RegistrationFormStates.next()


@dp.message_handler(state=RegistrationFormStates.name)
async def input_name(message: types.Message, state: FSMContext) -> None:
    """Сохраняем имя от пользователя"""

    name = str(message.text.capitalize())
    user_data = {
        'tg_chat_id': message.from_user.id,
        'name': name,
    }
    await state.update_data(data=user_data)
    await message.answer(
        f'Имя - {name}\n\nВыберите категорию:',
        reply_markup=RegistrationKeyboards.category,
    )
    await RegistrationFormStates.next()


@dp.callback_query_handler(state=RegistrationFormStates.category)
async def input_category(call: CallbackQuery, state: FSMContext) -> None:
    """Сохраняем категорию от пользователя"""

    user_data = await state.get_data()
    user_data['category'] = int(call.data)
    category = CategoriesEnums.labels.value.get(int(call.data))

    await call.message.delete_reply_markup()
    await state.update_data(data=user_data)
    await call.message.edit_text(
        f'Категория - {category}\n\n'
        f'Укажи <tg-spoiler>instagram</tg-spoiler>*, '
        f'чтобы найти себя потом в прошмандовках синглспидсакерc\n\n'
    )
    await RegistrationFormStates.next()


@dp.message_handler(state=RegistrationFormStates.instagram)
async def input_instagram(message: types.Message, state: FSMContext) -> None:
    """Сохраняем инстаграм от пользователя"""

    user_data = await state.get_data()
    name = user_data.get('name')
    category = CategoriesEnums.labels.value.get(user_data.get('category'))
    instagram = str(message.text)
    user_data['instagram'] = instagram

    await state.update_data(data=user_data)
    await message.answer(
        f'Проверьте, правильно ли записал данные:\n\n'
        f'имя - {name}\n'
        f'категория - {category}\n'
        f'instagram - {instagram}',
        reply_markup=RegistrationKeyboards.is_data_correct,
    )
    await RegistrationFormStates.next()


@dp.callback_query_handler(state=RegistrationFormStates.check_data, text='data_correct')
async def data_ok(call: CallbackQuery, state: FSMContext) -> None:
    """Обновляем пользователя в бд"""

    tg_chat_id = call.from_user.id
    user_data = await state.get_data()
    await update_participant_in_db(tg_chat_id=tg_chat_id, user_data=user_data)
    await state.reset_state(with_data=True)
    message_text = (
        (await get_message_after_registration_from_db())
        if not DEBUG
        else 'Регистрация прошла успешно'
    )
    await call.message.edit_reply_markup()
    await call.message.answer(text=f'{message_text}')


@dp.callback_query_handler(state=RegistrationFormStates.check_data, text='data_incorrect')
async def data_error(call: CallbackQuery, state: FSMContext) -> None:
    """Повторяем регистрацию"""

    await state.reset_state(with_data=True)
    await call.answer(cache_time=1)
    await RegistrationFormStates.start_registration.set()
