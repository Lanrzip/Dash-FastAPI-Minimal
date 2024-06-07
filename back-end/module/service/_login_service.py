from fastapi import Depends, Request, Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import JWTError, jwt

from datetime import timedelta, datetime
from typing import Union, Optional, Dict

from config.get_db import get_db
from config.env import JwtConfig
from module.vo.login_vo import UserLogin
from module.dao.login_dao import login_by_account
from utils.log_utils import logger
from utils.response_utils import LoginException
from utils.pwd_utils import PwdUtil



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login/loginByAccount")

class CustomOAuth2PasswordRequestForm(OAuth2PasswordRequestForm):
    """
    自定义OAuth2PasswordRequestForm类，增加用户邮箱
    """
    def __init__(
            self,
            grant_type: str = Form(default=None, regex="password"),
            username: str = Form(default=None),  # 必须要给默认值，否则会报错：422 Unprocessable Entity
            password: str = Form(),  # password是必填项
            scope: str = Form(default=""),
            client_id: Optional[str] = Form(default=None),
            client_secret: Optional[str] = Form(default=None),
            email: Optional[str] = Form(),
    ):
        super().__init__(grant_type=grant_type, username=username, password=password,
                         scope=scope, client_id=client_id, client_secret=client_secret)

        self.email = email
        


async def authenticate_user(query_db: Session, login_user: UserLogin):
    """
    根据用户名密码校验用户登录
    :param request: Request对象
    :param query_db: orm对象
    :param login_user: 登录用户对象
    :return: 校验结果
    """
    
    user = login_by_account(query_db, login_user.email)
    # print(user, 'user')
    if not user:
        logger.warning("用户不存在")
        raise LoginException(data="", message="用户不存在")
    if not PwdUtil.verify_password(login_user.password, PwdUtil.get_password_hash(user.password)):
        logger.warning("密码错误")
        raise LoginException(data="", message="密码错误")
    return user


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    """
    根据登录信息创建当前用户token
    :param data: 登录信息
    :param expires_delta: token有效期
    :return: token
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JwtConfig.jwt_secret_key, algorithm=JwtConfig.jwt_algorithm)
    return encoded_jwt