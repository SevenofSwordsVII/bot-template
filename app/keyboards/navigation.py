"""Reusable back-navigation buttons."""
from __future__ import annotations

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_back_keyboard(back_to: str = "menu:main") -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="🔙 بازگشت", callback_data=back_to)
    return kb.as_markup()


def get_back_to_main_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="🔙 بازگشت به منوی اصلی", callback_data="menu:main")
    return kb.as_markup()


def with_back_button(
    keyboard: InlineKeyboardMarkup,
    back_to: str = "menu:main",
    back_text: str = "🔙 بازگشت",
) -> InlineKeyboardMarkup:
    keyboard.inline_keyboard.append(
        InlineKeyboardBuilder()
        .button(text=back_text, callback_data=back_to)
        .as_markup()
        .inline_keyboard[0]
    )
    return keyboard
