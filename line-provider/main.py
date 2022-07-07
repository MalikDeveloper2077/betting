import asyncio
import decimal
import enum
import time
import random
from typing import Optional

import aiohttp
from fastapi import FastAPI, Path, HTTPException, BackgroundTasks
from pydantic import BaseModel

from .settings import get_settings


app = FastAPI()


class EventState(enum.Enum):
    NEW = 'new'
    WIN = 'win'
    LOSE = 'lose'


class Event(BaseModel):
    event_id: str
    coefficient: Optional[decimal.Decimal] = None
    deadline: Optional[int] = None
    state: Optional[EventState] = None


events: dict[str, Event] = {}


async def event_finish_callback(event_id: str | int, deadline: int):
    """Callback for betmaker service.
    Will make request when the event is finished
    """
    await asyncio.sleep(deadline - time.time())

    url = f'{get_settings().BETMAKER_DOMAIN}/bets/callback'
    event_state = random.choice([EventState.WIN.value, EventState.LOSE.value])

    async with aiohttp.ClientSession() as session:
        async with session.post(
            url,
            json={'event_id': event_id, 'state': event_state}
        ) as resp:
            return await resp.json()


@app.put('/event', response_model=Event)
async def create_event(event: Event, background_tasks: BackgroundTasks):
    """Create the event and add background task to notify betmaker
    service for the bet result: lose/win
    """
    if event.event_id in events:
        for p_name, p_value in event.dict(exclude_unset=True).items():
            setattr(events[event.event_id], p_name, p_value)

    events[event.event_id] = event
    background_tasks.add_task(event_finish_callback, event.event_id, event.deadline)

    return event


@app.get('/event/{event_id}', response_model=Event)
async def get_event(event_id: str = Path(default=None)):
    if event_id in events:
        return events[event_id]

    raise HTTPException(status_code=404, detail="Event not found")


@app.get('/events', response_model=list[Event])
async def get_events():
    return list(e for e in events.values() if time.time() < e.deadline)
