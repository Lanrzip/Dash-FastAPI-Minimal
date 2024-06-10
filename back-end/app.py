from fastapi import FastAPI
import uvicorn

from module.controller.login_controller import loginController
from config.env import AppConfig
from utils.redis_utils import RedisUtil
from utils.db_utils import init_create_table
from utils.log_utils import logger

app = FastAPI(
    title=AppConfig.app_name,
    root_path=AppConfig.app_root_path,
)

origins = [
    "http://localhost:8088",
    "http://127.0.0.1:8088",
]

app.include_router(loginController, prefix="/login", tags=["登录模块"])


@app.on_event("startup")
async def startup_event():
    logger.info(f"{AppConfig.app_name}开始启动")
    await init_create_table()
    app.state.redis = await RedisUtil.create_redis_pool()
    logger.info(f"{AppConfig.app_name}启动成功")


@app.on_event("shutdown")
async def shutdown_event():
    await RedisUtil.close_redis_pool(app)


if __name__ == '__main__':
    uvicorn.run(
        app='app:app',
        host=AppConfig.app_host,
        port=AppConfig.app_port,
        reload=AppConfig.app_reload
    )
