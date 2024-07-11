import dash
from dash import html
import feffery_antd_components as fac

import callbacks.layout_c.content_c


def render_main_content():
    return html.Div(
        id='main-content-container',
        style={
            'minWidth': '1200px'
        }
    )
