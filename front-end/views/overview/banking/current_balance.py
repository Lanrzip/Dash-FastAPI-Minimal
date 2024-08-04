from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import lanrzip_dash_components as ldc
# import lanrzip_utils_components as luc
# import sd_material_ui


def render_card(
    item
):
    """
    Render a single card.

    Args:
        item: A dictionary containing card details.
            Example:
                {
                    'card_balance': '¥99.99',
                    'card_number': '**** **** **** 3640',
                    'card_type': 'visa',
                    'card_holder': '张三',
                    'card_expire_date': '11/22'
                }

    Returns:
        html.Div: A Dash HTML Div component representing the card.
    """
    return html.Div(
        [
            html.Div(
                fac.AntdPopover(
                    fac.AntdButton(
                        shape='circle',
                        size='large',
                        type='text',
                        icon=fac.AntdIcon(icon='antd-more', style={'color': '#939393'}),
                        id={
                            'type': f'{type}-item-more',
                            'index': item['card_number']
                        }
                    ),
                    placement='leftTop',
                    trigger='click',
                    title='',
                    content=html.Div(
                        [
                            fac.AntdButton(
                                '编辑',
                                id={
                                    'type': f'{type}-item-edit',
                                    'index': item['card_number']
                                },
                                type='text',
                                block=True,
                                icon=fac.AntdIcon(icon='antd-edit'),
                            ),
                            fac.AntdButton(
                                '删除',
                                id={
                                    'type': f'{type}-item-delete',
                                    'index': item['card_number']
                                },
                                type='text',
                                block=True,
                                danger=True,
                                icon=fac.AntdIcon(icon='antd-delete'),
                            )
                        ],
                        style={
                            'maxWidth': '120px',
                        }
                    )
                ),
                style={
                    'position': 'absolute',
                    'top': '8px',
                    'right': '8px',
                    # 'zIndex': 9,
                    # 'opacity': 1,
                }
            ),
            html.Div(
                [
                    html.Div(
                        '当前余额',
                        style={
                            'marginBottom': '12px',
                            'fontWeight': '600',
                            'fontSize': '0.875rem',
                            'lineHeight': '1.57rem',
                            'opacity': 0.48,
                            'color': 'var(--palette-common-white)'
                        }
                    ),
                    html.Div(
                        [
                            html.Span(
                                item['card_balance'],
                                id={
                                    'type': f'{type}-item-balance',
                                    'index': item['card_number']
                                },
                                style={
                                    'fontSize': '1.5rem',
                                    'fontWeight': '700',
                                    'lineHeight': '1.5',
                                    'color': 'var(--palette-common-white)'
                                }
                            ),
                            fac.AntdButton(
                                '',
                                type='text',
                                icon=fac.AntdIcon(icon='antd-eye', style={'color': '#888B93'})
                            )
                        ],
                        style={
                            'gap': '8px',
                            'display': 'flex',
                            'alignItems': 'center',
                        }
                    )
                ],
                style={
                    'display': 'flex',
                    'flexDirection': 'column',
                }
            ),
            html.Div(
                [
                    html.Div(
                        fac.AntdImage(
                            src=f'./assets/imgs/banking/{item["card_type"]}.png',
                            preview=False,
                            width=24,
                            height=24
                        ),
                        style={
                            'padding': '0 6px',
                            'backgroundColor': 'white',
                            'borderRadius': '4px',
                            'display': 'inline-flex',
                        }
                    ),
                    item['card_number'],
                ],
                style={
                    'margin': '24px 0',
                    'gap': '8px',
                    'display': 'flex',
                    'alignItems': 'center',
                    'justifyContent': 'flex-end',
                    'fontWeight': '600',
                    'fontSize': '1rem',
                    'lineHeight': '1.5',
                    'color': 'var(--palette-common-white)'
                }
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                '持卡人',
                                style={
                                    'fontSize': '0.75rem',
                                    'lineHeight': '1.5',
                                    'fontWeight': '400',
                                    'opacity': 0.48,
                                    'color': 'var(--palette-common-white)',
                                    'marginBottom': '8px'
                                }
                            ),
                            html.Span(
                                item['card_holder'],
                                id={
                                    'type': f'{type}-item-holder',
                                    'index': item['card_number']
                                },
                                style={
                                    'fontSize': '1rem',
                                    'lineHeight': '1.5',
                                    'fontWeight': '600',
                                    'color': 'var(--palette-common-white)'
                                }
                            )
                        ],
                        style={
                            'display': 'block'
                        }
                    ),
                    html.Div(
                        [
                            html.Div(
                                '截止日期',
                                style={
                                    'fontSize': '0.75rem',
                                    'lineHeight': '1.5',
                                    'fontWeight': '400',
                                    'opacity': 0.48,
                                    'color': 'var(--palette-common-white)',
                                    'marginBottom': '8px'
                                }
                            ),
                            html.Span(
                                item['card_expire_date'],
                                id={
                                    'type': f'{type}-item-expire-date',
                                    'index': item['card_number']
                                },
                                style={
                                    'fontSize': '1rem',
                                    'lineHeight': '1.5',
                                    'fontWeight': '600',
                                    'color': 'var(--palette-common-white)'
                                }
                            )
                        ],
                        style={
                            'display': 'block'
                        }
                    )
                ],
                style={
                    'gap': '40px',
                    'display': 'flex',
                    'fontSize': '1rem',
                    'lineHeight': '1.5',
                    'fontWeight': '600',
                }
            )
        ],
        style={
            'width': '100%',
            'height': '240px',
            'borderRadius': '16px',
            'position': 'relative',
            'backgroundSize': 'cover',
            'backgroundPosition': 'center',
            'backgroundRepeat': 'no-repeat',
            'backgroundImage': 'url("https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/public/assets/background/background-4.jpg")',
            'transition': 'all 1s ease',
            'padding': '24px',
        },
        className='current-balance-item'
    )

def render_content(
    type,
    idx
):

    return html.Div(
        [
            ldc.Carousel(
                id={
                    'type': f'{type}-carousel',
                    'index': idx
                
                },
                arrows=False,
                infinite=True,
                slides_to_show=1,
                swipe_to_slide=True,
                center_mode=True,
                center_padding='25px',
            ),
            fuc.FefferyStyle(
                rawStyle='''
                    .slick-slide:not(.slick-active):not(.slick-center):not(.slick-current) .current-balance-item {
                        transform: scale(0.90);
                        background-color: rgba(255, 255, 255, 0.7);
                        background-blend-mode: lighten;
                    }
                    # .slick-arrow {
                    #     display: none !important;
                    # }
                '''
            ),
        ]
    )