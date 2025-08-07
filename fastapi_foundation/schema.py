from sqlmodel import Relationship, SQLModel, Field, Column, VARCHAR
from passlib.context import CryptContext

# SQLModel inherits from Pydantic BaseModel, so we can use it to define our models.
# We can also use Pydantic's model_config to add extra metadata to the model.

pwd_context = CryptContext(schemes=["bcrypt"])


class TripInput(SQLModel):
    start: int
    end: int
    description: str

class TripOutput(TripInput):
    id: int

""" Relationships are used to define the relationship between models.
In this case, a Trip belongs to a Car, and a Car can have many Trips.
We use the `Relationship` class to define the relationship."""
# Pass `table=True` when creating the class to map this to a DB table.
class Trip(TripInput, table=True):
    id: int | None = Field(primary_key=True, default=None)
    car_id: int= Field(foreign_key="car.id")
    car: "Car" = Relationship(back_populates="trips")


class CarInput(SQLModel):
    size: str
    fuel: str | None = "electric"
    doors: int
    transmission: str | None = "auto"

    model_config = {
        "json_schema_extra": {
            "example": {
                "size": "compact",
                "fuel": "electric",
                "doors": 4,
                "transmission": "auto"
            }
        }
    }
# Pass `table=True` when creating the class to map this to a DB table.
class Car(CarInput, table=True):
    id: int|None = Field(primary_key=True,default=None)
    trips: list[Trip] = Relationship(back_populates="car")

class CarOutput(CarInput):
    """Output model for Car, inheriting from CarInput."""
    id: int
    """nested Models example in CarOutput- one pydantic class holds another,like a car holds trips"""
    trips: list[TripOutput] = []


class UserOutput(SQLModel):
    id: int
    username: str


class User(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    # sa_column is used to define the SQLAlchemy column properties.This allows us to set constraints like unique and index.
    username: str = Field(sa_column=Column(VARCHAR, __name_pos="username", unique=True, index=True))
    password_hash: str = ""

    def set_password(self, password: str):
        """Set the password hash for the user."""
        self.password_hash = pwd_context.hash(password)

    def verify_password(self, password: str) -> bool:
        """Verify the password against the stored hash."""
        return pwd_context.verify(password, self.password_hash)