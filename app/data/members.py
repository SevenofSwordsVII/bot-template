"""Showcase content: people behind the team."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Member:
    name: str
    role: str
    expertise: str
    bio: str
    telegram: str = ""
    github: str = ""
    linkedin: str = ""


MEMBERS: list[Member] = [
    Member(
        name="میلاد جعفری",
        role="Backend Developer | Python",
        expertise="Python, FastAPI, REST API, PostgreSQL, Docker, AI Agents",
        bio=(
            "توسعه‌دهنده بک‌اند با Python؛ متخصص ساخت سرویس‌های قابل اعتماد، "
            "مقیاس‌پذیر و آماده استفاده در محیط واقعی. تمرکز من فقط «کار کردن» کد نیست؛ "
            "کد تمیز، امن، قابل تست و قابل توسعه می‌نویسم."
        ),
        telegram="https://t.me/sample_user",
        github="https://github.com/sample-user",
        linkedin="https://linkedin.com/in/sample-user",
    ),
    Member(
        name="کاربر نمونه",
        role="Test Developer",
        expertise="Python",
        bio="این یک عضو نمونه (تستی) است برای نمایش قابلیت مرور اعضا در ربات.",
        telegram="https://t.me/sample_user",
        github="https://github.com/example/sample-user",
        linkedin="",
    ),
]
