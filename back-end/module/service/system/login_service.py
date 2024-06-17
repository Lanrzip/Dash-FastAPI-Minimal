from fastapi import Depends, Request, Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import JWTError, jwt

from datetime import timedelta, datetime
from typing import Union, Optional, Dict
from abc import ABC, abstractmethod
import uuid

from config.env import JwtConfig
from module.vo.system_vo import UserLogin
from module.dao.login_dao import login_by_account
from utils.log_utils import logger
from utils.response_utils import LoginException
from utils.pwd_utils import PwdUtil
from utils.redis_utils import RedisUtil
from utils.response_utils import *
from utils.db_utils import get_db
from config.env import RedisInitKeyConfig


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login/loginByAccount")

class CustomOAuth2PasswordRequestForm(OAuth2PasswordRequestForm):
    """
    自定义OAuth2PasswordRequestForm类，增加用户邮箱
    OAuth2 规范规定，对于密码流，应该使用表单数据（而不是 JSON）收集数据，
    并且应该具有特定字段“用户名”和“密码”。
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
        


class ILoginService(ABC):
    
    @abstractmethod
    async def login(self, request: Request, form_data: CustomOAuth2PasswordRequestForm, query_db: Session):
        pass

    @abstractmethod
    async def logout(self, request: Request, token: Optional[str]):
        pass


class LoginService(ILoginService):
    
    async def login(self, request: Request, form_data: CustomOAuth2PasswordRequestForm, query_db: Session):
        user = UserLogin(
            **dict(
                email=form_data.email,
                password=form_data.password,
            )
        )
        try:
            result = await self.authenticate_user(request, query_db, user)
        except LoginException as e:
            return response_400(data="", message=e.message)
        
        try:
            access_token_expires = timedelta(minutes=JwtConfig.jwt_expire_minutes)
            session_id = str(uuid.uuid4())
            access_token = self.create_access_token(
                data={
                    "email": result.email,
                    "session_id": session_id,
                },
                expires_delta=access_token_expires
            )
            logger.info('登录成功')
            return response_200(
                data={'access_token': access_token, 'token_type': 'Bearer'},
                message='登录成功'
            )
        except Exception as e:
            logger.exception(e)
            return response_500(data="", message="登录失败")

    
    async def logout(self, request: Request, token: Optional[str]):
        """
        用户登出
        :param request: Request对象
        :param token: token
        :return: 登出结果
        """
        try:
            payload = jwt.decode(token, JwtConfig.jwt_secret_key, algorithms=[JwtConfig.jwt_algorithm])
            session_id: str = payload.get("session_id")
            await RedisUtil.delete(request, f"{RedisInitKeyConfig.ACCESS_TOKEN.get('key')}:{session_id}")
            logger.info('退出成功')
            return response_200(data="", message="退出成功")
        except Exception as e:
            logger.exception(e)
            return response_500(data="", message=str(e))

    async def authenticate_user(self, request:Request, query_db: Session, login_user: UserLogin):
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
        account_lock = await RedisUtil.get(request, f"{RedisInitKeyConfig.ACCOUNT_LOCK.get('key')}:{login_user.email}")
        if login_user.email == account_lock:
            logger.warning("账号已锁定，请稍后再试")
            raise LoginException(data="", message="账号已锁定，请稍后再试")
        if not PwdUtil.verify_password(login_user.password, PwdUtil.get_password_hash(user.password)):
            cache_password_error_count = await RedisUtil.get(request, f"{RedisInitKeyConfig.PASSWORD_ERROR_COUNT.get('key')}:{login_user.email}")
            password_error_counted = 0
            if cache_password_error_count:
                password_error_counted = cache_password_error_count
            password_error_count = int(password_error_counted) + 1
            await RedisUtil.set(request, f"{RedisInitKeyConfig.PASSWORD_ERROR_COUNT.get('key')}:{login_user.email}", password_error_count,
                                            expire=timedelta(minutes=10))
            if password_error_count > 5:
                await RedisUtil.delete(request, f"{RedisInitKeyConfig.PASSWORD_ERROR_COUNT.get('key')}:{login_user.email}")
                await RedisUtil.set(request, f"{RedisInitKeyConfig.ACCOUNT_LOCK.get('key')}:{login_user.email}", login_user.email,
                                                expire=timedelta(minutes=10))
                logger.warning("10分钟内密码已输错超过5次，账号已锁定，请10分钟后再试")
                raise LoginException(data="", message="10分钟内密码已输错超过5次，账号已锁定，请10分钟后再试")
            logger.warning("密码错误")
            raise LoginException(data="", message="密码错误")
        await RedisUtil.delete(request, f"{RedisInitKeyConfig.PASSWORD_ERROR_COUNT.get('key')}:{login_user.email}")
        return user
    

    def create_access_token(self, data: dict, expires_delta: Union[timedelta, None] = None):
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
    
    
    def __init__(self, request: Request):
        pass
        
    @classmethod
    async def instance(cls, request: Request):
        return cls(request)