from pydantic import BaseModel

class VehicleSchema(BaseModel):

    vin_number: str
    make: str
    model: str
    year: int
    mileage: int
    engine: str
    color: str
    description: str
    available: bool
    price: float

