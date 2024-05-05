import os 

os.system("cls || clear")

nome = input("Digite seu nome:")
sexo = input("Digite seu sexo (M ou F):")
estadCivil = input("Digite seu estado civil:")

os.system("cls || clear")

print(f"||EXIBINDO DADOS||")
print(f"Nome: {nome} ")
if sexo == "F":
    print("Sexo: Feminino")
else:
    print("Sexo: Masculino")
 
if sexo == "F" and estadCivil == "Casada":
    quanttemp = input("Digite quanto tempo de casamento:")
    print(f"Estado Civil: {estadCivil} com {quanttemp} anos de casamento")
else:
    print(f"Estado Civil: {estadCivil} ")




