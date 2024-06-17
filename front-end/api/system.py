from utils.request import api_request


def login_api(page_obj: dict):

    return api_request(method='post', url='/system/login', is_headers=False, data=page_obj)


def logout_api():

    return api_request(method='post', url='/system/logout', is_headers=True)


def register_api(page_obj: dict):
    
    return api_request(method='post', url='/system/register', is_headers=True, json=page_obj)