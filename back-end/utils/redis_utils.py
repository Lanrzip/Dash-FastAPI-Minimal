from fastapi import Request
from redis import asyncio as aioredis
from redis.exceptions import AuthenticationError, TimeoutError, RedisError
from config.env import RedisConfig
from config.database import SessionLocal
from utils.log_utils import logger


class RedisUtil:
    """
    Redis相关方法
    """

    @classmethod
    async def create_redis_pool(cls) -> aioredis.Redis:
        """
        应用启动时初始化redis连接
        :return: Redis连接对象
        """
        logger.info("开始连接redis...")
        redis = await aioredis.from_url(
            url=f"redis://{RedisConfig.redis_host}",
            port=RedisConfig.redis_port,
            username=RedisConfig.redis_username,
            password=RedisConfig.redis_password,
            db=RedisConfig.redis_database,
            encoding="utf-8",
            decode_responses=True
        )
        try:
            connection = await redis.ping()
            if connection:
                logger.info("redis连接成功")
            else:
                logger.error("redis连接失败")
        except AuthenticationError as e:
            logger.error(f"redis用户名或密码错误，详细错误信息：{e}")
        except TimeoutError as e:
            logger.error(f"redis连接超时，详细错误信息：{e}")
        except RedisError as e:
            logger.error(f"redis连接错误，详细错误信息：{e}")
        return redis

    @classmethod
    async def close_redis_pool(cls, app):
        """
        应用关闭时关闭redis连接
        :param app: fastapi对象
        :return:
        """
        await app.state.redis.close()
        logger.info("关闭redis连接成功")

    @classmethod
    async def set(cls, request: Request, key: str, value, expire: int = 0):
        """
        设置redis缓存
        :param request: Request对象
        :param key: 键
        :param value: 值
        :param redis_token: redis对象
        :param expire: 过期时间
        :return:
        """
        await request.app.state.redis.set(key, value, ex=expire)

    @classmethod
    async def get(cls, request: Request, key: str):
        """
        获取redis缓存
        :param request: Request对象
        :param key: 键
        :param redis_token: redis对象
        :return: 值
        """
        return await request.app.state.redis.get(key)
    
    @classmethod
    async def delete(cls, request: Request, key: str):
        """
        删除redis缓存
        :param request: Request对象
        :param key: 键
        :param redis_token: redis对象
        :return:
        """
        await request.app.state.redis.delete(key)
        
    # @classmethod
    # async def init_sys_dict(cls, redis):
    #     """
    #     应用启动时缓存字典表
    #     :param redis: redis对象
    #     :return:
    #     """
    #     session = SessionLocal()
    #     await DictDataService.init_cache_sys_dict_services(session, redis)

    #     session.close()

    # @classmethod
    # async def init_sys_config(cls, redis):
    #     """
    #     应用启动时缓存参数配置表
    #     :param redis: redis对象
    #     :return:
    #     """
    #     session = SessionLocal()
    #     await ConfigService.init_cache_sys_config_services(session, redis)

    #     session.close()
