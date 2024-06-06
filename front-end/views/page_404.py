from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc


def render_content():

    return html.Div(
        [
            html.Div(
                [
                    html.H1("未找到页面", style={'font-weight': 'bold'}),
                    html.P("您似乎点击了断开的链接或输入了此网站上不存在的网址。"),
                    html.P(
                        html.A(
                            [
                                fac.AntdIcon(
                                    icon='antd-rollback'
                                ),
                                html.A("返回我们的网站", href='/')
                            ],
                            style={
                                'color': 'rgb(14, 30, 37)'
                            }
                        ),
                    )
                ],
                className='card'
            ),
            fuc.FefferyStyle(
                rawStyle='''
                    .card {
                        position: relative;
                        display: flex;
                        flex-direction: column;
                        width: 75%;
                        max-width: 364px;
                        padding: 24px;
                        background: white;
                        color: rgb(14, 30, 37);
                        border-radius: 8px;
                        box-shadow: 0 2px 4px 0 rgba(14, 30, 37, .16);
                    }
'''
            )
        ],
        style={
            'height': '100vh',
            'display': 'flex',
            'alignItems': 'center',
            'justifyContent': 'center',
            'background': '#34383C'
        }
    )
