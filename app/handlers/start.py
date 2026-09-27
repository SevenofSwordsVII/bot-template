"""Entry point: /start plus return-to-menu navigation."""
from __future__ import annotations

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message

from app.keyboards import get_main_menu_keyboard

router = Router(name="start")

WELCOME_TEXT = (
    "🌟 <b>به ربات معرفی تیم نمونه خوش آمدید</b> 👋\n"
    "━━━━━━━━━━━━━━━\n"
    "از منوی زیر می‌توانید با تیم، اعضا، مهارت‌ها و نمونه‌کارهای ما آشنا شوید.\n"
    "👇 یک بخش را انتخاب کنید:"
)


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(WELCOME_TEXT, reply_markup=get_main_menu_keyboard())


@router.callback_query(F.data == "menu:main")
async def back_to_main_callback(callback: CallbackQuery) -> None:
    await callback.answer()
    if callback.message is not None and hasattr(callback.message, "edit_text"):
        await callback.message.edit_text(
            WELCOME_TEXT, reply_markup=get_main_menu_keyboard()
        )
