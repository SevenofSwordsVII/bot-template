"""Wire every section router into one root router."""
from __future__ import annotations

from aiogram import Router

from . import contact, errors, group, members, portfolio, rating, skills, start


def setup_routers() -> Router:
    router = Router(name="main")
    router.include_routers(
        start.router,
        group.router,
        members.router,
        skills.router,
        portfolio.router,
        contact.router,
        rating.router,
        errors.router,
    )
    return router
