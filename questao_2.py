def cadastrarProduto(dicionario, nomeP, precoP):
    dicionario[nomeP] = precoP
    return dicionario

produto ={ }
while True:
    nome = str(input("Digite o nome do produto ou (sair para fechar o programa): "))
    if nome == "sair":
        break
    preco = float(input("Digite o valor do produto: "))
    if preco > 0:
        cadastrarProduto(produto, nome, preco)
        print("\n>>>Produto cadastrado<<<\n")

print(" \n{")
for nome, preco in produto.items():
    print(f"     {nome}: {preco}")
print(" }")




