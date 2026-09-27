"""Contact page with link buttons."""
from __future__ import annotations

from aiogram import F, Router
from aiogram.types import CallbackQuery, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.services import content

router = Router(name="contact")

DIVIDER = "━━━━━━━━━━━━━━━"

CONTACT_TEXT = (
    "📞 <b>ارتباط با تیم نمونه</b>\n"
    f"{DIVIDER}\n"
    f"📧 <b>ایمیل:</b> {content.CONTACT_EMAIL}\n"
    f"{DIVIDER}\n"
    "از دکمه‌های زیر برای ارتباط استفاده کنید: 👇"
)


def get_contact_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for text, url in content.get_contact_links():
        kb.button(text=text, url=url)
    kb.button(text="🔙 منوی اصلی", callback_data="menu:main")
    kb.adjust(2)
    return kb.as_markup()


@router.callback_query(F.data == "menu:contact")
async def contact_callback(callback: CallbackQuery) -> None:
    await callback.answer()
    if callback.message is not None and hasattr(callback.message, "edit_text"):
        await callback.message.edit_text(
            CONTACT_TEXT, reply_markup=get_contact_keyboard()
        )
