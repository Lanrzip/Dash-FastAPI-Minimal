import dash
from dash import html
import feffery_antd_components as fac

from . import (
    indicator_card,
    chart_card,
    news,
    order_timeline,
    traffic_by_site,
    tasks
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
                        index=1,
                        img_src="https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/public/assets/icons/glass/ic-glass-bag.svg",
                        title='周销售量',
                        style={
                            'height': '186px',
                            'gridColumn': '1/4',
                            'backgroundColor': '#CAF7DD',
                        }
                    ),
                    indicator_card.render_layout(
                        type='analytics-indicator-card',
                        index=2,
                        img_src="https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/public/assets/icons/glass/ic-glass-users.svg",
                        title='新用户',
                        style={
                            'gridColumn': '4/7',
                            'backgroundColor': '#EBD2FF',
                        }
                    ),
                    indicator_card.render_layout(
                        type='analytics-indicator-card',
                        index=3,
                        img_src="https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/public/assets/icons/glass/ic-glass-buy.svg",
                        title='订单量',
                        style={
                            'gridColumn': '7/10',
                            'backgroundColor': '#FFEFC3',
                        }
                    ),
                    indicator_card.render_layout(
                        type='analytics-indicator-card',
                        index=4,
                        img_src="https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/public/assets/icons/glass/ic-glass-message.svg",
                        title='消息',
                        style={
                            'gridColumn': '10/13',
                            'backgroundColor': '#FFDFCE',
                        }
                    ),
                    chart_card.render_layout(
                        type='analytics-chart-card-pie',
                        idx='访问量',
                        title="访问量",
                        style={
                            'height': '500px',
                            'gridColumn': '1/5',
                        }
                    ),
                    chart_card.render_layout(
                        type='analytics-chart-card-bar',
                        idx='网站访问量',
                        title="网站访问量",
                        style={
                            'height': '500px',
                            'gridColumn': '5/13',
                        }
                    ),
                    chart_card.render_layout(
                        type='analytics-chart-card-hbar',
                        idx='兑换率',
                        title="兑换率",
                        subtitle="(+43%) 比去年",
                        style={
                            'height': '500px',
                            'gridColumn': '1/9',
                        }
                    ),
                    chart_card.render_layout(
                        type='analytics-chart-card-radar',
                        idx='当前主题',
                        title="当前主题",
                        style={
                            'height': '500px',
                            'gridColumn': '9/13',
                        }
                    ),
                    news.render_layout(
                        type='analytics-news-card',
                        idx='新闻',
                        title='新闻',
                        style={
                            'gridColumn': '1/9',
                        }
                    ),
                    order_timeline.render_layout(
                        type='analytics-order-timeline-card',
                        idx='订单时间轴',
                        title='订单时间轴',
                        style={
                            'gridColumn': '9/13',
                        }
                    ),
                    traffic_by_site.render_layout(
                        type='analytics-traffic-by-site-card',
                        idx='流量来源',
                        title='流量来源',
                        style={
                            'gridColumn': '1/5',
                        }
                    ),
                    tasks.render_layout(
                        type='analytics-tasks-card',
                        idx='任务',
                        title='任务',
                        style={
                            'gridColumn': '5/13',
                        }
                    )
                ],
                style={
                    'display': 'grid',
                    'gridTemplateColumns': 'repeat(12, 1fr)',
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

