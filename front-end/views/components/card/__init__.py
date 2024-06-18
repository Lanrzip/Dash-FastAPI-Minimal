from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc


def card_with_title(
        title=None,
        note=None,
        children=None,
        style={}
):

    upper_layout = html.Div(
        [
            html.Span(
                title,
                className='card-title'
            ),
            html.Span(
                note,
                className='card-note'
            )
        ],
        style={
            'display': 'flex',
            'flexDirection': 'column',
            'width': '100%',
        }
    ) if note else html.Div(
        html.Span(
            title,
            className='card-title',
        ),
        style={
            'padding': '24px'
        }
    )


    return html.Div(
        [
            upper_layout,
            children,
        ],
        className='card-with-title',
        style=style
    )