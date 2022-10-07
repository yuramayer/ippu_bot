from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


program_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Обеспечение безопасности'),
        ],
        [
            KeyboardButton(text='Гос. и мун. управление')
        ],
        [
            KeyboardButton(text='Юриспруденция')
        ]
    ], resize_keyboard=True
)
