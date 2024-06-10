from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from module.service.login_service import *
from module.vo.login_vo import *
# from utils.response_utils import *
from utils.db_utils import get_db

import uuid

loginController = APIRouter()


@loginController.post("/loginByAccount", response_model=Token)
async def login(request: Request,
                form_data: CustomOAuth2PasswordRequestForm = Depends(),
                login_service: ILoginService = Depends(LoginService.instance),
                query_db: Session = Depends(get_db)):
    
    return await login_service.login(request, form_data, query_db)


@loginController.post("/logout")
async def logout(request: Request,
                 login_service: ILoginService = Depends(LoginService.instance),
                 token: Optional[str] = Depends(oauth2_scheme)):
    # print('logout')
    return await login_service.logout(request, token)
