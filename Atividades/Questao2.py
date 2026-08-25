import os
os.system("cls")

numeros = []

while True:
    num = int(input("Digite o número: "))
    if(num!=0):
        numeros.append(num)
    else:
        break
    
soma = sum(numeros)
print(f"A soma dos numeros digitados é {soma}")
