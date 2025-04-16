"""
src/main.py
Основной файл проекта
"""
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram_dialog import setup_dialogs
from aiogram.fsm.storage.memory import MemoryStorage

from src.bot.dialogs import start_dialog
from src.bot.handlers import register_handlers
from src.config import TELEGRAM_BOT_TOKEN

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
)
storage = MemoryStorage()
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(storage=storage)
dp.include_router(start_dialog)
setup_dialogs(dp)


async def main():
    logger.info("Starting bot")
    register_handlers(dp)
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())
