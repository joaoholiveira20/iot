produtos = []

for i in range(5):
    produto = input(f"Digite o nome do produto {i + 1}: ")
    produtos.append(produto)

print("\nLista completa de produtos:", produtos)
print(f"Quantidade de produtos cadastrados: {len(produtos)}")
