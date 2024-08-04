from dash import html
import feffery_antd_components as fac

from views.components.card import title_card


def render_box(item):
    """
    Render a single news box.

    Args:
        item: A dictionary containing news details.
            Example:
                {
                    'news_img_url': 'https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/mock/assets/images/cover/cover-1.webp',
                    'news_title': '可再生能源的未来：未来的创新与挑战',
                    'news_detail': '太阳慢慢地落入地平线，将天空染成鲜艳的橙色和粉色。',
                }

    Returns:
        html.Div: A Dash HTML Div component representing the news box.
    """
    return html.Div(
        [
            html.Div(
                fac.AntdImage(
                    src=item.get('news_img_url'),
                    preview=False,
                    height='100%',
                    width='100%',
                    style={
                        'objectFit': 'cover',
                    }
                ),
                style={
                    'width': '48px',
                    'height': '48px',
                    'borderRadius': '12px',
                    'overflow': 'hidden',
                    'flexShrink': 0,  # Prevent image from shrinking
                }
            ),
            html.Div(
                [
                    html.A(
                        item.get('news_title'),
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
                        item.get('news_detail'),
                        style={
                            'color': 'var(--palette-text-secondary)',
                            'display': 'flex',
                            'gap': '4px',
                            'alignItems': 'center',
                            'fontSize': '0.875rem',
                            'fontWeight': '400',
                            'lineHeight': '1.57',
                            'textOverflow': 'ellipsis',
                            'overflow': 'hidden',
                            'whiteSpace': 'nowrap',
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
                item.get('news_released_date'),
                style={
                    'display': 'flex',
                    'justifyContent': 'flex-start',
                    'alignItems': 'center',
                    'overflow': 'hidden',
                    'color': 'var(--palette-text-disabled)',
                    'fontSize': '0.75rem',
                    'fontWeight': '400',
                    'lineHeight': '1.5',
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
        [
            html.Div(
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
            ),
            html.Div(
                fac.AntdButton(
                    '查看全部 >',
                    type='text',
                    href='/blog/list',
                    style={
                        'fontSize': '0.8125rem',
                        'fontWeight': '700',
                        'borderRadius': '8px',
                    }
                ),
                style={
                    'padding': '16px',
                    'textAlign': 'right'
                }
            ),
        ]
    )

    return title_card.render_card(
        title=title,
        children=layout,
        style=style,
        title_padding='24px'
    )