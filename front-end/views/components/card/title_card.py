from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc





def render_title(
        title=None,
        subtitle=None,
        title_padding='24px 24px 0'
):
    return html.Div(
        [
            html.Span(
                title,
                className='card-title'
            ),
            html.Span(
                subtitle,
                className='card-subtitle'
            )
        ],
        style={
            'display': 'flex',
            'flexDirection': 'column',
            'width': '100%',
            'padding': title_padding
        }
    ) if subtitle else html.Div(
        html.Span(
            title,
            className='card-title',
        ),
        style={
            'padding': title_padding
        }
    )


def render_card(
    title=None,
    subtitle=None,
    children=None,
    style={},
    title_padding='24px 24px 0'
):


    return html.Div(
        [
            render_title(title, subtitle, title_padding),
            children,
        ],
        className='title-card',
        style=style
    )