from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, mapped_column, Mapped

from app.database import Base


# Модель написана в соответствии с современным стилем Алхимии (версии 2.x)
class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    hashed_password: Mapped[str]

    bookings: Mapped[list["Bookings"]] = relationship(back_populates="user")

    def __str__(self):
        return f"Пользователь {self.email}"
    
    
# Модель написана в соответствии со старым стилем Алхимии (версии 1.x)
# class Users(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, nullable=False)
#     email = Column(String, nullable=False)
#     hashed_password = Column(String, nullable=False)

#     booking = relationship("Bookings", back_populates="user")

#     def __str__(self):
#         return f"Пользователь {self.email}"
