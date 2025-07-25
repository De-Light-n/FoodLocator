from fastapi import HTTPException, Response
from fastapi.routing import APIRouter
from authx import AuthX, AuthXConfig

from schemas import UserSchema, UserCreateSchema, UserLoginSchema, UserLoginSucsess
from models import User
from config import config as app_config

router = APIRouter()

config = AuthXConfig()
config.JWT_SECRET_KEY = app_config.SECRET_KEY
config.JWT_ACCESS_COOKIE_NAME = "auth_access_token"
config.JWT_REFRESH_COOKIE_NAME = "auth_refresh_token"
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config)

@router.get("/me", response_model=UserSchema)
def read_auth():
    return {"message": "Auth route"}


@router.post("/login", response_model=UserLoginSucsess, status_code=200)
def login(credentials: UserLoginSchema, responce: Response):
    if credentials.username == "test" and credentials.password == "password":
        token = security.create_access_token(uid="12345", data={"username": credentials.username})
        responce.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
        return {"access_token":token}   
    raise HTTPException(status_code=400, detail="Invalid credentials")

@router.post("/register")
def register(credentials: UserCreateSchema):
    user = User(**credentials)
    