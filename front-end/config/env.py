import os
import argparse
from pydantic_settings import BaseSettings
from functools import lru_cache
from dotenv import load_dotenv


class AppSettings(BaseSettings):

    app_env: str = 'dev'
    app_name: str = 'Minimal Dashboard'
    app_base_url: str = 'http://127.0.0.1:9099'
    app_proxy_path: str = '/dev-api'
    app_is_proxy: bool = False
    app_secret_key: str = 'DASH-FASTAPI-MINIMAL'
    app_host: str = 'localhost'
    app_port: int = 8088
    app_debug: bool = True
    app_compress_algorithm: str = 'br'
    app_compress_br_level: int = 11


class GetConfig:
    """
    获取配置
    """
    def __init__(self):
        self.parse_cli_args()

    # @lru_cache
    def get_app_config(self):

        return AppSettings()

    @staticmethod
    def parse_cli_args():
        """
        解析命令行参数
        """
        # 使用argparse定义命令行参数
        parser = argparse.ArgumentParser(description='命令行参数')
        parser.add_argument('--env', type=str, default='', help='运行环境')
        # 解析命令行参数
        args = parser.parse_args()
        # 设置环境变量，如果未设置命令行参数，默认APP_ENV为dev
        os.environ['APP_ENV'] = args.env if args.env else 'dev'
        # 读取运行环境
        run_env = os.environ.get('APP_ENV', '')
        # 运行环境未指定时默认加载.env.dev
        env_file = '.env.dev'
        # 运行环境不为空时按命令行参数加载对应.env文件
        if run_env != '':
            env_file = f'.env.{run_env}'
        # 加载配置
        load_dotenv(env_file)
    

get_config = GetConfig()
AppConfig = get_config.get_app_config()