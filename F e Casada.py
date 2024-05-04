import os 

os.system("cls || clear")

nome = input("Digite seu nome:")
sexo = input("Digite seu sexo (M ou F):")
estadCivil = input("Digite seu estado civil:")


if sexo == "F" and estadCivil == "Casada":
    quanttemp = int(input("Digite quanto tempo de casamento:"))


print(f"||EXIBINDO DADOS||")
print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado civil: {estadCivil}")


