from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from app.config import BOT_TOKEN
from app.handlers import register_handlers

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

def start_bot():
    register_handlers(dp)
    executor.start_polling(dp, skip_updates=True)
