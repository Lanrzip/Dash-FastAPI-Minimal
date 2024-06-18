from dash import html
import feffery_antd_components as fac


def render_box(
    item
):
    
    return html.Div(
                fac.AntdRow(
                    [
                        fac.AntdCol(
                            html.Div(
                                fac.AntdImage(
                                    src=item.get('icon'),
                                    preview=False
                                ),
                                style={
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center',
                                    'height': '48px',
                                    'width': '48px',
                                    'backgroundColor': 'var(--palette-background-neutral)',
                                    'borderRadius': '12px',
                                    'padding': '8px'
                                }
                            )
                        ),
                        fac.AntdCol(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.H6(
                                                    item.get('name'),
                                                    style={
                                                        'fontWeight': '600',
                                                        'fontSize': '0.875rem',
                                                        'overflow': 'hidden',
                                                        'textOverflow': 'ellipsis',
                                                        'whiteSpace': 'nowrap',
                                                    }
                                                ),
                                                html.Span(
                                                    item.get('price'),
                                                    style = {
                                                        'minWidth': '24px',
                                                        'padding': '0px 6px',
                                                        'fontSize': '0.75rem',
                                                        'fontWeight': '700',
                                                        'borderRadius': '6px',
                                                        'color': 'var(--palette-text-secondary)' if item.get('price') == 'Free' else 'var(--palette-success-dark)',
                                                        'backgroundColor': 'rgba(var(--palette-grey-500Channel) / 0.16)' if item.get('price') == 'Free' else 'rgba(var(--palette-success-mainChannel) / 0.16)',
                                                        'height': '20px'
                                                    }
                                                )
                                            ],
                                            style={
                                                'display': 'flex',
                                                'alignItems': 'center',
                                                'gap': '8px',
                                                'marginBottom': '8px',
                                                'color': 'var(--palette-text-primary)'
                                            }
                                        ),
                                        html.Div(
                                            [
                                                html.Div(
                                                    [
                                                        fac.AntdIcon(
                                                            icon='antd-download'
                                                        ),
                                                        item.get('downloads')
                                                    ],
                                                    style={
                                                        'display': 'flex',
                                                        'alignItems': 'center',
                                                        'gap': '4px',
                                                    }
                                                ),
                                                html.Div(
                                                    style={
                                                        'width': '4px',
                                                        'height': '4px',
                                                        'borderRadius': '50%',
                                                        'backgroundColor': 'var(--palette-text-disabled)',
                                                    }
                                                ),
                                                html.Div(
                                                    [
                                                        fac.AntdIcon(
                                                            icon='antd-save'
                                                        ),
                                                        item.get('size')
                                                    ],
                                                    style={
                                                        'display': 'flex',
                                                        'alignItems': 'center',
                                                        'gap': '4px',
                                                    }
                                                ),
                                                html.Div(
                                                    style={
                                                        'width': '4px',
                                                        'height': '4px',
                                                        'borderRadius': '50%',
                                                        'backgroundColor': 'var(--palette-text-disabled)',
                                                    }
                                                ),
                                                html.Div(
                                                    [
                                                        fac.AntdIcon(
                                                            icon='antd-star',
                                                            style={
                                                                'color': 'rgb(250, 175, 0)'
                                                            }
                                                        ),
                                                        item.get('star')
                                                    ],
                                                    style={
                                                        'display': 'flex',
                                                        'alignItems': 'center',
                                                        'gap': '4px',
                                                    }
                                                )
                                            ],
                                            style={
                                                'display': 'flex',
                                                'alignItems': 'center',
                                                'gap': '8px',
                                                'fontSize': '0.75rem',
                                                'fontWeight': '400',
                                                'lineHeight': '1.5',
                                            }
                                        )
                                    ],
                                    style={
                                        'display': 'block',
                                    }
                                ),
                            ]
                        ),
                    ],
                    gutter=16,
                    wrap=False
                )
            )