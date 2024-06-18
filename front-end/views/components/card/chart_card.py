import dash
from dash import html, dcc
from dash.dependencies import ClientsideFunction, Output, Input
import feffery_antd_components as fac

from . import card_with_title


def render_card(
        type,
        idx,
        title=None,
        note=None,
        with_select=False,
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
        style={'height': '100%'}
    )

    # 如果有select组件，则重写layout
    if with_select:
        upper_title = html.Div(
            [
                html.Span(
                    title,
                    className='card-title'
                ),
                html.Span(
                    note,
                    className='card-note'
                )
            ],
            style={
                'display': 'flex',
                'flexDirection': 'column',
                'width': '100%',
            }
        ) if note else html.Div(
            html.Span(
                title,
                className='card-title',
            ),
            style={
                'padding': '24px'
            }
        )

        upper_layout = html.Div(
            [
                html.Div(
                    [
                        upper_title,
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
                )
            ]
        )
    
        return html.Div(
            [
                upper_layout,
                chart_container
            ],
            className='card-with-title',
            style=style
        )

    # 如果没有select组件，则直接返回    
    return card_with_title(
        title=title,
        note=note,
        children=chart_container,
        style=style
    )
