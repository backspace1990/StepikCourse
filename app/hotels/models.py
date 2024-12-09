from sqlalchemy import JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base


# class Hotels(Base):
#     __tablename__ = "hotels"
# 
#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     location = Column(String, nullable=False)                 #Old style
#     services = Column(JSON)
#     rooms_quantity = Column(Integer, nullable=False)
#     image_id = Column(Integer)


class Hotels(Base):
    __tablename__ = "hotels"

    id             : Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name           : Mapped[str] = mapped_column(nullable=False)
    location       : Mapped[str] = mapped_column(nullable=False)
    services       : Mapped[list[str]] = mapped_column(JSON)
    rooms_quantity : Mapped[int] = mapped_column(nullable=False)
    image_id       : Mapped[int]
    
    rooms          : Mapped[list["Rooms"]] = relationship(
        back_populates="hotel"
    )



class Rooms(Base):
    __tablename__ = "rooms"

    id          : Mapped[int] = mapped_column(primary_key=True, nullable=False)
    hotel_id    : Mapped[int] = mapped_column(ForeignKey("hotels.id", ondelete="CASCADE"), nullable=False)
    name        : Mapped[str] = mapped_column(nullable=False)
    description : Mapped[str] = mapped_column(nullable=False)
    price       : Mapped[int] = mapped_column(nullable=False)
    services    : Mapped[list[str]] = mapped_column(JSON, nullable=False)
    quantity    : Mapped[int] = mapped_column(nullable=False)
    image_id    : Mapped[int]

    hotel       : Mapped["Hotels"] = relationship(
        back_populates="rooms"
    )