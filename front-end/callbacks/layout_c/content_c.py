from dash.dependencies import Input, Output

from server import app
from views.overview import *



@app.callback(
    Output('main-content-container', 'children'),
    Input('index-side-menu', 'currentKey'),
    prevent_initial_call=True
)
def handle_side_menu_change(current_key):

    if current_key == '/application':
        return application.render_content()
    
    if current_key == '/e-commerce':
        return e_commerce.render_content()
        
    if current_key == '/analytics':
        return analytics.render_content()
    
    if current_key == '/banking':
        return banking.render_content()
    
    return '404'