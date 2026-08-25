
numeros = []

for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)


qtd_positivos = 0
qtd_negativos = 0
soma_positivos = 0
vetor_negativos = []

for num in numeros:
    if num > 0:
        qtd_positivos += 1
        soma_positivos += num
    elif num < 0:
        qtd_negativos += 1
        vetor_negativos.append(num)


print("\n--- RESULTADOS ---")
print(f"Quantidade de números positivos: {qtd_positivos}")
print(f"Quantidade de números negativos: {qtd_negativos}")
print(f"Vetor com os números negativos: {vetor_negativos}")
print(f"Soma dos números positivos: {soma_positivos}")