from pydantic import BaseModel, ConfigDict
from datetime import date


class SBookings(BaseModel):
    id         : int
    room_id    : int
    user_id    : int
    date_from  : date
    date_to    : date
    price      : int
    total_cost : int
    totel_days : int

    #class Config:
    #    orm_mode = True
    model_config = ConfigDict(from_attributes=True)