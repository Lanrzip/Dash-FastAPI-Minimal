from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
from .aside import render_aside_content
from .head import render_head_content
from .content import render_main_content

def render_content():
    
    return fuc.FefferyTopProgress(
        html.Div(
            [
                # 全局重载
                fuc.FefferyReload(id='trigger-reload-output'),

                html.Div(id='idle-placeholder-container'),  # 空闲占位符


                # 各种弹窗


                # 平台主页面
                fac.AntdRow(
                    [
                        # 左侧导航栏
                        fac.AntdCol(
                            fac.AntdAffix(
                                html.Div(
                                    render_aside_content(),
                                    id='index-side-menu-container',
                                    style={
                                        'width': '280px',
                                        'height': '100%',  # 右侧出现滚动条的情况下，设置full-screen会使滚动条抽搐
                                        'transition': 'width 0.2s',
                                        'borderRight': '1px solid rgb(240, 240, 240)',
                                        'paddingRight': 10,
                                    }
                                    # className='w-[280px] h-screen transition-width duration-200 border-r border-gray-200 flex-column'
                                ),
                                offsetTop=0
                            ),
                            flex='none'
                            # className='flex-grow-0 flex-shrink-0 basis-auto h-full max-w-full relative'
                        ),
                        # 右侧内容区
                        fac.AntdCol(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            render_head_content(),
                                            className='min-h-20 px-10 flex items-center justify-between sticky top-0 z-1000 mb-4',
                                            style={
                                                'backdropFilter': 'blur(10px)',
                                                'backgroundColor': 'rgba(var(--palette-background-defaultChannel) / 0.8)'
                                            },
                                        ),
                                        html.Div(
                                            render_main_content()
                                        )
                                    ],
                                    # className='flex flex-col h-screen'
                                ),
                            ],
                            flex='auto'
                            # className='flex-grow-1 flex-shrink-1 basis-auto flex flex-col w-full'
                        )
                    ],
                    wrap=False  # 超出不自动换行
                    # className='flex flex-row min-w-full'
                )
            ],
            # id='index-main-content-container',
        )
    )


