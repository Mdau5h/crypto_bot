from config import config
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from manager import FSM
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
    await message.delete()


@dp.message_handler(commands=['encode'], state=None)
async def encode_message(message: types.Message):
    answer = "Введи сообщение для закодирования"
    await FSM.encode_state.set()
    await message.answer(answer, reply_markup=ReplyKeyboardRemove())
    await message.delete()


@dp.message_handler(state=FSM.encode_state)
async def send_encoded(message: types.Message, state: FSMContext):

    # encoded_message, key = manager.encode(message.text)

    answer = "Ваше сообщение должно быть закодировано тут"
    await state.finish()
    await message.answer(answer, reply_markup=kb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
