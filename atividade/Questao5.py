import os
os.system("cls")

nomes = []
contador = 0

while True:
    nome = input("Digite um nome (se quiser encerrar digite FIM): ")
    if nome == "FIM":
        break
    else: 
        nomes.append(nome)
        contador +=1
        
ordem = sorted(nomes)

print("")
print(f"A lista de nomes: {nomes}")
print(f"A lista de nomes em ordem alfabética: {ordem}")
print(f"A quantidade de nomes cadastrados: {contador}")