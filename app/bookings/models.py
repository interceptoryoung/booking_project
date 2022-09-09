from datetime import date
from sqlalchemy import Column, Computed, Date, ForeignKey, Integer
from sqlalchemy.orm import relationship, mapped_column, Mapped

from app.database import Base


# Модель написана в соответствии с современным стилем Алхимии (версии 2.x)
class Bookings(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    date_from: Mapped[date] = mapped_column(Date)
    date_to: Mapped[date] = mapped_column(Date)
    price: Mapped[int]
    total_cost: Mapped[int] = mapped_column(Computed("(date_to - date_from) * price"))
    total_days: Mapped[int] = mapped_column(Computed("date_to - date_from"))

    user: Mapped["Users"] = relationship(back_populates="bookings")
    room: Mapped["Rooms"] = relationship(back_populates="bookings")

    def __str__(self):
        return f"Booking #{self.id}"


# Модель написана в соответствии со старым стилем Алхимии (версии 1.x)
# class Bookings(Base):
#     __tablename__ = "bookings"

#     id = Column(Integer, primary_key=True)
#     room_id = Column(ForeignKey("rooms.id"))
#     user_id = Column(ForeignKey("users.id"))
#     date_from = Column(Date, nullable=False)
#     date_to = Column(Date, nullable=False)
#     price = Column(Integer, nullable=False)
#     total_cost = Column(Integer, Computed("(date_to - date_from) * price"))
#     total_days = Column(Integer, Computed("date_to - date_from"))

#     user = relationship("Users", back_populates="booking")
#     room = relationship("Rooms", back_populates="booking")

#     def __str__(self):
#         return f"Booking #{self.id}"