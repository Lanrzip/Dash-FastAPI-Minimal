from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

import callbacks.layout_c.head_c


def render_head_content():

    team_list = [
        {
            'team_name': '团队 1',
            'team_logo': 'assets/imgs/logo-team-1.webp',
            'team_type': 'Free'
        },
        {
            'team_name': '团队 2',
            'team_logo': 'assets/imgs/logo-team-2.webp',
            'team_type': 'Pro'
        },
        {
            'team_name': '团队 3',
            'team_logo': 'assets/imgs/logo-team-3.webp',
            'team_type': 'Pro'
        }
    ]


    return fac.AntdRow(
        [
            fac.AntdCol(
                html.Div(
                    [
                        fac.AntdSelect(
                            options=[
                                {
                                    'label': html.Div(
                                        [
                                            fac.AntdImage(
                                                src=team.get('team_logo'),
                                                preview=False,
                                                height=24,
                                                width=24
                                            ),
                                            fac.AntdText(team.get('team_name')),
                                            fac.AntdText(team.get('team_type'), code=True, style={'marginLeft': '4px'})
                                        ],
                                        style={
                                            'display': 'flex',
                                            'alignItems': 'center',
                                            'gap': '6px',
                                            'margin': 'auto',
                                            'height': '100%'
                                        }
                                    ),
                                    'value': team.get('team_name')
                                }
                                for team in team_list
                            ],
                            placeholder='请选择',
                            bordered=False,
                            defaultValue=team_list[0].get('team_name'),
                            style={
                                'width': 170
                            }
                        ),
                        fuc.FefferyStyle(
                            rawStyle='''
                            .head-team-select-container .ant-select-selection-item {
                                font-weight: 600;
                                font-size: 0.875rem;
                                line-height: 1.57rem;
                            },
                            .head-team-select-container .ant-select-item {
                                min-height: 48px;
                            }
                            '''
                        )
                    ],
                    className='head-team-select-container'
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
                        fac.AntdButton(
                            '',
                            shape='circle',
                            size='large',
                            type='text',
                            icon=fac.AntdAvatar(
                                id='user-avatar',
                                mode='image',
                                src='https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/mock/assets/images/avatar/avatar-25.webp',
                            ),
                            id='head-user-info-button',
                        )
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


