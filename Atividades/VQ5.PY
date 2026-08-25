import os
os.system("cls")

senha = input("Digite uma senha de 4 dígitos numéricos: ")

# Executa o laço enquanto a senha NÃO tiver tamanho 4 OU NÃO for composta só por números
while len(senha) != 4 or not senha.isdigit():
    print("Senha Inválida")
    senha = input("Digite uma senha de 4 dígitos numéricos: ")

print("Senha cadastrada com sucesso")