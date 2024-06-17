from dash import html, dcc


def render_store_container():
    
    return html.Div(
        [
            # token存储容器
            dcc.Store(id='token-container', storage_type='session'),
            # 菜单current_key存储容器
            dcc.Store(id='current-key-container'),
        ]
    )