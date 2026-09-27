"""Showcase content: selected projects."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Project:
    name: str
    description: str
    techs: list[str] = field(default_factory=list)
    github: str = ""
    demo: str = ""
    website: str = ""


PROJECTS: list[Project] = [
    Project(
        name="ربات معرفی تیم (همین پروژه)",
        description=(
            "ربات معرفی تیم با منوی Inline، مرور اعضا و نمونه‌کارها، "
            "صفحه مهارت‌ها، امتیازدهی و معماری Router-based."
        ),
        techs=["Python", "Pytest", "Docker"],
        github="https://github.com/sample-user/team-intro-bot",
        demo="https://t.me/sample_bot",
        website="",
    ),
    Project(
        name="بک‌اند فروشگاهی با FastAPI (نمونه)",
        description=(
            "سرویس بک‌اند نمونه با REST API ماژولار، احراز هویت JWT، "
            "اعتبارسنجی Pydantic، دیتابیس PostgreSQL و مایگریشن Alembic."
        ),
        techs=["Python", "FastAPI", "PostgreSQL", "SQLAlchemy", "Alembic", "Docker"],
        github="https://github.com/sample-user/shop-backend-sample",
        demo="",
        website="",
    ),
    Project(
        name="ربات تجاری تلگرام با پنل مدیریت (نمونه)",
        description=(
            "ربات تلگرام نمونه با ثبت‌نام و احراز هویت کاربران، "
            "اتصال به دیتابیس و API خارجی و قابلیت‌های مدیریتی."
        ),
        techs=["Python", "PostgreSQL", "Redis"],
        github="https://github.com/sample-user/shop-bot-sample",
        demo="https://t.me/sample_shop_bot",
        website="",
    ),
    Project(
        name="سرویس اتوماسیون با ایجنت هوش مصنوعی (نمونه)",
        description=(
            "فرایند هوشمند نمونه با اتصال مدل زبانی به API و "
            "پردازش پس‌زمینه با Celery و Redis."
        ),
        techs=["Python", "FastAPI", "LLM", "Celery", "Redis", "Docker"],
        github="",
        demo="",
        website="https://example.com/report-automation",
    ),
]
