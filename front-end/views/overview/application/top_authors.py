import dash
from dash import html
import feffery_antd_components as fac

from views.components.card import title_card



def render_box(item):

    return html.Div(
        [
            fac.AntdAvatar(
                src=item.get('avatar'),
                mode='image',
                style={
                    'width': '40px',
                    'height': '40px'
                }
            ),
            html.Div(
                [
                    html.Div(
                        item.get('name'),
                        style={
                            'fontWeight': '600',
                            'fontSize': '0.875rem',
                            'lineHeight': '1.57'
                        }
                    ),
                    html.Div(
                        [
                            fac.AntdIcon(
                                icon='md-favorite',
                            ),
                            item.get('favorite')
                        ],
                        style={
                            'color': 'var(--palette-text-secondary)',
                            'display': 'inline-flex',
                            'gap': '4px',
                            'alignItems': 'center',
                            'fontSize': '0.75rem',
                            'fontWeight': '400',
                            'lineHeight': '1.5'
                        }
                    )
                ],
                style={
                    'flexGrow': 1,
                }
            ),
            html.Div(
                fac.AntdIcon(
                    icon='antd-trophy',
                    # style={
                    #     'width': '30px',
                    #     'height': '30px',
                    # }
                ),
                style={
                    'height': '40px',
                    'width': '40px',
                    'color': item.get('color'),
                    'backgroundColor': item.get('bgc'),
                    'borderRadius': '50%',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            )
        ],
        style={
            'display': 'flex',
            'gap': '16px',
            'alignItems': 'center'
        }
    )


def render_layout(
    type=None,
    idx=None,
    style={}
):

    layout = html.Div(
        style={
            'display': 'flex',
            'flexDirection': 'column',
            'gap': '24px',
            'padding': '0 24px 24px 24px',
        },
        id={
            'type': type,
            'index': idx
        }
    )

    return title_card.render_card(
        title="最佳作者",
        children=layout,
        style=style,
        title_padding='24px'
    )