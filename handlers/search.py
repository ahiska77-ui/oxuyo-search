from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from database import async_session
from models import User
from utils import detect_search_type, truncate_text
from handlers.api_sources import search_fio, search_phone, search_email, search_telegram, search_car, search_domain, search_company

search_router = Router()

class SearchStates(StatesGroup):
    waiting_query = State()

@search_router.message(F.text == "🔍 Поиск")
async def search_start(message: Message, state: FSMContext):
    user_id = message.from_user.id

    async with async_session() as session:
        user = await session.get(User, user_id)
        if not user:
            await message.answer("❌ Пользователь не найден")
            return

        if user.queries <= 0:
            await message.answer("❌ У вас нет запросов. Купите в разделе 💳 Купить")
            return

    await message.answer(
        "🔍 <b>Введите данные для поиска:</b>\n\n"
        "• ФИО (Иванов Иван Иванович)\n"
        "• Номер телефона (79991234567)\n"
        "• Email (ivan@mail.ru)\n"
        "• Telegram (@username или ID)\n"
        "• Госномер (А123ВВ77) или VIN\n"
        "• IP-адрес или домен\n"
        "• ИНН компании\n\n"
        "Бот сам определит тип поиска."
    )
    await state.set_state(SearchStates.waiting_query)

@search_router.message(SearchStates.waiting_query)
async def search_process(message: Message, state: FSMContext):
    query = message.text.strip()
    user_id = message.from_user.id

    async with async_session() as session:
        user = await session.get(User, user_id)
        if not user or user.queries <= 0:
            await message.answer("❌ Недостаточно запросов")
            await state.clear()
            return

        user.queries -= 1
        await session.commit()

    search_type = detect_search_type(query)
    await message.answer(f"🔍 Ищу по <b>{search_type}</b>: {query}\n⏳ Пожалуйста, подождите...")

    result = ""
    if search_type == "fio":
        result = await search_fio(query)
    elif search_type == "phone":
        result = await search_phone(query)
    elif search_type == "email":
        result = await search_email(query)
    elif search_type == "telegram":
        result = await search_telegram(query)
    elif search_type == "car":
        result = await search_car(query)
    elif search_type == "domain":
        result = await search_domain(query)
    elif search_type == "company":
        result = await search_company(query)
    else:
        result = "❌ Не удалось определить тип поиска"

    await message.answer(truncate_text(result))
    await state.clear()
