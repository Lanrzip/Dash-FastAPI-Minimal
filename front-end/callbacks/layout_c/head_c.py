import dash
from dash import dcc
from flask import session
from dash.dependencies import Input, Output, State

from server import app
from api.system import logout_api


# 退出登录回调
@app.callback(
    [Output('redirect-container', 'children', allow_duplicate=True),
     Output('token-container', 'data', allow_duplicate=True)],
    Input('head-user-logout', 'nClicks'),
    prevent_initial_call=True
)
def logout(nClicks):
    # print('logout')
    if nClicks:
        result = logout_api()
        if result['code'] == 200:
            session.clear()

            return [
                dcc.Location(pathname='/login', id='router-redirect'),
                None
            ]

    return [dash.no_update] * 2