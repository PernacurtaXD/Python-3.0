import os 

os.system("cls || clear")

a = int(input("Digite o primeiro número:"))
b = int(input("Digite o segundo número:"))

if a == b:
    soma = a + b

else:
    soma = a * b

print(f'Valor de C: {soma}')