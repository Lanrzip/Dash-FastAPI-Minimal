from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

from views.components.card import title_card



def render_layout(
    type,
    idx,
    title=None,
    subtitle=None,
    style={}
):

    table_container = html.Div(
        [
            fac.AntdTable(
                size='large',
                id={
                    'type': f'{type}-table',
                    'index': idx
                },
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
                    .table-card .ant-pagination {
                        display: none;
                    }
                '''
            )
        ],
        # style={
        #     'display': 'flex',
        #     'flexDirection': 'column',
        # },
        className='table-card'
    )

    return title_card.render_card(
        title=title,
        subtitle=subtitle,
        children=table_container,
        style=style,
        title_padding='24px'
    )
