from aiogram.dispatcher.filters.state import State, StatesGroup


class FSM(StatesGroup):
    encode_state = State()
    decode_state_message = State()
    decode_state_key = State()
