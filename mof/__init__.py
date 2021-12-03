from mof_client.api_client import ApiClient
from mof_client.configuration import Configuration
from lib.conf import configuration as conf
from lib.auth import get_token


def mof_client():
    client_configuration = Configuration(conf['MOF']['base_url'])
    client_configuration.access_token = get_token()
    return ApiClient(client_configuration)

