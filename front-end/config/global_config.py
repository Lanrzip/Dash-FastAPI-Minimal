import os
from config.env import AppConfig


class PathConfig:

    # 项目绝对根目录
    ABS_ROOT_PATH = os.path.abspath(os.getcwd())


class RouterConfig:

    # 合法pathname列表
    BASIC_VALID_PATHNAME = [
        '/', '/login', '/forget'
    ]

    # 静态路由列表
    STATIC_VALID_PATHNAME = ['/', '/login', '/forget', '/user/profile']


class ApiBaseUrlConfig:

    BaseUrl = AppConfig.app_base_url + AppConfig.app_proxy_path if AppConfig.app_is_proxy else AppConfig.app_base_url

cn_to_en = {
    '个人资料': 'Profile',
    '卡片': 'Card',
    '列表': 'List',
    '创建': 'Create',
    '编辑': 'Edit',
    '账户': 'Account'
}
class MenuConfig:
    
    overviewSubMenu = {
        '应用 App antd-app-store': [],
        '电商 E-Commerce antd-shopping-cart': [],
        '分析 Analytics antd-line-chart': [],
        '银行 Banking antd-bank': [],
        '预定 Booking antd-book': [],
        '文件 File antd-file-text': []
    }


    managmentSubMenu = {
        '用户 User antd-user': ['个人资料', '卡片', '列表', '创建', '编辑', '账户'],
        '产品 Product antd-sketch': ['列表', '详情', '创建', '编辑'],
        '订单 Order antd-account-book': ['列表', '详情'],
        '发票 Invoice antd-dollar': ['列表', '详情', '创建', '编辑'],
        '博客 Blog antd-idcard': ['列表', '详情', '创建', '编辑'],
        '工作 Job antd-build': ['列表', '详情', '创建', '编辑'],
        '导览 Tour antd-flag': ['列表', '详情', '创建', '编辑'],
        '文件管理 File-Manager antd-folder-open': [],
        '邮件 Mail antd-mail': [],
        '聊天 Chat antd-comment': [],
        '日历 Calendar antd-calendar': [],
        '看板 Kanban antd-fund': []
    }


    otherCasesSubMenu = {
    }

    menuItems = [
        # ------- 概览 -------
        {
            'component': 'ItemGroup',
            'props': {
                'key': '概览',
                'title': '概览',
            },
            'children': [
                {
                    'component': 'Item',
                    'props': {
                        'key': key.split(' ')[0],
                        'title': key.split(' ')[0],
                        'icon': key.split(' ')[2],
                        'href': f'/{key.split(" ")[1].lower()}'
                    }
                }
                for key, value in overviewSubMenu.items()
            ]
        },
        # ------- 管理 -------
        {
            'component': 'ItemGroup',
            'props': {
                'key': '管理',
                'title': '管理',
            },
            'children': [
                {
                    'component': 'SubMenu',
                    'props': {
                        'key': "管理" + key.split(' ')[0],
                        'title': key.split(' ')[0],
                        'icon': key.split(' ')[2]
                    },
                    'children': [
                        {
                            'component': 'Item',
                            'props': {
                                'key': "管理" + key.split(' ')[0]+item,
                                'title': item,
                                'icon': '',
                                'href': f'/{key.split(" ")[1].lower()}/{cn_to_en[item].lower()}' if cn_to_en.get(item) else "404"
                            }
                        }
                        for item in value
                    ]
                }
                if value
                else {
                    'component': 'Item',
                    'props': {
                        'key': "管理" + key.split(' ')[0],
                        'title': key.split(' ')[0],
                        'icon': key.split(' ')[2],
                        'href': f'/{key.split(" ")[1].lower()}'
                    }
                }
                for key, value in managmentSubMenu.items()
                
            ]
            
        }
    ]

    # menuItems = [
    #     {
    #         'component': 'ItemGroup',
    #         'props': {
    #             'key': '概览',
    #             'title': '概览',

    #         },
    #         'children': [
    #             {
    #                 'component': 'Item',
    #                 'props': {
    #                     'key': '应用',
    #                     'title': '应用',
    #                     'icon': '',
    #                     'href': '/app'
    #                 }
    #             },
    #             {
    #                 'component': 'Item',
    #                 'props': {
    #                     'key': '电商',
    #                     'title': '电商',
    #                     'icon': '',
    #                     'href': '/e-commerce'
    #                 }
    #             },
    #             {
    #                 'component': 'Item',
    #                 'props': {
    #                     'key': '分析',
    #                     'title': '分析',
    #                     'icon': '',
    #                     'href': '/analytics'
    #                 }
    #             },
    #             {
    #                 'component': 'Item',
    #                 'props': {
    #                     'key': '银行',
    #                     'title': '银行',
    #                     'icon': '',
    #                     'href': '/banking'
    #                 }
    #             },
    #             {
    #                 'component': 'Item',
    #                 'props': {
    #                     'key': '预定',
    #                     'title': '预定',
    #                     'icon': '',
    #                     'href': '/booking'
    #                 }
    #             },
    #             {
    #                 'component': 'Item',
    #                 'props': {
    #                     'key': '文件',
    #                     'title': '文件',
    #                     'icon': '',
    #                     'href': '/file'
    #                 }
    #             }
    #         ]
    #     },
    #     {
    #         'component': 'ItemGroup',
    #         'props': {
    #             'key': '管理',
    #             'title': '管理',
    #         },
    #         'children': [
    #             {
    #                 'component': 'SubMenu',
    #                 'props': {
    #                     'key': '用户',
    #                     'title': '用户',
    #                     'icon': ''
    #                 },
    #                 'children': [
    #                     {
    #                         'component': 'Item',
    #                         'props': {
    #                             'key': '个人资料',
    #                             'title': '个人资料',
    #                             'icon': '',
    #                             'href': '/user/profile'
    #                         }
    #                     },
    #                     {
    #                         'component': 'Item',
    #                         'props': {
    #                             'key': '卡片',
    #                             'title': '卡片',
    #                             'icon': '',
    #                             'href': '/user/card'
    #                         }
    #                     },
    #                     {
    #                         'component': 'Item',
    #                         'props': {
    #                             'key': '列表',
    #                             'title': '列表',
    #                             'icon': '',
    #                             'href': '/user/list'
    #                         }
    #                     },
    #                     {
    #                         'component': 'Item',
    #                         'props': {
    #                             'key': '创建',
    #                             'title': '创建',
    #                             'icon': '',
    #                             'href': '/user/create'
    #                         }
    #                     },
    #                     {
    #                         'component': 'Item',
    #                         'props': {
    #                             'key': '编辑',
    #                             'title': '编辑',
    #                             'icon': '',
    #                             'href': '/user/edit'
    #                         }
    #                     },
    #                     {
    #                         'component': 'Item',
    #                         'props': {
    #                             'key': '账户',
    #                             'title': '账户',
    #                             'icon': '',
    #                             'href': '/user/account'
    #                         }
    #                     }
    #                 ]
    #             }
    #         ]
    #     }
    # ]