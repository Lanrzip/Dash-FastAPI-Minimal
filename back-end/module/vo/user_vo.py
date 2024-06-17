from pydantic import BaseModel
from typing import Union, Optional, List


class UserIn(BaseModel):
    """
    用户表对应pydantic模型
    """
    user_id: Optional[int]
    email: Optional[str]
    password: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    create_time: Optional[str]


    class Config:
        # 默认情况下，Pydantic 模型只接受字典形式的数据。通过启用 orm_mode，
        # Pydantic 模型可以直接从 ORM 模型实例中读取数据，而不需要将其显式转换为字典。
        orm_mode = True


# class CrudUserResponseOut(BaseModel):
#     """
#     操作用户响应模型
#     """
#     is_success: bool
#     message: str