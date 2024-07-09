from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn

from module.controller.system_controller import systemRouter
from config.env import AppConfig
from utils.redis_utils import RedisUtil
from utils.db_utils import init_create_table
from utils.log_utils import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        logger.info(f"{AppConfig.app_name}开始启动")
        await init_create_table()
        app.state.redis = await RedisUtil.create_redis_pool()
        logger.info(f"{AppConfig.app_name}启动成功")
        yield
    finally:
        await RedisUtil.close_redis_pool(app)


app = FastAPI(
    title=AppConfig.app_name,
    root_path=AppConfig.app_root_path,
    lifespan=lifespan
)


app.include_router(systemRouter, tags=["登录模块"])


# @app.on_event("startup")
# async def startup_event():
#     logger.info(f"{AppConfig.app_name}开始启动")
#     await init_create_table()
#     app.state.redis = await RedisUtil.create_redis_pool()
#     logger.info(f"{AppConfig.app_name}启动成功")


# @app.on_event("shutdown")
# async def shutdown_event():
#     await RedisUtil.close_redis_pool(app)



if __name__ == '__main__':
    uvicorn.run(
        app='app:app',
        host=AppConfig.app_host,
        port=AppConfig.app_port,
        reload=AppConfig.app_reload
    )
