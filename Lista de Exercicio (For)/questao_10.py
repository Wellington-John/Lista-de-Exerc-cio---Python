numeros = []
soma = 0
media = 0
par = 0
impa = 0

for i in range(1, 11):
    num = int(input(f"Digite um número{[i]}: "))
    numeros.append(num)

maior = numeros[0]
menor = numeros[0]

print("====Números Digitados===\n")
for num in numeros:
    print(num)
    soma += num

    if num % 2 == 0:
        par += 1
    if num % 2 != 0:
        impa += 1

    if num > maior:
        maior =num
    if num < menor:
        menor = num

media = soma / len(numeros)

print("\n======RELÁTORIO======")
print(f"Quantidade de Números: {len(numeros)}")
print(f"Soma: {soma}")
print(f"Média: {media:.2f}")
print(f"Maior Valor: {maior}")
print(f"Menor Valor: {menor}")
print(f"Quantidade Pares: {par}")
print(f"Quantidade Impares: {impa}")

