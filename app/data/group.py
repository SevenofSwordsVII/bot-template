"""Showcase content: group profile.

Plain editable values only — no messaging logic lives here.
To move to a database or admin UI later, swap the reader module
under app/services/content.py and leave handlers untouched.
"""
from __future__ import annotations

GROUP_NAME = "تیم نمونه"
GROUP_FIELD = "توسعه بک‌اند | Python ،FastAPI و ربات تلگرام"
GROUP_ABOUT = (
    "این ربات یک نمونه‌کار توسعه داده‌شده توسط میلاد جعفری، توسعه‌دهنده بک‌اند با Python است؛ "
    "برای معرفی مهارت‌ها، نمونه‌کارها و خدمات (بک‌اند، ربات تلگرام و اتوماسیون هوش مصنوعی) "
    "با معماری تمیز و ماژولار."
)
GROUP_SERVICES: list[str] = [
    "توسعه بک‌اند با Python و FastAPI (REST API ماژولار، Pydantic ،SQLAlchemy ،Alembic)",
    "طراحی و توسعه ربات‌های اختصاصی و تجاری تلگرام (اتصال به دیتابیس و API خارجی، پنل مدیریت)",
    "توسعه ایجنت‌های هوش مصنوعی و اتوماسیون (اتصال LLM به API و طراحی ورک‌فلوهای هوشمند)",
    "داکرایز و استقرار (Docker و Docker Compose، اجرای سرویس‌های چندکانتینری)",
]
GROUP_GOAL = "تبدیل نیاز کسب‌وکار به نرم‌افزار تمیز، امن، قابل تست و قابل توسعه؛ آماده استفاده در محیط واقعی."
