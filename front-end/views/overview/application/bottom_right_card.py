from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc


def render_card(
    value,
    percent,
    note,
    theme,
):
    
    img = {
        'primary': './assets/imgs/user.png',
        'info': './assets/imgs/mail.png'
    }

    return html.Div(
        [
            html.Div(
                [
                    fac.AntdProgress(
                            percent=percent,
                            type='circle',
                            strokeColor={
                                'from': f'var(--palette-{theme}-light)',
                                'to': f'var(--palette-{theme}-main)'
                            },
                            size='small',
                        ),
                    fuc.FefferyStyle(
                        rawStyle='''
                    .ant-progress-circle .ant-progress-text {
                        color: var(--palette-common-white);
                        font-weight: 600;
                        font-size: 1.25rem;
                        line-height: 1.5;
                    }
                    '''
                    )
                ]
            ),
            html.Div(
                [
                    html.Div(
                        value,
                        style={
                            'fontSize': '1.5rem',
                            'fontWeight': '700',
                            'lineHeight': '1.5',
                            'color': 'var(--palette-common-white)',
                        }
                    ),
                    html.Div(
                        note,
                        style={
                            'fontWeight': '600',
                            'fontSize': '0.875rem',
                            'lineHeight': '1.57',
                            'opacity': '0.64',
                            'color': 'var(--palette-common-white)',
                        }
                    )
                ],
                style={
                    'display': 'flex',
                    'flexDirection': 'column',
                }
            ),
            html.Div(
                fac.AntdImage(
                    src=img[theme],
                    width=130,
                    height=130,
                    preview=False,
                    style={
                        'flexShrink': '0',
                        'display': 'inline-flex',
                        'right': '-25px',
                        'opacity': '0.12',
                        'position': 'absolute',
                        'color': 'var(--palette-common-white)',
                    }
                ),
            )
        ],
        style={
            # 'height': '141px',
            'padding': '24px',
            'gap': '24px',
            'borderRadius': '16px',
            'display': 'flex',
            'alignItems': 'center',
            'color': 'var(--palette-common-white)',
            'backgroundColor': f'var(--palette-{theme}-dark)',
            'overflow': 'hidden',
        }
    )

    