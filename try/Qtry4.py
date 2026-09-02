import os
os.system("cls")
while True:
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))
        
        media = (nota1 + nota2 + nota3) / 3
        
        if (media >= 7):
            print("APROVADO!!")
            break
        elif (media>=5):
            print("RECUPERAÇÃO!")
            break   
        else: 
            print("REPROVADO!")
            break
    except:
        print("Erro, somente notas em números!")