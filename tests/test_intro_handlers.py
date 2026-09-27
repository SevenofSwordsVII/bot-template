"""Tests for the team-intro handlers (mocks, no bot instance required)."""
from __future__ import annotations

from unittest.mock import AsyncMock

from app.handlers import contact, group, members, portfolio, rating, skills, start


def make_callback(data: str) -> AsyncMock:
    callback = AsyncMock()
    callback.data = data
    return callback


async def test_start_handler_sends_welcome_with_menu() -> None:
    message = AsyncMock()

    await start.start_handler(message)

    message.answer.assert_called_once()
    text = message.answer.call_args.args[0]
    assert "خوش آمدید" in text
    assert message.answer.call_args.kwargs.get("reply_markup") is not None


async def test_back_to_main_edits_welcome() -> None:
    callback = make_callback("menu:main")

    await start.back_to_main_callback(callback)

    callback.answer.assert_called_once()
    callback.message.edit_text.assert_called_once()


async def test_group_callback_edits_group_text() -> None:
    callback = make_callback("menu:group")

    await group.group_callback(callback)

    callback.message.edit_text.assert_called_once()
    text = callback.message.edit_text.call_args.args[0]
    assert "تیم نمونه" in text


async def test_members_list_callback_shows_members() -> None:
    callback = make_callback("menu:members")

    await members.members_list_callback(callback)

    callback.message.edit_text.assert_called_once()
    text = callback.message.edit_text.call_args.args[0]
    assert "اعضای تیم" in text


async def test_member_detail_callback_valid_index() -> None:
    callback = make_callback("member:0")

    await members.member_detail_callback(callback)

    callback.message.edit_text.assert_called_once()


async def test_member_detail_callback_invalid_index_ignored() -> None:
    callback = make_callback("member:999")

    await members.member_detail_callback(callback)

    callback.message.edit_text.assert_not_called()


async def test_member_browser_wrap_around() -> None:
    from app.services import content

    total = len(content.MEMBERS)
    kb = members.get_member_browser_keyboard(0)
    callbacks = [b.callback_data for row in kb.inline_keyboard for b in row]
    assert f"member:{total - 1}" in callbacks  # prev of first wraps to last
    assert "member:1" in callbacks or total == 1


async def test_noop_callback_answers() -> None:
    callback = make_callback("noop")

    await members.noop_callback(callback)

    callback.answer.assert_called_once()
    callback.message.edit_text.assert_not_called()


async def test_skills_callback_shows_categories() -> None:
    callback = make_callback("menu:skills")

    await skills.skills_callback(callback)

    callback.message.edit_text.assert_called_once()
    text = callback.message.edit_text.call_args.args[0]
    assert "مهارت‌های تیم" in text


async def test_skill_detail_callback_valid_index() -> None:
    callback = make_callback("skill:0")

    await skills.skill_detail_callback(callback)

    callback.message.edit_text.assert_called_once()


async def test_skill_all_callback_shows_all() -> None:
    callback = make_callback("skill:all")

    await skills.skill_detail_callback(callback)

    callback.message.edit_text.assert_called_once()
    text = callback.message.edit_text.call_args.args[0]
    assert "مهارت‌های تیم" in text


async def test_skill_detail_callback_invalid_ignored() -> None:
    callback = make_callback("skill:999")

    await skills.skill_detail_callback(callback)

    callback.message.edit_text.assert_not_called()


async def test_portfolio_list_callback_shows_projects() -> None:
    callback = make_callback("menu:portfolio")

    await portfolio.portfolio_list_callback(callback)

    callback.message.edit_text.assert_called_once()
    text = callback.message.edit_text.call_args.args[0]
    assert "نمونه‌کارها" in text


async def test_project_detail_callback_invalid_index_ignored() -> None:
    callback = make_callback("project:999")

    await portfolio.project_detail_callback(callback)

    callback.message.edit_text.assert_not_called()


async def test_project_browser_wrap_around() -> None:
    from app.services import content

    total = len(content.PROJECTS)
    kb = portfolio.get_project_browser_keyboard(0)
    callbacks = [b.callback_data for row in kb.inline_keyboard for b in row]
    assert f"project:{total - 1}" in callbacks


async def test_contact_callback_edits_contact_text() -> None:
    callback = make_callback("menu:contact")

    await contact.contact_callback(callback)

    callback.message.edit_text.assert_called_once()
    text = callback.message.edit_text.call_args.args[0]
    assert "ارتباط با تیم" in text


async def test_rate_menu_callback_edits_rate_text() -> None:
    callback = make_callback("menu:rate")

    await rating.rate_menu_callback(callback)

    callback.message.edit_text.assert_called_once()


def test_setup_routers_registers_all() -> None:
    from app.handlers import setup_routers

    router = setup_routers()
    names = [r.name for r in router.sub_routers]
    assert names == ["start", "group", "members", "skills", "portfolio", "contact", "rating", "errors"]
