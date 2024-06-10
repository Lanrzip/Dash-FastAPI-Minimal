import dash
from dash import html, dcc, set_props
from dash.dependencies import Input, Output, State
import feffery_antd_components as fac
import feffery_utils_components as fuc
from flask import session

from server import app
from store import render_store_container
from config.env import AppConfig
from config.global_config import RouterConfig

import views

app.layout = html.Div(
    [
        # url监听
        fuc.FefferyLocation(id='url-container'),

        # 页面内容挂载点
        html.Div(id='app-mount'),

        html.Div(id='test-container'),
        # 重定向容器
        html.Div(id='redirect-container'),

        # store存储
        render_store_container(),

        # 注入全局消息提示容器
        html.Div(id='global-message-container'),
        # 注入全局通知信息容器
        html.Div(id='global-notification-container')
    ]
)


@app.callback(
    output=dict(
        app_mount=Output('app-mount', 'children'),
        redirect_container=Output('redirect-container', 'children', allow_duplicate=True),
        global_message_container=Output('global-message-container', 'children', allow_duplicate=True),
    ),
    inputs=dict(
        pathname=Input('url-container', 'pathname')
    ),
    state=dict(
        url_trigger=State('url-container', 'trigger'),
        session_token=State('token-container', 'data')
    ),
    prevent_initial_call=True,
)
def router(pathname, url_trigger, session_token):
    # 检查当前会话是否已经登录
    token_result = session.get('Authorization')
    # print('app.py--router:  ', token_result, session_token)
    # 若已登录
    if token_result and session_token and token_result == session_token:
        if pathname in RouterConfig.STATIC_VALID_PATHNAME:
            if pathname == '/':
                current_key = '首页'
            
            if url_trigger == 'load':
                
                if pathname == '/login' or pathname == '/forget':
                    # 若已登录且访问登录页面，则重定向至首页
                    return dict(
                        app_mount=dash.no_update,
                        redirect_container=dcc.Location(pathname='/', id='router-redirect'),
                        global_message_container=None
                    )

                # 正常渲染主页面
                return dict(
                    app_mount=views.layout.render_content(),
                    redirect_container=None,
                    global_message_container=None,
                )
            
            return dict(
                app_mount=dash.no_update,
                redirect_container=None,
                global_message_container=None,
            )
        
        else:
            # 返回404状态页面
            pass


    else:
        # 若未登录
        # 根据pathname控制渲染行为
        # 检验pathname合法性
        if pathname not in RouterConfig.BASIC_VALID_PATHNAME:
            # 返回404状态页面
            return dict(
                app_mount=views.page_404.render_content(),
                redirect_container=None,
                global_message_container=None,
            )

        if pathname == '/login':
            return dict(
                app_mount=views.login.render_content(),
                redirect_container=None,
                global_message_container=None,
            )
        
        if pathname == '/forget':
            return dict(
                app_mount=views.forget.render_content(),
                redirect_container=None,
                global_message_container=None,
            )
            # return
        
        # set_props('redirect-container', {'children': dcc.Location(pathname='/login', id='router-redirect')})
        # print("%%%%%%%%%")
        return dict(
            app_mount=dash.no_update,
            redirect_container=dcc.Location(pathname='/login', id='router-redirect'),
            global_message_container=None,
        )
        

if __name__ == '__main__':
    app.run(host=AppConfig.app_host, port=AppConfig.app_port, debug=AppConfig.app_debug)
