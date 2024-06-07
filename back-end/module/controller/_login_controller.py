from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from module.service.login_service import *
from module.vo.login_vo import *
from utils.response_utils import *
from config.get_db import get_db

import uuid

loginController = APIRouter()


@loginController.post("/loginByAccount", response_model=Token)
async def login(form_data: CustomOAuth2PasswordRequestForm = Depends(), query_db: Session = Depends(get_db)):
    # 类型验证
    user = UserLogin(
        **dict(
            email=form_data.email,
            password=form_data.password,
        )
    )
    try:
        result = await authenticate_user(query_db, user)
    except LoginException as e:
        return response_400(data="", message=e.message)
    
    try:

        access_token = result.email
        logger.info('登录成功')
        return response_200(
            data={'access_token': access_token, 'token_type': 'Bearer'},
            message='登录成功'
        )
    except Exception as e:
        logger.exception(e)
        return response_500(data="", message="登录失败")
