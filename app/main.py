from fastapi import FastAPI, Depends, HTTPException
import time
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError
from app.db import SessionLocal, engine
from app.models import Base
from app import schemas, crud

app = FastAPI()

for i in range(5):
    try:
        Base.metadata.create_all(bind=engine)
        break
    except OperationalError:
        time.sleep(i + 1)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/vehicles/", response_model=schemas.VehicleSchema)
def create_vehicle(vehicle: schemas.VehicleSchema, db: Session = Depends(get_db)):
    return crud.create_vehicle(db=db, schema=vehicle)

@app.get("/vehicles/{vehicle_id}", response_model=schemas.VehicleSchema)
def read_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    db_item = crud.read_vehicle(db=db, vehicle_id=vehicle_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Vehicle not found!")
    return db_item

@app.put("/vehicles/{vehicle_id}", response_model=schemas.VehicleSchema)
def update_vehicle(vehicle_id: int, vehicle: schemas.VehicleSchema, db: Session = Depends(get_db)):
    db_item = crud.update_vehicle(db=db, vehicle_id=vehicle_id, schema=vehicle)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Vehicle not found!")
    return db_item

@app.delete("/vehicles/{vehicle_id}", response_model=schemas.VehicleSchema)
def delete_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete_vehicle(db=db, vehicle_id=vehicle_id)
    if db_item is None:
        raise HTTPException(status_code=400, detail="Vehicle not found!")
    return db_item

@app.get("/vehicles/", response_model=list[schemas.VehicleSchema])
def list_all_vehicles(db: Session = Depends(get_db)):
    return crud.list_all_vehicles(db=db)
