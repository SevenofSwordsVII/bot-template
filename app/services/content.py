"""Content reader — the only bridge between handlers and data.

Handlers always go through this module instead of app.data.
To back the bot with a database or admin UI later, update this file only.
"""
from __future__ import annotations

from app.data import contact as contact_data
from app.data import group as group_data
from app.data import members as members_data
from app.data import portfolio as portfolio_data
from app.data import skills as skills_data
from app.data.contact import (
    CONTACT_EMAIL,
    CONTACT_GITHUB,
    CONTACT_LINKEDIN,
    CONTACT_TELEGRAM,
    CONTACT_WEBSITE,
)
from app.data.group import GROUP_ABOUT, GROUP_FIELD, GROUP_GOAL, GROUP_NAME, GROUP_SERVICES
from app.data.members import MEMBERS, Member
from app.data.portfolio import PROJECTS, Project
from app.data.skills import SKILL_CATEGORIES, SkillCategory

__all__ = [
    "CONTACT_EMAIL",
    "CONTACT_GITHUB",
    "CONTACT_LINKEDIN",
    "CONTACT_TELEGRAM",
    "CONTACT_WEBSITE",
    "GROUP_ABOUT",
    "GROUP_FIELD",
    "GROUP_GOAL",
    "GROUP_NAME",
    "GROUP_SERVICES",
    "MEMBERS",
    "PROJECTS",
    "SKILL_CATEGORIES",
    "Member",
    "Project",
    "SkillCategory",
    "contact_data",
    "get_contact_links",
    "get_group_text",
    "get_member_links",
    "get_project_links",
    "get_skills_text",
    "group_data",
    "members_data",
    "portfolio_data",
    "skills_data",
]

DIVIDER = "━━━━━━━━━━━━━━━"


def get_group_text() -> str:
    lines = [f"👥 <b>{GROUP_NAME}</b>", DIVIDER]
    if GROUP_FIELD:
        lines.append(f"📌 حوزه فعالیت: {GROUP_FIELD}")
    if GROUP_ABOUT:
        lines.append(GROUP_ABOUT)
    if GROUP_SERVICES:
        service_lines = "\n".join(f"▫️ {service}" for service in GROUP_SERVICES)
        lines.append(f"<b>خدمات اصلی:</b>\n{service_lines}")
    if GROUP_GOAL:
        lines.append(f"🎯 هدف: {GROUP_GOAL}")
    return "\n\n".join(lines)


def get_skills_text() -> str:
    sections: list[str] = []
    for category in SKILL_CATEGORIES:
        rows = "\n".join(f"▫️ {item}" for item in category.items)
        sections.append(f"{category.emoji} <b>{category.title}</b>\n{rows}")
    return f"🛠 <b>مهارت‌های تیم</b>\n{DIVIDER}\n\n" + "\n\n".join(sections)


def get_member_links(member: Member) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    if member.telegram:
        out.append(("✈️ Telegram", member.telegram))
    if member.github:
        out.append(("🐙 GitHub", member.github))
    if member.linkedin:
        out.append(("💼 LinkedIn", member.linkedin))
    return out


def get_project_links(project: Project) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    if project.github:
        out.append(("🐙 GitHub", project.github))
    if project.demo:
        out.append(("🚀 Demo", project.demo))
    if project.website:
        out.append(("🌐 Website", project.website))
    return out


def get_contact_links() -> list[tuple[str, str]]:
    return [
        ("✈️ Telegram", CONTACT_TELEGRAM),
        ("🐙 GitHub", CONTACT_GITHUB),
        ("💼 LinkedIn", CONTACT_LINKEDIN),
        ("🌐 Website", CONTACT_WEBSITE),
    ]
