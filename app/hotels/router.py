from fastapi import APIRouter, Response, Depends
from app.hotels.dao import HotelsDAO
from app.database import async_session_maker
from sqlalchemy import select, update, delete
from sqlalchemy.orm import selectinload
from app.hotels.models import Hotels
from app.hotels.schemas import SHotels, SHotelUpdate
from app.exceptions import HotelAlreadyExistsException, HotelIsNotPresentException
from app.users.dependencies import get_current_user
from app.users.models import Users



router = APIRouter(
    prefix="/hotels",
    tags=["Отели"]
)


@router.get("/only_hotel")
async def get_only_hotels():
    return await HotelsDAO.find_all()




@router.get("/hotel&rooms")
async def get_hotels_and_rooms():
    async with async_session_maker() as session:
        query = (
            select(Hotels)
            .options(selectinload(Hotels.rooms))
            )
        
        res = await session.execute(query)
        result = res.scalars().all()
        return result
    

@router.get("/{id}")
async def get_hotel_by_id(id:int):
    async with async_session_maker() as session:
        existing_hotel = await HotelsDAO.find_one_or_none(id=id)
        if existing_hotel is None:
            raise HotelIsNotPresentException
        query = (
            select(Hotels)
            .options(selectinload(Hotels.rooms))
            .filter_by(id=id)
        )

        res = await session.execute(query)
        result = res.scalars().all()
        return result


@router.post("/add")
async def add_hotel(hotel_data: SHotels, user: Users =Depends(get_current_user)):
    existing_hotel = await HotelsDAO.find_one_or_none(name=hotel_data.name)
    if existing_hotel:
        raise HotelAlreadyExistsException

    await HotelsDAO.add(
        name=hotel_data.name,
        location=hotel_data.location,
        services=hotel_data.services,
        rooms_quantity=hotel_data.rooms_quantity,
        image_id=hotel_data.image_id
        )
    return "Added Hotel"


@router.put("/update/{id}")
async def update_hotel(id: int, hotel_data: SHotelUpdate):
    async with async_session_maker() as session:
        existing_hotel = await HotelsDAO.find_one_or_none(id=id)
        if existing_hotel is None:
            raise HotelIsNotPresentException
        
        old_hotel = update(Hotels).filter_by(id=id).values(
            location = hotel_data.location, 
            services = hotel_data.services,
            rooms_quantity = hotel_data.rooms_quantity,
            image_id = hotel_data.image_id
            )
        
        await session.execute(old_hotel)
        await session.commit()
        new_hotel = await HotelsDAO.find_one_or_none(id=id)
        return new_hotel


@router.delete("/delete/{id}")
async def delete_hotel(id: int):
    async with async_session_maker() as session:
        existing_hotel = await HotelsDAO.find_one_or_none(id=id)
        if existing_hotel is None:
            raise HotelIsNotPresentException

        deleting_hotel = delete(Hotels).where(Hotels.id==id).returning(Hotels)
        deleted_hote = await session.execute(deleting_hotel)
        await session.commit()

        return {"status":f"hotel_id: {id} is deleted!",
                "hotel" : deleted_hote.scalar(),
                }

