from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    username: str
    email: str
    
class UserLoginSchema(UserSchema):
    password: str 
    
class UserCreateSchema(UserLoginSchema):
    password_confirm: str
    
class UserLoginSucsess(BaseModel):
    access_token: str
    

