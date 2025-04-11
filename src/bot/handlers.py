"""
src/bot/handlers.py
"""
from aiogram import Dispatcher, F
from aiogram.filters import Command, Filter
from aiogram_calendar import SimpleCalendarCallback

from .dialogs import cmd_start, process_name, process_date, process_time, process_guests, cmd_get


def register_handlers(dp: Dispatcher):
    dp.message.register(cmd_start, Command("start"))
    dp.message.register(process_guests, F.text.regexp(r"^[1-9]$").as_("guests_number"))
    dp.message.register(process_time, F.text.regexp(r"^([0-1][0-9]|2[0-3]):(00|30)$").as_("time_HHMM"))
    dp.message.register(process_name, F.text.regexp(r"^([А-Я]?[а-я]+)(\s([А-Я]?[а-я]+)?(-[А-Я]?[а-я]+)?)?$"))
    dp.callback_query.register(process_date, SimpleCalendarCallback.filter())

    dp.message.register(cmd_get, Command("get"))


