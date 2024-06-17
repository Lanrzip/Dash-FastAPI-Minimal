import dash
from dash import html, dcc
from dash.dependencies import ClientsideFunction, Output, Input

from server import app


def render_card(
        title=None,
        note=None,
        chart=None,
        grid_row=None,
        grid_col=None,
        height='500px',
):
    style = {
        'backgroundColor': '#FFFFFF',
        'transition': 'box-shadow 300ms cubic-bezier(0.4, 0, 0.2, 1) 0ms',
        'overflow': 'hidden',
        'position': 'relative',
        'boxShadow': 'rgba(145, 158, 171, 0.2) 0px 0px 2px 0px, rgba(145, 158, 171, 0.12) 0px 12px 24px -4px',
        'borderRadius': '16px',
        'zIndex': '0',
        'display': 'flex',
        'flexDirection': 'column',
        # 'alignItems': 'center',
        'padding': '24px',
    }
    if grid_row is not None:
        style['gridRow'] = grid_row
    if grid_col is not None:
        style['gridColumn'] = grid_col
    if height is not None:
        style['height'] = height

    
    return html.Div(
        [
            dcc.Store(
                id='chart-card-1-chart-data',
                data=[
                    { 'value': 1048, 'name': 'Search Engine' },
                    { 'value': 735, 'name': 'Direct' },
                    { 'value': 580, 'name': 'Email' },
                    { 'value': 484, 'name': 'Union Ads' },
                    { 'value': 300, 'name': 'Video Ads' }
                ]
            ),
            html.Div(
                [
                    html.Span(
                        title,
                        style={
                            'fontWeight': 600,
                            'fontSize': '1.125rem',
                            'lineHeight': 1.5556
                        }
                    ),
                    html.Span(
                        note,
                        style={
                            'marginTop': '4px',
                            'fontWeight': 400,
                            'fontSize': '0.875rem',
                            'lineHeight': 1.57143,
                            'color': '#637381'
                        },
                    )
                ],
                style={
                    'display': 'flex',
                    'flexDirection': 'column',
                    'width': '100%',
                }
            ),
            html.Div(
                id='chart-card-1-chart-container',
                style={
                    'height': '100%',
                    'width': '100%',
                    # 'padding': 'auto',
                    # 'marginTop': '20px'
                }
            )
        ],
        style=style
    )


app.clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='renderChartCard1Chart'
    ),
    Output('chart-card-1-chart-container', 'children'),
    Input('chart-card-1-chart-data', 'data'),
)