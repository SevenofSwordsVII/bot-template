"""Project browser with pager and detail view."""
from __future__ import annotations

from aiogram import F, Router
from aiogram.types import CallbackQuery, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.services import content

router = Router(name="portfolio")

DIVIDER = "━━━━━━━━━━━━━━━"


def get_project_text(index: int) -> str:
    project = content.PROJECTS[index]
    stack = "، ".join(project.techs) if project.techs else "—"
    return (
        f"💼 <b>{project.name}</b>\n"
        f"{DIVIDER}\n"
        f"{project.description}\n"
        f"{DIVIDER}\n"
        f"🛠 <b>تکنولوژی‌ها:</b> {stack}"
    )


def get_project_browser_keyboard(index: int) -> InlineKeyboardMarkup:
    total = len(content.PROJECTS)
    kb = InlineKeyboardBuilder()
    prev_pos = (index - 1) % total
    next_pos = (index + 1) % total
    kb.button(text="◀️ قبلی", callback_data=f"project:{prev_pos}")
    kb.button(text=f"{index + 1}/{total}", callback_data="noop")
    kb.button(text="بعدی ▶️", callback_data=f"project:{next_pos}")
    for text, url in content.get_project_links(content.PROJECTS[index]):
        kb.button(text=text, url=url)
    kb.button(text="📋 لیست نمونه‌کارها", callback_data="menu:portfolio")
    kb.button(text="🔙 منوی اصلی", callback_data="menu:main")
    kb.adjust(3, 1, 2)
    return kb.as_markup()


def get_portfolio_list_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for pos, project in enumerate(content.PROJECTS):
        kb.button(
            text=f"💼 {project.name}",
            callback_data=f"project:{pos}",
        )
    kb.button(text="🔙 منوی اصلی", callback_data="menu:main")
    kb.adjust(1)
    return kb.as_markup()


@router.callback_query(F.data == "menu:portfolio")
async def portfolio_list_callback(callback: CallbackQuery) -> None:
    await callback.answer()
    if callback.message is not None and hasattr(callback.message, "edit_text"):
        await callback.message.edit_text(
            f"💼 <b>نمونه‌کارها</b> ({len(content.PROJECTS)} پروژه)\n"
            f"{DIVIDER}\n"
            "برای مشاهده جزئیات، یک پروژه را انتخاب کنید: 👇",
            reply_markup=get_portfolio_list_keyboard(),
        )


@router.callback_query(F.data.startswith("project:"))
async def project_detail_callback(callback: CallbackQuery) -> None:
    await callback.answer()
    if callback.data is None:
        return
    try:
        index = int(callback.data.split(":", 1)[1])
    except (ValueError, IndexError):
        return
    if not 0 <= index < len(content.PROJECTS):
        return
    if callback.message is not None and hasattr(callback.message, "edit_text"):
        await callback.message.edit_text(
            get_project_text(index),
            reply_markup=get_project_browser_keyboard(index),
        )


@router.callback_query(F.data == "noop")
async def noop_callback(callback: CallbackQuery) -> None:
    await callback.answer()
