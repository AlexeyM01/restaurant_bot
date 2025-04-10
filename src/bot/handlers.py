"""
src/bot/handlers.py
"""
from aiogram import Dispatcher
from aiogram.filters import Command

from .dialogs import cmd_test1, cmd_test2, cmd_dice, cmd_start, cmd_add_to_list, cmd_show_list, cmd_info


def register_handlers(dp: Dispatcher):
    dp.message.register(cmd_start, Command("start"))
    dp.message.register(cmd_test1, Command("test1"))
    dp.message.register(cmd_test2, Command("test2"))
    dp.message.register(cmd_dice, Command("dice"))
    dp.message.register(cmd_add_to_list, Command("add_to_list"))
    dp.message.register(cmd_show_list, Command("show_list"))
    dp.message.register(cmd_info, Command("info"))

