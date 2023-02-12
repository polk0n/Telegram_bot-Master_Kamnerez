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
