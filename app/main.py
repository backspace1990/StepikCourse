from fastapi import FastAPI
import uvicorn
from app.bookings.router import router as router_bookings
from app.users.router import router as router_users
from app.hotels.router import router as router_hotels
from app.pages.router import router as router_pages
from app.hotels.rooms.router import router as router_rooms


app = FastAPI(title="FastAPI Stepik Courses")

app.include_router(router_users)
app.include_router(router_hotels)
app.include_router(router_rooms)
app.include_router(router_bookings)
app.include_router(router_pages)



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)