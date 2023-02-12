from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

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
