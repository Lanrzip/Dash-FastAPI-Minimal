from fastapi import FastAPI
import uvicorn
from module.controller.login_controller import loginController
from config.env import AppConfig

app = FastAPI(
    title=AppConfig.app_name,
    root_path=AppConfig.app_root_path,
)

origins = [
    "http://localhost:8088",
    "http://127.0.0.1:8088",
]

app.include_router(loginController, prefix="/login", tags=["登录模块"])

if __name__ == '__main__':
    uvicorn.run(
        app='app:app',
        host=AppConfig.app_host,
        port=AppConfig.app_port,
        reload=AppConfig.app_reload
    )
