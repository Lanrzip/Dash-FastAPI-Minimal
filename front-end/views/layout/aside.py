import feffery_antd_components as fac
import feffery_utils_components as fuc
import dash
from dash import html

from config.global_config import MenuConfig
import callbacks.layout_c.aside_c


def render_aside_content():

    return [
        fac.AntdImage(
            src='./assets/imgs/logo.png',
            preview=False,
            className='h-10 w-10 ml-6 mt-6 mb-2'
        ),
        fuc.FefferyScrollbars(
            fac.AntdMenu(
                id='index-side-menu',
                menuItems=MenuConfig.menuItems,
                mode='inline',
                className='index-side-menu',
                style={
                    'height': '100%',
                    'paddingBottom': '50px'
                }
            ),
            style={
                'height': 'calc(100vh - 80px)', # 高度要比整个页面高度少多于72px，否则右侧会出现滚动条
                'overflowY': 'auto',
                'overflowX': 'hidden'
            }
        ),
        
        fac.AntdButton(
            fac.AntdIcon(
                id='fold-side-menu-icon',
                icon='antd-arrow-left',
                className='h-[16px] w-[16px]'
            ),
            id='fold-side-menu',
            type='text',
            shape='circle',
            style={
                'position': 'absolute',
                'zIndex': 1001,
                'top': '32px',
                'left': '264px',
                'background': 'white',
                'color': 'rgb(99, 115, 129)',
                'padding': '4px',
                'border': '1px dashed rgba(145, 158, 171, 0.2)'
            }
        )

    ]