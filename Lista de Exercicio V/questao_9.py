def cadastroCliente(nomeP, emailP, telefoneP):
    dicionario = {
        "nome": nomeP,
        "email": emailP,
        "telefone": telefoneP,
    }
    return dicionario

def realizarCadastro(listaCadastro):
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    telefone = input("Digite seu telefone: ")
    listaCadastro.append(cadastroCliente(nome, email, telefone))
    print("Cadastro Realizado<<<<<\n")

def listaClientes(listaClientes):
    if len(listaClientes) == 0:
        print("Lista vazia<<<<<")
    else:
        for cliente in listaClientes:
            print(f"{cliente['nome']}")

def pesquisar(listaClientes):
    if len(listaClientes) > 0:
        nomePesquisa = input("\nDIgite o nome que deseja pesquisar: ")
        encontrado = False
        for cliente in listaClientes:
            if cliente["nome"].lower() == nomePesquisa.lower():
                print(">>>CLIENTE ENCONTRADO<<<\n")
                print(f"Nome: {cliente['nome']}| Email: {cliente['email']}| Telefone: {cliente['telefone']}\n")
                encontrado = True
                break

        if encontrado == False:
            print("O nome não está na lista")
    else:
        print("Nome não está na lista!")


listaCadastro = []
while True:
    print("\n1 - Cadastrar Cliente ")
    print("2 - Mostrar Lista de Cientes ")
    print("3 - Pesquisar Cliente ")
    print("4 - Sair ")
    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            print("\n---Realizar Cadastro---")
            realizarCadastro(listaCadastro)
        case 2:
            listaClientes(listaCadastro)
        case 3:
            pesquisar(listaCadastro)
        case 4:
            print("Clesed program")
            break
        case _:
            print("Opção invalida")
