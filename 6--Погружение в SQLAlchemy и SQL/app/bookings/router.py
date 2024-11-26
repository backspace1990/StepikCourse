from fastapi import APIRouter, Request,Depends
from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBookings
from typing import Optional
from app.users.models import Users
from app.users.dependencies import get_current_user
from datetime import date
from app.exceptions import RoomCannotBeBooked



router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@router.get("/all_booking")
async def get_all_bookings(user: Users =Depends(get_current_user)):
   return await BookingDAO.find_all()


@router.get("/me")
async def get_me_bookings(user: Users =Depends(get_current_user)) -> list[SBookings]:
   return await BookingDAO.find_all(user_id=user.id)


@router.get("/{id}")
async def get_bookings_by_id(id:int):
   return await BookingDAO.find_by_id(id)


@router.post("")
async def add_booking(
   room_id: int,
   date_from: date,
   date_to: date,
   user: Users = Depends(get_current_user),
):
   booking = await BookingDAO.add(user.id, room_id, date_from, date_to)
   if not booking:
      raise RoomCannotBeBooked
