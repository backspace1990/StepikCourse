from pydantic import BaseModel
from typing import Optional




class SHotels(BaseModel):
    name: str
    location: str
    services: list
    rooms_quantity: int
    image_id: int


class SHotelUpdate(BaseModel):
    location: Optional[str] = None
    services: Optional[list] = None
    rooms_quantity: Optional[int] = 0
    image_id: Optional[int] = None