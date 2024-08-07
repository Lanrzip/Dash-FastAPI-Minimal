import dash
from dash import html
import feffery_antd_components as fac

from views.components.card import indicator_card
from . import (
    sale_by_gender,
    yearly_sales,
    sales_overview,
    current_balance,
    best_salesman,
    latest_products
)
import callbacks.views_c.e_commerce_c


def render_carsousel(
    tag,
    title,
    img_url,
    index
):
    
    return html.Div(
                html.Div(
                    [
                        fac.AntdText(
                            tag,
                            style = {
                                'fontWeight': '700',
                                'lineHeight': '1.5',
                                'fontSize': '0.95rem',
                                'color': 'rgba(104, 205, 249, 0.48)'
                            }

                        ),
                        fac.AntdText(
                            title,
                            style = {
                                'fontWeight': '700',
                                'lineHeight': '1.5',
                                'fontSize': '1.125rem',
                                'overflow': 'hidden',
                                'textOverflow': 'ellipsis',
                                'whiteSpace': 'nowrap',
                                'color': 'rgb(255, 255, 255)'
                            }
                        ),
                        fac.AntdButton(
                            '购买',
                            id={
                                'type': 'e-commerce-carousel-card-buy-button',
                                'index': index
                            },
                            type='primary',
                            style={
                                'backgroundColor': 'var(--palette-primary-main)',
                                'borderColor': 'var(--palette-primary-main)',
                                'borderRadius': '8px',
                                'fontWeight': '700',
                                'fontSize': '0.875rem',
                                'marginTop': '16px',
                                'width': '80px'
                            }
                        ),
                    ],
                    style={
                        'width': '100%',
                        'overflow': 'hidden',
                        'display': 'flex',
                        'flexDirection': 'column',
                        'gap': '8px',
                        'padding': '24px',
                        'bottom': '0px',
                        # 'zIndex': '9',
                        'textAlign': 'left',
                        'position': 'absolute',
                        'color': 'rgb(255, 255, 255)'
                    }
                ),
                style={
                    'height': '320px',
                    'borderRadius': '16px',
                    'position': 'relative',
                    'backgroundImage': (
                        'linear-gradient(to bottom, rgba(0, 0, 0, 0) -20%, rgba(0, 0, 0, 1) 100%), '
                        'url({})'.format(img_url)
                    ),
                    'backgroundRepeat': 'no-repeat',  # 确保背景图像覆盖整个元素
                    'backgroundSize': 'cover',  # 防止背景图像重复
                }
            )

def render_content():
    return html.Div(
        [
            fac.AntdRow(
                [
                    fac.AntdCol(
                        html.Div(
                            [
                                fac.AntdText(
                                    '祝贺🎉 \n张三',
                                    style={
                                        'color': '#FFFFFF',
                                        'fontSize': '1.5rem',
                                        'fontWeight': '700',
                                        'lineHeight': '1.5',
                                        'marginBottom': '16px',
                                        'whiteSpace': 'pre-line'
                                    }
                                ),
                                fac.AntdText(
                                    "作为本月最畅销商品，您今天的销量增长了 57.6%。",
                                    style={
                                        'color': '#FFFFFF',
                                        'marginBottom': '40px',
                                        'lineHeight': '1.57',
                                        'fontSize': '0.875rem',
                                        'fontWeight': '400',
                                        'opacity': '0.8',
                                        'maxWidth': '360px'
                                    }
                                ),
                                fac.AntdButton(
                                    '出发',
                                    id='e-commerce-start-button',
                                    type='primary',
                                    style={
                                        'fontSize': '0.875rem',
                                        'fontWeight': '700',
                                        'backgroundColor': 'var(--palette-primary-main)',
                                        'borderColor': 'var(--palette-primary-main)',
                                        'borderRadius': '8px',
                                    }
                                ),
                            ],
                            style={
                                'height': '100%',
                                'width': '100%',
                                'padding': '56px 40px',
                                'display': 'flex',
                                'flexDirection': 'column',
                                'alignItems': 'flex-start'
                            }
                        ),
                        flex='3'
                    ),
                    fac.AntdCol(
                        html.Div(
                            [
                                fac.AntdImage(
                                    src='./assets/imgs/e-commerce/image.png',
                                    preview=False,
                                    height=150,
                                ),
                                html.Div(
                                    fac.AntdImage(
                                        src='./assets/imgs/e-commerce/character-2.webp',
                                        height=160,
                                        preview=False
                                    ),
                                    style={
                                        'position': 'absolute',
                                        'right': '30px',
                                    }
                                )
                            ],
                            style={
                                'height': '100%',
                                'width': '100%',
                                'padding': '24px',
                                'display': 'flex',
                                'justifyContent': 'center',
                                'alignItems': 'center',
                                'position': 'relative'
                            }
                        ),
                        flex='2'
                    )
                ],
                wrap=False,
                style={
                    'backgroundColor': '#0A323C',
                    'borderRadius': '16px',
                    'height': '100%',
                    'gridColumn': '1/3',
                    'height': '320px'
                    # 'minWidth': '520px'
                }
            ),
            fac.AntdCarousel(
                [
                    render_carsousel(
                        tag='新品',
                        title='城市探险家运动鞋',
                        img_url='https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/mock/assets/images/m-product/product-1.webp',
                        index=0
                    ),
                    render_carsousel(
                        tag='新品',
                        title='经典皮革乐福鞋',
                        img_url='https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/mock/assets/images/m-product/product-2.webp',
                        index=1
                    ),
                    render_carsousel(
                        tag='新品',
                        title='山地徒步靴',
                        img_url='https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/mock/assets/images/m-product/product-3.webp',
                        index=2
                    ),
                    render_carsousel(
                        tag='新品',
                        title='优雅细高跟鞋',
                        img_url='https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/mock/assets/images/m-product/product-4.webp',
                        index=3
                    ),
                ],
                dotPosition='top',
                autoplay=True,
            ),
            indicator_card.render_layout(
                type='e-commerce-indicator-card',
                idx='售出产品',
                title='售出产品',
                chart_type='mini-line',
                style={
                    'height':'162px'
                }
            ),
            indicator_card.render_layout(
                type='e-commerce-indicator-card',
                idx='总余额',
                title='总余额',
                chart_type='mini-line',
                style={
                    'height':'162px'
                }
            ),
            indicator_card.render_layout(
                type='e-commerce-indicator-card',
                idx='销售利润',
                title='销售利润',
                chart_type='mini-line',
                style={
                    'height':'162px'
                }
            ),
            sale_by_gender.render_layout(
                type='e-commerce-chart-card-circle',
                idx='按性别销售',
                title="按性别销售",
                style={
                    'height': '500px'
                }
            ),
            yearly_sales.render_layout(
                type='e-commerce-chart-card-area',
                idx='年销售额',
                title="年销售额",
                subtitle="(+43%) 比去年",
                style={
                    'height': '500px',
                    'gridColumn': '2/4'
                }
            ),
            sales_overview.render_layout(
                type='e-commerce-progress-card',
                idx='销售概览',
                title="销售概览",
                style={
                    'height': '320px',
                    'gridColumn': '1/3'
                }
            ),
            current_balance.render_layout(
                type='e-commerce-current-balance-card',
                title="当前余额",
                style={
                    'height': '320px',
                    'gridColumn': '3/4'
                }
            ),
            best_salesman.render_layout(
                type='e-commerce-table-card',
                idx='最佳销售',
                title='最佳销售',
                style={
                    # 'height': '540px',
                    'gridColumn': '1/3'
                }
            ),
            latest_products.render_layout(
                type='e-commerce-latest-products-card',
                idx='最新产品',
                title='最新产品',
                style={
                }
            )
        ],
        style={
            'display': 'grid',
            'gridTemplateColumns': 'repeat(3, minmax(260px, 1fr))',
            'gap': '24px',
            'backgroundColor': '#FFFFFF',
            'padding': '8px 40px 88px 40px',
            'maxWidth': '1536px',
            'margin': '0 auto'
        }
    )

