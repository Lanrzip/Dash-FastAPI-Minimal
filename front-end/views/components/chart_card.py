import dash
from dash import html, dcc
from dash.dependencies import ClientsideFunction, Output, Input
import feffery_antd_components as fac

from server import app


def render_card(
        type,
        idx,
        title=None,
        note=None,
        chart=None,
        grid_row=None,
        grid_col=None,
        height='500px',
        with_select=False
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
        'padding': '24px',
    }
    if grid_row is not None:
        style['gridRow'] = grid_row
    if grid_col is not None:
        style['gridColumn'] = grid_col
    if height is not None:
        style['height'] = height

    upper_title_note = html.Div(
        [
            html.Span(
                title,
                className='card-title'
            ),
            html.Span(
                note,
                className='card-note mt-1'
            )
        ],
        style={
            'display': 'flex',
            'flexDirection': 'column',
            'width': '100%',
        }
    )

    upper_layout = html.Div(
            [
            dcc.Store(
                id={
                    'type': f'{type}-chart-data',
                    'index': idx
                },
            ),
            html.Div(
                    [
                        upper_title_note,
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
                                id={
                                    'type': f'{type}-year-select',
                                    'index': idx
                                },
                                style={
                                    'width': '100px'
                                }
                            )
                        )
                    ],
                    style={
                        'display': 'flex',
                    }
                ) if with_select
                else upper_title_note
        ]
    )

    chart_container = html.Div(
        id={
            'type': f'{type}-chart-container',
            'index': idx
        },
        style={
            'height': '100%',
            'width': '100%',
        }
    )
    
    return html.Div(
        [
            upper_layout,
            chart_container
        ],
        style=style
    )
