import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import BOT_TOKEN
from database import init_db
from middlewares import AntiFloodMiddleware

from handlers.start import start_router
from handlers.search import search_router
from handlers.payment import payment_router
from handlers.promo import promo_router
from handlers.vip import vip_router
from handlers.referral import referral_router
from handlers.bonus import bonus_router
from handlers.admin import admin_router
from handlers.databases import databases_router

logging.basicConfig(level=logging.INFO)

async def main():
    await init_db()

    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.message.middleware(AntiFloodMiddleware())

    dp.include_router(start_router)
    dp.include_router(search_router)
    dp.include_router(payment_router)
    dp.include_router(promo_router)
    dp.include_router(vip_router)
    dp.include_router(referral_router)
    dp.include_router(bonus_router)
    dp.include_router(admin_router)
    dp.include_router(databases_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
