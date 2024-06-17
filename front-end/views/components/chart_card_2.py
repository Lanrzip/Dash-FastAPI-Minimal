import dash
from dash import html, dcc
from dash.dependencies import ClientsideFunction, Output, Input
import feffery_antd_components as fac

from server import app
import callbacks.views_c.application_c


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
                id='chart-card-2-chart-data',
                data=[
                    {
                        'name': 'Email',
                        'type': 'bar',
                        'stack': 'Ad',
                        'emphasis': {
                        'focus': 'series'
                        },
                        'data': [120, 132, 101, 134, 90, 230, 210]
                    },
                    {
                        'name': 'Union Ads',
                        'type': 'bar',
                        'stack': 'Ad',
                        'emphasis': {
                        'focus': 'series'
                        },
                        'data': [220, 182, 191, 234, 290, 330, 310]
                    },
                    {
                        'name': 'Video Ads',
                        'type': 'bar',
                        'stack': 'Ad',
                        'emphasis': {
                        'focus': 'series'
                        },
                        'data': [150, 232, 201, 154, 190, 330, 410]
                    }
                ]
            ),
            html.Div(
                [
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
                            # 'flexGrow': '1'
                        }
                    ),
                    html.Div(
                        fac.AntdSelect(
                            options=[
                                {
                                    'label': i,
                                    'value': i
                                }
                                for i in [2022, 2023, 2024]
                            ],
                            defaultValue=2024,
                            id='chart-card-2-year-select',
                            style={
                                'width': '100px'
                            }
                        )
                    )
                ],
                style={
                    'display': 'flex',
                }
            ),
            html.Div(
                id='chart-card-2-chart-container',
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
        function_name='renderChartCard2Chart'
    ),
    Output('chart-card-2-chart-container', 'children'),
    Input('chart-card-2-chart-data', 'data'),
)