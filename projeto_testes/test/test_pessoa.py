import pytest
from projeto_testes.models.pessoa import Pessoa
from ..models.enum.sexo import Sexo 

@pytest.fixture
def pessoa_valida():
    pessoa = Pessoa("Luis", "18", Sexo.MASCULINO)
    return pessoa

def test_pessoa_alterar_nome(pessoa_valida):
    pessoa_valida.nome == "Luis"
    assert pessoa_valida.nome == "Luis"