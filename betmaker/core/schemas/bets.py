from pydantic import validator
from tortoise.contrib.pydantic import pydantic_model_creator

from betmaker.core.models.bets import Bet, BetState


BetIn_Pydantic = pydantic_model_creator(Bet, name="BetIn", exclude=('id', 'state'))
BetWithoutState_Pydantic = pydantic_model_creator(Bet, name="Bet", exclude=('state',))


class Bet_Pydantic(BetWithoutState_Pydantic):
    state: str

    @validator('state')
    def allowed_state(cls, v):
        if v not in [s.value for s in BetState]:
            raise ValueError('Неизвестный статус ставки')
        return v
