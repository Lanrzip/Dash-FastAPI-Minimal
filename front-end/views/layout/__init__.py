from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
from .components.aside import render_aside_content

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
                                    id='side-menu-container',
                                    style={
                                        'width': '280px',
                                        # 'height': 'calc(100vh - 1px)',
                                        'transition': 'width 0.2s',
                                        'borderRight': '1px solid rgb(240, 240, 240)',
                                        'paddingRight': 20,
                                }
                                    # className='w-[280px] h-screen transition-width duration-200 border-r border-gray-200 flex-column'
                                ),
                                offsetTop=0,
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
                                            '右侧头部区域',
                                            className='min-h-20 px-10 flex items-center justify-between sticky top-0 bg-white z-1000 mb-4',
                                        ),
                                        html.Div(
                                            html.Div(
                                                '右侧内容区',
                                                # className='min-h-screen',
                                                # className='flex-grow-1'
                                                # style={
                                                #     'minHeight': 'cal(100vh - 90px)',
                                                # }
                                            ),
                                            id='docs-content',
                                            # className='flex-grow-1',
                                            style={
                                                'backgroundColor': 'rgb(255, 255, 255)'
                                            }
                                        )
                                    ],
                                    # className='flex flex-col h-screen'
                                ),
                                # html.Div(
                                    
                                #     className='min-h-screen'
                                #     # className="relative h-full py-[88px] px-4 bg-gray-100",
                                # ),
                            ],
                            flex='auto'
                            # className='flex-grow-1 flex-shrink-1 basis-auto flex flex-col w-full'
                        )
                    ],
                    wrap=False
                    # className='flex flex-row min-w-full'
                )
            ],
            id='index-main-content-container',
        )
    )


