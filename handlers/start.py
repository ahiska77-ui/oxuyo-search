from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from datetime import datetime

from database import async_session
from models import User
from keyboards import main_kb, back_kb

start_router = Router()

@start_router.message(F.text == "/start")
async def cmd_start(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    async with async_session() as session:
        user = await session.get(User, user_id)
        if not user:
            user = User(
                id=user_id,
                username=username,
                first_name=first_name,
                last_name=last_name,
                queries=3
            )
            session.add(user)
            await session.commit()

    await message.answer(
        f"👋 <b>Добро пожаловать в Ahiska Search!</b>\n\n"
        f"🔍 Поиск по:\n"
        f"• ФИО\n"
        f"• Номеру телефона\n"
        f"• Email\n"
        f"• Telegram\n"
        f"• Instagram\n"
        f"• Госномеру / VIN\n"
        f"• IP / домену\n"
        f"• ИНН компании\n\n"
        f"💎 У вас {user.queries} запросов\n"
        f"━━━━━━━━━━━━━━\n"
        f"Используйте меню ниже 👇",
        reply_markup=main_kb()
    )

@start_router.message(F.text == "👤 Профиль")
async def profile(message: Message):
    user_id = message.from_user.id

    async with async_session() as session:
        user = await session.get(User, user_id)
        if not user:
            await message.answer("❌ Пользователь не найден")
            return

        vip_status = "✅ Активен" if user.is_vip else "❌ Неактивен"
        vip_until = f"до {user.vip_until.strftime('%d.%m.%Y')}" if user.vip_until else "—"

        text = f"""
<b>👤 Ваш профиль</b>

🆔 ID: <code>{user.id}</code>
👤 Имя: {user.first_name or "—"}
💎 Запросов: {user.queries}
👑 VIP: {vip_status}
📅 VIP до: {vip_until}
💰 Реферальный баланс: {user.referral_balance} ₽
📊 Роль: {user.role}
"""
        await message.answer(text, reply_markup=back_kb())

@start_router.callback_query(F.data == "back_main")
async def back_main(callback: CallbackQuery):
    await callback.message.answer("Главное меню:", reply_markup=main_kb())
    await callback.answer()
