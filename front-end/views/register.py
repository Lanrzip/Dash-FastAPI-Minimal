import os
import dash
from dash import html
import feffery_antd_components as fac

from views.login import render_layout_left
import callbacks.register_c



def render_layout_right():

    return html.Div(
        [
            html.Div(
                [
                    html.P('开始完全免费使用', className="text-xl font-bold text-left"),
                    html.Div(
                        [
                            html.P("已经有账号？"),
                            html.A(
                                "登录",
                                className="text-teal-500 font-bold hover:underline",
                                # id='login-link',
                                href='/login',
                                target='_self',
                            )
                        ],
                        className="flex"
                    )
                ],
                className="w-full flex flex-col gap-4 text-left mb-10 mt-0"
            ),
            html.Div(
                    [
                        html.Div(
                            [
                                fac.AntdFormItem(
                                    fac.AntdInput(
                                        id="register-last-name",
                                        prefix=fac.AntdImage(
                                            src='/assets/imgs/register/last-name.png',
                                            preview=False,
                                            height=14
                                        ),
                                        placeholder='请输入性',
                                        className="h-12 rounded-lg"
                                    ),
                                    id='register-last-form-item',
                                    className='m-0'
                                ),
                                fac.AntdFormItem(
                                    fac.AntdInput(
                                        id="register-first-name",
                                        prefix=fac.AntdImage(
                                            src='/assets/imgs/register/first-name.png',
                                            preview=False,
                                            height=14
                                        ),
                                        placeholder='请输入名',
                                        className="h-12 rounded-lg"
                                    ),
                                    id='register-first-form-item',
                                    className='m-0'
                                ),
                            ],
                            className="flex flex-row gap-5"
                        ),
                        fac.AntdFormItem(
                            fac.AntdInput(
                                id="register-email",
                                prefix=fac.AntdIcon(
                                    icon='antd-mail'
                                ),
                                placeholder='请输入邮箱',
                                className="h-12 rounded-lg"
                            ),
                            id='register-email-form-item',
                            className='m-0'
                        ),
                        fac.AntdFormItem(
                            fac.AntdInput(
                                id="register-password",
                                mode='password',
                                passwordUseMd5=True,
                                prefix=fac.AntdIcon(
                                    icon='antd-lock'
                                ),
                                placeholder='请输入密码',
                                className="h-12 rounded-lg"
                            ),
                            id='register-password-form-item',
                            className='m-0'
                        ),
                        fac.AntdButton(
                            "创建账号",
                            id="register-button",
                            # autoSpin=True,
                            className="w-full h-12 text-white bg-gray-800 hover:text-gray-800 hover:bg-white hover:border-gray-900 rounded-lg"
                        ),
                        fac.AntdParagraph(
                            [
                                fac.AntdText("通过注册，我同意"),
                                html.A("服务条款"),
                                fac.AntdText("和"),
                                html.A("隐私政策"),
                            ],
                            style={
                                'fontSize': '0.75rem',
                                'color': 'rgb(99, 115, 129)',
                                'textAlign': 'center'
                            }
                        )
                    ],
                    className='w-full flex flex-col gap-5'
            ),
        ],
        className="max-w-[480px] h-screen flex flex-col items-center px-16 pt-40 pb-0",
    )

def render_content():

    return html.Div(
        [
            html.Div(
                [
                    render_layout_left(title="使用Minimal更有效地管理作业"),
                    render_layout_right()
                ],
                className="flex"
            )
        ],
        # id='container'
    )