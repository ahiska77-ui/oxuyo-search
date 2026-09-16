from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def main_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🔍 Поиск"), KeyboardButton(text="💳 Купить")],
            [KeyboardButton(text="👑 VIP"), KeyboardButton(text="🎁 Бонус")],
            [KeyboardButton(text="🤝 Партнёры"), KeyboardButton(text="🎟 Промокод")],
            [KeyboardButton(text="👤 Профиль")]
        ],
        resize_keyboard=True
    )

def admin_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📊 Статистика", callback_data="admin_stats")],
            [InlineKeyboardButton(text="🎟 Создать промокод", callback_data="admin_create_promo")],
            [InlineKeyboardButton(text="👮 Назначить админа", callback_data="admin_set_admin")],
            [InlineKeyboardButton(text="👑 Выдать VIP", callback_data="admin_give_vip")],
            [InlineKeyboardButton(text="💎 Выдать запросы", callback_data="admin_give_queries")],
            [InlineKeyboardButton(text="📢 Рассылка", callback_data="admin_mailing")],
            [InlineKeyboardButton(text="📂 Управление базами", callback_data="db_manage")],
            [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_main")]
        ]
    )

def db_manage_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📤 Добавить базу", callback_data="db_add")],
            [InlineKeyboardButton(text="📂 Список баз", callback_data="db_list")],
            [InlineKeyboardButton(text="✏️ Переименовать", callback_data="db_rename")],
            [InlineKeyboardButton(text="🔄 Обновить", callback_data="db_update")],
            [InlineKeyboardButton(text="🗑 Удалить", callback_data="db_delete")],
            [InlineKeyboardButton(text="📊 Статистика баз", callback_data="db_stats")],
            [InlineKeyboardButton(text="⬅️ Назад", callback_data="admin_panel")]
        ]
    )

def payment_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⭐ Telegram Stars", callback_data="pay_stars")],
            [InlineKeyboardButton(text="💠 TON (CryptoBot)", callback_data="pay_ton")],
            [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_main")]
        ]
    )

def back_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_main")]
        ]
    )
