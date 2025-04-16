"""
src/bot/dialogs.py
"""
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode, Dialog

from src.bot.states import BotMenu
from src.bot.windows import start_window

start_dialog = Dialog(start_window)


async def start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(BotMenu.start, mode=StartMode.RESET_STACK)


