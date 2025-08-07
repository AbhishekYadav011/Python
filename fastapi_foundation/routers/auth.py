# Commented lines are used for basic authentication learning purposes.
# Uncomment them if you want to use basic authentication in your application.
# This file currently uses OAuth2 for authentication.

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
# from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlmodel import Session, select

from db import get_session
from schema import User, UserOutput



# security = HTTPBasic()

# def get_current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)],
#                      session: Annotated[Session, Depends(get_session)]) -> UserOutput:

#     # Query the database for the user with the provided username
#     query = select(User).where(User.username == credentials.username)
#     # Execute the query and get the first result
#     user = session.exec(query).first()
#     if user and user.verify_password(credentials.password):
#         return UserOutput.model_validate(user)
#     else:
#         raise HTTPException(status_code=401, detail="Invalid credentials")



URL_PREFIX ="/auth"
router = APIRouter(prefix=URL_PREFIX)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{URL_PREFIX}/token")

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)],
                     session: Annotated[Session, Depends(get_session)]) -> UserOutput:
    """Get the current user based on the provided token."""
    query = select(User).where(User.username == token)
    user = session.exec(query).first()
    if not user:
        raise HTTPException(status_code=401, 
                            detail="Invalid authentication credentials",
                            )
    return UserOutput.model_validate(user)

@router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                session: Annotated[Session, Depends(get_session)]):
    """Login and return a token."""
    query = select(User).where(User.username == form_data.username)
    user = session.exec(query).first()
    if user and user.verify_password(form_data.password):
        return {"access_token": user.username, "token_type": "bearer"}
    raise HTTPException(status_code=400, detail="Invalid credentials")