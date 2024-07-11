import dash
from dash import html
import feffery_antd_components as fac

from . import (
    indicator_card,
)
import callbacks.views_c.analytics_c

def render_content():
    return html.Div(
        [
            html.H4(
                '嗨，欢迎回来！👋',
                style={
                    'marginBottom': '24px',
                    'fontSize': '1.5rem',
                    'fontWeight': '700',
                    'lineHeight': '1.5',
                }
            ),
            html.Div(
                [
                    indicator_card.render_layout(
                        type='analytics-indicator-card',
                        index='周销售量',
                        title='周销售量',
                        style={
                            'height': '186px',
                            'gridColumn': '1/4',
                        }
                    ),
                    indicator_card.render_layout(
                        type='analytics-indicator-card',
                        index='周销售量',
                        title='周销售量',
                        style={
                            'gridColumn': '4/7',
                        }
                    ),
                    indicator_card.render_layout(
                        type='analytics-indicator-card',
                        index='周销售量',
                        title='周销售量',
                        style={
                            'gridColumn': '7/10',
                        }
                    ),
                    indicator_card.render_layout(
                        type='analytics-indicator-card',
                        index='周销售量',
                        title='周销售量',
                        style={
                            'gridColumn': '10/13',
                        }
                    )
                ],
                style={
                    'display': 'grid',
                    'gridTemplateColumns': 'repeat(12, minmax(260, 3fr))',
                    'gap': '24px',
                }
            )
        ],
        style={
            'backgroundColor': '#FFFFFF',
            'padding': '8px 40px 88px 40px',
            'maxWidth': '1536px',
            'margin': '0 auto',
            'overflow': 'hidden',
        }
    )

