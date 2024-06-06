from sqlalchemy.orm import Session
from sqlalchemy import and_
from module.entity.do.user_do import SysUser


def login_by_account(db: Session, email: str):
    """
    根据用户名查询用户信息
    :param db: orm对象
    :param email: 用户邮箱
    :return: 用户对象
    """
    user = db.query(SysUser)\
        .filter(SysUser.email == email) \
        .distinct() \
        .first()

    return user
