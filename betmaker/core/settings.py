from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = 'postgres://user:password@db/db'  # postgres
    TORTOISE_MODELS: list = ['betmaker.core.models.bets']
    LINE_PROVIDER_DOMAIN = 'http://127.0.0.1:8080'


@lru_cache()
def get_settings():
    return Settings()
