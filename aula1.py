uni1 = float(input('Digite a nota da 1ª unidade: '))
uni2 = float(input('Digite a nota da 2ª unidade: '))
uni3 = float(input('Digite a nota da 3ª unidade: '))

media = (uni1 + uni2 + uni3) / 3

if(media>=5):
    print(f"A sua média é {media:.1f} - você foi Aprovado!!")
else:
    print(f"A sua média é {media:.1f} - você foi Reprovado!!")