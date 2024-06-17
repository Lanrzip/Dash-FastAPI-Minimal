import dash
from dash.dependencies import Output, Input, State, MATCH, ALL, ClientsideFunction

from server import app


# 指标卡数据回调测试------------- 待完成 -----------------
@app.callback(
    output=dict(
        indicator_card_value=Output({'type': 'application-indicator-card-value', 'index': MATCH}, 'children'),
    ),
    inputs=dict(
        global_interval=Input('global-interval-container', 'n_intervals')
    ),
    state=dict(
        indicator_card_value=State({'type': 'application-indicator-card-value', 'index': MATCH}, 'children'),
    ),
    prevent_initial_call=True
)
def update_indicator_card(global_interval, indicator_card_value):
    
    return dict(
        indicator_card_value=int(indicator_card_value)+1
    )



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