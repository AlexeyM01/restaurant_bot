"""
src/bot/handlers.py
"""
from aiogram import Dispatcher
from aiogram.filters import Command

from src.bot import dialogs


def register_handlers(dp: Dispatcher):
    dp.message.register(dialogs.start, Command("start"))

