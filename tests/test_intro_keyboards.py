"""Tests for the team-intro keyboards."""
from __future__ import annotations

from app.keyboards import (
    get_back_keyboard,
    get_back_to_main_keyboard,
    get_main_menu_keyboard,
)


def test_main_menu_has_five_buttons() -> None:
    kb = get_main_menu_keyboard()
    buttons = [btn for row in kb.inline_keyboard for btn in row]
    assert len(buttons) == 6
    assert buttons[0].callback_data == "menu:group"
    assert buttons[1].callback_data == "menu:members"
    assert buttons[2].callback_data == "menu:skills"
    assert buttons[3].callback_data == "menu:portfolio"
    assert buttons[4].callback_data == "menu:contact"
    assert buttons[5].callback_data == "menu:rate"


def test_back_keyboard_points_to_main() -> None:
    kb = get_back_keyboard()
    assert kb.inline_keyboard[0][0].callback_data == "menu:main"


def test_back_to_main_keyboard_label() -> None:
    kb = get_back_to_main_keyboard()
    btn = kb.inline_keyboard[0][0]
    assert btn.callback_data == "menu:main"
    assert "منوی اصلی" in btn.text
