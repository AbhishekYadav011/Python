from db import get_session
from routers.auth import get_current_user
from schema import Car, CarInput, Trip, TripInput, User


from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import Session, select


from typing import Annotated


router = APIRouter(prefix="/api/cars")

""" Here we are using a dependency injection to get the session, which is injected into the function."""
# Declaring to FastAPI that this function depends on the session
@router.get("/")
def get_cars(session: Annotated[Session,Depends(get_session)],size:str|None =None, doors: int|None =None) -> list:
        query = select(Car)
        if size:
            query = query.where(Car.size == size)
        if doors:
            query = query.where(Car.doors >= doors)
        return session.exec(query).all()


@router.get("/{id}")
def car_by_id(session: Annotated[Session,Depends(get_session)],id: int)->Car:
    car = session.get(Car, id)
    if car:
        return car
    else:
        raise HTTPException(status_code=404, detail= f"No car found with id {id}")


@router.post("/")
def add_car(session: Annotated[Session,Depends(get_session)],
            user: Annotated[User, Depends(get_current_user)],
            car_input: CarInput) -> Car:
    """Add a new car to the database."""
    new_car = Car.model_validate(car_input)
    session.add(new_car)
    session.commit()
    session.refresh(new_car)
    return new_car


@router.delete(path="/{id}",status_code=204)
def remove_car(session: Annotated[Session,Depends(get_session)],id: int) -> None:
    car = session.get(Car, id)
    if car:
        session.delete(car)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"No car found with id {id}")


@router.put("/{id}")
def change_car(session: Annotated[Session,Depends(get_session)],id: int, new_data: CarInput) -> Car:
    car = session.get(Car, id)
    if car:
        car.size = new_data.size
        car.fuel = new_data.fuel
        car.transmission = new_data.transmission
        car.doors = new_data.doors
        session.commit()
        return car
    else:
        raise HTTPException(status_code=404, detail=f"No car found with id {id}")

class BadTripException(Exception):
    """Custom exception for bad trip data."""
    pass

@router.post("/{car_id}/trips")
def add_trip(session: Annotated[Session,Depends(get_session)],car_id: int,trip_input: TripInput)-> Trip:
    car = session.get(Car, car_id)
    if car:
        new_trip = Trip.model_validate(trip_input,update={"car_id": car_id})
        if new_trip.end <= new_trip.start:
            raise BadTripException("End time must be after start time.")
        car.trips.append(new_trip)
        session.commit()
        session.refresh(new_trip)
        return new_trip
    else:
        raise HTTPException(status_code=404, detail=f"No car found with id {car_id}")