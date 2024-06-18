import dash
from dash import html, dcc
from dash.dependencies import ClientsideFunction, Output, Input
import feffery_antd_components as fac
import feffery_utils_components as fuc

from server import app


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
                    fac.AntdTable(
                        columns=[
                            {
                                'title': 'int型示例',
                                'dataIndex': 'int型示例'
                            },
                            {
                                'title': 'float型示例',
                                'dataIndex': 'float型示例'
                            },
                            {
                                'title': 'str型示例',
                                'dataIndex': 'str型示例'
                            },
                        ],
                        data=[
                            {
                                'int型示例': 123,
                                'float型示例': 1.23,
                                'str型示例': '示例字符',
                            }
                        ] * 3,
                        size='large'
                    ),
                    fuc.FefferyStyle(
                        rawStyle='''
                            .table-card .ant-table-thead>tr>th {
                                background: var(--palette-background-neutral);
                                color: #637381;
                                font-weight: 600;
                                font-size: 14px;
                                line-height: 2.3;
                            }
                            .table-card .ant-table-tbody {
                                font-weight: 400;
                                font-size: 0.875rem;
                                line-height: 3.1;
                                color: var(--palette-text-primary);
                            }
                        '''
                    )
                ],
                className='table-card'
            )
        ],
        style=style
    )
