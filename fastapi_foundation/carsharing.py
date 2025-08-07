from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from sqlmodel import SQLModel
from contextlib import asynccontextmanager
from routers import cars, web, auth
from routers.cars import BadTripException
from fastapi.middleware.cors import CORSMiddleware
from db import engine

@asynccontextmanager # Lifespan event to create tables
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)  # Create the database tables
    yield  # This is where the application starts and returns control back to the function.

# Create the FastAPI app
app = FastAPI(title="Car Sharing Service API", lifespan=lifespan)
app.include_router(cars.router)
app.include_router(web.router)
app.include_router(auth.router)

origins = [
    "http://localhost:8000",
    "http://localhost:8080"
]

# CORS middleware to allow cross-origin requests from specified origins.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/")
# async def welcome(name):
#     return {"message": f"Welcome, {name} to the Car Sharing Service!"}

@app.exception_handler(BadTripException)
async def bad_trip_exception_handler(request: Request, exc: BadTripException):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"message": "Bad Trip"}
    )

@app.middleware("http")
async def add_cars_cookie(request: Request, call_next):
    response = await call_next(request)
    response.set_cookie(key="cars_cookie", value="you_visited_the_carsharing_service")
    return response




# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("carsharing:app", reload=True)