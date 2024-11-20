from app.database import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped, mapped_column


#class Users(Base):
#    __tablename__ = "users"
#
#    id = Column(Integer, primary_key=True, nullable=False)             #Old style
#    email = Column(String, nullable=False)
#    hashed_password = Column(String, nullable=False)


class Users(Base):
    __tablename__ = "users"

    id              : Mapped[int] = mapped_column(primary_key=True, nullable=False)
    email           : Mapped[str] = mapped_column(nullable=False)
    hashed_password : Mapped[str] = mapped_column(nullable=False)