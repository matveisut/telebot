from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu_reply = [
    [KeyboardButton(text="🖼 Генерировать текст"),
    KeyboardButton(text="🖼 Генерировать текст"),
    KeyboardButton(text="клавиатура")],
    [KeyboardButton(text="/register"),
    KeyboardButton(text="💰 Баланс")],
    [KeyboardButton(text="💎 Партнёрская программа"),
    KeyboardButton(text="🎁 Бесплатные токены")],
    [KeyboardButton(text="🔎 Помощь")]
]

menu = [
    [InlineKeyboardButton(text="q", callback_data="callback_q"),
    InlineKeyboardButton(text="w", callback_data="callback_w"),
    InlineKeyboardButton(text="e", callback_data="callback_e")],
]

start_kb = [[KeyboardButton(text="/start", callback_data = '/start')]]

start = ReplyKeyboardMarkup(keyboard=start_kb)
menu = InlineKeyboardMarkup(inline_keyboard=menu, resize_keyboard=True) #в чате
menu_reply = ReplyKeyboardMarkup(keyboard = menu_reply) #внутри 
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
