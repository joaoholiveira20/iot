
# import os
# os.system("cls")
    
# # For - Estrutura de repetição com variável de controle
# # while - Estrutura de repetição com condição de parada

# for i in range(61):
#     if i % 2 == 0:
#         print(f"{i} - PAR")
#     else:
#         print(f"{i} - IMPAR")


carrinho = []

while True:
    produto = float(input("Digite o valor do produto: "))
    if produto == 0:
        break
    else:
        carrinho.append(produto)
        
total = sum(carrinho)
print(f"O total da compra é: {total:.2f}")