from models.pessoa import Pessoa
from models.endereco import Endereco
from models.enum.sexo import Sexo
from models.enum.unidadefederativa import UnidadeFederativa

pessoa1 = Pessoa(4002, "Marta", "12/10/1926", "71 9899589", "marta.gmail.com", Sexo.FEMININO,
                  Endereco("Rua C", "42", "Residência", "4512121", UnidadeFederativa.SAO_PAULO))


print(pessoa1)