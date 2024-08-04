from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

from views.components.card import title_card


def render_box(label, type, idx): 

    return html.Div(
        [
            html.Div(
                [
                    fac.AntdCheckbox(
                        label=label,
                    ),
                    fuc.FefferyStyle(
                        rawStyle='''
                        .ant-checkbox-wrapper-checked *:last-child {
                            color: var(--palette-text-disabled);
                            text-decoration: line-through;
                        }
                        .ant-checkbox-checked .ant-checkbox-inner {
                            background-color: var(--palette-primary-main);
                            border-color: var(--palette-primary-main);
                        }
                        .ant-checkbox-input:focus+.ant-checkbox-inner, .ant-checkbox-wrapper:hover .ant-checkbox-inner, .ant-checkbox:hover .ant-checkbox-inner {
                            border-color: var(--palette-primary-main);
                        }
                    '''
                    )
                ],
                style={
                    'display': 'flex',
                    'alignItems': 'center',
                    'flexGrow': '1',
                }
            ),
            fac.AntdPopover(
                fac.AntdButton(
                    shape='circle',
                    size='large',
                    type='text',
                    icon=fac.AntdIcon(icon='antd-more'),
                    id={
                        'type': f'{type}-item-more',
                        'index': idx
                    }
                ),
                placement='leftTop',
                trigger='click',
                title='',
                content=html.Div(
                    [
                        fac.AntdButton(
                            '编辑',
                            id={
                                'type': f'{type}-item-edit',
                                'index': idx
                            },
                            type='text',
                            block=True,
                            icon=fac.AntdIcon(icon='antd-edit'),
                        ),
                        fac.AntdButton(
                            '分享',
                            id={
                                'type': f'{type}-item-share',
                                'index': idx
                            },
                            type='text',
                            block=True,
                            icon=fac.AntdIcon(icon='antd-send'),
                        ),
                        fac.AntdButton(
                            '删除',
                            id={
                                'type': f'{type}-item-delete',
                                'index': idx
                            },
                            type='text',
                            block=True,
                            danger=True,
                            icon=fac.AntdIcon(icon='antd-delete'),
                        )
                    ],
                    style={
                        'maxWidth': '120px',
                    }
                ),
            ),
        ],
        style={
            'padding': '12px 8px 12px 16px',
            'display': 'flex',
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
            render_box('准备月度财务报告', type=f'{type}-item', idx=0),
            render_box('设计新的营销活动', type=f'{type}-item', idx=1),
            render_box('分析客户反馈', type=f'{type}-item', idx=2),
            render_box('更新网站内容', type=f'{type}-item', idx=3),
            render_box('进行市场调研', type=f'{type}-item', idx=4),
            render_box('更新客户数据库', type=f'{type}-item', idx=5),
        ],
        style={
            'display': 'flex',
            'flexDirection': 'column',
            'padding': '8px 24px 24px 24px',
            'overflow': 'auto',
        }
    )

    return title_card.render_card(
        title=title,
        subtitle=subtitle,
        children=layout,
        style=style,
        title_padding='24px'
    )