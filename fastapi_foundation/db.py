from sqlalchemy import create_engine
from sqlmodel import Session


# Create the database engine
engine = create_engine("sqlite:///carsharing.db",
            connect_args={"check_same_thread": False},# needed for SQLite to allow multiple threads to access the database
            echo= True       # Set to True to see SQL queries in the console
                    )


def get_session():
    """Get a new SQLModel session."""
    with Session(engine) as session:
        yield session