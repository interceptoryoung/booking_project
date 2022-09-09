from typing import Optional
from sqlalchemy import JSON, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.database import Base


# Модель написана в соответствии с современным стилем Алхимии (версии 2.x)
class Rooms(Base):
    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(primary_key=True)
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.id"))
    name: Mapped[str]
    description: Mapped[Optional[str]]
    price: Mapped[int]
    services: Mapped[list[str]] = mapped_column(JSON)
    quantity: Mapped[int]
    image_id: Mapped[int]

    hotel: Mapped["Hotels"] = relationship(back_populates="rooms")
    bookings: Mapped[list["Bookings"]] = relationship(back_populates="room")

    def __str__(self):
        return f"Номер {self.name}"


# Модель написана в соответствии со старым стилем Алхимии (версии 1.x)
# class Rooms(Base):
#     __tablename__ = "rooms"

#     id = Column(Integer, primary_key=True)
#     hotel_id = Column(ForeignKey("hotels.id"), )
#     name = Column(String, )
#     description = Column(String, nullable=True)
#     price = Column(Integer, )
#     services = Column(JSON, nullable=True)
#     quantity = Column(Integer, )
    # image_id = Column(Integer)

#     hotel = relationship("Hotels", back_populates="rooms")
#     booking = relationship("Bookings", back_populates="room")

#     def __str__(self):
#         return f"Номер {self.name}"
