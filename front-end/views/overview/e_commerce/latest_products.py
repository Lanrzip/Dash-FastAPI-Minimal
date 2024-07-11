from dash import html
import feffery_antd_components as fac

from views.components.card import title_card



def render_box(item):
    """
    Render a single product box.

    Args:
        item: A dictionary containing product details.
            Example:
                {
                    'product_img_url': 'https://example.com/image.webp',
                    'product_name': '示例产品',
                    'product_price': fac.AntdText('¥99.99'),
                    'product_tags': ['#d29200', '#ffb900']
                }

    Returns:
        html.Div: A Dash HTML Div component representing the product box.
    """
    return html.Div(
        [
            html.Div(
                fac.AntdImage(
                    src=item.get('product_img_url'),
                    preview=False,
                    style={
                        'objectFit': 'cover',
                    }
                ),
                style={
                    'width': '48px',
                    'height': '48px',
                    'borderRadius': '12px',
                    'overflow': 'hidden',
                    'flexShrink': 0  # Prevent image from shrinking
                }
            ),
            html.Div(
                [
                    html.A(
                        item.get('product_name'),
                        style={
                            'fontWeight': '600',
                            'fontSize': '0.875rem',
                            'lineHeight': '1.57',
                            'color': 'var(--palette-text-primary)',
                            'textOverflow': 'ellipsis',
                            'overflow': 'hidden',
                            'whiteSpace': 'nowrap',
                        },
                        className='hover:underline'
                    ),
                    html.Div(
                        item.get('product_price'),
                        style={
                            'color': 'var(--palette-text-secondary)',
                            'display': 'flex',
                            'gap': '4px',
                            'alignItems': 'center',
                            'fontSize': '0.875rem',
                            'fontWeight': '400',
                            'lineHeight': '1.57',
                        }
                    )
                ],
                style={
                    'flexGrow': 1,
                    'gap': '4px',
                    'display': 'flex',
                    'flexDirection': 'column',
                }
            ),
            html.Div(
                fac.AntdAvatarGroup(
                    [
                        fac.AntdAvatar(
                            mode='text',
                            text='',
                            style={
                                'background': background
                            }
                        )
                        for background in item.get('product_tags')
                    ],
                    size=14
                ),
                style={
                    'display': 'flex',
                    'justifyContent': 'flex-start',
                    'alignItems': 'center',
                    'overflow': 'hidden',
                }
            )
        ],
        style={
            'display': 'flex',
            'gap': '16px',
            'alignItems': 'center',
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