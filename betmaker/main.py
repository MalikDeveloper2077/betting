from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from betmaker.core.settings import get_settings
from betmaker.v1.bets import router as bets_router


app = FastAPI()
app.include_router(bets_router)


register_tortoise(
    app,
    db_url=get_settings().DATABASE_URL,
    modules={"models": get_settings().TORTOISE_MODELS},
    generate_schemas=True,
    add_exception_handlers=True,
)
