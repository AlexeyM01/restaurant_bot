from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(DateTime)
    guests = Column(Integer)

    def __repr__(self):
        return f"<Booking(name={self.name}, date={self.date}, guests={self.guests})>"


