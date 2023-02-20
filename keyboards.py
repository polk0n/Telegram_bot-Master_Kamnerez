from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

keyboard_buttons = [
    [
        KeyboardButton(text="/description"),
        KeyboardButton(text="Открыть галерею")
    ],
]
keyboard = ReplyKeyboardMarkup(
    keyboard=keyboard_buttons,
    resize_keyboard=True
)

keyboard_galery_buttons = [
    [
        KeyboardButton(text="Шары"),
        KeyboardButton(text="Яйца"),
        KeyboardButton(text="Шкатулки")
    ],
]
keyboard_galery = ReplyKeyboardMarkup(
    keyboard=keyboard_galery_buttons,
    resize_keyboard=True
)


def make_inl_keyb(link):
    inl_keyboard_buttons = [
        [
            InlineKeyboardButton(text="Посмотреть на сайте", url=link),
            InlineKeyboardButton(text="👍 ", callback_data="like"),
            InlineKeyboardButton(text="👎 ", callback_data="dislike"),
            InlineKeyboardButton(text="Предыдущий товар", callback_data="previous photo"),
            InlineKeyboardButton(text="Следующий товар", callback_data="next photo"),
            InlineKeyboardButton(text="Главное меню", callback_data="main")
        ],
    ]
    inl_keyboard = InlineKeyboardMarkup(
        keyboard=inl_keyboard_buttons,
        resize_keyboard=True
    )
    return inl_keyboard
