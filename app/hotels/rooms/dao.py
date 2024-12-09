from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.hotels.models import Rooms
from sqlalchemy import select, func, and_, or_, insert, update
from app.hotels.dao import HotelsDAO
from app.hotels.models import Rooms, Hotels
from app.exceptions import RoomIsNotPresentException, HotelIsNotPresentException, RoomAlreadyExistsException





class RoomsDAO(BaseDAO):
    model = Rooms
