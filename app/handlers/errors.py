"""Safety net — record unexpected failures while keeping the bot alive."""
from __future__ import annotations

import logging

from aiogram import Router
from aiogram.types import ErrorEvent

router = Router(name="errors")
logger = logging.getLogger(__name__)


@router.error()
async def error_handler(event: ErrorEvent) -> None:
    logger.exception("Uncaught failure while handling update: %s", event.exception)
