import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from server import app



# 侧边栏折叠回调
app.clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='handleSideMenuCollapse'
    ),
    [Output('index-side-menu', 'inlineCollapsed'),
     Output('fold-side-menu-icon', 'icon'),
     Output('fold-side-menu', 'style'),
     Output('index-side-menu-container', 'style')],
    Input('fold-side-menu', 'nClicks'),
    State('index-side-menu', 'inlineCollapsed')
)



# url-pathname控制currentKey回调
app.clientside_callback(
    '''
    (data) => {
        if (data) {
            return data['current_key'];
        }
        return window.dash_clientside.no_update;
    }
    ''',
    Output('index-side-menu', 'currentKey'),
    Input('current-key-container', 'data'),
    prevent_initial_call=True
)
