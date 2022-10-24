from aiogram.dispatcher.filters.state import State, StatesGroup
from generator import get_key


class FSM(StatesGroup):
    encode_state = State()
    decode_state_message = State()
    decode_state_key = State()


def encode(message):
    key = get_key()
    return message + " (типа, закодировано)", key


def decode(message, key):
    return message + " (типа, раскодировано ключом:)" + key
