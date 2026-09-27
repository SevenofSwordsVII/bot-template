"""Showcase content: skill set organised by area."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class SkillCategory:
    emoji: str
    title: str
    items: list[str] = field(default_factory=list)


SKILL_CATEGORIES: list[SkillCategory] = [
    SkillCategory(
        emoji="🐍",
        title="Backend | Python و FastAPI",
        items=[
            "Python",
            "FastAPI",
            "REST API",
            "Pydantic",
            "SQLAlchemy",
            "Alembic",
            "Swagger/OpenAPI",
            "JWT Auth",
        ],
    ),
    SkillCategory(
        emoji="✈️",
        title="Telegram Bot",
        items=[
            "Router-based Architecture",
            "ربات‌های تجاری و اتوماسیون",
            "اتصال به دیتابیس و API خارجی",
            "پنل مدیریت",
            "FSM و Middlewares",
        ],
    ),
    SkillCategory(
        emoji="🧠",
        title="AI Agents و اتوماسیون",
        items=[
            "AI Agents",
            "LLM Integration",
            "Workflowهای هوشمند",
            "اتصال مدل‌ها به API",
        ],
    ),
    SkillCategory(
        emoji="🗄️",
        title="Database و زیرساخت",
        items=[
            "PostgreSQL",
            "Redis",
            "Celery و Background Tasks",
            "Caching",
            "Async",
            "سرویس ایمیل",
        ],
    ),
    SkillCategory(
        emoji="🐳",
        title="Docker و Deployment",
        items=[
            "Docker",
            "Docker Compose",
            "سرویس‌های چندکانتینری",
            "Linux و VPS Deploy",
            "Env و تنظیمات پروژه",
        ],
    ),
    SkillCategory(
        emoji="🧪",
        title="Quality و همکاری",
        items=[
            "Pytest",
            "GitHub Actions (CI)",
            "Git و GitHub",
            "Branching و Pull Request",
            "Logging و مدیریت خطا",
        ],
    ),
]
