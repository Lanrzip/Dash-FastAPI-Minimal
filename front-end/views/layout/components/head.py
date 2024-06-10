from dash import html
import feffery_antd_components as fac

import callbacks.layout_c.head_c


def render_head_content():
    return fac.AntdRow(
        [
            fac.AntdCol(
                [
                    html.Div(
                        [
                            fac.AntdButton(
                                '',
                                shape='circle',
                                type='text',
                                icon=fac.AntdIcon(icon='fc-search')
                            ),
                            fac.AntdText(
                                '⌘K',
                                keyboard=True,
                            )
                        ],

                    )
                ],
            ),
            fac.AntdCol(
                html.Div(
                    [
                        fac.AntdPopover(
                            fac.AntdButton(
                                '',
                                shape='circle',
                                size='large',
                                type='text',
                                icon=fac.AntdIcon(icon='fc-like')
                            ),
                        ),
                        fac.AntdButton(
                            '',
                            shape='circle',
                            size='large',
                            type='text',
                            icon=fac.AntdIcon(icon='fc-advertising')
                        ),
                        fac.AntdPopover(
                            fac.AntdButton(
                                '',
                                shape='circle',
                                size='large',
                                type='text',
                                icon=fac.AntdIcon(icon='fc-conference-call')
                            )
                        ),
                        fac.AntdButton(
                            '',
                            shape='circle',
                            size='large',
                            type='text',
                            icon=fac.AntdIcon(icon='fc-settings')
                        ),
                        fac.AntdPopover(
                            fac.AntdButton(
                                '',
                                shape='circle',
                                size='large',
                                type='text',
                                icon=fac.AntdAvatar(
                                    id='avatar-info',
                                )
                            ),
                            # className='ml-2',
                            trigger='click',
                            placement='bottomRight',
                            title=[
                                fac.AntdText('张三', strong=True),
                                fac.AntdText('email')
                            ],
                            content=html.Div(
                                [
                                    fac.AntdButton(
                                        '个人中心',
                                        type='text',
                                        block=True,
                                        className='text-left'
                                    ),
                                    fac.AntdButton(
                                        '退出登录',
                                        type='text',
                                        block=True,
                                        id='head-user-logout',
                                        className='text-left'
                                    ),
                                ]
                            )
                        ),
                    ],
                    className='flex items-center justify-end flex-grow-1 gap-2'
                ),
                flex='auto'
            ),
        ],
        align='middle',
        style={
            'width': '100%',
            'backgroundColor': 'rgba(255, 255, 255, 0.8)',
        },
        wrap=False
    )


