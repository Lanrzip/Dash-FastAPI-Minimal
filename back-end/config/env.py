from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    """
    应用配置
    """
    app_env: str = 'dev'
    app_name: str = 'Dash-FasAPI-Minimal'
    app_root_path: str = '/dev-api'
    app_host: str = '0.0.0.0'
    app_port: int = 9099
    app_version: str = '0.0.0'
    app_reload: bool = True
    app_ip_location_query: bool = True
    app_same_time_login: bool = True


class DataBaseSettings(BaseSettings):
    """
    数据库配置
    """
    db_host: str = 'localhost'
    db_port: int = 3306
    db_username: str = 'root'
    db_password: str = '34808'
    db_database: str = 'dfm'
    db_echo: bool = True
    db_max_overflow: int = 10
    db_pool_size: int = 50
    db_pool_recycle: int = 3600
    db_pool_timeout: int = 30


class JwtSettings(BaseSettings):
    """
    Jwt配置
    """
    jwt_secret_key: str = 'b01c66dc2c58dc6a0aabfe2144256be36226de378bf87f72c0c795dda67f4d55'
    jwt_algorithm: str = 'HS256'
    jwt_expire_minutes: int = 1440
    jwt_redis_expire_minutes: int = 30

class GetConfig:
    """
    获取配置
    """

    def get_app_config(self):
        """
        获取应用配置
        """
        # 实例化应用配置模型
        return AppSettings()


    def get_database_config(self):
        """
        获取数据库配置
        """
        # 实例化数据库配置模型
        return DataBaseSettings()
    
    def get_jwt_config(self):
        """
        获取Jwt配置
        """
        # 实例化Jwt配置模型
        return JwtSettings()


get_config = GetConfig()

# 应用配置
AppConfig = get_config.get_app_config()

# 数据库配置
DataBaseConfig = get_config.get_database_config()

# Jwt配置
JwtConfig = get_config.get_jwt_config()