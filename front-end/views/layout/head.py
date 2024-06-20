from dash import html
import feffery_antd_components as fac

import callbacks.layout_c.head_c


def render_head_content():
    return fac.AntdRow(
        [
            fac.AntdCol(
                html.Div(
                    fac.AntdSelect(
                        options=[
                            {
                                'label': f'选项{i}',
                                'value': f'选项{i}'
                            }
                            for i in range(1, 6)
                        ],
                        placeholder='请选择',
                        bordered=False,
                        style={
                            'width': 200
                        }
                    )
                ),
            ),
            fac.AntdCol(
                html.Div(
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
                            style={
                                'paddingRight': '8px',
                                'borderRadius': '12px',
                                'cursor': 'pointer',
                                'backgroundColor': 'rgba(var(--palette-grey-500Channel) / 0.08)',
                                'marginTop': '8px',
                                'display': 'flex',
                                'alignItems': 'center',
                                'justifyContent': 'center',
                            }
                        ),
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
                            title=html.Div(
                                [
                                    fac.AntdText('张三', strong=True),
                                    fac.AntdText('email')
                                ],
                                className='flex flex-col px-4 mt-4'
                            ),
                            content=html.Div(
                                [
                                    fac.AntdButton(
                                        '主页',
                                        type='text',
                                        block=True,
                                        className='text-left'
                                    ),
                                    fac.AntdButton(
                                        '个人资料',
                                        type='text',
                                        block=True,
                                        className='text-left'
                                    ),
                                    fac.AntdButton(
                                        '设置',
                                        type='text',
                                        block=True,
                                        className='text-left'
                                    ),
                                    fac.AntdDivider(),
                                    fac.AntdButton(
                                        '退出登录',
                                        type='text',
                                        block=True,
                                        id='head-user-logout',
                                    ),
                                ]
                            ),
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
            # 'backgroundColor': 'rgba(255, 255, 255, 0.8)',
        },
        wrap=False
    )


