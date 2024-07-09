def format_currency(amount):
    return f"{amount:,}"



def validate_data_not_empty(input_data):
    """
    工具方法：根据输入数据校验数据是否不为None和''
    :param input_data: 输入数据
    :return: 校验结果
    """
    return input_data is not None and input_data != ''




def generate_shortcut_panel_data(raw_menu_items):
    """基于侧边菜单栏数据结构推导搜索面板数据结构

    Args:
        raw_menu_items (_type_): 输入的侧边菜单栏数据结构
    """

    output_data = []

    # “概览”
    output_data.extend(
        [
            {
                'id': item['props']['key'],
                'title': item['props']['title'],
                'section': '概览',
                'handler': '() => window.open("%s")' % item['props']['href'],
            }
            for item in raw_menu_items[0]['children']
        ]
    )

    # “管理”
    for level1 in raw_menu_items[1]['children']:
        if level1['component'] == 'SubMenu':
            for level2 in level1['children']:
                # 若为常规菜单项
                # if level2['component'] == 'Item':
                output_data.append(
                    {
                        'id': level2['props']['key'],
                        'title': level1['props']['title'] + ' - ' +  level2['props']['title'],
                        'section': '管理',
                        'handler': '() => window.open("%s")' % level2['props']['href'],
                    }
                )
        elif level1['component'] == 'Item':
            output_data.append(
                {
                    'id': level1['props']['key'],
                    'title': level1['props']['title'],
                    'section': '管理',
                    'handler': '() => window.open("%s")' % level1['props']['href'],
                }
            )

    return output_data