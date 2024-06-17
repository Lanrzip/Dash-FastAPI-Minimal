from sqlalchemy import and_, or_, desc, func
from sqlalchemy.orm import Session
from module.entity.user_entity import User
from module.vo.system_vo import RegisterUserIn

class UserDao:
    """
    用户管理模块数据库操作层
    """

    @classmethod
    def get_user_by_email(cls, db: Session, email: str):
        """
        根据用户名获取用户信息
        :param db: orm对象
        :param user_name: 用户名
        :return: 当前用户名的用户信息对象
        """
        query_user_info = db.query(User) \
            .filter(User.email == email) \
            .distinct().first()

        return query_user_info
    
    @classmethod
    def register_user(cls, db: Session, user: RegisterUserIn):
        """
        注册用户
        :param db: orm对象
        :param user: 用户信息
        :return: 注册成功的用户信息对象
        """
        db_user = User(**user.model_dump())
        db.add(db_user)
        db.flush()  # 将更改发送到数据库，但不会提交，直到调用commit()方法

        return db_user