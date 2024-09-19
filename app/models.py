from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    ...

class Vehicle(Base):

     __tablename__ = 'vehicles'

     id: Mapped[int] = mapped_column(primary_key=True)
     vin_number: Mapped[str]
     make: Mapped[str]
     model: Mapped[str]
     year: Mapped[int]
     mileage: Mapped[int]
     engine: Mapped[str]
     color: Mapped[str]
     description: Mapped[str]
     available: Mapped[bool] = mapped_column(default=True)
     price: Mapped[float]


