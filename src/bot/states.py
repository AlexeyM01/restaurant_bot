"""
src/bot/states.py
"""

from aiogram.filters.state import StatesGroup, State


class BotMenu(StatesGroup):
    start = State()


