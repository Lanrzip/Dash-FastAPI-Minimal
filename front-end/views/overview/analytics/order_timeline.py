from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

from views.components.card import title_card



def render_layout(
    type,
    idx,
    title=None,
    subtitle=None,
    style={}
):
    
    layout = html.Div(
        fac.AntdTimeline(
            items=[
                {
                    'content': '1983, orders, $4220',
                    'label': '17 7月 2024 1:36 下午',
                    'color': 'blue'
                },
                {
                    'content': '12 Invoices have been paid',
                    'label': '16 7月 2024 12:36 中午',
                    'color': 'green'
                },
                {
                    'content': 'New order received',
                    'label': '15 7月 2024 9:36 上午',
                    'color': 'red'
                },
                {
                    'content': '1983, orders, $4220',
                    'label': '14 7月 2024 1:36 下午',
                    'color': 'blue'
                },
                {
                    'content': '12 Invoices have been paid',
                    'label': '13 7月 2024 12:36 中午',
                    'color': 'green'
                },
                {
                    'content': 'New order received',
                    'label': '12 7月 2024 9:36 上午',
                    'color': 'red'
                },
                {
                    'content': '1983, orders, $4220',
                    'label': '11 7月 2024 1:36 下午',
                    'color': 'blue'
                },
            ],
            mode='right'
        ),
        style={
            'display': 'flex',
            'flexDirection': 'column',
            'gap': '28px',
            'padding': '8px 24px 24px 24px',
            'overflow': 'auto',
        }
    )

    return title_card.render_card(
        title=title,
        subtitle=subtitle,
        children=layout,
        style=style,
        title_padding='24px'
    )