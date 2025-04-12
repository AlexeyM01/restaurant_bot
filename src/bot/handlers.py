"""
src/bot/handlers.py
"""
from aiogram import Dispatcher, F
from aiogram.filters import Command
from aiogram_calendar import SimpleCalendarCallback

from .dialogs import cmd_start, process_name, process_date, process_time, process_guests, cmd_get, cmd_egit, \
    process_edit, cmd_delete, process_delete


def register_handlers(dp: Dispatcher):
    dp.message.register(cmd_get, Command("get"))
    dp.message.register(cmd_delete, Command("delete"))
    dp.message.register(cmd_start, Command("start"))
    dp.message.register(cmd_egit, Command("egit"))

    # Обработчик для удаления
    dp.message.register(process_delete, F.text.regexp(r'^(У|у)(далить)s+(d+)$').as_("delete_command"))

    # Обработчик для количества гостей
    dp.message.register(process_guests, F.text.regexp(r"^[1-9][0-9]?$").as_("guests_number"))

    # Обработчик для времени
    dp.message.register(process_time, F.text.regexp(r"^([0-1][0-9]|2[0-3]):(00|30)$").as_("time_HHMM"))

    # Обработчик для имени
    dp.message.register(process_name, F.text.regexp(r"^([А-Я]?[а-я]+)(\s([А-Я]?[а-я]+)?(-[А-Я]?[а-я]+)?)?$"))

    # Обработчик для выбора даты
    dp.callback_query.register(process_date, SimpleCalendarCallback.filter())

    # Обработчик для редактирования
    dp.message.register(process_edit, F.text)


