import os
import time
import dash
from loguru import logger
from config.env import AppConfig
from config.global_config import PathConfig


app = dash.Dash(
    __name__,
    compress=True,
    suppress_callback_exceptions=True,
    update_title=None,
    # external_stylesheets=[
    #     "./css/base.css",
    #     "./css/out.css",
    # ],
    serve_locally=True,
    # external_scripts=[
    #     # "https://unpkg.com/@material-tailwind/html@latest/scripts/ripple.js",
    #     # "node/node_modules/@material-tailwind/html/scripts/ripple.js"
    # ]
)


server = app.server


# 配置密钥
app.server.secret_key = AppConfig.app_secret_key
# app.server.config['COMPRESS_ALGORITHM'] = AppConfig.app_compress_algorithm
# app.server.config['COMPRESS_BR_LEVEL'] = AppConfig.app_compress_br_level

log_time = time.strftime("%Y%m%d", time.localtime())
api_log_file_path = os.path.join(PathConfig.ABS_ROOT_PATH, 'log', 'api_log', f'api_request_log_{log_time}.log')
# 日志过滤器 (filter):
# 使用 lambda record: '[api]' in record['message'] 作为过滤器，确保只有包含 [api] 字符串的日志消息才会记录到指定的日志文件。

# 文件回滚 (rotation):
# 设置 rotation="50MB"，当日志文件达到 50MB 时，将创建一个新的日志文件。这有助于管理日志文件的大小，防止单个日志文件过大。

# 文件编码 (encoding):
# 设置 encoding="utf-8"，确保日志文件以 UTF-8 编码存储，支持各种字符集。

# 异步记录 (enqueue):
# 设置 enqueue=True，启用异步日志记录。这样可以提高性能，特别是在高并发的场景下，防止日志记录成为性能瓶颈。

# 日志压缩 (compression):
# 设置 compression="zip"，当日志文件回滚时，将其压缩为 zip 文件，节省存储空间。
logger.add(api_log_file_path, filter=lambda x: '[api]' in x['message'],
           rotation="50MB", encoding="utf-8", enqueue=True, compression="zip")