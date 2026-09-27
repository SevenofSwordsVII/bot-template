"""Runtime settings loaded from the environment file.

Expects BOT_TOKEN inside .env. The token value is never written to logs.
"""
from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def is_token_set(self) -> bool:
        return bool(self.bot_token) and self.bot_token != "YOUR_BOT_TOKEN_HERE"


settings = Settings()
