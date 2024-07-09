from fastapi import Depends, Request, Form
from sqlalchemy.orm import Session

from abc import ABC, abstractmethod

from module.vo.system_vo import RegisterUserIn
from module.dao.user_dao import *
from utils.log_utils import logger
from utils.response_utils import *


class IRegisterService(ABC):
        
    @abstractmethod
    async def register(self, request: Request, register_user_in: RegisterUserIn, query_db: Session):
        pass


class RegisterService(IRegisterService):
     
    async def register(self, request: Request, register_user_in: RegisterUserIn, query_db: Session):
        """
        根据注册信息注册用户
        :param request: Request对象
        :param form_data: 注册信息
        :param query_db: orm对象
        """
        print('-------- resgister service --------')
        try:
            user = UserDao.get_user_by_email(query_db, register_user_in.email)
            # print('user:', user)
            if user:
                result = dict(is_success=False, message='账号已存在')
            else:
                try:
                    UserDao.register_user(query_db, register_user_in)
                    query_db.commit()  # 提交事务
                    result = dict(is_success=True, message='注册成功')
                except Exception as e:
                    query_db.rollback()  # 回滚事务
                    result = dict(is_success=False, message='注册失败')

            if result.get('is_success'):
                logger.info(result.get('message'))
                return response_200(data=result, message=result.get('message'))
            else:
                logger.warning(result.get('message'))
                return response_400(data="", message=result.get('message'))
        except Exception as e:
            logger.exception(e)
            return response_500(data="", message=str(e))
    
    def __init__(self, request: Request):
        pass
        
    @classmethod
    async def instance(cls, request: Request):
        print('-------- resgister service instance --------')
        return cls(request)