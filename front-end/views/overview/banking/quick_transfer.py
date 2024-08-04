from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import lanrzip_dash_components as ldc

from utils.common import css_to_dash_style
from views.components.card import title_card


def render_content(
    type,
    idx,
    title=None,
    subtitle=None,
    style={},
):
    children = html.Div(
        [
            html.Div(
                [
                    html.Span(
                        '最近',
                        style={
                            'fontWeight': '700',
                            'fontSize': '0.75rem',
                            'lineHeight': '1.5',
                            'color': 'var(--palette-text-secondary)',
                        }
                    ),
                    fac.AntdButton(
                        '查看全部 >',
                        type='text',
                        # href='/blog/list',
                        style={
                            'fontSize': '0.8125rem',
                            'fontWeight': '700',
                            'borderRadius': '8px',
                        }
                    ),
                ],
                style={
                    'display': 'flex',
                    'alignItems': 'center',
                    'justifyContent': 'space-between',
                }
            ),
            html.Div(
                [
                    html.Span('用户：'),
                    html.Span(id=f'{type}-user-carousel-user-name')
                ],
                style={
                    'display': 'flex',
                    'alignItems': 'center',
                    'justifyContent': 'flex-start',
                    'fontWeight': '600',
                    'fontSize': '1.125rem',
                    'lineHeight': '1.56',
                    'color': 'var(--palette-text-secondary)',
                }
            ),
            ldc.Carousel(
                [
                    html.Div(
                        fac.AntdImage(
                            src=f'https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/mock/assets/images/avatar/avatar-{i}.webp',
                            preview=False,
                            style={
                                'width': '100%',
                                'height': '100%',
                                # 'objectFit': 'cover',
                                'color': 'transparent',
                                'borderRadius': '50%',
                                'overflow': 'hidden',
                                'width': '40px',
                                'height': '40px',
                                'opacity': '0.48',
                                'transition': 'all 300ms cubic-bezier(0.4, 0, 0.2, 1) 0ms',
                                # 'position': 'absolute',
                                # 'left': '0px'
                                'transform': 'translateX(-10px)'
                            },
                            className='quick-transfer-avatar'
                        ),
                        style={
                            'width': '70px',
                            'height': '70px',
                            'display': 'flex',
                            'alignItems': 'center',
                            'justifyContent': 'center',
                            # 'position': 'relative',
                        },
                        
                    )
                    for i in range(1, 12)
                ],
                arrows=True,
                infinite=True,
                slides_to_show=7,
                swipe_to_slide=True,
                center_mode=True,
                center_padding='25px',
                focusOnSelect=True,
                activeSlide=0,
                style={
                    'overflow': 'hidden',
                    'margin': '20px 0',
                    'alignItems': 'center',
                    'justifyContent': 'center',
                    'minHeight': '100px',
                },
                className='banking-quick-transfer',
                id={
                    'type': f'{type}-user-carousel',
                    'index': idx
                }
            ),
            fuc.FefferyStyle(
                rawStyle='''
                    .banking-quick-transfer.slick-track {
                        height: 65px;
                    }
                    .banking-quick-transfer.slick-slide {
                        width: 70px !important;
                    }
                    .slick-slide.slick-active.slick-center.slick-current .quick-transfer-avatar {
                        # height: 50px !important;
                        # width: 50px !important;
                        transform: translateX(-10px) scale(1.25) !important;
                        opacity: 1 !important;
                        box-shadow: 0px 4px 8px 0 rgba(var(--palette-common-blackChannel) / 0.12);
                    }
                '''
            ),
            html.Span(
                '转账金额：',
                style=css_to_dash_style(
                    '''
                        margin: 0px;
                        font-weight: 700;
                        font-size: 0.75rem;
                        line-height: 1.5;
                        text-transform: uppercase;
                        color: var(--palette-text-secondary);
                    '''
                )
            ),
            html.Div(
                [
                    html.Span(
                        '￥',
                        style=css_to_dash_style(
                            '''
                                font-weight: 700;
                                font-size: 1.125rem;
                                line-height: 1.5;
                            '''
                        )
                    ),
                    html.Div(
                        '200',
                        id=f'{type}-insert-amount',
                        style=css_to_dash_style(
                            '''
                                font-weight: 700;
                                font-size: 1.5rem;
                                line-height: 1.5;
                                color: var(--palette-text-primary);
                                box-sizing: border-box;
                                cursor: text;
                                display: inline-flex;
                                -webkit-box-align: center;
                                align-items: center;
                                position: relative;
                            '''
                        )
                    )
                ],
                style={
                    'display': 'flex',
                    'justifyContent': 'center',
                    'margin': '24px 0',
                }
            ),
            fac.AntdSlider(
                min=0,
                max=1000,
                defaultValue=200,
                style={
                    'width': '100%'
                },
                id=f'{type}-amount-slider'
            ),
            html.Div(
                [
                    html.Span(
                        '账户余额',
                        style={
                            'flexGrow': 1,
                        }
                    ),
                    '￥342,12'
                ],
                style=css_to_dash_style(
                    '''
                        margin-top: 32px;
                        margin-bottom: 32px;
                        display: flex;
                        -webkit-box-align: center;
                        align-items: center;
                        font-weight: 600;
                        font-size: 1rem;
                        line-height: 1.5;
                    '''
                )
            ),
            fac.AntdButton(
                '转账',
                id=f'{type}-transfer-button',
                type='primary',
                style={
                    'fontSize': '0.937rem',
                    'fontWeight': '700',
                    'lineHeight': '1.71',
                    'backgroundColor': 'var(--palette-text-primary)',
                    'borderColor': 'var(--palette-text-primary)',
                    'borderRadius': '8px',
                    'height': '48px',
                }
            ),
            fac.AntdModal(
                [
                    html.H2(
                        '转账给',
                        style=css_to_dash_style(
                            '''
                                margin: 0px;
                                font-weight: 600;
                                font-size: 1.0625rem;
                                line-height: 1.55556;
                                flex: 0 0 auto;
                                padding: 24px;
                            '''
                        )
                    ),
                    html.Div(
                        [
                            html.Div(
                                fac.AntdRow(
                                    [
                                        fac.AntdCol(
                                            fac.AntdAvatar(
                                                mode='image',
                                                src='https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/mock/assets/images/avatar/avatar-3.webp',
                                                size=48,
                                            ),
                                        ),
                                        fac.AntdCol(
                                            [
                                                html.Div(
                                                    [
                                                        html.Div(
                                                            '张三',
                                                            style=css_to_dash_style(
                                                                '''
                                                                    margin: 0px;
                                                                    display: block;
                                                                    font-weight: 600;
                                                                    font-size: 0.875rem;
                                                                    line-height: 1.57143;
                                                                '''
                                                            )
                                                        ),
                                                        html.Div(
                                                            'milo.farrell@hotmail.com',
                                                            style=css_to_dash_style(
                                                                '''
                                                                    margin: 4px 0px 0px;
                                                                    font-weight: 400;
                                                                    font-size: 0.875rem;
                                                                    line-height: 1.57143;
                                                                    color: var(--palette-text-secondary);
                                                                    display: block;
                                                                '''
                                                            )
                                                        )
                                                    ],
                                                    style={
                                                        'display': 'block',
                                                    }
                                                ),
                                            ]
                                        ),
                                    ],
                                    gutter=16,
                                    wrap=False
                                )
                            )
                        ],
                        style={
                            'padding': '0 24px',
                            'gap': '24px',
                            'display': 'flex',
                            'flexDirection': 'column',
                        }
                    )
                ],
                id=f'{type}-transfer-modal',
            )
        ],
        style={
            'display': 'flex',
            'flexDirection': 'column',
            'padding': '0 24px 24px 24px',
        }
    )

    return html.Div(
        [
            title_card.render_title(title, subtitle, title_padding='24px'),
            children,
        ],
        style={
            'display': 'flex',
            'flexDirection': 'column',
            'borderRadius': '16px',
            'backgroundColor': 'var(--palette-background-neutral)',
            **style
        }
    )