import dash
from dash import html
import feffery_antd_components as fac

from views.components.card import card_with_title


def render_card():

    author_list = [
        {
            'name': '张三',
            'avatar': 'https://api-prod-minimal-v6.vercel.app/assets/images/avatar/avatar-1.webp',
            'favorite': 9911,
            'bgc': 'rgba(var(--palette-primary-mainChannel) / 0.08)',
            'color': 'var(--palette-primary-main)'
        },
        {
            'name': '李四',
            'avatar': 'https://api-prod-minimal-v6.vercel.app/assets/images/avatar/avatar-3.webp',
            'favorite': 9124,
            'bgc': 'rgba(var(--palette-info-mainChannel) / 0.08)',
            'color': 'var(--palette-info-main)'
        },
        {
            'name': '王五',
            'avatar': 'https://api-prod-minimal-v6.vercel.app/assets/images/avatar/avatar-2.webp',
            'favorite': 8798,
            'bgc': 'rgba(var(--palette-error-mainChannel) / 0.08)',
            'color': 'var(--palette-error-main)'
        },
        {
            'name': '赵六',
            'avatar': 'https://api-prod-minimal-v6.vercel.app/assets/images/avatar/avatar-4.webp',
            'favorite': 6674,
            'bgc': 'rgba(var(--palette-secondary-mainChannel) / 0.08)',
            'color': 'var(--palette-secondary-main)'
        },
        {
            'name': '林七',
            'avatar': 'https://api-prod-minimal-v6.vercel.app/assets/images/avatar/avatar-5.webp',
            'favorite': 3320,
            'bgc': 'rgba(var(--palette-warning-mainChannel) / 0.08)',
            'color': 'var(--palette-warning-main)'
        }
    ]


    layout = html.Div(
        [
            html.Div(
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
            for item in author_list
        ],
        style={
            'display': 'flex',
            'flexDirection': 'column',
            'gap': '24px',
            'padding': '0 24px 24px 24px',
        }
    )

    return card_with_title(
        title="最佳作者",
        children=layout,
        style={
            'gridRow': '5/7',
            # 'height': '306px'
        }
    )