

cn_to_en = {
    '个人资料': 'Profile',
    '卡片': 'Card',
    '列表': 'List',
    '创建': 'Create',
    '编辑': 'Edit',
    '详情': 'Detail',
    '账户': 'Account'
}

def generate_menu_children(key, k=None):
    '''
    生成菜单项
    key: 
    '''
    if k:
        k_href = f'/{key.split(" ")[1].lower()}/{cn_to_en[k].lower()}' if cn_to_en.get(k) else "404"
        return {
            'component': 'Item',
            'props': {
                'key': k_href,
                'title': k,
                'href': k_href
            }
        }
    
    title, eng, icon = key.split(' ')
    hey_href = f'/{eng.lower()}'

    return {
        'component': 'Item',
        'props': {
            'key': hey_href,
            'title': title,
            'icon': icon,
            'href': hey_href
        }
    }

def generate_submenu_children(group, key, value):
    
    
    title, eng, icon = key.split(' ')
    hey_href = f'/{eng.lower()}'

    return (
        {
            'component': 'SubMenu',
            'props': {
                'key': group + title,
                'title': title,
                'icon': icon
            },
            'children': [
                generate_menu_children(key, k)
                for k in value
            ]
        }
        if value
        else {
            'component': 'Item',
            'props': {
                'key': hey_href,
                'title': title,
                'icon': icon,
                'href': hey_href
            }
        }
    )