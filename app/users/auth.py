from passlib.context import CryptContext
from datetime import datetime, timezone, timedelta
import jwt
from pydantic import EmailStr

from app.users.dao import UsersDAO
from app.config import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data:dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, settings.ALGORITHM
    )
    return encoded_jwt


async def authenticate_user(email:EmailStr, password:str):
    user = await UsersDAO.find_one_or_none(email=email)
    if not (user and verify_password(password, user.hashed_password)):
        return None
    return user


# from secrets import token_bytes
# from base64 import b64encode
#
# print(b64encode(token_bytes(32)).decode())
# mUeeLEAhl7EFh7OU3z5gHRxvn9yl7KtnN3fEqoEow2w=