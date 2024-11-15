from aiogram import executor, Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api=
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Бот запущен! Приветствую вас!")

@dp.message_handler(content_types=types.ContentType.TEXT)
async def all_messages(message: types.Message):
    user_message = message.text
    await message.answer(f"Вы написали: {user_message}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
