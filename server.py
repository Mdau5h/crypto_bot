from config import config
import logging
from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = config.TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    welcome_message = "Привет! Это бот-шифратор. Если ты сюда попал, мой создатель тебе очень доверяет.\n"
    if message.from_user['id'] == config.ADMIN_ID:
        welcome_message = "Здравствуй, создатель!\n"
    await message.answer(welcome_message)
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
