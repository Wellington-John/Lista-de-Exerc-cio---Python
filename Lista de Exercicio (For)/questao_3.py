soma = 0
pares = 0
impa = 0

for i in range(1, 51):
    soma += i
    if i % 2 == 0:
        pares += i
    else:
        impa += i

print(f"Soma de todos os números: {soma}")
print(f"Soma de todos os Pares: {pares}")
print(f"Soma de todos os impares: {impa}")