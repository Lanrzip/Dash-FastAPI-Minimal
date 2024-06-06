import requests
from typing import Optional
from flask import session, request

from config.env import AppConfig
from config.global_config import ApiBaseUrlConfig
from server import logger

def api_request(method: str, url: str, is_headers: bool, params: Optional[dict] = None, data: Optional[dict] = None,
                json: Optional[dict] = None, timeout: Optional[int] = None, stream: Optional[bool] = False):
    """
    API请求函数
    :param method: 请求方法
    :param url: 请求地址
    :param is_headers: 是否携带headers
    :param params: 请求参数
    :param data: 请求数据
    :param json: 请求json数据
    :param timeout: 请求超时时间
    :param stream: 是否以流的方式返回
    :return: 请求结果
    """
    api_url = ApiBaseUrlConfig.BaseUrl + url
    method = method.lower().strip()
    user_agent = request.headers.get('User-Agent')
    authorization = session.get('Authorization') if session.get('Authorization') else ''
    remote_addr = request.headers.get('X-Forwarded-For') if AppConfig.app_env == 'prod' else request.remote_addr
    if is_headers:
        api_headers = {'Authorization': 'Bearer ' + authorization, 'remote_addr': remote_addr,
                       'User-Agent': user_agent, 'is_browser': 'no'}
    else:
        api_headers = {'remote_addr': remote_addr, 'User-Agent': user_agent, 'is_browser': 'no'}

    try:
        request_methods = {
            'get': requests.get,
            'post': requests.post,
            'delete': requests.delete,
            'put': requests.put,
            'patch': requests.patch
        }
        if method not in request_methods:
            raise ValueError(f'不支持的请求方法：{method}')
        # print(api_url, params, data, json, api_headers, timeout, stream)
        response = request_methods[method](
            url=api_url, params=params, data=data, json=json, headers=api_headers,
            timeout=timeout, stream=stream
        )
        print('------------response------------', response.json())
        data_list = [params, data, json]
        if stream:
            pass
        else:
            response_code = response.json().get('code')
            response_message = response.json().get('message')
        print('------------session------------', session.get('user_info').get('user_name') if session.get('user_info') else None)
        session['code'] = response_code
        session['message'] = response_message
        if response_code == 200:
            logger.info("[api]请求人:{}||请求IP:{}||请求方法:{}||请求Api:{}||请求参数:{}||请求结果:{}",
                        session.get('user_info').get('user_name') if session.get('user_info') else None,
                        remote_addr,
                        method,
                        url,
                        ','.join([str(x) for x in data_list if x]),
                        response_message)
        else:
            logger.warning("[api]请求人:{}||请求IP:{}||请求方法:{}||请求Api:{}||请求参数:{}||请求结果:{}",
                           session.get('user_info').get('user_name') if session.get('user_info') else None,
                           remote_addr,
                           method,
                           url,
                           ','.join([str(x) for x in data_list if x]),
                           response_message)
            
        return response if stream else response.json()
    
    except Exception as e:
        logger.error("[api]请求人:{}||请求IP:{}||请求方法:{}||请求Api:{}||请求结果:{}",
                     session.get('user_info').get('user_name') if session.get('user_info') else None,
                     remote_addr,
                     method,
                     url,
                     str(e))

        session['code'] = 500
        session['message'] = str(e)

        return dict(code=500, data='', message=str(e))