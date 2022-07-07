from pydantic import BaseModel


class EventBaseSchema(BaseModel):
    event_id: str
    state: str


class EventSchema(EventBaseSchema):
    coefficient: float
    deadline: int
