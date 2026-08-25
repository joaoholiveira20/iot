import os
os.system("cls")

import random

nomes = []

for i in range(10):
    nome = input(f"Digite o {i+1}° nome: ")
    nomes.append(nome)
    
nome_sorteado = random.choice(nomes)

print(f"\nO nome sorteado foi: {nome_sorteado}")