from dash import html
from dash.dependencies import Output, Input, State, MATCH, ALL, ClientsideFunction

from views.overview.application import related_applications, top_installed_countries, top_authors

from server import app


# 指标卡数据回调测试------------- 待完成 -----------------
@app.callback(
    output=dict(
        indicator_card_value=Output({'type': 'application-indicator-card-value', 'index': MATCH}, 'children'),
        indicator_card_note_value=Output({'type': 'application-indicator-card-note-value', 'index': MATCH}, 'children'),
        indicator_card_note_icon=Output({'type': 'application-indicator-card-note-icon', 'index': MATCH}, 'icon'),
        indicator_card_note_style=Output({'type': 'application-indicator-card-note-icon', 'index': MATCH}, 'style'),
        indicator_card_note_text=Output({'type': 'application-indicator-card-note-text', 'index': MATCH}, 'children'),
    ),
    inputs=dict(
        global_interval=Input('global-interval-container', 'n_intervals'),
    ),
    state=dict(
        indicator_card_title=State({'type': 'application-indicator-card-title', 'index': MATCH}, 'children'),
    ),
    # prevent_initial_call=True
)
def update_indicator_card(global_interval, indicator_card_title):

    item_dict = {
        '活跃用户': {
            'value': '18765',
            'note-value': '+2.6%',
            'note-icon': 'antd-rise',
            'note-style': {
                'color': '#22C55E',
                'width': '24px',
                'height': '24px',
                'marginTop': '4px'
            },
        },
        '安装次数': {
            'value': '4876',
            'note-value': '+0.2%',
            'note-icon': 'antd-rise',
            'note-style': {
                'color': '#22C55E',
                'width': '24px',
                'height': '24px',
                'marginTop': '4px'
            },
        },
        '下载次数': {
            'value': '678',
            'note-value': '-0.1%',
            'note-icon': 'antd-fall',
            'note-style': {
                'color': '#FF5630',
                'width': '24px',
                'height': '24px',
                'marginTop': '4px'
            },
        },
    }
    return dict(
        indicator_card_value=item_dict[indicator_card_title]['value'],
        indicator_card_note_value=item_dict[indicator_card_title]['note-value'],
        indicator_card_note_icon=item_dict[indicator_card_title]['note-icon'],
        indicator_card_note_style=item_dict[indicator_card_title]['note-style'],
        indicator_card_note_text='较上月'
    )



# 图表卡获取数据回调测试------------- 待完成 -----------------
@app.callback(
    [
        Output({'type': 'application-chart-card-donut-chart-data', 'index': '下载量'}, 'data'),
        Output({'type': 'application-chart-card-bar-chart-data', 'index': '区域下载量'}, 'data')
    ],
    Input('global-interval-container', 'n_intervals')
)
def update_chart_card_chart_data(n_intervals):

    # 接口形式
    # return get_chart_card_chart_data()

    download_data = [
            { 'value': 1048, 'name': 'Search Engine' },
            { 'value': 735, 'name': 'Direct' },
            { 'value': 580, 'name': 'Email' },
            { 'value': 484, 'name': 'Union Ads' },
            { 'value': 300, 'name': 'Video Ads' }
        ]
    area_download_data = [
        {
            'name': 'Email',
            'type': 'bar',
            'stack': 'Ad',
            'emphasis': {
            'focus': 'series'
            },
            'data': [120, 132, 101, 134, 90, 230, 210]
        },
        {
            'name': 'Union Ads',
            'type': 'bar',
            'stack': 'Ad',
            'emphasis': {
            'focus': 'series'
            },
            'data': [220, 182, 191, 234, 290, 330, 310]
        },
        {
            'name': 'Video Ads',
            'type': 'bar',
            'stack': 'Ad',
            'emphasis': {
            'focus': 'series'
            },
            'data': [150, 232, 201, 154, 190, 330, 410]
        }
    ]
    return [download_data, area_download_data]


# 浏览器端渲染图表卡图表
app.clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='renderChartCardDonutChart'
    ),
    Output({'type': 'application-chart-card-donut-chart-container', 'index': MATCH}, 'children'),
    Input({'type': 'application-chart-card-donut-chart-data', 'index': MATCH}, 'data'),
)

app.clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='renderChartCardBarChart'
    ),
    Output({'type': 'application-chart-card-bar-chart-container', 'index': MATCH}, 'children'),
    Input({'type': 'application-chart-card-bar-chart-data', 'index': MATCH}, 'data'),
)



# 区域下载量年份选择回调
@app.callback(
    Output({'type': 'application-chart-card-bar-chart-data', 'index': '区域下载量'}, 'data', allow_duplicate=True),
    Input({'type': 'application-chart-card-bar-year-select', 'index': '区域下载量'}, 'value'),
    prevent_initial_call=True
)
def update_chart_card_bar_chart_data(year):

    # return get_chart_card_2_chart_data(year)  # 接口形式
    year_value_dict = {
        2024: [
            {
                'name': 'Email',
                'type': 'bar',
                'stack': 'Ad',
                'emphasis': {
                'focus': 'series'
                },
                'data': [120, 132, 101, 134, 90, 230, 210]
            },
            {
                'name': 'Union Ads',
                'type': 'bar',
                'stack': 'Ad',
                'emphasis': {
                'focus': 'series'
                },
                'data': [220, 182, 191, 234, 290, 330, 310]
            },
            {
                'name': 'Video Ads',
                'type': 'bar',
                'stack': 'Ad',
                'emphasis': {
                'focus': 'series'
                },
                'data': [150, 232, 201, 154, 190, 330, 410]
            }
        ],
        2023: [
            {
                'name': 'Email',
                'type': 'bar',
                'stack': 'Ad',
                'emphasis': {
                'focus': 'series'
                },
                'data': [220, 182, 191, 234, 290, 330, 310]
            },
            {
                'name': 'Union Ads',
                'type': 'bar',
                'stack': 'Ad',
                'emphasis': {
                'focus': 'series'
                },
                'data': [120, 132, 101, 134, 90, 230, 210]
            },
            {
                'name': 'Video Ads',
                'type': 'bar',
                'stack': 'Ad',
                'emphasis': {
                'focus': 'series'
                },
                'data': [150, 232, 201, 154, 190, 330, 410]
            }
        ],
        2022: [
            {
                'name': 'Email',
                'type': 'bar',
                'stack': 'Ad',
                'emphasis': {
                'focus': 'series'
                },
                'data': [150, 232, 201, 154, 190, 330, 410]
            },
            {
                'name': 'Union Ads',
                'type': 'bar',
                'stack': 'Ad',
                'emphasis': {
                'focus': 'series'
                },
                'data': [120, 132, 101, 134, 90, 230, 210]
            },
            {
                'name': 'Video Ads',
                'type': 'bar',
                'stack': 'Ad',
                'emphasis': {
                'focus': 'series'
                },
                'data': [220, 182, 191, 234, 290, 330, 310]
            }
        ]
    }
    return year_value_dict[year]



# table-card获取数据回调测试------------- 待完成 -----------------
@app.callback(
    Output({'type': 'application-table-card', 'index': '新发票'}, 'data'),
    Input('global-interval-container', 'n_intervals')
)
def update_table_card_data(n_intervals):
    # print('update_table_card_data')
    data = [

        {
            '发票ID': 'INV-1990',
            '类别': 'Android',
            '金额': '¥83.74',
            '状态': {
                'tag': 'Paid',
                'color': 'green'
            }
        },
        {
            '发票ID': 'INV-1991',
            '类别': 'Mac',
            '金额': '¥97.14',
            '状态': {
                'tag': 'Out of date',
                'color': 'red'
            }
        },
        {
            '发票ID': 'INV-1992',
            '类别': 'Windows',
            '金额': '¥68.71',
            '状态': {
                'tag': 'Progress',
                'color': 'orange'
            }
        },
        {
            '发票ID': 'INV-1993',
            '类别': 'Android',
            '金额': '¥85.21',
            '状态': {
                'tag': 'Paid',
                'color': 'green'
            }
        },
        {
            '发票ID': 'INV-1994',
            '类别': 'Mac',
            '金额': '¥52.17',
            '状态': {
                'tag': 'Paid',
                'color': 'green'
            }
        },
    ]

    return data


# tab-card获取数据回调测试------------- 待完成 -----------------
@app.callback(
    Output({'type': 'application-tab-card', 'index': '相关应用'}, 'items'),
    Input('global-interval-container', 'n_intervals')
)
def update_tab_card_data(n_intervals):

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

    item_list = [
        {
            'key': '7日最佳',
            'label': '7日最佳',
            'children': html.Div(
                [
                    related_applications.render_box(item)
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
    ]

    return item_list



# top-installed-country获取数据回调测试------------- 待完成 -----------------
@app.callback(
    Output({'type': 'application-top-country', 'index': '安装最多的国家'}, 'children'),
    Input('global-interval-container', 'n_intervals')
)
def update_top_installed_country_data(n_intervals):
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

    return [
        top_installed_countries.render_box(item)
        for item in country_list
    ]


# top-author获取数据回调测试------------- 待完成 -----------------
@app.callback(
    Output({'type': 'application-top-author', 'index': '最佳作者'}, 'children'),
    Input('global-interval-container', 'n_intervals')
)
def update_top_author_data(n_intervals):
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

    return [
        top_authors.render_box(item)
        for item in author_list
    ]

