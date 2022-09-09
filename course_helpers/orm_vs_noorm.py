"""
Поместите этот код в hotels/rooms/router.py, если хотите
увидеть работу SQLAlchemy ORM и получить вложенные структуры данных
"""

from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload
from app.hotels.models import Hotels
from app.hotels.rooms.models import Rooms
from app.bookings.models import Bookings
from app.database import async_session_maker
from fastapi.encoders import jsonable_encoder


@router.get("/example/no_orm")
async def get_noorm():
    async with async_session_maker() as session:
        query = (
            select(
                Rooms.__table__.columns, 
                Hotels.__table__.columns, 
                Bookings.__table__.columns
            )
            .join(Hotels, Rooms.hotel_id==Hotels.id)
            .join(Bookings, Bookings.room_id==Rooms.id)
        )
        res = await session.execute(query)
        res = res.mappings().all()
        return res


@router.get("/example/orm")
async def get_noorm():
    async with async_session_maker() as session:
        query = (
            select(Rooms)
            .options(joinedload(Rooms.hotel))
            .options(selectinload(Rooms.bookings))
        )
        res = await session.execute(query)
        res = res.scalars().all()
        res = jsonable_encoder(res)
        return res


# SELECT запрос без использования ORM стиля
[
    {
        # Данные о номере
        "room_id": 1,
        "room_name": "Номер люкс",

        # Данные об отеле
        "hotel_name": "Отель Алтай 5 звезд",
        "hotel_description": "...",

        # Данные о брони
        "booking_id": 1,
        "price": 123
    },
    {
        "room_id": 1,
        "room_name": "Номер люкс",

        "hotel_name": "Отель Алтай 5 звезд",
        "hotel_description": "...",

        "booking_id": 2,
        "price": 321
    }
]


# SELECT запрос с использованием ORM стиля
[
    {
        # Данные о номере
        "id": 1,
        "name": "Номер люкс",
        "hotel": {
            # Данные об отеле
            "id": 2,
            "name": "Отель Алтай 5 звезд",
            "description": "..."
        },
        "bookings": [
            # Данные о всех бронях
            {
                "id": 1,
                "price": 123
            },
            {
                "id": 2,
                "price": 321
            }
        ]
    },
]