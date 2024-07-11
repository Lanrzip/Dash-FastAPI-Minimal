import os
from config.env import AppConfig
from utils.menu_gene import generate_menu_children, generate_submenu_children


class PathConfig:

    # 项目绝对根目录
    ABS_ROOT_PATH = os.path.abspath(os.getcwd())


class RouterConfig:

    # 合法pathname列表
    BASIC_VALID_PATHNAME = [
        '/', '/login', '/forget', '/register'
    ]

    # 静态路由列表
    STATIC_VALID_PATHNAME = ['/', '/login', '/forget', '/register', '/application', '/e-commerce', '/analytics', '/user/profile']


class ApiBaseUrlConfig:

    BaseUrl = AppConfig.app_base_url + AppConfig.app_proxy_path if AppConfig.app_is_proxy else AppConfig.app_base_url


class MenuConfig:
    
    overviewSubMenu = {
        '应用 Application antd-app-store': [],
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
                generate_menu_children(key)
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
                generate_submenu_children('管理', key, value)
                for key, value in managmentSubMenu.items()
                
            ]
            
        }
    ]