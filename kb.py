from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

menu = [
    [InlineKeyboardButton(text= 'Гэмини', callback_data = 'generate_text')],
    InlineKeyboardButton(text= 'Генерировать изображение', callback_data = 'generate_image'),
    InlineKeyboardButton(text= 'Генерировать звук', callback_data = 'generate_sound')
]

menu = InlineKeyboardMarkup(inline_keyboard=menu)

exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])