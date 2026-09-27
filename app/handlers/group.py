"""Group profile page."""
from __future__ import annotations

from aiogram import F, Router
from aiogram.types import CallbackQuery

from app.keyboards import get_back_to_main_keyboard
from app.services import content

router = Router(name="group")


@router.callback_query(F.data == "menu:group")
async def group_callback(callback: CallbackQuery) -> None:
    await callback.answer()
    if callback.message is not None and hasattr(callback.message, "edit_text"):
        await callback.message.edit_text(
            content.get_group_text(),
            reply_markup=get_back_to_main_keyboard(),
        )
