temperatura = []

for x in range (5):
    temp = float(input(f"digite a {x+1}° temperatura: "))
    temperatura.append(temp)

media = sum(temperatura)/len(temperatura)
menor = min(temperatura)
maior = max(temperatura)

print(f'A maior temperatura do dia foi {maior}°C')
print(f'A menor temperatura do dia foi {menor}°C')
print(f'A temperatura media do dia foi {media:.1f}°C')