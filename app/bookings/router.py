from fastapi import APIRouter
from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBookings
from typing import Optional



router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@router.get("")
async def get_bookings() -> list[SBookings]:
   # async with async_session_maker() as session:



   #     query = select(Bookings)
   #     result = await session.execute(query)
   #     #return result.scalars().all()
   #     #print(result.mappings().all())
   #     return result.mappings().all()s
   return await BookingDAO.find_all()


@router.get("/{id}")
async def get_bookings_by_id(id:int):
   return await BookingDAO.find_by_id(id)

