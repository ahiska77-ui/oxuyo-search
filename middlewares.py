from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from datetime import datetime

class AntiFloodMiddleware(BaseMiddleware):
    def __init__(self, limit=1, period=1.0):
        self.limit = limit
        self.period = period
        self.user_timestamps = {}

    async def __call__(self, handler, event, data):
        user_id = None
        if isinstance(event, Message):
            user_id = event.from_user.id
        elif isinstance(event, CallbackQuery):
            user_id = event.from_user.id

        if user_id:
            now = datetime.utcnow().timestamp()
            user_ts = self.user_timestamps.get(user_id, [])
            user_ts = [ts for ts in user_ts if now - ts < self.period]

            if len(user_ts) >= self.limit:
                if isinstance(event, Message):
                    await event.answer("⏳ Слишком много запросов. Подождите немного.")
                elif isinstance(event, CallbackQuery):
                    await event.answer("⏳ Подождите немного", show_alert=True)
                return

            user_ts.append(now)
            self.user_timestamps[user_id] = user_ts

        return await handler(event, data
