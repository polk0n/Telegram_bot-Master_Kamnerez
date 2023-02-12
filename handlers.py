from aiogram import Dispatcher, types
from keyboards import keyboard_galery
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from create_bot import MyStatesGroup


async def open_galery(msg: types.Message, state=FSMContext):
    await msg.answer(text="Оцени наши работы!",
                     reply_markup=keyboard_galery)
    await msg.delete()
    await state.set_state(MyStatesGroup.galery)


def register_handlers(dp: Dispatcher):
    dp.message.register(open_galery, Text(text="Открыть галерею"))
