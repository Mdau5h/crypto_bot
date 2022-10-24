from config import config
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from manager import FSM, encode, decode
from keyboard import kb

API_TOKEN = config.TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    welcome_message = "Привет! Это бот-шифратор. Если ты сюда попал, мой создатель тебе очень доверяет.\n"
    if message.from_user['id'] == config.ADMIN_ID:
        welcome_message = "Здравствуй, создатель!\n"
    await message.answer(welcome_message, reply_markup=kb)
    # await message.delete()


@dp.message_handler(commands=['encode'], state=None)
async def encode_message(message: types.Message):
    answer = "Введи сообщение для закодирования"
    await FSM.encode_state.set()
    await message.answer(answer, reply_markup=ReplyKeyboardRemove())
    # await message.delete()


@dp.message_handler(state=FSM.encode_state)
async def send_encoded(message: types.Message, state: FSMContext):
    encoded_message, key = encode(message.text)

    answer = "Ваше сообщение должно быть закодировано тут: "
    answer_key = "Ключ: "
    await state.finish()
    await message.answer(answer)
    await message.answer(f"`{encoded_message}`", reply_markup=kb, parse_mode="Markdown")
    await message.answer(answer_key)
    await message.answer(f"`{key}`", reply_markup=kb, parse_mode="Markdown")


@dp.message_handler(commands=['decode'], state=None)
async def decode_message(message: types.Message):
    answer = "Введи сообщение для декодирования:"
    await FSM.decode_state_message.set()
    await message.answer(answer, reply_markup=ReplyKeyboardRemove())
    # await message.delete()


@dp.message_handler(state=FSM.decode_state_message)
async def get_key(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['message'] = message.text

    answer = "Введи ключ:"
    await FSM.decode_state_key.set()
    await message.answer(answer, reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=FSM.decode_state_key)
async def send_encoded(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['key'] = message.text
        decoded_message = decode(data['message'], data['key'])

    answer = "Ваше сообщение должно быть раскодировано тут:"
    await state.finish()
    await message.answer(answer)
    await message.answer(f"`{decoded_message}`", reply_markup=kb, parse_mode="Markdown")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
