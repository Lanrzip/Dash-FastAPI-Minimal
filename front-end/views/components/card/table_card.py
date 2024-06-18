import dash
from dash import html, dcc
from dash.dependencies import ClientsideFunction, Output, Input
import feffery_antd_components as fac
import feffery_utils_components as fuc

from server import app
from . import card_with_title


def render_card(
    type,
    idx,
    title=None,
    note=None,
    style={}
):

    table_container = html.Div(
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

    return card_with_title(
        title=title,
        note=note,
        children=table_container,
        style=style
    )
