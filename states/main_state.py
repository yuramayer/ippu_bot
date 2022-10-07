from aiogram.dispatcher.filters.state import StatesGroup, State


class new_user(StatesGroup):
    name = State()
    sex = State()
    course = State()
    type = State()
    level = State()
    program = State()
    base = State()
    year = State()
    birth = State()
    vacation = State()
