"""Home inline menu shown after /start."""
from __future__ import annotations

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

MAIN_MENU_CALLBACKS = {
    "menu:group": "👥 معرفی گروه",
    "menu:members": "👨‍💻 اعضای تیم",
    "menu:skills": "🛠 مهارت‌ها",
    "menu:portfolio": "💼 نمونه‌کارها",
    "menu:contact": "📞 ارتباط با تیم",
    "menu:rate": "⭐ امتیاز به تیم",
}


def get_main_menu_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for callback_data, text in MAIN_MENU_CALLBACKS.items():
        kb.button(text=text, callback_data=callback_data)
    # two-column grid for the opening rows, single column for the last ones
    kb.adjust(2, 2, 1, 1)
    return kb.as_markup()
