"""
src/main.py
"""
import asyncio
import logging
from datetime import datetime

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog.setup import DialogRegistry

from src.config import TELEGRAM_BOT_TOKEN

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TELEGRAM_BOT_TOKEN)

storage = MemoryStorage()
dp = Dispatcher(storage=storage)
dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
registry = DialogRegistry(dp)


# Запуск процесса поллинга новых апдейтов
async def main():
    """Основная функция для запуска бота"""
    from src.bot.handlers import register_handlers
    register_handlers(dp)
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    asyncio.run(main())

