from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc


def render_layout(
    type,
    index,
    img_src,
    title=None,
    style={}
):
    
    return html.Div(
        [
            html.Div(
                fac.AntdImage(
                    src=img_src,
                    preview=False
                ),
                style={
                    'width': '48px',
                    'height': '48px',
                    'marginBottom': '24px',
                }
            ),
            html.Div(
                [
                    fac.AntdIcon(
                        id={
                            'type': f'{type}-trend-icon',
                            'index': index
                        },
                        style={
                            'width': '20px',
                            'height': '20px',
                            'flexShrink': '0',
                            'color': 'var(--palette-primary-darker)',
                        }
                    ),
                    html.Span(
                        id={
                            'type': f'{type}-trend-value',
                            'index': index
                        },
                        style={
                            'fontSize': '0.875rem',
                            'fontWeight': '600',
                            'lineHeight': '1.57',
                            'fontFamily': '"Public Sans Variable", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"'
                        }
                    )
                ],
                style={
                    'top': '16px',
                    'gap': '4px',
                    'right': '16px',
                    'position': 'absolute',
                    'display': 'flex',
                    'alignItems': 'center',
                }
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                title,
                                id={
                                    'type': f'{type}-title',
                                    'index': index
                                },
                                style={
                                    'marginBottom': '8px',
                                    'fontSize': '0.875rem',
                                    'fontWeight': '600',
                                    'lineHeight': '1.57',
                                }
                            ),
                            html.Div(
                                id={
                                    'type': f'{type}-title-value',
                                    'index': index
                                },
                                style={
                                    'fontSize': '1.5rem',
                                    'fontWeight': '700',
                                    'lineHeight': '1.5',
                                }
                            )
                        ],
                        style={
                            'flexGrow': '1',
                            'minWidth': '112px',
                        }
                    ),
                    html.Div(
                        [
                            fac.AntdTable(
                                columns=[
                                    {
                                        'title': '',
                                        'dataIndex': 'indicator-mini-chart',
                                        'renderOptions': {
                                            'renderType': 'mini-line'
                                        },
                                        'width': '50%'
                                    },
                                ],
                                # data=[
                                #     {
                                #         'indicator-mini-chart': [
                                #             3,4,5,5,1,2,3,5,6,3,2
                                #         ],
                                #     }
                                # ],
                                bordered=False,
                                id={
                                    'type': f'{type}-mini-chart',
                                    'index': index
                                },
                            ),
                            fuc.FefferyStyle(
                                rawStyle=f'''
                                    .analytics-indicator-card-{index} .ant-table-thead {{
                                        display: none;
                                    }}
                                    .analytics-indicator-card-{index} .ant-pagination {{
                                        display: none;
                                    }}
                                    .analytics-indicator-card-{index} .tr {{
                                        background-color: {style.get('backgroundColor')};
                                    }}
                                    .analytics-indicator-card-{index} .ant-table-tbody>tr.ant-table-row:hover>td, .ant-table-tbody>tr>td.ant-table-cell-row-hover {{
                                        background-color: {style.get('backgroundColor')};
                                    }}
                                    .analytics-indicator-card-{index} .ant-table-tbody>tr.ant-table-row>td {{
                                        background-color: {style.get('backgroundColor')};
                                    }}
                                '''
                            )
                        ],
                        style={
                            'width': '100px',
                            'height': '80px',
                            'flexShrink': '0',
                            'position': 'absolute',
                            'bottom': -10
                        },
                        className=f'analytics-indicator-card-{index}'
                    )
                ],
                style={
                    'display': 'flex',
                    'flexWrap': 'wrap',
                    'alignItems': 'flex-end',
                    'justifyContent': 'flex-end',
                }
            ),
            html.Span(
                style={
                    'width': '240px',
                    'height': '240px',
                    'display': 'inline-flex',
                    'flexShrink': '0',
                    'backgroundColor': 'currentColor',
                    'mask': 'url("https://pub-c5e31b5cdafb419fb247a8ac2e78df7a.r2.dev/public/assets/background/shape-square.svg") center center / contain no-repeat',
                    'top': '0',
                    'left': '-20px',
                    'zIndex': '-1',
                    'position': 'absolute',
                    'opacity': '0.24',
                    'color': 'var(--palette-primary-main)',
                }
            )
        ],
        style={
            'position': 'relative',
            'color': 'var(--palette-primary-darker)',
            'overflow': 'hidden',
            'borderRadius': '16px',
            'padding': '24px',
            'zIndex': '0',
            **style
        }
    )