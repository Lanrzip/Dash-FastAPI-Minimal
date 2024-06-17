import dash
from dash import dcc
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State
from flask import session

from server import app
from utils.common import validate_data_not_empty
from api.system import login_api


@app.callback(
    # Output('login-button', 'loading_state'),
    output=dict(
        email_form_status=Output('login-email-form-item', 'validateStatus'),
        password_form_status=Output('login-password-form-item', 'validateStatus'),
        email_form_help=Output('login-email-form-item', 'help'),
        password_form_help=Output('login-password-form-item', 'help'),
        token=Output('token-container', 'data'),
        redirect_container=Output('redirect-container', 'children', allow_duplicate=True),
        global_message_container=Output('global-message-container', 'children', allow_duplicate=True)
    ),
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
                    # set_props('global-message-container', {'children': fuc.FefferyFancyMessage('登陆成功', type='success')})
                    # set_props('redirect-container', {'children': dcc.Location(pathname='/', id='login-redirect')})
                    # set_props('token-container', {'data': token})
                    return dict(
                        email_form_status=None,
                        password_form_status=None,
                        email_form_help=None,
                        password_form_help=None,
                        token=token,
                        redirect_container=dcc.Location(pathname='/', id='login-redirect'),
                        global_message_container=fuc.FefferyFancyMessage('登陆成功', type='success')
                    )
                else:
                    # set_props('global-message-container', {'children': fuc.FefferyFancyMessage(userinfo_result.get('message'), type='error')})
                    return dict(
                        email_form_status=None,
                        password_form_status=None,
                        email_form_help=None,
                        password_form_help=None,
                        token=None,
                        redirect_container=None,
                        global_message_container=fuc.FefferyFancyMessage(userinfo_result.get('message'), type='error')
                    )
            except Exception as e:
                # set_props('global-message-container', {'children': fuc.FefferyFancyMessage('接口异常', type='error')})
                return dict(
                    email_form_status=None,
                    password_form_status=None,
                    email_form_help=None,
                    password_form_help=None,
                    token=None,
                    redirect_container=None,
                    global_message_container=fuc.FefferyFancyMessage(f'接口异常: {str(e)}', type='error')
                )

        # set_props('login-email-form-item', {
        #     'validateStatus': None if validate_data_not_empty(email) else 'error',
        #     'help': None if validate_data_not_empty(email) else '请输入用户名！'
        # })
        # set_props('login-password-form-item', {
        #     'validateStatus': None if validate_data_not_empty(password) else 'error',
        #     'help': None if validate_data_not_empty(password) else '请输入密码！'
        # })
        # set_props('global-message-container', {'children': fuc.FefferyFancyMessage('用户名或密码不能为空', type='error')})
        return dict(
            email_form_status=None if validate_data_not_empty(email) else 'error',
            password_form_status=None if validate_data_not_empty(password) else 'error',
            email_form_help=None if validate_data_not_empty(email) else '请输入邮箱！',
            password_form_help=None if validate_data_not_empty(password) else '请输入密码！',
            token=None,
            redirect_container=None,
            global_message_container=None
        )
    
    return dict(
        email_form_status=dash.no_update,
        password_form_status=dash.no_update,
        email_form_help=dash.no_update,
        password_form_help=dash.no_update,
        token=dash.no_update,
        redirect_container=dash.no_update,
        global_message_container=dash.no_update
    )