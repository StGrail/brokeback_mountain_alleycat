from typing import Union

from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


class GeoPointsKeyboards:
    def __init__(
        self,
        kb_data: Union[dict, str] = None,
    ):
        self.kb_data = kb_data

    def point_kb(self) -> InlineKeyboardMarkup:
        """Создаем клавиатуру с текстом и коллбек датой для гео точек"""

        keyboard = InlineKeyboardMarkup(one_time_keyboard=True)
        for element in self.kb_data:
            keyboard.add(
                InlineKeyboardButton(text=element.get('name'), callback_data=(element.get('id')))
            )

        return keyboard

    @staticmethod
    def get_start_point() -> InlineKeyboardMarkup:
        keyboard = InlineKeyboardMarkup(
            one_time_keyboard=True,
            inline_keyboard=[
                [InlineKeyboardButton('Я на точке', callback_data='got_the_start_point')]
            ],
        )
        return keyboard

    @staticmethod
    def get_finish_point() -> InlineKeyboardMarkup:
        keyboard = InlineKeyboardMarkup(
            one_time_keyboard=True,
            inline_keyboard=[
                [InlineKeyboardButton('Я забрался на гору', callback_data='got_the_finish_point')]
            ],
        )
        return keyboard

    @staticmethod
    def location_button() -> ReplyKeyboardMarkup:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text='Отправь своё местоположение 🗺', request_location=True)]
            ],
        )
        return keyboard
