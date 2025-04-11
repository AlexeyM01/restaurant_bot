"""
src/bot/dialogs.py
"""
from aiogram import types
from aiogram.enums.dice_emoji import DiceEmoji
from datetime import datetime
from src.database.database import get_db
from src.database.models import Booking


async def cmd_start(message: types.Message):
    await message.answer("Hello!")


async def cmd_test1(message: types.Message):
    await message.reply("Test 1")


async def cmd_test2(message: types.Message):
    await message.reply("Test 2")


async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji=DiceEmoji.DICE)


async def cmd_add_to_list(message: types.Message, mylist: list[int]):
    mylist.append(7)
    await message.answer("Добавлено число 7")


async def cmd_show_list(message: types.Message, mylist: list[int]):
    await message.answer(f"Ваш список: {mylist}")


async def cmd_info(message: types.Message, started_at: str):
    await message.answer(f"Бот запущен {started_at}")


async def db_add_booking(name: str, date: datetime, guests: int):
    new_booking = Booking(name=name, date=date, guests=guests)
    async for db in get_db():
        db.add(new_booking)
        await db.commit()
        await db.refresh(new_booking)
