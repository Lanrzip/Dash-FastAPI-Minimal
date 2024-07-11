import dash
from dash import html
import feffery_antd_components as fac

from views.components.card import title_card


def render_box(item):

    return html.Div(
        [
            html.Div(
                [
                    fac.AntdImage(
                        src=item.get('icon'),
                        preview=False,
                        height=20,
                        width=26,
                        style={
                            'borderRadius': '5px'
                        },
                        id='application-top-installed-country-icon'
                    ),
                    html.Span(
                        item.get('name'),
                        style={
                            'fontWeight': '700',
                            'fontSize': '0.875rem',
                            'lineHeight': '1.57',
                            'textOverflow': 'ellipsis',
                            'whiteSpace': 'nowrap',
                        },
                        id='application-top-installed-country-name'
                    )
                ],
                style={
                    'display': 'flex',
                    'alignItems': 'center',
                    'gap': '8px',
                    'minWidth': '120px',
                }
            ),
            html.Div(
                [
                    fac.AntdImage(
                        src='assets/imgs/operation-system/android.png',
                        preview=False,
                        height=14,
                        width=14,
                    ),
                    html.Span(
                        item.get('android'),
                        id='application-top-installed-country-android'
                    )
                ],
                style={
                    'display': 'flex',
                    'alignItems': 'center',
                    'gap': '4px',
                    'minWidth': '80px',
                    'fontSize': '0.875rem',
                    'fontWeight': '400',
                    'lineHeight': '1.57',
                }
            ),
            html.Div(
                [
                    fac.AntdImage(
                        src='assets/imgs/operation-system/windows.png',
                        preview=False,
                        height=14,
                        width=14
                    ),
                    html.Span(
                        item.get('windows'),
                        id='application-top-installed-country-windows'
                    )
                ],
                style={
                    'display': 'flex',
                    'alignItems': 'center',
                    'gap': '4px',
                    'minWidth': '80px',
                    'fontSize': '0.875rem',
                    'fontWeight': '400',
                    'lineHeight': '1.57',
                }
            ),
            html.Div(
                [
                    fac.AntdImage(
                        src='assets/imgs/operation-system/apple.png',
                        preview=False,
                        height=14,
                        width=14
                    ),
                    html.Span(
                        item.get('apple'),
                        id='application-top-installed-country-apple'
                    )
                ],
                style={
                    'display': 'flex',
                    'alignItems': 'center',
                    'gap': '4px',
                    'minWidth': '80px',
                    'fontSize': '0.875rem',
                    'fontWeight': '400',
                    'lineHeight': '1.57',
                }
            )
        ],
        style={
            'display': 'flex',
            'alignItems': 'center',
            'gap': '16px',
            'height': '100%'
        }
    )


def render_layout(
    type,
    idx,
    title=None,
    style={}
):



    layout = html.Div(
        style={
            'display': 'flex',
            'flexDirection': 'column',
            'gap': '24px',
            'padding': '0 24px 24px 24px',
            'overflow': 'auto'
        },
        id={
            'type': type,
            'index': idx
        }
    )

    return title_card.render_card(
        title=title,
        children=layout,
        style=style,
        title_padding='24px'
    )