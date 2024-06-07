from sqlalchemy import and_, or_, desc, func
from sqlalchemy.orm import Session
from module.entity.user_entity import User

class UserDao:
    """
    用户管理模块数据库操作层
    """

    @classmethod
    def get_user_by_name(cls, db: Session, user_name: str):
        """
        根据用户名获取用户信息
        :param db: orm对象
        :param user_name: 用户名
        :return: 当前用户名的用户信息对象
        """
        query_user_info = db.query(User) \
            .filter(User.user_name == user_name) \
            .distinct().first()

        return query_user_info