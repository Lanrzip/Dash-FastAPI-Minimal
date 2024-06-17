import dash
from dash import dcc, set_props
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State
from flask import session

from server import app
from utils.common import validate_data_not_empty
from api.system import register_api


@app.callback(
    output=dict(
        last_name_form_status=Output('register-last-form-item', 'validateStatus'),
        first_name_form_status=Output('register-first-form-item', 'validateStatus'),
        email_form_status=Output('register-email-form-item', 'validateStatus'),
        password_form_status=Output('register-password-form-item', 'validateStatus'),
        last_name_form_help=Output('register-last-form-item', 'help'),
        first_name_form_help=Output('register-first-form-item', 'help'),
        email_form_help=Output('register-email-form-item', 'help'),
        password_form_help=Output('register-password-form-item', 'help'),
        redirect_container=Output('redirect-container', 'children', allow_duplicate=True),
        global_message_container=Output('global-message-container', 'children', allow_duplicate=True)
    ),
    inputs=dict(
        nClicks=Input('register-button', 'nClicks')
    ),
    state=dict(
        last_name=State('register-last-name', 'value'),
        first_name=State('register-first-name', 'value'),
        email=State('register-email', 'value'),
        password=State('register-password', 'value')
    ),
    prevent_initial_call=True
)
def register(nClicks, last_name, first_name, email, password):

    if nClicks:
        if all(validate_data_not_empty(item) for item in [last_name, first_name, email, password]):

            try:
                user_params = dict(last_name=last_name, first_name=first_name, email=email, password=password)
                print('---------- user_params ----------: ', user_params)
                userinfo_result = register_api(user_params)
                print('---------- userinfo_result ----------: ', userinfo_result)
                if userinfo_result['code'] == 200:
                    return dict(
                        last_name_form_status=None,
                        first_name_form_status=None,
                        email_form_status=None,
                        password_form_status=None,
                        last_name_form_help=None,
                        first_name_form_help=None,
                        email_form_help=None,
                        password_form_help=None,
                        redirect_container=dcc.Location(pathname='/login', id='register-redirect'),
                        global_message_container=fuc.FefferyFancyMessage('注册成功', type='success')
                    )
                else:
                    return dict(
                        last_name_form_status=None,
                        first_name_form_status=None,
                        email_form_status=None,
                        password_form_status=None,
                        last_name_form_help=None,
                        first_name_form_help=None,
                        email_form_help=None,
                        password_form_help=None,
                        redirect_container=None,
                        global_message_container=fuc.FefferyFancyMessage(userinfo_result.get('message'), type='error')
                    )
            except Exception as e:
                return dict(
                    last_name_form_status=None,
                    first_name_form_status=None,
                    email_form_status=None,
                    password_form_status=None,
                    last_name_form_help=None,
                    first_name_form_help=None,
                    email_form_help=None,
                    password_form_help=None,
                    redirect_container=None,
                    global_message_container=fuc.FefferyFancyMessage(f"接口异常: {str(e)}", type='error')
                )
        
        return dict(
            last_name_form_status=None if validate_data_not_empty(last_name) else 'error',
            first_name_form_status=None if validate_data_not_empty(first_name) else 'error',
            email_form_status=None if validate_data_not_empty(email) else 'error',
            password_form_status=None if validate_data_not_empty(password) else 'error',
            last_name_form_help=None if validate_data_not_empty(last_name) else '请输入性',
            first_name_form_help=None if validate_data_not_empty(first_name) else '请输入名',
            email_form_help=None if validate_data_not_empty(email) else '请输入邮箱',
            password_form_help=None if validate_data_not_empty(password) else '请输入密码',
            redirect_container=None,
            global_message_container=None
        )
    
    return dict(
        last_name_form_status=dash.no_update,
        first_name_form_status=dash.no_update,
        email_form_status=dash.no_update,
        password_form_status=dash.no_update,
        last_name_form_help=dash.no_update,
        first_name_form_help=dash.no_update,
        email_form_help=dash.no_update,
        password_form_help=dash.no_update,
        redirect_container=dash.no_update,
        global_message_container=dash.no_update
    )