from aiogram import Dispatcher, types
from db.base_utils import get_group_obj
from keyboards import keyboard_galery, make_inl_keyb
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from create_bot import bot, MyStatesGroup
from db.models import Product


async def open_galery(msg: types.Message, state=FSMContext):
    await msg.answer(text="Оцени наши работы!",
                     reply_markup=keyboard_galery)
    await msg.delete()
    await state.set_state(MyStatesGroup.galery)


async def send_photo(msg: types.Message, product):
    """
    The function takes an object of the Product class
    and sends a photo and description generated from the object to the chat.
    """
    photo = product.photo
    caption = "".join([product.material, "\n", product.size, "\n", product.price])
    link = product.site_link
    await bot.send_photo(chat_id=msg.chat.id,
                         photo=photo,
                         caption=caption,
                         reply_markup=make_inl_keyb(link))


async def show_canvas(msg: types.Message, state: FSMContext):
    """
    The function receives a product group list, takes the first element from it
    and passes it to the next function 'send_photo'.
    """
    products = await get_group_obj(Product, msg.text)
    await state.update_data(products=products)
    await state.update_data(product_number=0)
    data = await state.get_data()
    product_number = data["product_number"]
    products = data["products"]
    product = products[product_number]
    await send_photo(msg, product)


def register_handlers(dp: Dispatcher):
    dp.message.register(open_galery, Text(text="Открыть галерею"))
    dp.message.register(show_canvas, Text(text=["Шары", "Яйца", "Шкатулки"]), MyStatesGroup.galery)
