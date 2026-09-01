import os
os.system("cls")

numeros = []

for i in range(6):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)
    
    
soma = sum(numeros)
maior = max(numeros)
menor = min(numeros)
ordem = sorted(numeros)

print("")
print(f"A soma dos números: {soma}")
print(f"O maior número: {maior}")
print(f"O menor número: {menor}")
print(f"ordem crescente dos números: {ordem}")
