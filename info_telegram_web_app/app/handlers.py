from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.utils.deep_linking import get_start_link
import jwt

async def start_handler(message: types.Message):
    # Создаем JWT токен
    payload = {'tg_id': message.from_user.id}
    token = jwt.encode(payload, JWT_SECRET, algorithm='HS256')
    web_app_url = f"https://your-domain.com/?token={token}"
    keyboard = types.InlineKeyboardMarkup()
    web_app_button = types.InlineKeyboardButton(
        text="Открыть личную карточку",
        web_app=types.WebAppInfo(url=web_app_url)
    )
    keyboard.add(web_app_button)
    await message.answer("Нажмите кнопку ниже, чтобы открыть личную карточку.", reply_markup=keyboard)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])

