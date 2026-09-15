temperatura = [28, 30, 27, 31, 29, 32, 26]
soma = 0
media = 0 
maior = temperatura[0]
menor = temperatura[0]

for temp in temperatura:
    soma += temp
    print(f"Temperatura: {temp}")

    if temp > maior:
        maior = temp
    if temp < menor:
        menor = temp

media = soma / len(temperatura)

cout = 0
for temp in temperatura:
    if temp > media:
        cout += 1

print(f"\nTemperatura Média: {media}")
print(f"Maior Temperatura Encontrada: {maior}")
print(f"Menor Temperatura Encontrada: {menor}")
print(f"Quantos Dias Esteve Acima da Média {cout}")