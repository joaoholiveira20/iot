import os
os.system("cls")

while True:
    try: 
        numero = int(input("Digite um número: "))
        
        for i in range(1, 11):
            tabuada = numero * i
            print(f"{numero} * {i} = {tabuada}")
    except:
        print("Erro: somente números!")