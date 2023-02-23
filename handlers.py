from aiogram import Dispatcher, types
from db.base_utils import get_group_obj
from keyboards import keyboard_galery, make_inl_keyb
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from create_bot import bot, MyStatesGroup
from db.models import Product
from keyboards import keyboard
from aiogram import F


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


async def foto_callback_like(callback: types.CallbackQuery):
    await callback.answer(text="You like it!")


async def foto_callback_dislike(callback: types.CallbackQuery):
    await callback.answer(text="You don't like it..")


async def foto_callback_main_menu(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(text="Добро пожаловать в Главное меню", reply_markup=keyboard)
    await callback.message.delete()
    await state.clear()


async def foto_callback_products_movement(callback: types.CallbackQuery, state: FSMContext):
    """
    The product number is checked each time and if it is out of the list, is reset to zero,
    so you can scroll around.
    """
    data = await state.get_data()
    products = data["products"]
    product_number = data["product_number"] % len(products)
    product = products[product_number]
    photo = product.photo
    caption = "".join([product.material, "\n", product.size, "\n", product.price])
    link = product.site_link
    await callback.message.edit_media(types.InputMedia(media=photo,
                                                       type="photo",
                                                       caption=caption),
                                      reply_markup=make_inl_keyb(link))


async def foto_callback_previous_photo(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    product_number = data["product_number"]
    product_number -= 1
    await state.update_data(product_number=product_number)
    await foto_callback_products_movement(callback, state)


async def foto_callback_next_photo(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    product_number = data["product_number"]
    product_number += 1
    await state.update_data(product_number=product_number)
    await foto_callback_products_movement(callback, state)


def register_handlers(dp: Dispatcher):
    dp.message.register(open_galery, Text(text="Открыть галерею"))
    dp.message.register(show_canvas, Text(text=["Шары", "Яйца", "Шкатулки"]), MyStatesGroup.galery)
    dp.callback_query.register(foto_callback_like, MyStatesGroup.galery, F.data == "like")
    dp.callback_query.register(foto_callback_dislike, MyStatesGroup.galery, F.data == "dislike")
    dp.callback_query.register(foto_callback_main_menu, MyStatesGroup.galery, F.data == "main")
    dp.callback_query.register(foto_callback_previous_photo, MyStatesGroup.galery, F.data == "previous photo")
    dp.callback_query.register(foto_callback_next_photo, MyStatesGroup.galery, F.data == "next photo")
