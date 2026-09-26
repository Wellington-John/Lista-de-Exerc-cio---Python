def adicionarProduto(nomeP, unidadeP, precoP):
    carrinho = {
        "nome": nomeP,
        "quantidade": unidadeP,
        "preco": precoP
    }
    return carrinho

def calcularTotal(carrinho):
    valor_final = 0
    for produto in carrinho:
        total = produto["quantidade"] * produto["preco"]
        valor_final += total
    return valor_final

carrinho = []
while True:
    nomeProduto = input("Digite o nome do produto: ")
    if nomeProduto == "sair":
        break
    quantidadeProduto = int(input("Digite o quantidade do produto: "))
    precoProduto = float(input("Digite o preço do produto: "))

    carrinho.append(adicionarProduto(nomeProduto, quantidadeProduto, precoProduto))
    print(f"\n>>>>Produto {nomeProduto} foi adiconado ao carrinho<<<<\n")

print("=======CARRINHO=======")
for produtos in carrinho:
    print(f"{produtos["quantidade"]}x {produtos["nome"]} R${produtos["preco"]:.2f}")


valorPagar = calcularTotal(carrinho)
print(f"\nVALOR A PAGAR: R${valorPagar:.2f}")