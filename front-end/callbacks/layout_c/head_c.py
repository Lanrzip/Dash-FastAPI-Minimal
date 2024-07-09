import dash
from dash import dcc
from flask import session
from dash.dependencies import Input, Output, State

from server import app
from api.system import logout_api



# 打开用户信息抽屉回调
@app.callback(
    Output('user-info-drawer', 'visible'),
    Input('head-user-info-button', 'nClicks'),
    prevent_initial_call=True
)
def open_user_info_drawer(nClicks):
    return True


# 退出登录回调
@app.callback(
    [Output('redirect-container', 'children', allow_duplicate=True),
     Output('token-container', 'data', allow_duplicate=True)],
    Input('head-user-logout-button', 'nClicks'),
    prevent_initial_call=True
)
def logout(nClicks):

    if nClicks:
        result = logout_api()
        if result['code'] == 200:
            session.clear()

            return [
                dcc.Location(pathname='/login', id='router-redirect'),
                None
            ]

    return [dash.no_update] * 2