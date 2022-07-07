from enum import Enum

from tortoise import fields, Model


class BetState(Enum):
    NEW = 'new'
    WIN = 'win'
    LOSE = 'lose'


class Bet(Model):
    id = fields.IntField(pk=True)
    event_id = fields.IntField()
    state = fields.CharField(10, default=BetState.NEW.value)
    amount = fields.DecimalField(
        max_digits=10,
        decimal_places=2
    )
