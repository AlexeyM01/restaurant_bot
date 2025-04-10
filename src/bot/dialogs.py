"""
src/bot/dialogs.py
"""
from aiogram import types
from aiogram.enums.dice_emoji import DiceEmoji


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
