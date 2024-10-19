from projeto_testes.models.enum.sexo import Sexo

class Pessoa:
    def __init__(self, nome: str, idade: str, sexo: Sexo) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo



