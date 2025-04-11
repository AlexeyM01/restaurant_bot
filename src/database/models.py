"""
src/database/models.py
"""
from sqlalchemy import Column, Integer, String, DateTime
from src.database.database import Base


class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    date = Column(DateTime)
    guests = Column(Integer)

    def __repr__(self):
        return f"<Booking(name={self.name}, date={self.date}, guests={self.guests})>"
