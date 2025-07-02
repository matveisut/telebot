from config import BOT_TOKEN
from aiogram import Bot, Dispatcher
import asyncio
import handlers
import logging
from aiogram.enums import ParseMode
import database.models

async def main():
    await database.models.async_main()
    bot = Bot(token= BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(handlers.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

    print('бот выключен')