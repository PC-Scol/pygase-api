import requests
from lib.conf import configuration


def get_token(username=None, password=None):
    username = username \
        or configuration['AUTH']['username']
    password = password \
        or configuration['AUTH']['password']
    response = requests.post(
        configuration['AUTH']['service'],
        headers={'content-type': 'application/x-www-form-urlencoded'},
        data={'username': username, 'password': password, 'token': 'true'},
    )
    if response.status_code == 201:
        return response.text
    raise Exception(response.status_code)
