from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu_reply = [
    [KeyboardButton(text="🖼 Генерировать текст", callback_data="generate_text"),
    KeyboardButton(text="🖼 Генерировать текст", callback_data="generate_text"),
    KeyboardButton(text="🖼 Генерировать текст", callback_data="generate_text")],
    [KeyboardButton(text="💳 Купить токены", callback_data="buy_tokens"),
    KeyboardButton(text="💰 Баланс", callback_data="balance")],
    [KeyboardButton(text="💎 Партнёрская программа", callback_data="ref"),
    KeyboardButton(text="🎁 Бесплатные токены", callback_data="free_tokens")],
    [KeyboardButton(text="🔎 Помощь", callback_data="help")]
]

menu = [
    [InlineKeyboardButton(text="🖼 Генерировать текст", callback_data="generate_text"),
    InlineKeyboardButton(text="🖼 Генерировать текст", callback_data="generate_text"),
    InlineKeyboardButton(text="🖼 Генерировать текст", callback_data="generate_text")],
    [InlineKeyboardButton(text="💳 Купить токены", callback_data="buy_tokens"),
    InlineKeyboardButton(text="💰 Баланс", callback_data="balance")],
    [InlineKeyboardButton(text="💎 Партнёрская программа", callback_data="ref"),
    InlineKeyboardButton(text="🎁 Бесплатные токены", callback_data="free_tokens")],
    [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")]
]

start_kb = [[KeyboardButton(text="/start", callback_data = '/start')]]

start = ReplyKeyboardMarkup(keyboard=start_kb)
menu = InlineKeyboardMarkup(inline_keyboard=menu, resize_keyboard=True) #в чате
menu_reply = ReplyKeyboardMarkup(keyboard = menu_reply) #внутри 
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
