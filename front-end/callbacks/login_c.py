import dash
from dash import dcc, set_props
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State
from flask import session

from server import app
from utils.common import validate_data_not_empty
from api.login import login_api


@app.callback(
    # Output('login-button', 'loading_state'),
    inputs=dict(
        nClicks=Input('login-button', 'nClicks')
    ),
    state=dict(
        email=State('login-email', 'value'),
        password=State('login-password', 'value')
    ),
    prevent_initial_call=True
)
def login_auth(nClicks, email, password):

    if nClicks:
        if all(validate_data_not_empty(item) for item in [email, password]):

            try:
                user_params = dict(email=email, password=password)
                userinfo_result = login_api(user_params)
                if userinfo_result['code'] == 200:
                    token = userinfo_result['data']['access_token']
                    session['Authorization'] = token
                    set_props('global-message-container', {'children': fuc.FefferyFancyMessage('登陆成功', type='success')})
                    set_props('redirect-container', {'children': dcc.Location(pathname='/', id='login-redirect')})
                    set_props('token-container', {'data': token})
                    return
                else:
                    set_props('global-message-container', {'children': fuc.FefferyFancyMessage(userinfo_result.get('message'), type='error')})
                    return
            except Exception as e:
                set_props('global-message-container', {'children': fuc.FefferyFancyMessage('接口异常', type='error')})
                return

        set_props('login-email-form-item', {
            'validateStatus': None if validate_data_not_empty(email) else 'error',
            'help': None if validate_data_not_empty(email) else '请输入用户名！'
        })
        set_props('login-password-form-item', {
            'validateStatus': None if validate_data_not_empty(password) else 'error',
            'help': None if validate_data_not_empty(password) else '请输入密码！'
        })
        set_props('global-message-container', {'children': fuc.FefferyFancyMessage('用户名或密码不能为空', type='error')})
        return
    
    return