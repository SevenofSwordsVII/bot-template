"""Tests for the content service (no Telegram objects required)."""
from __future__ import annotations

from app.services import content


def test_group_text_contains_name_and_services() -> None:
    text = content.get_group_text()
    assert content.GROUP_NAME in text
    if content.GROUP_FIELD:
        assert content.GROUP_FIELD in text
    if content.GROUP_GOAL:
        assert content.GROUP_GOAL in text
    for service in content.GROUP_SERVICES:
        assert service in text


def test_skills_text_contains_all_categories() -> None:
    text = content.get_skills_text()
    for category in content.SKILL_CATEGORIES:
        assert category.title in text
        for item in category.items:
            assert item in text


def test_member_links_skips_empty_urls() -> None:
    member = [m for m in content.MEMBERS if not m.linkedin][0]
    links = content.get_member_links(member)
    assert links, "member should have at least one link"
    assert all(url for _, url in links)
    assert not any("LinkedIn" in label for label, _ in links)


def test_project_links_skips_empty_urls() -> None:
    project = [p for p in content.PROJECTS if not p.github][0]
    links = content.get_project_links(project)
    assert links, "project should have at least one link"
    assert all(url for _, url in links)


def test_contact_links_all_have_urls() -> None:
    links = content.get_contact_links()
    assert len(links) == 4
    assert all(url.startswith("http") for _, url in links)


def test_members_and_projects_not_empty() -> None:
    assert len(content.MEMBERS) >= 1
    assert len(content.PROJECTS) >= 1
