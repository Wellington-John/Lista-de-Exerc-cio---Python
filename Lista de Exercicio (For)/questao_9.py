vendas = [15, 22, 18, 30, 25, 20]
soma = 0
media = 0
maior = vendas[0]

for dia, venda in enumerate(vendas, 1):
    print(f"Dia {dia}: {venda}")
    soma += venda
    if venda > maior:
        maior = venda

media = soma / len(vendas)


print(f"\nMédia: {media:.2f}\n")

for dia, venda in enumerate(vendas, 1):
    if venda > media:
        print(f"Dia: {dia} <<< CIMA DA MÉDIA")

for dia, venda in enumerate(vendas, 1):
        if venda == maior:
            print(f"\nDia {dia}: {maior} <<< MAIOR NÚMERO DE VENDAS")