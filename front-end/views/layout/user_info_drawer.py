from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc


def render_drawer_layout():

    item_list = [
        {
            'button': '主页',
            'icon': 'antd-home',
            'href': ''
        },
        {
            'button': '个人资料',
            'icon': 'antd-user',
            'href': ''
        },
        {
            'button': '项目',
            'icon': 'antd-branches',
            'href': ''
        },
        {
            'button': '订阅',
            'icon': 'antd-book',
            'href': ''
        },
        {
            'button': '安全',
            'icon': 'antd-lock',
            'href': ''
        },
        {
            'button': '账户设置',
            'icon': 'antd-setting',
            'href': ''
        }
    ]


    layout = fac.AntdDrawer(
        [
            html.Div(
                [
                    fac.AntdAvatar(
                        mode='image',
                        src='https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/mock/assets/images/avatar/avatar-25.webp',
                        style={
                            'height': '86px',
                            'width': '86px'
                        }
                    ),
                    html.H6(
                        '张三',
                        style={
                            'fontWeight': '600',
                            'fontSize': '1rem',
                            'lineHeight': '1.5',
                            'margin': '16px 0 0',
                            'overflow': 'hidden',
                            'textOverflow': 'ellipsis'
                        }
                    ),
                    html.P(
                        'demo@minimals.cc',
                        style={
                            'margin': '4px 0 0',
                            'fontWeight': '400',
                            'fontSize': '0.875rem',
                            'lineHeight': '1.57',
                            'overflow': 'hidden',
                            'textOverflow': 'ellipsis',
                            'color': 'var(--palette-text-secondary)'
                        }
                    ),
                    html.Div(
                        [
                            fac.AntdButton(
                                item.get('button'),
                                type='text',
                                block=True,
                                icon=fac.AntdIcon(
                                    icon=item.get('icon'),
                                ),
                                style={
                                    'textAlign': 'left',
                                    'fontWeight': '400',
                                    'fontSize': '0.875rem',
                                    'lineHeight': '1.57',
                                    'color': 'var(--palette-text-secondary)',
                                    'height': '40px'
                                }
                            )
                            for item in item_list
                        ],
                        style={
                            'width': '100%',
                            'padding': '24px 0 0',
                        }
                    ),
                    fac.AntdButton(
                        '退出登录',
                        type='text',
                        block=True,
                        id='head-user-logout-button',
                        style={
                            'position': 'absolute',
                            'bottom': '0',
                            'borderRadius': '8px',
                            'color': 'var(--palette-error-dark)',
                            'backgroundColor': 'rgba(var(--palette-error-mainChannel) / 0.16)',
                            'height': '48px',
                            'fontWeight': '700',
                            'fontSize': '0.875rem',
                            'lineHeight': '1.71',
                        },
                    )
                ],
                style={
                    'padding': '64px 0 0',
                    'display': 'flex',
                    'flexDirection': 'column',
                    'alignItems': 'center',
                    'position': 'relative',
                    'height': '100%'
                }
            ),
            fuc.FefferyStyle(
                rawStyle='''
                .user-info-drawer .ant-drawer-content-wrapper {
                    border-radius: 10px 0 0 10px;
                    background-color: rgba(var(--palette-background-defaultChannel) / 0.5);
                    
                }

                .user-info-drawer .ant-drawer-content {
                    border-radius: 10px 0 0 10px;
                    box-shadow: -40px 40px 80px -8px rgba(var(--palette-grey-500Channel) / 0.24);
                    background-color: rgba(var(--palette-background-defaultChannel) / 0.8);
                    backdrop-filter: blur(20px);
                    
                }
                '''
            )
        ],
        id='user-info-drawer',
        className='user-info-drawer',
        width=320,
        maskStyle={
            'background': 'rgba(0, 0, 0, 0)'
        },
        headerStyle={
            'display': 'none'
        }
    )




    return layout