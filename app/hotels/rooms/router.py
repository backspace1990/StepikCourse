from fastapi import APIRouter, Depends
from app.hotels.rooms.dao import RoomsDAO
from app.database import async_session_maker
from sqlalchemy import select, update, delete, insert
from app.users.models import Users
from app.exceptions import RoomIsNotPresentException, HotelIsNotPresentException, RoomCannotHotels
from app.hotels.models import Rooms, Hotels
from app.hotels.dao import HotelsDAO
from app.hotels.rooms.schemas import SRooms, SRoomUpdate


router = APIRouter(
    prefix="/rooms",
    tags=["Rooms-Комнаты"]
)


@router.get("/")
async def get_rooms():
    return await RoomsDAO.find_all()


@router.get("/{id}")
async def get_room_by_id(id:int):
    async with async_session_maker() as session:
        existing_room = await RoomsDAO.find_one_or_none(id=id)
        if existing_room is None:
            raise RoomIsNotPresentException
        query = (
            select(Rooms)
            .filter_by(id=id)
        )

        res = await session.execute(query)
        result = res.scalars().all()
        return result


@router.post("/add")
async def add_room(room_data: SRooms):
        async with async_session_maker() as session:
            existing_room_hotel_id = select(Hotels.id).filter_by(id = room_data.hotel_id)                                          
            existing_room_hotel = await session.execute(existing_room_hotel_id)
            if existing_room_hotel == None:
                raise HotelIsNotPresentException
            if room_data.quantity > 0:
                room_add=insert(Rooms).values(
                    hotel_id=room_data.hotel_id,
                    name=room_data.name,
                    description=room_data.description,
                    price=room_data.price,
                    services=room_data.services,
                    quantity=room_data.quantity,
                    image_id=room_data.image_id
                    ).returning(Rooms)

                get_old_quantity = select(Hotels.rooms_quantity).filter_by(id = room_data.hotel_id )
                old_quantity = await session.execute(get_old_quantity)
                hotel_quan: int = old_quantity.scalar()
                new_quantity = room_data.quantity + hotel_quan
                hotel_update = update(Hotels).filter_by(id=room_data.hotel_id).values(
                    rooms_quantity = new_quantity
                ).returning(Hotels)

                new_room = await session.execute(room_add)
                update_hotel = await session.execute(hotel_update)
                await session.commit() 


                return {"status":"Success",
                        "update_hotel" : update_hotel.scalar(),
                        "room_added" : new_room.scalar()
                    }

@router.put("/update/{id}")
async def update_room(id: int, room_data: SRoomUpdate):
    async with async_session_maker() as session:
        existing_room = await RoomsDAO.find_one_or_none(id=id)
        if existing_room is None:
            raise RoomIsNotPresentException
        
        room_update = update(Rooms).filter_by(id=id).values(
            hotel_id = room_data.hotel_id, 
            description = room_data.description, 
            price = room_data.price, 
            services = room_data.services, 
            quantity = room_data.quantity, 
            image_id = room_data.image_id, 
            ).returning(Rooms)
        
        hotel_id: int = existing_room.hotel_id
        old_room_quantity: int = existing_room.quantity
        get_old_quantity = select(Hotels.rooms_quantity).filter_by(id = hotel_id )
        old_quantity = await session.execute(get_old_quantity)
        hotel_quantity: int = old_quantity.scalar()
        new_room_quantity = hotel_quantity - old_room_quantity + room_data.quantity
        hotel_update = update(Hotels).filter_by(id=hotel_id).values(
                rooms_quantity = new_room_quantity
            ).returning(Hotels)
        
        updaed_room = await session.execute(room_update)
        update_hotel = await session.execute(hotel_update)
        await session.commit()
        return {
            "status" : "Success",
            "updaed_room" : updaed_room.scalar(),
            "update_hotel" : update_hotel.scalar()
        }


@router.delete("/delete/{room_id}")
async def delete_room(room_id: int):
    async with async_session_maker() as session:
        existing_room = await RoomsDAO.find_one_or_none(id=room_id)
        if existing_room is None:
            raise RoomIsNotPresentException

        hotel_id: int = existing_room.hotel_id
        del_room_quantity: int = existing_room.quantity
        get_old_quantity = select(Hotels.rooms_quantity).filter_by(id = hotel_id )
        old_quantity = await session.execute(get_old_quantity)
        hotel_quantity: int = old_quantity.scalar()
        new_room_quantity = hotel_quantity - del_room_quantity
        if new_room_quantity >= 0:
            hotel_update = update(Hotels).filter_by(id=hotel_id).values(
                rooms_quantity = new_room_quantity
            ).returning(Hotels)

            deleting_room = delete(Rooms).where(Rooms.id==room_id).returning(Rooms)
            
            deleted_room = await session.execute(deleting_room)
            update_hotel = await session.execute(hotel_update)
            await session.commit()

            return {"status":"Success!",
                    "deleted_room" : deleted_room.scalar(),
                    "updated_hotel" : update_hotel.scalar()
                    }
        else:
            raise RoomCannotHotels


