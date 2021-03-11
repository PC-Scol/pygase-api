import requests
from functools import wraps, partial
from pegase_ref_client.api_client import ApiClient, Endpoint
from pegase_ref_client.configuration import Configuration
from pegase_ref_client.apis import StructureApi


ENV = ""
REF_API = f"https://ref.{ENV}/api/v1/ref"
CAS_ENDPOINT = f"https://authn-app.{ENV}/cas/v1/tickets"


def get_token(username, password):
    response = requests.post(
        CAS_ENDPOINT,
        headers={'content-type': 'application/x-www-form-urlencoded'},
        data={'username': username, 'password': password, 'token': 'true'},
    )
    if response.status_code == 201:
        return response.text
    raise Exception(response.status_code)


def get_client(base_url, username, password):
    client_configuration = Configuration(base_url)
    client_configuration.access_token = get_token(username, password)
    return ApiClient(client_configuration)


if __name__ == '__main__':
    client = get_client(REF_API, "username", "mdp???")
    structure_client = StructureApi(client, _check_return_type=False)
    etab00 = structure_client.lire("ETAB00")
    print(etab00, type(etab00))
