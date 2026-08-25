import os
os.system("cls")

nomes = []

for i in range(5):
    nome = input(f"Digite o {i+1}° nome: ")
    nomes.append(nome)
    
ordem = sorted(nomes)

print(f"Os nomes em ordem alfabética: {ordem}")