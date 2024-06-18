import dash
from dash import html, dcc
from dash.dependencies import ClientsideFunction, Output, Input
import feffery_antd_components as fac
import feffery_utils_components as fuc

from server import app
from views.components.box import application_box


def render_card(
        type,
        idx,
        title=None,
        grid_row=None,
        grid_col=None,
        height='540px',
        with_select=False
):
    style = {
        'backgroundColor': '#FFFFFF',
        'transition': 'box-shadow 300ms cubic-bezier(0.4, 0, 0.2, 1) 0ms',
        'overflow': 'hidden',
        'position': 'relative',
        'boxShadow': 'rgba(145, 158, 171, 0.2) 0px 0px 2px 0px, rgba(145, 158, 171, 0.12) 0px 12px 24px -4px',
        'borderRadius': '16px',
        'zIndex': '0',
        'display': 'flex',
        'flexDirection': 'column',
        # 'padding': '24px',
    }
    if grid_row is not None:
        style['gridRow'] = grid_row
    if grid_col is not None:
        style['gridColumn'] = grid_col
    if height is not None:
        style['height'] = height


    application_list = [
        {
            'name': 'Microsoft office 365',
            'icon': 'https://raw.githubusercontent.com/demo-minimal/public-assets/main/public/assets/icons/app/ic-app-1.webp',
            'price': 'Free',
            'downloads': 9911,
            'size': '9.98 Mb',
            'star': 9911
        },
        {
            'name': 'Opera',
            'icon': 'https://raw.githubusercontent.com/demo-minimal/public-assets/main/public/assets/icons/app/ic-app-2.webp',
            'price': 'Free',
            'downloads': 1947,
            'size': '1.9 Mb',
            'star': 1947
        },
        {
            'name': 'Adobe acrobat reader DC',
            'icon': 'https://raw.githubusercontent.com/demo-minimal/public-assets/main/public/assets/icons/app/ic-app-3.webp',
            'price': '￥68.71',
            'downloads': 9124,
            'size': '8.91 Mb',
            'star': 9124
        },
        {
            'name': 'Joplin',
            'icon': 'https://raw.githubusercontent.com/demo-minimal/public-assets/main/public/assets/icons/app/ic-app-4.webp',
            'price': 'Free',
            'downloads': 6984,
            'size': '6.82 Mb',
            'star': 6984
        },
        {
            'name': 'Topaz photo AI',
            'icon': 'https://raw.githubusercontent.com/demo-minimal/public-assets/main/public/assets/icons/app/ic-app-5.webp',
            'price': '￥52.17',
            'downloads': 8488,
            'size': '8.29 Mb',
            'star': 8488
        }
    ]
    
    return html.Div(
        [
            html.Div(
                html.Span(
                    title,
                    className='card-title',
                ),
                style={
                    'padding': '24px'
                }
            ),
            html.Div(
                [
                    fac.AntdTabs(
                        items=[
                            {
                                'key': '7日最佳',
                                'label': '7日最佳',
                                'children': html.Div(
                                    [
                                        application_box.render_box(item)
                                        for item in application_list
                                    ],
                                    className='tab-item-container'
                                )
                            },
                            {
                                'key': '30日最佳',
                                'label': '30日最佳',
                                'children': html.Div(
                                    '30日最佳',
                                    className='tab-item-container'
                                )
                            },
                            {
                                'key': '历史最佳',
                                'label': '历史最佳',
                                'children': html.Div(
                                    '',
                                    className='tab-item-container'
                                )
                            }
                        ],
                        centered=True
                    ),
                    fuc.FefferyStyle(
                        rawStyle='''
                            .application-tab-card .ant-tabs-nav-wrap {
                                background: var(--palette-background-neutral);
                                line-height: 2.3;
                            }
                            .application-tab-card .ant-tabs-tab.ant-tabs-tab-active .ant-tabs-tab-btn {
                                color: var(--palette-text-primary);
                            }
                            .application-tab-card .ant-tabs-tab {
                                color: var(--palette-text-secondary);
                                font-weight: 600;
                            }
                            .application-tab-card .ant-tabs-tab.ant-tabs-tab-active {
                            }

                            .application-tab-card .tab-item-container {
                                display: flex;
                                flex-direction: column;
                                padding: 10px 24px 24px 24px;
                                gap: 24px;
                                min-width: 360px;
                            }
                        '''
                    )
                ],
                className='application-tab-card'
            )
        ],
        style=style
    )
