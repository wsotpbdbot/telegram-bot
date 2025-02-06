import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = "আপনার_BOT_TOKEN"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("👋 হ্যালো! আমি WSOTP Telegram Bot ।")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
