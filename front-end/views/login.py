from dash import html
import feffery_antd_components as fac

import callbacks.login_c



def render_content():

    return html.Div(
        [
            html.Div(
                [
                    # 左边
                    html.Div(
                        [
                            fac.AntdText(
                                "嗨，欢迎回来！",
                                style={
                                    'fontSize': '24px',
                                    'fontWeight': 'bold'
                                }
                            ),
                            fac.AntdImage(
                                src="./assets/imgs/illustration_dashboard.png",
                                preview=False
                            ),
                            html.Div(
                                [
                                    html.P("请使用您的用户名和密码登录")
                                ],
                                style={
                                    'marginTop': '20px',
                                    'color': 'rgba(0, 0, 0, 0.45)',
                                }
                            )
                        ],
                        className="min-w-[400px] h-screen flex flex-col justify-center items-center gap-20 flex-grow-1",
                        style={
                            'background': 'linear-gradient(rgba(255, 255, 255, 0.88), rgba(255, 255, 255, 0.88)) center center / cover no-repeat, url(/assets/imgs/overlay_2.jpg)',
                        }
                    ),
                    # 右边
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.P('登录至Mnimal', className="text-xl font-bold text-left"),
                                    html.Div(
                                        [
                                            html.P("新用户？"),
                                            html.A("立即创建", className="text-teal-500 font-bold hover:underline")
                                        ],
                                        className="flex"
                                    )
                                ],
                                className="w-full flex flex-col gap-4 text-left mb-10 mt-0"
                            ),
                            html.Div(
                                [
                                    fac.AntdIcon(
                                        icon='antd-alert',
                                        className="mr-3 py-1.5"
                                    ),
                                    html.Div(
                                        [
                                            "Use email : ",
                                            fac.AntdText("demo@minimals.cc ", strong=True),
                                            "/ password : ",
                                            fac.AntdText("demo1234", strong=True),
                                        ],
                                        className="py-2"
                                    )
                                ],
                                className="flex transition-shadow duration-300 ease-out delay-0 rounded-lg shadow-none bg-none leading-relaxed text-sm font-sans font-normal flex p-1.5 px-4 text-[#003768] bg-[#cafdf5] mb-6"
                            ),
                            html.Div(
                                    [
                                        fac.AntdFormItem(
                                            fac.AntdInput(
                                                id="login-email",
                                                prefix=fac.AntdIcon(
                                                    icon='antd-user'
                                                ),
                                                placeholder='请输入邮箱',
                                                className="h-12 rounded-lg"
                                            ),
                                            id='login-email-form-item',
                                            className='m-0'
                                        ),

                                        fac.AntdFormItem(
                                            fac.AntdInput(
                                                id="login-password",
                                                mode='password',
                                                passwordUseMd5=True,
                                                prefix=fac.AntdIcon(
                                                    icon='antd-lock'
                                                ),
                                                placeholder='请输入密码',
                                                className="h-12 rounded-lg"
                                            ),
                                            id='login-password-form-item',
                                            className='m-0'
                                        ),
                                        html.A(
                                            "忘记密码？",
                                            id='forget-password-link',
                                            href='/forget',
                                            target='_self',
                                            className="self-end text-xs text-blue-500 hover:underline m-0"
                                        ),
                                        fac.AntdButton(
                                            "登录",
                                            id="login-button",
                                            # autoSpin=True,
                                            className="w-full h-12 text-white bg-gray-800 hover:text-gray-800 hover:bg-white hover:border-gray-900 rounded-lg"
                                        )
                                    ],
                                    className='w-full flex flex-col gap-5'
                            ),
                        ],
                        className="max-w-[480px] h-screen flex flex-col items-center px-16 pt-40 pb-0",
                    ),
                ],
                className="flex"
            )
        ],
        id='container'
    )
