"""Skill catalogue with per-area detail view."""
from __future__ import annotations

from aiogram import F, Router
from aiogram.types import CallbackQuery, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.services import content

router = Router(name="skills")

DIVIDER = "━━━━━━━━━━━━━━━"


def get_skills_menu_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for pos, category in enumerate(content.SKILL_CATEGORIES):
        kb.button(
            text=f"{category.emoji} {category.title}",
            callback_data=f"skill:{pos}",
        )
    kb.button(text="📋 همه مهارت‌ها", callback_data="skill:all")
    kb.button(text="🔙 منوی اصلی", callback_data="menu:main")
    kb.adjust(2)
    return kb.as_markup()


def get_skill_text(index: int) -> str:
    category = content.SKILL_CATEGORIES[index]
    rows = "\n".join(f"▫️ {item}" for item in category.items)
    return (
        f"{category.emoji} <b>{category.title}</b>\n"
        f"{DIVIDER}\n"
        f"{rows}"
    )


@router.callback_query(F.data == "menu:skills")
async def skills_callback(callback: CallbackQuery) -> None:
    await callback.answer()
    if callback.message is not None and hasattr(callback.message, "edit_text"):
        await callback.message.edit_text(
            f"🛠 <b>مهارت‌های تیم نمونه</b>\n"
            f"{DIVIDER}\n"
            "یک دسته را انتخاب کنید: 👇",
            reply_markup=get_skills_menu_keyboard(),
        )


@router.callback_query(F.data.startswith("skill:"))
async def skill_detail_callback(callback: CallbackQuery) -> None:
    await callback.answer()
    if callback.data is None:
        return
    _, _, value = callback.data.partition(":")
    kb = InlineKeyboardBuilder()
    if value == "all":
        text = content.get_skills_text()
    else:
        try:
            pos = int(value)
        except ValueError:
            return
        if not 0 <= pos < len(content.SKILL_CATEGORIES):
            return
        text = get_skill_text(pos)
    kb.button(text="📋 دسته‌بندی‌ها", callback_data="menu:skills")
    kb.button(text="🔙 منوی اصلی", callback_data="menu:main")
    kb.adjust(2)
    if callback.message is not None and hasattr(callback.message, "edit_text"):
        await callback.message.edit_text(text, reply_markup=kb.as_markup())
