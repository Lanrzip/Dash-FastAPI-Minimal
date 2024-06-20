import dash
from dash import html, dcc
from dash.dependencies import ClientsideFunction, Output, Input
import feffery_antd_components as fac

from views.components.card import title_card


def render_layout(
        type,
        idx,
        title=None,
        subtitle=None,
        style={}
):
    
    upper_layout = html.Div(
        [
            html.Div(
                [
                    title_card.render_title(title, subtitle, title_padding='0'),
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
                    'padding': '24px 24px 0'
                }
            )
        ]
    )


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

    
    return html.Div(
        [
            upper_layout,
            chart_container
        ],
        className='title-card',
        style=style
    )

