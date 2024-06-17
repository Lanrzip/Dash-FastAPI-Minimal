import dash
from dash import html
import feffery_antd_components as fac

from views.components import indicator_card, chart_card
import callbacks.views_c.application_c


def render_content():
    return html.Div(
        [
            fac.AntdRow(
                [
                    fac.AntdCol(
                        html.Div(
                            [
                                fac.AntdText(
                                    '欢迎回来👋 \n张三',
                                    style={
                                        'color': '#012972',
                                        'fontSize': '1.5rem',
                                        'fontWeight': '700',
                                        'lineHeight': '1.5',
                                        'marginBottom': '16px',
                                        'whiteSpace': 'pre-line'
                                    }
                                ),
                                fac.AntdText(
                                    "If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything.",
                                    style={
                                        'color': '#012972',
                                        'marginBottom': '40px',
                                        'lineHeight': '1.57',
                                        'fontSize': '0.875rem',
                                        'fontWeight': '400',
                                        'opacity': '0.8',
                                        'maxWidth': '360px'
                                    }
                                ),
                                fac.AntdButton(
                                    '出发',
                                    type='primary',
                                    style={
                                        'fontSize': '0.875rem',
                                        'fontWeight': '700',
                                    }
                                ),
                            ],
                            style={
                                'height': '100%',
                                'width': '100%',
                                'padding': '56px 40px',
                                'display': 'flex',
                                'flexDirection': 'column',
                                'alignItems': 'flex-start'
                            }
                        ),
                        flex='3'
                    ),
                    fac.AntdCol(
                        html.Div(
                            fac.AntdImage(
                                src='./assets/imgs/dashboard.png',
                                preview=False,
                                height=200,
                                width=260
                            ),
                            style={
                                'height': '100%',
                                'width': '100%',
                                'padding': '24px',
                                'display': 'flex',
                                'justifyContent': 'center',
                                'alignItems': 'center'
                            }
                        ),
                        flex='2'
                    )
                ],
                wrap=False,
                style={
                    'backgroundColor': '#DAF0FD',
                    'borderRadius': '16px',
                    'height': '100%',
                    'gridColumn': '1/3',
                    'height': '320px'
                    # 'minWidth': '520px'
                }
            ),
            html.Div(
                html.Div(
                    [
                        fac.AntdText(
                            '特色应用',
                            style = {
                                'fontWeight': '700',
                                'lineHeight': '1.5',
                                'fontSize': '0.95rem',
                                'color': 'rgb(104, 205, 249)'
                            }

                        ),
                        fac.AntdText(
                            '生产力黑客的终极指南',
                            style = {
                                'fontWeight': '700',
                                'lineHeight': '1.5',
                                'fontSize': '1.125rem',
                                'overflow': 'hidden',
                                'textOverflow': 'ellipsis',
                                'whiteSpace': 'nowrap',
                                'color': 'rgb(255, 255, 255)'
                            }
                        ),
                        fac.AntdText(
                            '她迫不及待地打开礼物，眼睛里闪烁着兴奋的光芒。',
                            style = {
                                'margin': '0px',
                                'lineHeight': '1.57143',
                                'fontSize': '0.875rem',
                                'fontWeight': '400',
                                'overflow': 'hidden',
                                'textOverflow': 'ellipsis',  # 超出省略
                                'whiteSpace': 'nowrap',
                                'color': 'rgb(255, 255, 255)'
                            }
                        )
                    ],
                    style={
                        'width': '100%',
                        'overflow': 'hidden',
                        'display': 'flex',
                        'flexDirection': 'column',
                        'gap': '8px',
                        'padding': '24px',
                        'bottom': '0px',
                        'zIndex': '9',
                        'textAlign': 'left',
                        'position': 'absolute',
                        'color': 'rgb(255, 255, 255)'
                    }
                ),
                style={
                    'height': '320px',
                    'borderRadius': '16px',
                    'position': 'relative',
                    'backgroundImage': (
                        'linear-gradient(to bottom, rgba(0, 0, 0, 0) -20%, rgba(0, 0, 0, 1) 100%), '
                        'url({})'.format(dash.get_asset_url('imgs/slider_1.jpg'))
                    ),
                    'backgroundRepeat': 'no-repeat',  # 确保背景图像覆盖整个元素
                    'backgroundSize': 'cover',  # 防止背景图像重复
                }
            ),
            indicator_card.render_card(
                type='application-indicator-card',
                idx='活跃用户',
                title='活跃用户',
                value='18765',
                note=['rise', '+2.6%', '比上周'],
            ),
            indicator_card.render_card(
                type='application-indicator-card',
                idx='安装次数',
                title='安装次数',
                value='4876',
                note=['rise', '+0.2%', '比上周'],
            ),
            indicator_card.render_card(
                type='application-indicator-card',
                idx='下载次数',
                title='下载次数',
                value='678',
                note=['fall', '-0.1%', '比上周'],
            ),
            chart_card.render_card(
                type='application-chart-card-donut',
                idx='下载量',
                title="下载量",
                note="通过操作系统下载",
                grid_row='3/5'
            ),
            chart_card.render_card(
                type='application-chart-card-bar',
                idx='区域下载量',
                title="区域下载量",
                note="(+43%) 比去年",
                grid_row='3/5',
                grid_col='2/4',
                with_select=True
            )

        ],
        style={
            'display': 'grid',
            'gridTemplateColumns': 'repeat(3, minmax(260px, 1fr))',
            'gap': '24px',
            'backgroundColor': '#FFFFFF',
            'padding': '8px 40px 88px 40px',
            'maxWidth': '1536px',
            'margin': '0 auto'
        }
    )

