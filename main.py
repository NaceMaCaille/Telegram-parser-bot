import os
import asyncio

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import router
from parser import client

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main():
    await client.start()
    dp.include_router(router)
    await dp.start_polling(bot)
    
    aiogram_parsing = asyncio.create_task(dp.start_polling(bot))
    
    await asyncio.sleep(120)
    await aiogram_parsing
    
if __name__ == '__main__':
    asyncio.run(main())
    
    