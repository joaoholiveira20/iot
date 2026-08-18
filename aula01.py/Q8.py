import os
os.system("cls")

while True:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    operacao = input("Digite uma operação (+ - * / ): ")


    match operacao:
        case "+": 
            soma = num1 + num2
            print(f"\nSOMA: {num1} + {num2} = {soma}")
            break
        case "-":
            sub = num1 - num2
            print(f"\nSUBTRAÇÃO: {num1} - {num2} = {sub}")
            break
        case "*":
            mult = num1 * num2
            print(f"\nMULTIPLICAÇÃO: {num1} * {num2} = {mult}")
            break
        case "/":
            div = num1 / num2
            print(f"\nDIVISÃO: {num1} / {num2} = {div}")
            break
        case _:
            import os
            os.system("cls")
            print("Por favor, digite um operador!")

