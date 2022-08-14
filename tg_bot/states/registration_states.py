from aiogram.dispatcher.filters.state import State, StatesGroup


class RegistrationFormStates(StatesGroup):
    """Состояния регистрации для FSM"""

    start_registration = State()
    name = State()
    category = State()
    instagram = State()
    check_data = State()
