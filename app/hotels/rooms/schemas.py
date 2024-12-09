from pydantic import BaseModel
from typing import Optional


class SRooms(BaseModel):
    hotel_id: int
    name: str
    description: str
    price: int
    services: list
    quantity: int
    image_id: int


class SRoomUpdate(BaseModel):
    hotel_id: Optional[int] = None
    description: Optional[str] = None
    price: Optional[int] = None
    services: Optional[list] = None
    quantity: Optional[int] = None
    image_id: Optional[int] = None
