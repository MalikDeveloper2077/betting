from fastapi import APIRouter

from betmaker.core.models.bets import Bet
from betmaker.core.schemas.bets import Bet_Pydantic, BetIn_Pydantic
from betmaker.core.schemas.events import EventSchema, EventBaseSchema
from betmaker.services.lineprovider import get_available_events


router = APIRouter()


@router.get('/events', response_model=list[EventSchema])
async def get_events():
    return await get_available_events()


@router.get('/bets', response_model=list[Bet_Pydantic])
async def get_bets_history():
    return await Bet_Pydantic.from_queryset(Bet.all()) or []


@router.post('/bet', response_model=Bet_Pydantic)
async def create_bet(bet: BetIn_Pydantic):
    created_bet = await Bet.create(event_id=bet.event_id, amount=bet.amount)
    return await Bet_Pydantic.from_tortoise_orm(created_bet)


@router.post('/bets/callback')
async def bets_end_callback(event: EventBaseSchema):
    """Callback for updating bet states when event is finished"""
    return await Bet.filter(event_id=str(event.event_id)).update(state=event.state)
