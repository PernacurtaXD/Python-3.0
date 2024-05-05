import os 

os.system("cls || clear")

a = int(input("Digite o primeiro número:"))
b = int (input("Digite o segundo número:"))
c = int(input("Digite o terceiro número:"))

soma= a+ b

if soma < c:
    print("Total menor que C")
else: 
    print("Total maior que C")    