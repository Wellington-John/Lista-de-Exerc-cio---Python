precos = [25.50, 40.00, 15.75, 80.00, 120.50]
media = 0
soma = 0

for preco in precos:
    soma += preco
    if preco < 50:
        print(preco)
    else:
        print(f"{preco} <<<<<<")

media = soma / len(precos)
print(f"\nMédia dos preços: {media}")