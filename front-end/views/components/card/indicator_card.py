from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc


def render_card(
        type,
        idx,
        title=None,
        value=None,
        note=None,
        grid_row=None,
        grid_col=None,
        height='162px',
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
        'alignItems': 'center',
        'padding': '24px',
    }
    if grid_row is not None:
        style['gridRow'] = grid_row
    if grid_col is not None:
        style['gridColumn'] = grid_col
    if height is not None:
        style['height'] = height

    
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
                                value,
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
                                        icon=f'antd-{note[0]}',
                                        id={
                                            'type': f'{type}-note-icon',
                                            'index': idx
                                        },
                                        style={
                                            'color': '#22C55E' if note[0] == 'rise' else '#FF5630',
                                            'width': '24px',
                                            'height': '24px',
                                            'marginTop': '4px'
                                        }
                                    ),
                                    html.Span(
                                        note[1],
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
                                        note[2],
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
                                        'dataIndex': 'mini-bar示例1',
                                        'renderOptions': {
                                            'renderType': 'mini-bar'
                                        },
                                        'width': '50%'
                                    },
                                ],
                                data=[
                                    {
                                        'mini-bar示例1': [
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
                        className='indicator-card'
                    )
                ),
            ],
            wrap=False,
            align='middle',
            style={'width': '100%'}
        ),
        style=style
    )