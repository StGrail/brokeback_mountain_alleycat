from aiogram.dispatcher.filters.state import State, StatesGroup


class RaceStates(StatesGroup):
    """Состояния FSM для гонки"""

    start_race = State()
    check_you_are_on_the_start = State()
    choose_all_points = State()
    choose_next_point = State()
    intermediate_start = State()
    intermediate_from_start_to_finish = State()
    intermediate_finish = State()
    finish_race = State()
    check_you_are_on_the_finish = State()
