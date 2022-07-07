from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    BETMAKER_DOMAIN: str = 'http://fastapi_1:8000'


@lru_cache()
def get_settings():
    return Settings()
