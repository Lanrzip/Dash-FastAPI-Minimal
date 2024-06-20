from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc


def render_layout(
        type,
        idx,
        title=None,
        style={},
):
    
    return html.Div(
        fac.AntdRow(
            [
                fac.AntdCol(
                    html.Div(
                        [
                            html.Div(
                                title,
                                id={
                                    'type': f'{type}-title',
                                    'index': idx
                                },
                                className='card-title',
                            ),
                            html.Div(
                                id={
                                    'type': f'{type}-value',
                                    'index': idx
                                },
                                style={
                                    'marginTop': '12px',
                                    'marginBottom': '8px',
                                    'fontWeight': 700,
                                    'fontSize': '2rem',
                                    'lineHeight': 1.5
                                },
                            ),
                            html.Div(
                                [
                                    fac.AntdIcon(
                                        id={
                                            'type': f'{type}-note-icon',
                                            'index': idx
                                        },
                                        style={
                                            # 'color': '#22C55E',
                                            'width': '24px',
                                            'height': '24px',
                                            'marginTop': '4px'
                                        }
                                    ),
                                    html.Span(
                                        id={
                                            'type': f'{type}-note-value',
                                            'index': idx
                                        },
                                        style={
                                            'fontWeight': 600,
                                            'fontSize': '0.875rem',
                                            'lineHeight': 1.57143
                                        }
                                    ),
                                    html.Span(
                                        id={
                                            'type': f'{type}-note-text',
                                            'index': idx
                                        },
                                        className='card-note',
                                    )
                                ],
                                style={
                                    'display': 'flex',
                                    'alignItems': 'center',
                                    'gap': '4px'
                                }
                            )
                        ],
                        style={
                            'display': 'flex',
                            'flexDirection': 'column',
                            'alignItems': 'flex-start',
                            'flexGrow': '1'
                        }
                    ),
                    flex='auto'
                ),
                fac.AntdCol(
                    html.Div(
                        [
                            fac.AntdTable(
                                columns=[
                                    {
                                        'title': '',
                                        'dataIndex': 'indicator-mini-chart',
                                        'renderOptions': {
                                            'renderType': 'mini-bar'
                                        },
                                        'width': '50%'
                                    },
                                ],
                                data=[
                                    {
                                        'indicator-mini-chart': [
                                            3,4,5,5,1,2,3,5,6,3,2
                                        ],
                                    }
                                ],
                                bordered=False,
                                id={
                                    'type': f'{type}-chart',
                                    'index': idx
                                }
                            ),
                            fuc.FefferyStyle(
                                rawStyle='''
                                    .indicator-card .ant-table-thead {
                                        display: none;
                                    }
                                    .indicator-card .ant-pagination {
                                        display: none;
                                    }
                                '''
                            )
                        ],
                        style={
                            'width': '100px',
                            'height': '100%',
                        },
                    )
                ),
            ],
            wrap=False,
            align='middle',
            style={'width': '100%'}
        ),
        style=style,
        className='indicator-card'
    )