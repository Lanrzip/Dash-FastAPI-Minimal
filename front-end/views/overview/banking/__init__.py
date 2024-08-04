import dash
from dash import html
import feffery_antd_components as fac

from views.components.card import indicator_card
from . import (
    income_expenses,
    current_balance,
    quick_transfer
)
import callbacks.views_c.banking_c

def render_content():
    return html.Div(
        [
            html.Div(
                [
                    income_expenses.render_content(
                        type='banking-income-expenses-card',
                        idx='收入支出',
                        style={
                            'gridColumn': '1/3'
                        }
                    )
                ],
                style={
                    'display': 'flex',
                    'flexDirection': 'column',
                    'gap': '24px',
                    'flex': '2',
                }
            ),
            html.Div(
                [
                    current_balance.render_content(
                        type='banking-current-balance-card',
                        idx='当前余额'
                    ),
                    quick_transfer.render_content(
                        type='banking-quick-transfer-card',
                        idx='快速转账',
                        title='快速转账',
                    )
                ],
                style={
                    'display': 'flex',
                    'flexDirection': 'column',
                    'gap': '24px',
                    'flex': '1',
                    'minWidth': 0
                }
            )
        ],
        style={
            # 'display': 'grid',
            # 'gridTemplateColumns': 'repeat(3, minmax(260px, 1fr))',
            # 'gap': '24px',
            'display': 'flex',
            'justifyContent': 'center',
            'gap': '24px',
            'flexDirection': 'row',
            'backgroundColor': '#FFFFFF',
            'padding': '8px 40px 88px 40px',
            'maxWidth': '1536px',
            'margin': '0 auto'
        }
    )

