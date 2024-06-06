from pydantic import BaseModel
from typing import Optional


class UserLogin(BaseModel):
    
    email: str
    password: str
    # captcha: Optional[str]
    # session_id: Optional[str]
    # login_info: Optional[dict]
    # captcha_enabled: Optional[bool]


class Token(BaseModel):
    access_token: str
    token_type: str