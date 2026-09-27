"""Star-rating flow (scores from 1 to 5)."""
from __future__ import annotations

from aiogram import F, Router
from aiogram.types import CallbackQuery, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router(name="rating")

DIVIDER = "━━━━━━━━━━━━━━━"

RATE_TEXT = (
    "⭐ <b>امتیاز به تیم نمونه</b>\n"
    f"{DIVIDER}\n"
    "به تیم ما چند ستاره می‌دهید؟ 👇"
)

THANKS_TEXTS = {
    1: f"⭐\n{DIVIDER}\nممنون از نظرتان 🙏 حتماً تلاش می‌کنیم بهتر شویم.",
    2: f"⭐⭐\n{DIVIDER}\nممنون از نظرتان 🙏 حتماً تلاش می‌کنیم بهتر شویم.",
    3: f"⭐⭐⭐\n{DIVIDER}\nممنون! نظر شما به ما برای بهتر شدن کمک می‌کند.",
    4: f"⭐⭐⭐⭐\n{DIVIDER}\nخیلی ممنون! خوشحالیم که راضی بودید 🙏",
    5: f"⭐⭐⭐⭐⭐\n{DIVIDER}\nفوق‌العاده! خیلی ممنون از لطفتان 🙏",
}


def get_rate_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for stars in range(1, 6):
        kb.button(text="⭐" * stars, callback_data=f"rate:{stars}")
    kb.button(text="🔙 منوی اصلی", callback_data="menu:main")
    kb.adjust(1)
    return kb.as_markup()


@router.callback_query(F.data == "menu:rate")
async def rate_menu_callback(callback: CallbackQuery) -> None:
    await callback.answer()
    if callback.message is not None and hasattr(callback.message, "edit_text"):
        await callback.message.edit_text(RATE_TEXT, reply_markup=get_rate_keyboard())


@router.callback_query(F.data.startswith("rate:"))
async def rate_value_callback(callback: CallbackQuery) -> None:
    await callback.answer()
    if callback.data is None:
        return
    try:
        stars = int(callback.data.split(":", 1)[1])
    except (ValueError, IndexError):
        return
    if not 1 <= stars <= 5:
        return
    kb = InlineKeyboardBuilder()
    kb.button(text="🔙 بازگشت به منوی اصلی", callback_data="menu:main")
    if callback.message is not None and hasattr(callback.message, "edit_text"):
        await callback.message.edit_text(
            THANKS_TEXTS[stars], reply_markup=kb.as_markup()
        )
