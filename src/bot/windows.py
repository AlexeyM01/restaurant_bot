"""
src/bot/windows.py
Здесь управление окнами
"""
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const

from src.bot.states import BotMenu

start_window = Window(
    Const("Создать бронирование"),
    Button(Const("Создать бронирование"), id="create"),
    Button(Const("Просмотреть все мои бронирования"), id="read"),
    Button(Const("Изменить бронирование"), id="update"),
    Button(Const("Удалить бронирование"), id="delete"),
    state=BotMenu.start,
)

