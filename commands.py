from aiogram import Dispatcher, types
from aiogram.filters.command import Command
from create_bot import BOT_DESCRIPTION
from keyboards import keyboard


async def start(msg: types.Message):
    await msg.answer(text="Добрый день! Начнём, пожалуй.", reply_markup=keyboard)
    await msg.delete()


async def desc(msg: types.Message):
    await msg.answer(text=BOT_DESCRIPTION)
    await msg.delete()


def register_handlers(dp: Dispatcher):
    dp.message.register(start, Command(commands=["start"]))
    dp.message.register(desc, Command(commands=["description"]))
