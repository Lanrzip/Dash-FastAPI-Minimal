import dash
from dash import html, dcc
import feffery_antd_components as fac
import feffery_utils_components as fuc

from dash.dependencies import Input, Output, State

from server import app


def render_box(
    type,
):
    
    type_dict = {
        'income': {
            'icon-src': './assets/imgs/banking/income.png',
            'icon-background-color': 'var(--palette-primary-darker)',
            'title': 'Income',
            'title-tooltip': '收入',
            'amount': '￥9,990',
            'tag-icon': 'antd-rise',
            'tag-text': '+8.2%',
            'tag-color': 'var(--palette-success-dark)',
            'tag-background-color': 'rgba(var(--palette-success-mainChannel) / 0.16)',
            'text-color': 'var(--palette-text-primary)',
        },
        'expenses': {
            'icon-src': './assets/imgs/banking/expenses.png',
            'icon-background-color': 'var(--palette-warning-darker)',
            'title': 'Expenses',
            'title-tooltip': '支出',
            'amount': '￥1,989',
            'tag-icon': 'antd-fall',
            'tag-text': '-6.6%',
            'tag-color': 'var(--palette-error-dark)',
            'tag-background-color': 'rgba(var(--palette-error-mainChannel) / 0.16)',
            'text-color': 'var(--palette-text-secondary)',
        }
    }

    return html.Div(
        [
            html.Div(
                fac.AntdImage(
                    src=type_dict[type]['icon-src'],
                    preview=False,
                    width=24,
                    height=24,
                    style={
                        'flexShrink': 0,
                        'display': 'inline-flex',
                    }
                ),
                style={
                    'width': '48px',
                    'height': '48px',
                    'flexShrink': 0,
                    'display': 'inline-flex',
                    'alignItems': 'center',
                    'justifyContent': 'center',
                    'backgroundColor': type_dict[type]['icon-background-color'],
                    'borderRadius': '50%',
                }
            ),
            html.Div(
                [
                    html.Div(
                        [
                            type_dict[type]['title'],
                            fac.AntdTooltip(
                                fac.AntdIcon(
                                    icon='md-info-outline',
                                    style={
                                        'width': '16px',
                                        'height': '16px',
                                        'flexShrink': 0,
                                        'display': 'inline-flex ',
                                        'color': 'var(--palette-text-disabled)',
                                    }
                                ),
                                title=type_dict[type]['title-tooltip'],
                                placement='bottom'
                            )
                        ],
                        style={
                            'marginBottom': 8,
                            'display': 'flex',
                            'alignItems': 'center',
                            'gap': 4,
                            'fontWeight': 600,
                            'fontSize': '0.875rem',
                            'lineHeight': '1.57143',
                        }
                    ),
                    html.Div(
                        type_dict[type]['amount'],
                        style={
                            'fontSize': '1.5rem',
                            'fontWeight': 700,
                            'lineHeight': 1.5,
                        }
                    )
                ],
            ),
            html.Span(
                [
                    html.Span(
                        fac.AntdIcon(
                            icon=type_dict[type]['tag-icon'],
                            style={
                                'width': '16px',
                                'height': '16px',
                                'flexShrink': 0,
                                'display': 'inline-flex ',
                                'color': type_dict[type]['tag-color'],
                            }
                        ),
                        style={
                            'marginRight': '6px',
                            'width': '16px',
                            'height': '16px',
                        }
                    ),
                    "+8.2%"
                ],
                style={
                    'height': '24px',
                    'minWidth': '24px',
                    'lineHeight': 0,
                    'cursor': 'default',
                    'display': 'inline-flex',
                    'alignItems': 'center',
                    'whiteSpace': 'nowrap',
                    'justifyContent': 'center',
                    'padding': '0px 6px',
                    'fontSize': '0.75rem',
                    'fontWeight': 700,
                    'borderRadius': '6px',
                    'transition': 'all 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms',
                    'color': type_dict[type]['tag-color'],
                    'backgroundColor': type_dict[type]['tag-background-color'],
                    'position': 'absolute',  # 添加此属性以使top和right生效
                    'top': '8px',
                    'right': '8px',
                }
            )
        ],
        style={
            'padding': '24px',
            'color': type_dict[type]['text-color'],
            # 'color': 'var(--income-expenses-box-color)',
            'height': '110px',
            'flex': '1 1 0px',
            'cursor': 'pointer',
            'display': 'flex',
            'flexDirection': 'row',
            'alignItems': 'flex-start',
            'gap': '20px',
            'position': 'relative',
            'transition': 'color 200ms ease-in-out',
        },
        id=f'{type}-div',
        n_clicks=0
    )


def render_content(
    type,
    idx,
    style={},
):
    
    layout = html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                [
                                    'Total Balance',
                                    fac.AntdTooltip(
                                        fac.AntdIcon(
                                            icon='md-info-outline',
                                            style={
                                                'width': '16px',
                                                'height': '16px',
                                                'flexShrink': 0,
                                                'display': 'inline-flex ',
                                                'color': 'var(--palette-text-disabled)',
                                            }
                                        ),
                                        title='我正处于震惊的状态',
                                        placement='bottom'
                                    )
                                ],
                                style={
                                    'marginBottom': 8,
                                    'gap': 4,
                                    'display': 'flex',
                                    'alignItems': 'center',
                                    'color': 'var(--palette-text-secondary)',
                                    'fontWeight': 600,
                                    'fontSize': '0.875rem',
                                    'lineHeight': 1.57,
                                }
                            ),
                            html.Div(
                                '￥49,990',
                                style={
                                    'fontSize': '2rem',
                                    'fontWeight': 700,
                                    'lineHeight': 1.5,
                                }
                            )
                        ],
                        style={
                            'flexGrow': 1
                        }
                    ),
                    html.Div(
                        [
                            fac.AntdButton(
                                '发送',
                                type='text',
                                icon=fac.AntdIcon(
                                    icon='antd-send'
                                )
                            ),
                            fac.AntdButton(
                                '新建',
                                type='text',
                                icon=fac.AntdIcon(
                                    icon='antd-app-store-add'
                                )
                            ),
                            fac.AntdButton(
                                '请求',
                                type='text',
                                icon=fac.AntdIcon(
                                    icon='antd-download'
                                )
                            )
                        ],
                        style={
                            'display': 'flex',
                            'gap': '8px'
                        }
                    )
                ],
                style={
                    'display': 'flex',
                    'alignItems': 'flex-start',
                    'flexDirection': 'row',
                    'gap': '16px',
                    'width': '100%'
                }
            ),
            html.Div(
                html.Div(
                        [
                            fuc.FefferyCssVar(
                                id='income-expenses-css-var-output'
                            ),
                            html.Div(
                                [
                                    render_box('income'),
                                    render_box('expenses'),
                                ],
                                style={
                                    'display': 'flex',
                                    'position': 'relative',
                                    'zIndex': 1
                                }
                            ),
                            html.Span(
                                html.Span(
                                    style={
                                        'width': '100%',
                                        'height': '100%',
                                        'borderRadius': '16px',
                                        'display': 'block',
                                        'backgroundColor': 'var(--palette-common-white)',
                                        'boxShadow': 'rgba(145, 158, 171, 0.16) 0px 4px 8px 0px'
                                    }
                                ),
                                id='income-expenses-sliding-box',
                                style={
                                    'position': 'absolute',
                                    'left': '0px',
                                    # 'left': 'var(--income-expenses-sliding-box-left)',
                                    'top': '0px',
                                    'flex': '1 1 0px',
                                    'height': '100%',
                                    'backgroundColor': 'transparent',
                                    'width': '51%',
                                    'padding': '8px',
                                    'transition': 'all 300ms cubic-bezier(0.4, 0, 0.2, 1) 0ms'
                                }
                            ),
                    ],
                    style={
                        'padding': '8px',
                        'display': 'inline-block',
                        'flex': '1 1 auto',
                        'whiteSpace': 'nowrap',
                        'width': '100%',
                        'height': '130px',
                        'position': 'relative',
                    }
                ),
                style={
                    'width': '100%',
                    'display': 'flex',
                    'minHeight': '38px',
                    'alignItems': 'center',
                    'backgroundColor': 'var(--palette-background-neutral)',
                    'margin': '24px 0',
                    'borderRadius': '16px',
                }
            ),
            html.Div(
                [
                    dcc.Store(
                        id={
                            'type': f'{type}-line-chart-data',
                            'index': idx
                        },
                    ),
                    html.Div(
                        id={
                            'type': f'{type}-line-chart-container',
                            'index': idx
                        },
                        style={'height': '100%'}
                    )
                ],
                style={
                    'height': '300px',
                    'width': '100%',
                }
            )
        ],
        style={
            'display': 'flex',
            'flexDirection': 'column',
            **style
        },
        className='indicator-card'
    )


    return layout





