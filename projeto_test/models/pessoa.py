from enum.sexo import Sexo

class Pessoa:
    def __init__(self, nome: str, idade: str, sexo: Sexo) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def __str__(self) -> str:
        return f"Nome: {self.nome}\nIdade: {self.idade}\nSexo: {self.sexo.value}"