import os,random,time

numero_secreto =random.randint(1,20)
tentativas = 0


while True:
    numero = int(input("Informe o Número Secreto: "))
    tentativas +=1
    if(numero == numero_secreto):
        print(f"Parabens voce e foda em {tentativas}° Tentativas.")
        break
    elif(numero_secreto>numero):
        print(f"O  seu Numero e Menor do que Número secreto! {tentativas}° Tentativas.")
        time.sleep(2)
        os.system("cls ")
    else:
        print(f"O seu Número e Maior do que o Número secreto! {tentativas}° Tentativas.")
        time.sleep(2)
        os.system("cls")