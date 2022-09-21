"""
Funções auxiliares e fixtures dos testes.
"""
import pytest
import yaml
from yaml.loader import SafeLoader

@pytest.fixture(scope="module")
def prepare_header() -> dict:
    """Prepara o cabeçalho para ser utilizado em requisições."""

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": 'request'
    }

    return headers

@pytest.fixture(scope="module")
def get_url() -> str:
    """Pega o valor da chave url do arquivo YAML de especificação da API"""
    with open('../openapi.yaml', encoding='utf-8') as file:
        data = yaml.load(file, Loader=SafeLoader)
        url = (data["servers"][0]["url"])

    return url
