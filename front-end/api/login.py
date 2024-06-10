from utils.request import api_request


def login_api(page_obj: dict):

    return api_request(method='post', url='/login/loginByAccount', is_headers=False, data=page_obj)


def logout_api():
    return api_request(method='post', url='/login/logout', is_headers=True)