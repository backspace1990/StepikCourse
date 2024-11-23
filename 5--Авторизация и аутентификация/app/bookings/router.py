from fastapi import APIRouter, Request,Depends
from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBookings
from typing import Optional
from app.users.models import Users
from app.users.dependencies import get_current_user



router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@router.get("")
async def get_bookings(user: Users =Depends(get_current_user)):# -> list[SBookings]:
   # async with async_session_maker() as session:
   #     query = select(Bookings)
   #     result = await session.execute(query)
   #     #return result.scalars().all()
   #     #print(result.mappings().all())
   #     return result.mappings().all()
   #return await BookingDAO.find_all()

   #print(request.cookies)
   #print(request.url)
   #print(request.client)
   #return dir(request)
   print(user, type(user), user.email)
   #return await  BookingDAO.find_by_id()
   return user


@router.get("/me")
async def get_me_bookings(user: Users =Depends(get_current_user)):# -> list[SBookings]:
   return await BookingDAO.find_all(user_id=user.id)


@router.get("/{id}")
async def get_bookings_by_id(id:int):
   return await BookingDAO.find_by_id(id)

