from pydantic import BaseModel
from typing import Optional


class UserLoginIn(BaseModel):
    
    email: str
    password: str


class TokenOut(BaseModel):
    access_token: str
    token_type: str


class RegisterUserIn(BaseModel):
    
    last_name: str
    first_name: str
    email: str
    password: str