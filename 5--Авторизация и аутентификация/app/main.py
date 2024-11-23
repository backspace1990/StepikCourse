from fastapi import FastAPI, Query, Depends
import uvicorn
from datetime import date
from typing import Optional
from pydantic import BaseModel

from app.bookings.router import router as router_bookings
from app.users.router import router as router_users


app = FastAPI(title="FastAPI Stepik Courses")

app.include_router(router_users)
app.include_router(router_bookings)



@app.get("/hotels")
def get_hotels_root():
    return "Otel Antalya 5 yildiz" 


@app.get("/hotels_path_param_ex/{hotel_id}")#path param
def get_hotels(hotel_id: int):
    return hotel_id 


@app.get("/hotels_pat_and_puth_param_ex/{hotel_id}")#path param
def get_hotels(hotel_id: int, date_from, date_to): # query params date_from - date_to
    return {
        "hotel_id" : hotel_id, #path param        #http://127.0.0.1:8000/hotels_pat_and_puth_param_ex/1
        "date_from" : date_from, #query params    #?date_from=today
        "date_to": date_to, #query params         #&date_to=tomorrow
        }


@app.get("/hotels_params")
def get_hotels_params(
    location  : str,
    date_from : date,
    date_to   : date,
    has_spa   : Optional[bool] = None,
    stars     : Optional[int] = Query(None, ge=1, le=5),
    ):
    return {
        "location"  : location,
        "date_from" : date_from,
        "date_to"   : date_to,
        "has_spa"   : has_spa,
        "stars"     : stars,
        }


class SHotel(BaseModel):
    address: str
    name: str
    stars: int
    #has_spa: bool


@app.get("/Shotels_params", response_model=list[SHotel])
def get_Shotels_params(
    location  : str,
    date_from : date,
    date_to   : date,
    has_spa   : Optional[bool] = None,
    stars     : Optional[int] = Query(None, ge=1, le=5),
    ):
    hotels = [
        {
            "address": "273/6 sokak no 2 daire:21 kat:6 Mansuroglu/Bayrakli/IZMIR",
            "name": "Benim Evim",
            "stars": 5,
        }
    ]
    return hotels


@app.get("/Shotels_params_ex")
def get_Shotels_params_Ex_Responses_model(
    location  : str,
    date_from : date,
    date_to   : date,
    has_spa   : Optional[bool] = None,
    stars     : Optional[int] = Query(None, ge=1, le=5),
    ) -> list[SHotel]:
    hotels = [
        {
            "address": "273/6 sokak no 2 daire:21 kat:6 Mansuroglu/Bayrakli/IZMIR",
            "name": "Benim Evim",
            "stars": 5,
        }
    ]
    return hotels



class HotelsSearchArags:
    def __init__(
            self,
            location  : str,
            date_from : date,
            date_to   : date,
            has_spa   : Optional[bool] = None,
            stars     : Optional[int] = Query(None, ge=1, le=5),
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars


@app.get("/Shotels_params_ex1")
def get_Shotels_params_Ex1_Responses_model(
    search_args: HotelsSearchArags = Depends()
    ) -> list[SHotel]:
    hotels = [
        {
            "address": "273/6 sokak no 2 daire:21 kat:6 Mansuroglu/Bayrakli/IZMIR",
            "name": "Benim Evim",
            "stars": 5,
        }
    ]
    return hotels


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date



@app.post("/bookings")
def add_booking(booking: SBooking): #requests body
    pass




if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)