from dash import html
import feffery_antd_components as fac


def render_layout(
    type,
    title,
    style={}
):

    def render_item(item_title):
        return html.Div(
            [
                html.Span(
                    item_title,
                    id={
                        'type': f'{type}-item-title',
                        'index': item_title
                    },
                    style={
                        'color': 'var(--palette-text-secondary)'
                    }
                ),
                html.Span(
                    id={
                        'type': f'{type}-item-value',
                        'index': item_title
                    }
                )
            ],
            style={
                'display': 'flex',
                'fontSize': '0.875rem',
                'fontWeight': 400,
                'lineHeight': 1.57,
                'fontFamily': '"Public Sans Variable", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"',
                'justifyContent': 'space-between',
            }
        )

    def render_button(
        button_title,
        id,
        button_style='warning'
    ):
        return fac.AntdButton(
            button_title,
            id=id,
            type='primary',
            block=True,
            style={
                'fontSize': '0.875rem',
                'fontWeight': '700',
                'lineHeight': '1.714',
                'color': f'var(--palette-{button_style}-contrastText)',
                'backgroundColor': f'var(--palette-{button_style}-main)',
                'borderColor': f'var(--palette-{button_style}-main)',
                'borderRadius': '8px',
                'height': '36px'
            }
        
    )

    return html.Div(
        [
            html.Div(
                title,
                id={
                    'type': f'{type}-item-title',
                    'index': title
                },
                style={
                    'marginBottom': '8px',
                },
                className='card-title',
            ),
            html.Div(
                [
                    html.Div(
                        id={
                            'type': f'{type}-item-value',
                            'index': title
                        },
                        style={
                            'fontWeight': 700,
                            'fontSize': '2rem',
                            'lineHeight': 1.5,
                            'fontFamily': 'Barlow, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"'
                        },
                    ),
                    render_item('合计订单'),
                    render_item('盈利'),
                    render_item('已退款'),
                    html.Div(
                        [
                            render_button('Request', id=f'{type}-request-button'),
                            render_button('Transfer', id=f'{type}-transfer-button', button_style='primary'),
                        ],
                        style={
                            'display': 'flex',
                            'gap': '16px',
                            'marginTop': '16px'
                        }
                    )
                ],
                style={
                    'display': 'flex',
                    'flexDirection': 'column',
                    'gap': '16px',
                    'width': '100%'
                }
            )
        ],
        style={
            'display': 'flex',
            'flexDirection': 'column',
            'alignItems': 'flex-start',
            **style
        },
        className='indicator-card'
    )