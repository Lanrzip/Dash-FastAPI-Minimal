from dash import html, dcc


def render_store_container():
    
    return html.Div(
        [
            dcc.Store(id='token-container', storage_type='session')
        ]
    )