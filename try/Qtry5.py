import os
os.system("cls")

while True:
    try:
        saldo = float(input("Digite o valor do saldo: "))
        saque = float(input("Digite o valor do saque: "))
        
        if (saque <= 0):
            print("O valor do saque deve ser maior que 0!")
        elif (saque <= saldo):
            saque2 = saldo - saque
            print(f"Saque de R${saque} feito com sucesso!!")
            print(f"O saldo restante foi de: R${saque2}")
            break
        else:
            print(f"O valor do saque de {saque} é maior doque o seu saldo disponível!")
    except:
        print("Erro: só números por favor!!")