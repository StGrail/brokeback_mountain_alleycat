from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton

invite_to_bot = 'Регистрируйся на аллейкат от СингоСпид'  # TODO


class RegistrationKeyboards:

    show_disclaimer = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton('Правила гонки ℹ️', callback_data='disclaimer_message')],
        ],
    )

    start_registration = InlineKeyboardMarkup(
        hide_keyboard=True,
        inline_keyboard=[
            [
                InlineKeyboardButton('Ок ✔️', callback_data='start_registration'),
                InlineKeyboardButton('Скинуть инвайт ковбою', switch_inline_query=invite_to_bot),
            ],
        ],
    )

    category = InlineKeyboardMarkup(
        hide_keyboard=True,
        inline_keyboard=[
            [
                InlineKeyboardButton('Фиксированный ковбои брейклесс 🚲', callback_data='1'),
            ],
            [
                InlineKeyboardButton('Любой тормозной ковбой 🚴', callback_data='2'),
            ],
            [
                InlineKeyboardButton('Cowgirls', callback_data='3'),
            ],
        ],
    )

    is_data_correct = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Всё верно', callback_data='data_correct'),
                InlineKeyboardButton(text='Изменить данные', callback_data='data_incorrect'),
            ],
        ],
    )

    # change_user_info = InlineKeyboardMarkup(
    #     inline_keyboard=[
    #         [
    #             InlineKeyboardButton('Имя', callback_data='name'),
    #         ],
    #         [
    #             InlineKeyboardButton('Категорию', callback_data='category'),
    #         ],
    #         [
    #             InlineKeyboardButton('Инстаграм', callback_data='instagram'),
    #         ],
    #     ],
    # )

    #
    # are_you_ready = InlineKeyboardMarkup(
    #     inline_keyboard=[[InlineKeyboardButton('Готов конечно', callback_data='ready')]],
    # )
    #
    # got_the_point = InlineKeyboardMarkup(
    #     inline_keyboard=[[InlineKeyboardButton('Я на точке', callback_data='got_the_point')]],
    # )

    # change_reg_data = InlineKeyboardMarkup(
    #     inline_keyboard=[
    #         [InlineKeyboardButton('Пригласи друга на гонку', switch_inline_query=send_to_friend)],
    #         [
    #             InlineKeyboardButton('Жду старта 🏁', callback_data='data_ok'),
    #             InlineKeyboardButton('Изменить данные ♲', callback_data='data_not_ok'),
    #         ],
    #     ],
    # )
