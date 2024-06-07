from sqlalchemy import Column, Integer, String, DateTime, Boolean
from config.database import Base


class SysUser(Base):
    """
    用户表
    """
    __tablename__ = 'sys_user'

    user_id = Column(Integer, primary_key=True, autoincrement=True, comment='用户ID')
    email = Column(String(50, collation='utf8_general_ci'), nullable=False, comment='用户邮箱')
    password = Column(String(100, collation='utf8_general_ci'), default='', comment='密码')
    first_name = Column(String(30, collation='utf8_general_ci'), default='', comment='名')
    last_name = Column(String(30, collation='utf8_general_ci'), default='', comment='姓')