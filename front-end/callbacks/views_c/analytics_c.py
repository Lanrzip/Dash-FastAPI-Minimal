from dash.dependencies import Input, Output, State, MATCH, ClientsideFunction

from server import app
from views.overview.analytics import news


@app.callback(
    output=dict(
        indicator_card_title_value=Output({'type': 'analytics-indicator-card-title-value', 'index': MATCH}, 'children'),
        indicator_card_trend_icon=Output({'type': 'analytics-indicator-card-trend-icon', 'index': MATCH}, 'icon'),
        indicator_card_trend_value=Output({'type': 'analytics-indicator-card-trend-value', 'index': MATCH}, 'children'),
        indicator_card_mini_chart_data=Output({'type': 'analytics-indicator-card-mini-chart', 'index': MATCH}, 'data'),
    ),
    inputs=dict(
        interval=Input('global-interval-container', 'n_intervals'),
    ),
    state=dict(
        indicator_card_title=State({'type': 'analytics-indicator-card-title', 'index': MATCH}, 'children'),
    ),
)
def update_analytics_indicator_card(interval, indicator_card_title):
    from random import randint

    item_dict = {
        '周销售量': {
            'title_value': '71.4万',
            'trend': 'antd-rise',
            'trend_value': '12.5%',
            'chart_data': [
                {
                    'indicator-mini-chart': [
                        randint(1, 10) for _ in range(11)
                    ],
                }
            ]
        },
        '新用户': {
            'title_value': '12.3万',
            'trend': 'antd-rise',
            'trend_value': '8.3%',
            'chart_data': [
                {
                    'indicator-mini-chart': [
                        randint(1, 10) for _ in range(11)
                    ],
                }
            ]
        },
        '订单量': {
            'title_value': '9.8万',
            'trend': 'antd-fall',
            'trend_value': '-3.1%',
            'chart_data': [
                {
                    'indicator-mini-chart': [
                        randint(1, 10) for _ in range(11)
                    ],
                }
            ]
        },
        '消息': {
            'title_value': '1.2万',
            'trend': 'antd-rise',
            'trend_value': '2.5%',
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
        indicator_card_title_value=item_dict[indicator_card_title]['title_value'],
        indicator_card_trend_icon=item_dict[indicator_card_title]['trend'],
        indicator_card_trend_value=item_dict[indicator_card_title]['trend_value'],
        indicator_card_mini_chart_data=item_dict[indicator_card_title]['chart_data'],
    )


# 访问量图表卡获取数据回调测试------------- 待完成 -----------------
@app.callback(
    [
        Output({'type': 'analytics-chart-card-pie-chart-data', 'index': '访问量'}, 'data'),
        Output({'type': 'analytics-chart-card-bar-chart-data', 'index': '网站访问量'}, 'data'),
        Output({'type': 'analytics-chart-card-hbar-chart-data', 'index': '兑换率'}, 'data'),
        Output({'type': 'analytics-chart-card-radar-chart-data', 'index': '当前主题'}, 'data')
    ],
    Input('global-interval-container', 'n_intervals')
)
def update_chart_card_chart_data(n_intervals):

    # 接口形式
    # return get_chart_card_chart_data()

    current_visits_data = [
        { 'value': 3500, 'name': '美洲' },
        { 'value': 2500, 'name': '亚洲' },
        { 'value': 1500, 'name': '欧洲' },
        { 'value': 484, 'name': '非洲' },
    ]

    website_visits_data = {
        'source': [
            ['Team', 'Team A', 'Team B'],
            ['一月', 43, 51],
            ['二月', 33, 70],
            ['三月', 45, 24],
            ['四月', 45, 24],
            ['五月', 45, 24],
            ['六月', 45, 24],
            ['七月', 45, 24],
            ['八月', 45, 24],
            ['九月', 45, 24],
            ['十月', 45, 24],
            ['十一月', 45, 24],
            ['十二月', 45, 24]
        ]
    }

    conversion_rates_data = {
        'data': ['Brazil', 'Indonesia', 'USA', 'India', 'China', 'World'],
        'series': [
            {
                'name': '2011',
                'type': 'bar',
                'data': [18203, 23489, 29034, 104970, 131744, 630230]
            },
            {
                'name': '2012',
                'type': 'bar',
                'data': [19325, 23438, 31000, 121594, 134141, 681807]
            }
        ]
    }

    current_subject_data = {
        'indicator': [
            { 'name': 'Sales', 'max': 100 },
            { 'name': 'Administration', 'max': 100 },
            { 'name': 'Information Technology', 'max': 100 },
            { 'name': 'Customer Support', 'max': 100 },
            { 'name': 'Development', 'max': 100 },
            { 'name': 'Marketing', 'max': 100 }
        ],
        'data':  [
            {
                'value': [42, 30, 20, 35, 50, 18],
                'name': 'Series 1'
            },
            {
                'value': [50, 14, 28, 26, 40, 21],
                'name': 'Series 2'
            }
        ],
        'series': ['Series 1', 'Series 2']
    }

    return [
        current_visits_data,
        website_visits_data,
        conversion_rates_data,
        current_subject_data
    ]

# 浏览器端渲染图表卡图表
app.clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='renderChartCardPieChartAnalytics'
    ),
    Output({'type': 'analytics-chart-card-pie-chart-container', 'index': MATCH}, 'children'),
    Input({'type': 'analytics-chart-card-pie-chart-data', 'index': MATCH}, 'data'),
)

app.clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='renderChartCardBarChartAnalytics'
    ),
    Output({'type': 'analytics-chart-card-bar-chart-container', 'index': MATCH}, 'children'),
    Input({'type': 'analytics-chart-card-bar-chart-data', 'index': MATCH}, 'data'),
)

app.clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='renderChartCardHBarChartAnalytics'
    ),
    Output({'type': 'analytics-chart-card-hbar-chart-container', 'index': MATCH}, 'children'),
    Input({'type': 'analytics-chart-card-hbar-chart-data', 'index': MATCH}, 'data'),
)

app.clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='renderChartCardRadarChartAnalytics'
    ),
    Output({'type': 'analytics-chart-card-radar-chart-container', 'index': MATCH}, 'children'),
    Input({'type': 'analytics-chart-card-radar-chart-data', 'index': MATCH}, 'data'),
)



# 新闻卡获取数据回调
@app.callback(
    Output({'type': 'analytics-news-card', 'index': '新闻'}, 'children'),
    Input('global-interval-container', 'n_intervals')
)
def update_top_author_data(n_intervals):
    author_list = [
        {
            'news_img_url': 'https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/mock/assets/images/cover/cover-1.webp',
            'news_title': '可再生能源的未来：未来的创新与挑战',
            'news_detail': '太阳慢慢地落入地平线，将天空染成鲜艳的橙色和粉色。',
            'news_released_date': '12分钟'
        },
        {
            'news_img_url': 'https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/mock/assets/images/cover/cover-2.webp',
            'news_title': '探索人工智能对现代医疗保健的影响',
            'news_detail': '她急切地打开礼物，眼睛里闪烁着兴奋的光芒。',
            'news_released_date': '1小时'
        },
        {
            'news_img_url': 'https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/mock/assets/images/cover/cover-3.webp',
            'news_title': '气候变化及其对全球粮食安全的影响',
            'news_detail': '那棵古老的橡树高大雄伟，树枝在微风中轻轻摇曳。',
            'news_released_date': '2小时'
        },
        {
            'news_img_url': 'https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/mock/assets/images/cover/cover-4.webp',
            'news_title': '远程工作的兴起：优势、挑战和未来趋势',
            'news_detail': '刚煮好的咖啡的香气弥漫在空气中，唤醒了我的感官。',
            'news_released_date': '3天'
        },
        {
            'news_img_url': 'https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/mock/assets/images/cover/cover-5.webp',
            'news_title': '了解区块链技术：超越加密货币',
            'news_detail': '炎热的夏日里，孩子们在洒水喷头旁奔跑，开心地咯咯笑着。',
            'news_released_date': '1周'
        }
        
        
    ]

    return [
        news.render_box(item)
        for item in author_list
    ]


# 按网站划分的流量数据更新
@app.callback(
    Output({'type': 'analytics-traffic-by-site-card-item-count', 'index': MATCH}, 'children'),
    Input('global-interval-container', 'n_intervals'),
    State({'type': 'analytics-traffic-by-site-card-item-title', 'index': MATCH}, 'children')
)
def update_traffic_by_site_card(n_intervals, title):
    from random import randint

    item_dict = {
        'Facebook': {
            'count': 1234
        },
        'Google': {
            'count': 2234
        },
        'Linkedin': {
            'count': 3234
        },
        'Twitter': {
            'count': 4234
        },
    }

    return item_dict[title]['count']