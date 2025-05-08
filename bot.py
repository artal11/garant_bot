from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import logging

API_TOKEN = 'YOUR_BOT_TOKEN'  # Замените на свой токен от @BotFather

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: Message):
    await message.answer("Привет! Я гарант-бот. Используй /deal для создания сделки.")

@dp.message_handler(commands=['deal'])
async def deal_handler(message: Message):
    await message.answer("Пока что команды сделки не реализованы.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)