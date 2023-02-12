import os
from aiogram import Bot, Dispatcher
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage

bot = Bot(token=os.getenv("TOKEN"))

storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)


class MyStatesGroup(StatesGroup):
    galery = State()


BOT_DESCRIPTION = "https://master-kamnerez.ru/"
