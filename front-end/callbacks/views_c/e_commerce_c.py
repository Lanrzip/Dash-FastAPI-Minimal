from random import randint
from dash import html
from dash.dependencies import Output, Input, State, MATCH, ALL, ClientsideFunction

from server import app


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

