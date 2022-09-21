"""
Testes relacionados aos endpoints da API.
"""
import requests
import pytest


query_endpoints = [
    "/comprasContratos/v1/contratos?data_publicacao=2021-04-20"
]

path_endpoints = [
    "/comprasContratos/doc/contrato/114325",
    "/comprasContratos/doc/contrato/136100/cronogramas",
    "/comprasContratos/doc/contrato/136100/cronogramas/28589500",
    "/comprasContratos/doc/contrato/84650/despesas_acessorias",
    "/comprasContratos/doc/contrato/84650/despesas_acessorias/215",
    "/comprasContratos/doc/contrato/50500/empenhos",
    "/comprasContratos/doc/contrato/2629/empenhos/8415275",
    "/comprasContratos/doc/contrato/36939/faturas",
    "/comprasContratos/doc/contrato/94113/faturas/78330",
    "/comprasContratos/doc/contrato/105754/garantias",
    "/comprasContratos/doc/contrato/115090/garantias/8423",
    "/comprasContratos/doc/contrato/136100/historicos",
    "/comprasContratos/doc/contrato/93390/historicos/337465",
    "/comprasContratos/doc/contrato/136100/itens_compras_contratos",
    "/comprasContratos/doc/contrato/136100/itens_compras_contratos/853152",
    "/comprasContratos/doc/contrato/119441/prepostos",
    "/comprasContratos/doc/contrato/44820/prepostos/2665",
    "/comprasContratos/doc/contrato/2268/responsaveis",
    "/comprasContratos/doc/contrato/84390/responsaveis/41285",
    "/comprasContratos/doc/contrato/4198/terceirizados",
    "/comprasContratos/doc/contrato/3140/terceirizados/4325"

]

@pytest.mark.parametrize("server", ["http://compras.dados.gov.br/docs/",
                                "http://api.compras.dados.gov.br"]
                        )
def test_url_is_reachable(server: list):
    """
    Testa se o server está respondendo
    """
    print ("Testando a url: " + server)
    assert requests.head(server).ok


@pytest.mark.parametrize("endpoint", query_endpoints)
def test_query_endpoint(get_url: str, prepare_header:dict, endpoint: list):
    """
    Testa o endpoint (formato query)
    TODO: isolar os parâmetros de consulta para cada endpoint no
    padrão query (url...?parametro=valor)
    """

    response = requests.get(get_url + endpoint,
                          headers=prepare_header)
    print ("\nTestando o endpoint: " + get_url  + endpoint)
    assert response.status_code == 200


@pytest.mark.parametrize("endpoint", path_endpoints)
def test_path_endpoint(get_url: str, prepare_header: dict, endpoint: list):
    """
    Testa o endpoint (formato path)
    TODO: isolar os parâmetros de consulta para cada endpoint no
    padrão path (url.../{valor})
    """
    print ("\nTestando o endpoint: " + get_url  + endpoint)
    response = requests.get(get_url  + endpoint,
                          headers=prepare_header)

    assert response.status_code == 200
