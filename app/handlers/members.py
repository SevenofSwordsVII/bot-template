"""Team browser with pager and detail view."""
from __future__ import annotations

from aiogram import F, Router
from aiogram.types import CallbackQuery, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.services import content

router = Router(name="members")

DIVIDER = "━━━━━━━━━━━━━━━"


def get_members_list_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for pos, member in enumerate(content.MEMBERS):
        kb.button(
            text=f"👤 {member.name}",
            callback_data=f"member:{pos}",
        )
    kb.button(text="🔙 منوی اصلی", callback_data="menu:main")
    kb.adjust(2)
    return kb.as_markup()


def get_member_browser_keyboard(index: int) -> InlineKeyboardMarkup:
    total = len(content.MEMBERS)
    kb = InlineKeyboardBuilder()
    prev_pos = (index - 1) % total
    next_pos = (index + 1) % total
    kb.button(text="◀️ قبلی", callback_data=f"member:{prev_pos}")
    kb.button(text=f"{index + 1}/{total}", callback_data="noop")
    kb.button(text="بعدی ▶️", callback_data=f"member:{next_pos}")
    for text, url in content.get_member_links(content.MEMBERS[index]):
        kb.button(text=text, url=url)
    kb.button(text="📋 لیست اعضا", callback_data="menu:members")
    kb.button(text="🔙 منوی اصلی", callback_data="menu:main")
    kb.adjust(3, 1, 2)
    return kb.as_markup()


def get_member_text(index: int) -> str:
    member = content.MEMBERS[index]
    return (
        f"👨‍💻 <b>{member.name}</b>\n"
        f"{DIVIDER}\n"
        f"📌 <b>سمت:</b> {member.role}\n"
        f"⚙️ <b>تخصص:</b> {member.expertise}\n"
        f"{DIVIDER}\n"
        f"{member.bio}"
    )


@router.callback_query(F.data == "menu:members")
async def members_list_callback(callback: CallbackQuery) -> None:
    await callback.answer()
    if callback.message is not None and hasattr(callback.message, "edit_text"):
        await callback.message.edit_text(
            f"👨‍💻 <b>اعضای تیم نمونه</b> ({len(content.MEMBERS)} نفر)\n"
            f"{DIVIDER}\n"
            "برای مشاهده جزئیات، یک عضو را انتخاب کنید: 👇",
            reply_markup=get_members_list_keyboard(),
        )


@router.callback_query(F.data.startswith("member:"))
async def member_detail_callback(callback: CallbackQuery) -> None:
    await callback.answer()
    if callback.data is None:
        return
    try:
        index = int(callback.data.split(":", 1)[1])
    except (ValueError, IndexError):
        return
    if not 0 <= index < len(content.MEMBERS):
        return
    if callback.message is not None and hasattr(callback.message, "edit_text"):
        await callback.message.edit_text(
            get_member_text(index),
            reply_markup=get_member_browser_keyboard(index),
        )


@router.callback_query(F.data == "noop")
async def noop_callback(callback: CallbackQuery) -> None:
    await callback.answer()
