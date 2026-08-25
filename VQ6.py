import os
os.system("cls")

notas = []

for i in range(8):
    nota_aluno = float(input(f"Digite a nota do {i+1}° aluno: "))
    notas.append(nota_aluno)
    
media = sum(notas)/len(notas)


notas_acima = []
for nota in notas:
    if nota > media:
        notas_acima.append(nota)
        
        
print(f"\nMédia da turma: {media:.2f}")
print(f"\nNotas acima da média: {notas_acima}")