from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from module.service.login_service import *
from module.vo.login_vo import *
# from utils.response_utils import *
from config.get_db import get_db

import uuid

loginController = APIRouter()


@loginController.post("/loginByAccount", response_model=Token)
async def login(form_data: CustomOAuth2PasswordRequestForm = Depends(),
                login_service: ILoginService = Depends(LoginService.instance),
                query_db: Session = Depends(get_db)):
    
    return await login_service.login(form_data, query_db)
