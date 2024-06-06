from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from config.env import DataBaseConfig

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DataBaseConfig.db_username}:{quote_plus(DataBaseConfig.db_password)}@" \
                          f"{DataBaseConfig.db_host}:{DataBaseConfig.db_port}/{DataBaseConfig.db_database}"


# SQLALCHEMY_DATABASE_URL: 使用前面构建的数据库连接 URL。
# echo: 如果为 True，SQLAlchemy 会打印所有执行的 SQL 语句，主要用于调试。
# max_overflow: 控制在连接池达到最大大小后可以增加的连接数量。
# pool_size: 连接池的大小。
# pool_recycle: 控制连接池中连接的生命周期（秒），用于防止连接超时。
# pool_timeout: 控制获取连接时的超时时间（秒）。
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # echo=DataBaseConfig.db_echo,
    # max_overflow=DataBaseConfig.db_max_overflow,
    # pool_size=DataBaseConfig.db_pool_size,
    # pool_recycle=DataBaseConfig.db_pool_recycle,
    # pool_timeout=DataBaseConfig.db_pool_timeout
)

SessionLocal = sessionmaker(
    # autocommit=False,
    # autoflush=False,
    bind=engine
)
Base = declarative_base()  # 对应peewee中的BaseModel
