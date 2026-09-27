"""Tests for the rating handler (mocks, no bot instance required)."""
from __future__ import annotations

from unittest.mock import AsyncMock

from app.handlers import rating


def make_callback(data: str) -> AsyncMock:
    callback = AsyncMock()
    callback.data = data
    return callback


def test_rate_keyboard_has_five_options_plus_back() -> None:
    kb = rating.get_rate_keyboard()
    buttons = [btn for row in kb.inline_keyboard for btn in row]
    assert len(buttons) == 6
    assert buttons[0].callback_data == "rate:1"
    assert buttons[4].callback_data == "rate:5"
    assert buttons[5].callback_data == "menu:main"


async def test_rate_menu_callback_edits_rate_text() -> None:
    callback = make_callback("menu:rate")

    await rating.rate_menu_callback(callback)

    callback.message.edit_text.assert_called_once()
    text = callback.message.edit_text.call_args.args[0]
    assert "امتیاز به تیم" in text


async def test_rate_value_callback_thanks_user() -> None:
    callback = make_callback("rate:5")

    await rating.rate_value_callback(callback)

    callback.message.edit_text.assert_called_once()
    text = callback.message.edit_text.call_args.args[0]
    assert "⭐" in text


async def test_rate_value_callback_invalid_ignored() -> None:
    callback = make_callback("rate:99")

    await rating.rate_value_callback(callback)

    callback.message.edit_text.assert_not_called()
