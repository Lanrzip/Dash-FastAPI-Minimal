import dash
from dash import html
import feffery_antd_components as fac

from views.components.card import card_with_title


def render_card():

    country_list = [
        {
            'name': 'Germany',
            'icon': 'https://raw.githubusercontent.com/demo-minimal/public-assets/main/public/assets/icons/flagpack/de.webp',
            'android': 9911,
            'windows': 1947,
            'apple': 9124
        },
        {
            'name': 'England',
            'icon': 'https://raw.githubusercontent.com/demo-minimal/public-assets/main/public/assets/icons/flagpack/gb.webp',
            'android': 1947,
            'windows': 9124,
            'apple': 6984
        },
        {
            'name': 'France',
            'icon': 'https://raw.githubusercontent.com/demo-minimal/public-assets/main/public/assets/icons/flagpack/fr.webp',
            'android': 9124,
            'windows': 6984,
            'apple': 8488
        },
        {
            'name': 'Korean',
            'icon': 'https://raw.githubusercontent.com/demo-minimal/public-assets/main/public/assets/icons/flagpack/kr.webp',
            'android': 6984,
            'windows': 8488,
            'apple': 9911
        },
        {
            'name': 'USA',
            'icon': 'https://raw.githubusercontent.com/demo-minimal/public-assets/main/public/assets/icons/flagpack/us.webp',
            'android': 8488,
            'windows': 9911,
            'apple': 1947
        },
        {
            'name': 'Japan',
            'icon': 'https://raw.githubusercontent.com/demo-minimal/public-assets/main/public/assets/icons/flagpack/jp.webp',
            'android': 8488,
            'windows': 9911,
            'apple': 1947
        },
        {
            'name': 'Russia',
            'icon': 'https://raw.githubusercontent.com/demo-minimal/public-assets/main/public/assets/icons/flagpack/ru.webp',
            'android': 8488,
            'windows': 9911,
            'apple': 1947
        }
    ]


    layout = html.Div(
        [
            html.Div(
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
                                }
                            ),
                            html.Span(
                                item.get('name'),
                                style={
                                    'fontWeight': '700',
                                    'fontSize': '0.875rem',
                                    'lineHeight': '1.57',
                                    'textOverflow': 'ellipsis',
                                    'whiteSpace': 'nowrap',
                                }
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
                                width=14
                            ),
                            item.get('android')
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
                                src='assets/imgs/operation-system/android.png',
                                preview=False,
                                height=14,
                                width=14
                            ),
                            item.get('windows')
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
                                src='assets/imgs/operation-system/android.png',
                                preview=False,
                                height=14,
                                width=14
                            ),
                            item.get('apple')
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
            for item in country_list
        ],
        style={
            'display': 'flex',
            'flexDirection': 'column',
            'gap': '24px',
            'padding': '0 24px 24px 24px',
            'overflow': 'auto'
        }
    )

    return card_with_title(
        title="安装最多的国家",
        children=layout,
        style={
            'gridRow': '5/7',
            # 'height': '306px'
        }
    )