from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

from views.components.card import title_card


def render_box(item, type, idx):

    return html.Div(
        [
            fac.AntdImage(
                src=f'assets/imgs/analytics/{item["img_src"]}',
                width=32,
                height=32,
                preview=False,
                style={
                    # 'display': 'inline-block',
                    'flexShrink': '0',
                }
            ),
            html.H6(
                id={
                    'type': f'{type}-item-count',
                    'index': idx
                },
                style={
                    'fontSize': '1.125rem',
                    'fontWeight': '600',
                    'lineHeight': '1.556',
                    'margin': '8px 0 0',
                    # 'display': 'inline-block',
                }
            ),
            html.P(
                item['title'],
                id={
                    'type': f'{type}-item-title',
                    'index': idx
                },
                style={
                    'fontSize': '0.875rem',
                    'fontWeight': '400',
                    'lineHeight': '1.571',
                    'color': 'var(--palette-text-secondary)',
                    'margin': '0',
                }
            )
        ],
        style={
            'paddingTop': '20px',
            'paddingBottom': '20px',
            'display': 'flex',
            'borderRadius': '12px',
            'textAlign': 'center',
            'alignItems': 'center',
            'flexDirection': 'column',
            'border': 'solid 1px rgba(var(--palette-grey-500Channel) / 0.12)',
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
            render_box(
                {
                    'img_src': 'facebook.png',
                    # 'count': '1234',
                    'title': 'Facebook'
                },
                type=type,
                idx='facebook'
            ),
            render_box(
                {
                    'img_src': 'google.png',
                    # 'count': '2234',
                    'title': 'Google'
                },
                type=type,
                idx='google'
            ),
            render_box(
                {
                    'img_src': 'linkedin.png',
                    # 'count': '3234',
                    'title': 'Linkedin'
                },
                type=type,
                idx='linkedin'
            ),
            render_box(
                {
                    'img_src': 'TwitterX.png',
                    # 'count': '4234',
                    'title': 'Twitter'
                },
                type=type,
                idx='twitter'
            )

        ],
        style={
            'display': 'grid',
            'gridTemplateColumns': 'repeat(2, 1fr)',
            'gap': '16px',
            'padding': '8px 24px 24px 24px',
        }
    )

    return title_card.render_card(
        title=title,
        subtitle=subtitle,
        children=layout,
        style=style,
        title_padding='24px'
    )