from dash import html, dcc

from views.components.card import title_card


def render_layout(
        type,
        idx,
        title=None,
        subtitle=None,
        style={}
):
    
    chart_container = html.Div(
        [
            dcc.Store(
                id={
                    'type': f'{type}-chart-data',
                    'index': idx
                },
            ),
            html.Div(
                id={
                    'type': f'{type}-chart-container',
                    'index': idx
                },
                style={'height': '100%'}
            )
        ],
        style={
            'height': '100%',
            'padding': '0 24px 24px'
        }
    )

    return title_card.render_card(
        title=title,
        subtitle=subtitle,
        children=chart_container,
        style=style
    )
