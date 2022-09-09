from sqlalchemy import JSON, Column, Integer, String
from sqlalchemy.orm import relationship, mapped_column, Mapped

from app.database import Base


# Модель написана в соответствии с современным стилем Алхимии (версии 2.x)
class Hotels(Base):
    __tablename__ = "hotels"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
    location: Mapped[str]
    services: Mapped[list[str]] = mapped_column(JSON)
    rooms_quantity: Mapped[int]
    image_id: Mapped[int]
    
    rooms: Mapped[list["Rooms"]] = relationship(back_populates="hotel")

    def __str__(self):
        return f"Отель {self.name} {self.location[:30]}"


# Модель написана в соответствии со старым стилем Алхимии (версии 1.x)
# class Hotels(Base):
#     __tablename__ = "hotels"

#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     location = Column(String, nullable=False)
#     services = Column(JSON)
#     rooms_quantity = Column(Integer, nullable=False)
#     image_id = Column(Integer)
    
#     rooms = relationship("Rooms", back_populates="hotel")

#     def __str__(self):
#         return f"Отель {self.name} {self.location[:30]}"
