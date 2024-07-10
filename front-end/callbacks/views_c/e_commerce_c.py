from random import randint
from dash import html
from dash.dependencies import Output, Input, State, MATCH, ALL, ClientsideFunction
import feffery_antd_components as fac

from server import app
from utils.common import format_currency


# 指标卡数据回调测试------------- 待完成 -----------------
@app.callback(
    output=dict(
        indicator_card_value=Output({'type': 'e-commerce-indicator-card-value', 'index': MATCH}, 'children'),
        indicator_card_note_value=Output({'type': 'e-commerce-indicator-card-note-value', 'index': MATCH}, 'children'),
        indicator_card_note_icon=Output({'type': 'e-commerce-indicator-card-note-icon', 'index': MATCH}, 'icon'),
        indicator_card_note_style=Output({'type': 'e-commerce-indicator-card-note-icon', 'index': MATCH}, 'style'),
        indicator_card_note_text=Output({'type': 'e-commerce-indicator-card-note-text', 'index': MATCH}, 'children'),
        indicator_card_chart_data=Output({'type': 'e-commerce-indicator-card-chart', 'index': MATCH}, 'data'),
    ),
    inputs=dict(
        global_interval=Input('global-interval-container', 'n_intervals'),
    ),
    state=dict(
        indicator_card_title=State({'type': 'e-commerce-indicator-card-title', 'index': MATCH}, 'children'),
    ),
    # prevent_initial_call=True
)
def update_indicator_card(global_interval, indicator_card_title):

    item_dict = {
        '售出产品': {
            'value': '765',
            'note-value': '+2.6%',
            'note-icon': 'antd-rise',
            'note-style': {
                'color': '#22C55E',
                'width': '24px',
                'height': '24px',
                'marginTop': '4px'
            },
            'chart_data': [
                {
                    'indicator-mini-chart': [
                        randint(1, 10) for _ in range(11)
                    ],
                }
            ]
        },
        '总余额': {
            'value': '18,765',
            'note-value': '-0.1%',
            'note-icon': 'antd-fall',
            'note-style': {
                'color': '#22C55E',
                'width': '24px',
                'height': '24px',
                'marginTop': '4px'
            },
            'chart_data': [
                {
                    'indicator-mini-chart': [
                        randint(1, 10) for _ in range(11)
                    ],
                }
            ]
        },
        '销售利润': {
            'value': '4,876',
            'note-value': '+0.6%',
            'note-icon': 'antd-rise',
            'note-style': {
                'color': '#FF5630',
                'width': '24px',
                'height': '24px',
                'marginTop': '4px'
            },
            'chart_data': [
                {
                    'indicator-mini-chart': [
                        randint(1, 10) for _ in range(11)
                    ],
                }
            ]
        },
    }
    return dict(
        indicator_card_value=item_dict[indicator_card_title]['value'],
        indicator_card_note_value=item_dict[indicator_card_title]['note-value'],
        indicator_card_note_icon=item_dict[indicator_card_title]['note-icon'],
        indicator_card_note_style=item_dict[indicator_card_title]['note-style'],
        indicator_card_note_text='较上周',
        indicator_card_chart_data=item_dict[indicator_card_title]['chart_data'],
    )



# 图表卡获取数据回调测试------------- 待完成 -----------------
@app.callback(
    [
        Output({'type': 'e-commerce-chart-card-circle-chart-data', 'index': '按性别销售'}, 'data'),
        Output({'type': 'e-commerce-chart-card-area-chart-data', 'index': '年销售额'}, 'data')
    ],
    Input('global-interval-container', 'n_intervals')
)
def update_chart_card_chart_data(n_intervals):

    # 接口形式
    # return get_chart_card_chart_data()

    sale_by_gender_data = {
        'name': ['小孩', '女性', '男性'],
        'value': [3, 2, 1],
        'total': 2324
    }

    yearly_sales_data = {
        'x': ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
        'y': {
            '总支出': [120, 132, 101, 134, 90, 230, 210, 220, 182, 191, 234, 290],
            '总收入': [220, 182, 191, 234, 290, 330, 310, 123, 234, 290, 330, 310],
        }
    }
    return [sale_by_gender_data, yearly_sales_data]


# 浏览器端渲染图表卡图表
app.clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='renderChartCardCircleChart'
    ),
    Output({'type': 'e-commerce-chart-card-circle-chart-container', 'index': MATCH}, 'children'),
    Input({'type': 'e-commerce-chart-card-circle-chart-data', 'index': MATCH}, 'data'),
)


app.clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='renderChartCardAreaChart'
    ),
    Output({'type': 'e-commerce-chart-card-area-chart-container', 'index': MATCH}, 'children'),
    Input({'type': 'e-commerce-chart-card-area-chart-data', 'index': MATCH}, 'data'),
)




# 区域下载量年份选择回调
@app.callback(
    Output({'type': 'e-commerce-chart-card-area-chart-data', 'index': '年销售额'}, 'data', allow_duplicate=True),
    Input({'type': 'e-commerce-chart-card-area-year-select', 'index': '年销售额'}, 'value'),
    prevent_initial_call=True
)
def update_chart_card_area_chart_data(year):

    # return get_chart_card_2_chart_data(year)  # 接口形式
    year_value_dict = {
        2024: {
            'x': ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
            'y': {
                '总支出': [120, 132, 101, 134, 90, 230, 210, 220, 182, 191, 234, 290],
                '总收入': [220, 182, 191, 234, 290, 330, 310, 123, 234, 290, 330, 310],
            }
        },
        2023: {
            'x': ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
            'y': {
                '总支出': [220, 182, 191, 234, 290, 330, 310, 123, 234, 290, 330, 310],
                '总收入': [120, 132, 101, 134, 90, 230, 210, 220, 182, 191, 234, 290],
            }
        },
        2022: {
            'x': ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
            'y': {
                '总支出': [120, 132, 101, 134, 90, 230, 210, 220, 182, 191, 234, 290],
                '总收入': [220, 182, 191, 234, 290, 330, 310, 123, 234, 290, 330, 310],
            }
        }
    }
    return year_value_dict[year]



# 销售概览Progress回调
@app.callback(
    [
        Output({'type': 'e-commerce-progress-card-progress-box-value', 'index': MATCH}, 'children'),
        Output({'type': 'e-commerce-progress-card-progress-box-progress', 'index': MATCH}, 'percent')
    ],
    Input('global-interval-container', 'n_intervals'),
    State({'type': 'e-commerce-progress-card-progress-box-title', 'index': MATCH}, 'children'),
    # prevent_initial_call=True
)
def update_progress_card_progress_box(global_interval, progress_box_title):
    # return get_progress_card_progress()  # 接口形式
    sales_over_progress_data = {
        '总利润': {
            'value': '￥' + format_currency(8374),
            'percent': 10.1
        },
        '总收入': {
            'value': '￥' + format_currency(9714),
            'percent': 13.6
        },
        '总支出': {
            'value': '￥' + format_currency(6871),
            'percent': 28.2
        }
    }
    return [
        sales_over_progress_data[progress_box_title]['value'],
        sales_over_progress_data[progress_box_title]['percent'],
    ]


# 当前余额回调
@app.callback(
    Output({'type': 'e-commerce-current-balance-card-item-value', 'index': MATCH}, 'children'),
    Input('global-interval-container', 'n_intervals'),
    State({'type': 'e-commerce-current-balance-card-item-title', 'index': MATCH}, 'children'),
)
def update_current_balance_card_line(global_interval, item_title):
    # return get_current_balance_card_line()  # 接口形式
    current_balance_data = {
        '合计订单': '￥' + format_currency(287650),
        '盈利': '￥' + format_currency(25500),
        '已退款': '￥' + format_currency(1600),
        '当前余额': '￥' + format_currency(187650),
    }
    return current_balance_data[item_title]



# 最佳销售table-card获取数据回调测试------------- 待完成 -----------------
@app.callback(
    [
        Output({'type': 'e-commerce-table-card-table', 'index': '最佳销售'}, 'columns'),
        Output({'type': 'e-commerce-table-card-table', 'index': '最佳销售'}, 'data'),
    ],
    Input('global-interval-container', 'n_intervals')
)
def update_best_salesman_table_card_data(n_intervals):
    # print('update_table_card_data')
    columns = [
        {
            'title': '销售',
            'dataIndex': '销售',
        },
        {
            'title': '产品',
            'dataIndex': '产品'
        },
        {
            'title': '国家',
            'dataIndex': '国家'
        },
        {
            'title': '总计',
            'dataIndex': '总计'
        },
        {
            'title': '排名',
            'dataIndex': '排名',
            'renderOptions': {
                'renderType': 'tags'
            }
        },
    ]

    best_salesman_items = [
        {
            'avatar': 'https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/mock/assets/images/avatar/avatar-1.webp',
            'name': '张三',
            'product': 'CAP',
            'flag': 'https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/public/assets/icons/flagpack/de.webp',
            'total': '¥83.74',
            'rank_color': 'green'
        },
        {
            'avatar': 'https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/mock/assets/images/avatar/avatar-2.webp',
            'name': '李四',
            'product': 'T-shirt',
            'flag': 'https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/public/assets/icons/flagpack/us.webp',
            'total': '¥75.14',
            'rank_color': 'purple'
        },
        {
            'avatar': 'https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/mock/assets/images/avatar/avatar-3.webp',
            'name': '王五',
            'product': 'Shoes',
            'flag': 'https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/public/assets/icons/flagpack/jp.webp',
            'total': '¥67.14',
            'rank_color': 'blue'
        },
        {
            'avatar': 'https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/mock/assets/images/avatar/avatar-4.webp',
            'name': '赵六',
            'product': 'Pants',
            'flag': 'https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/public/assets/icons/flagpack/kr.webp',
            'total': '¥65.14',
            'rank_color': 'orange'
        },
        {
            'avatar': 'https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/mock/assets/images/avatar/avatar-5.webp',
            'name': '钱七',
            'product': 'Socks',
            'flag': 'https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/public/assets/icons/flagpack/au.webp',
            'total': '¥63.14',
            'rank_color': 'red'
        }
    ]

    data = [
        {
            '销售': html.Div(
                [
                    fac.AntdAvatar(
                        mode='image',
                        src=item['avatar'],
                        size=40,
                    ),
                    item['name']
                ],
                style={
                    'display': 'flex',
                    'alignItems': 'center',
                    'gap': '8px',
                    'fontSize': '0.875rem',
                    'fontWeight': 400,
                    'lineHeight': '1.57',
                    'color': 'var(--palette-text-primary)',
                    'paddingLeft': '8px'
                }
            ),
            '产品': item['product'],
            '国家': html.Div(
                fac.AntdImage(
                    src=item['flag'],
                    height=20,
                    width=26,
                    preview=False,
                    style={'borderRadius': '5px'}
                ),
                style={
                    'display': 'flex',
                    'alignItems': 'center',
                    'justifyContent': 'center',
                }
            ),
            '总计': item['total'],
            '排名': {
                'tag': f'Top {i}',
                'color': item['rank_color']
            }
        }
        for i, item in enumerate(best_salesman_items, start=1)
    ]

    return [columns, data]