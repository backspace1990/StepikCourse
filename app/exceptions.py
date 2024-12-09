from fastapi import  HTTPException, status, Response, Depends


UserAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Пользователь уже существует"
)

UserIsNotPresentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Пользователь отсуствует"
)

UserIDIsNotInTokenJWTException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Пользователь отсуствует внутри JWT токена"
)

IncorrectEmailOrPasswordException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверная почта или пароль"
)

TokenExpiredException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Токен истек"
)


TokenAbsentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Токен отсуствует"
)


IncorrectTokenFormatException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверный формат Токена "
)


RoomCannotBeBooked = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Не осталось свободных номеров"
)

HotelAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Отель уже существует"
)

HotelIsNotPresentException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Hotel отсуствует"
)

RoomIsNotPresentException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Room отсуствует"
)

RoomAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Room уже существует"
)

RoomCannotHotels = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Не осталось комнаты Отеля"
)