numeros = []

for i in range(10):
    num = int(input(f"Digite o {i+1} número inteiro: "))
    numeros.append(num)

positivos = 0
negativos = 0
zeros = 0

print("\n--- Números digitados ---")

for num in numeros:
    print(num)

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        zeros += 1

print(f"\nQuantidade de positivos: {positivos}")
print(f"Quantidade de negativos: {negativos}")
print(f"Quantidade de zeros: {zeros}")