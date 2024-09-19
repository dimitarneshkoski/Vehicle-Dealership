from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas


def create_vehicle(db: Session, schema: schemas.VehicleSchema):
    vehicle = models.Vehicle(**schema.dict())
    db.add(vehicle)
    db.commit()
    db.refresh(vehicle)
    return vehicle

def read_vehicle(db: Session, vehicle_id: int):
    vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found!")
    return vehicle

def update_vehicle(db: Session, vehicle_id: int, schema: schemas.VehicleSchema):
    vehicle = read_vehicle(db, vehicle_id)

    if vehicle:
        for key, value in schema.dict().items():
            setattr(vehicle, key, value)

        db.commit()
        db.refresh(vehicle)
    return vehicle

def delete_vehicle(db: Session, vehicle_id: int):
    vehicle = read_vehicle(db, vehicle_id)

    db.delete(vehicle)
    db.commit()

    return vehicle

def list_all_vehicles(db: Session):
    return db.query(models.Vehicle).all()
