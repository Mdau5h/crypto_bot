from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn_encode = KeyboardButton('/encode')
btn_decode = KeyboardButton('/decode')

kb = ReplyKeyboardMarkup(resize_keyboard=True).row(btn_encode, btn_decode)
