import os
os.system("cls")

while True:
    try:
        import os
        os.system("cls")
    
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        soma = num1 + num2
        print("\n=== RESULTADO ===")
        print(f"resultado da soma: {soma}")
        break
    except:
        print("Erro: somente números!")