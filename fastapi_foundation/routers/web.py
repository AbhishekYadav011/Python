from typing import Annotated
from fastapi import APIRouter, Cookie, Depends, Form , Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session

from db import get_session
from routers.cars import get_cars

router = APIRouter()
templates = Jinja2Templates(directory="templates")  

@router.get(path="/",response_class=HTMLResponse)
def home(request: Request,cars_cookie: Annotated[str | None,Cookie()]):
    print(cars_cookie)
    return templates.TemplateResponse("home.html", {"request": request})

@router.post(path="/search", response_class=HTMLResponse)
def search(size: Annotated[str, Form()], 
           doors: Annotated[int, Form()], 
           request: Request,
           session: Annotated[Session, Depends(get_session)]):
    
    """Search for cars based on size and number of doors."""
    cars =get_cars(session, size=size, doors=doors)
    return templates.TemplateResponse("search_results.html", {"request": request, "cars": cars})