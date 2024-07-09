from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

from views.components.card import title_card


def render_progress_box(
    item_title,
    color,
    type
):

    return html.Div(
        [
            html.Div(
                [
                    html.Span(
                        item_title,
                        style={
                            'flexGrow': '1',
                        },
                        id={
                            'type': f'{type}-progress-box-title',
                            'index': item_title
                        }
                    ),
                    html.Span(
                        id={
                            'type': f'{type}-progress-box-value',
                            'index': item_title
                        }
                    ),
                    # html.Span(
                    #     ' (' + str(percentage) + '%)',
                    #     style={
                    #         'fontWeight': '400',
                    #         'color': 'var(--palette-text-secondary)'
                    #     }
                    # )

                ],
                style={
                    'display': 'flex',
                    'alignItems': 'center',
                    'gap': '4px',
                    'marginBottom': '8px',
                    'fontSize': '0.875rem',
                    'fontWeight': '600',
                    'lineHeight': '1.57',
                    'fontFamily': '"Public Sans Variable", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"',
                }
            ),
            fac.AntdProgress(
                strokeColor=color,
                format={
                    'content': None,
                    'suffix': None
                },
                style={
                    'width': '100%'
                },
                id={
                    'type': f'{type}-progress-box-progress',
                    'index': item_title
                }
            )
        ],
        style={
            'display': 'flex',
            'flexDirection': 'column',
        }
    )


def render_layout(
    type,
    idx,
    title=None,
    subtitle=None,
    style={}
):
    
    layout = html.Div(
        [
            render_progress_box(
                item_title='总利润',
                color='#00A76F',
                type=type
            ),
            render_progress_box(
                item_title='总收入',
                color='#00B7D7',
                type=type
            ),
            render_progress_box(
                item_title='总支出',
                color='#FCA900',
                type=type
            ),
        ],
        style={
            'display': 'flex',
            'flexDirection': 'column',
            'gap': '28px',
            'padding': '8px 24px 24px 24px',
            'overflow': 'auto'
        }
    )

    return title_card.render_card(
        title=title,
        subtitle=subtitle,
        children=layout,
        style=style,
        title_padding='24px'
    )