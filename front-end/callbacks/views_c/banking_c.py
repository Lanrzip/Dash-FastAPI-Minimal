import dash
from dash.dependencies import Input, Output, State, ClientsideFunction, MATCH

from server import app
from views.overview.banking import current_balance

# app.clientside_callback(
#     ClientsideFunction(
#         namespace='clientside',
#         function_name='handleBankingIncomeExpensesSlidingBox'
#     ),
#     Output('income-expenses-sliding-box', 'style'),
#     [Input('income-div', 'n_clicks'),
#      Input('expenses-div', 'n_clicks')],
#     State('income-expenses-sliding-box', 'style'),
# )

# 切换收入支出卡片
@app.callback(
    [Output('income-expenses-sliding-box', 'style'),
     Output('income-div', 'style'),
     Output('expenses-div', 'style'),
     Output({'type': 'banking-income-expenses-card-line-chart-data', 'index': '收入支出'}, 'data')],
    [Input('income-div', 'n_clicks'),
     Input('expenses-div', 'n_clicks'),
     Input('global-interval-container', 'n_intervals')],
    [State('income-expenses-sliding-box', 'style'),
     State('income-div', 'style'),
     State('expenses-div', 'style')]
)
def slide_income_expenses_div(income_nClicks, expenses_nClicks, n_intervals, sliding_box_style, income_style, expenses_style):
    ctx = dash.callback_context
    if ctx.triggered_id == 'income-div' or not ctx.triggered_id:
        return [
            {
                **sliding_box_style,
                'left': '0px',
            },
            {
                **income_style,
                'color': 'var(--palette-text-primary)',
            },
            {
                **expenses_style,
                'color': 'var(--palette-text-secondary)',
            },
            {
                'data': [820, 932, 901, 934, 1290, 1330, 1320, 2340, 1290, 1330, 1320, 2340],
                'color': '#004B50'
            }
        ]
    elif ctx.triggered_id == 'expenses-div':
        return [
            {
                **sliding_box_style,
                'left': 'calc(50% - 8px)',
            },
            {
                **income_style,
                'color': 'var(--palette-text-secondary)',
            },
            {
                **expenses_style,
                'color': 'var(--palette-text-primary)',
            },
            {
                'data': [460, 530, 450, 530, 690, 820, 850, 1390, 690, 820, 850, 1390],
                'color': '#7A4100'
            }
        ]
    return dash.no_update


# # 切换卡片联动图表
# @app.callback(
#     Output('banking-income-expenses-card-line-chart-data', 'data'),
#     [Input('income-div', 'n_clicks'),
#      Input('expenses-div', 'n_clicks'),
#      Input('global-interval-container', 'n_intervals')]
# )
# def update_banking_income_expenses_chart_data(income_nClicks, expenses_nClicks, n_intervals):
#     ctx = dash.callback_context
#     print(ctx.triggered_id)
#     if ctx.triggered_id == 'n_intervals' or ctx.triggered_id == 'income-div':
#         return [820, 932, 901, 934, 1290, 1330, 1320, 2340, 1290, 1330, 1320, 2340]
    
#     elif ctx.triggered_id == 'expenses-div':
#         return [460, 530, 450, 530, 690, 820, 850, 1390, 690, 820, 850, 1390]
    
#     return dash.no_update
    

app.clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='handleBankingIncomeExpensesChart'
    ),
    Output({'type': 'banking-income-expenses-card-line-chart-container', 'index': MATCH}, 'children'),
    Input({'type': 'banking-income-expenses-card-line-chart-data', 'index': MATCH}, 'data'),
)


@app.callback(
    Output({'type': 'banking-current-balance-card-carousel', 'index': '当前余额'}, 'children'),
    Input('global-interval-container', 'n_intervals'),
)
def update_banking_current_balance_card_carousel(n_intervals):

    card_list = [
        {
            'card_balance': '¥99.99',
            'card_number': '**** **** **** 3640',
            'card_type': 'visa',
            'card_holder': '张三',
            'card_expire_date': '11/22'
        },
        {
            'card_balance': '¥999.99',
            'card_number': '**** **** **** 3641',
            'card_type': 'mastercard',
            'card_holder': '李四',
            'card_expire_date': '12/23'
        },
        {
            'card_balance': '¥9999.99',
            'card_number': '**** **** **** 3642',
            'card_type': 'visa',
            'card_holder': '王五',
            'card_expire_date': '01/24'
        },
    ]

    return [
        current_balance.render_card(item)
        for item in card_list
    ]


@app.callback(
    Output('banking-quick-transfer-card-user-carousel-user-name', 'children'),
    Input({'type': 'banking-quick-transfer-card-user-carousel', 'index': '快速转账'}, 'activeSlide'),
)
def update_banking_quick_transfer_card_user_name(active_slide):
    print(active_slide)

    return str(active_slide)


# 转账金额滑块
@app.callback(
    Output('banking-quick-transfer-card-insert-amount', 'children'),
    Input('banking-quick-transfer-card-amount-slider', 'value'),
)
def update_banking_quick_transfer_card_insert_amount(slider_value):

    return str(slider_value)

# 转账
@app.callback(
    Output('banking-quick-transfer-card-transfer-modal', 'visible'),
    Input('banking-quick-transfer-card-transfer-button', 'nClicks'),
    State('banking-quick-transfer-card-amount-slider', 'value')
)
def open_banking_quick_transfer_card_transfer_modal(n_clicks, slider_value):

    if n_clicks:
        return True
    return False