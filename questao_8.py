def adicionarTarefa(listaDeTarefa):
    tarefa = input("\nAdicionar Tarefa: ")
    listaDeTarefa.append(tarefa)
    print("Tarefa Adiconada<<<<<<<\n")

def listaTarefas(listaDeTarefas):
    if len(listaDeTarefas) == 0:
        print("\nA lista está vazia<<<<\n")
    else:
        print("\n---Lista de Tarefa---")
        for i in range(len(listaDeTarefas)):
            print(f"{i+1} - {listaDeTarefas[i]}")

def removerTarefa(listaDeTarefas):
    listaTarefas(listaDeTarefas)

    if len(listaDeTarefas) > 0:
        number = int(input("Digite o indice da tarefa que deseja remover: "))
        indice = number - 1
        if indice >= 0 and indice < len(listaDeTarefas):
            remover = listaDeTarefas.pop(indice)
            print(f"\nTarefa {remover} foi romovida<<<\n")
        else:
            print("Número invalido<<<<\n")

tarefa = []
while True:
    print("\n1 - Adicionar Tarefa ")
    print("2 - Lista Tarefa ")
    print("3 - Remover Tarefa ")
    print("4 - Sair ")
    opcao = int(input("Escolha uma opção: "))
    match opcao:
        case 1:
            adicionarTarefa(tarefa)
        case 2:
            listaTarefas(tarefa)
        case 3:
            removerTarefa(tarefa)
        case 4:
            print("Closed program")
            break
        case _:
            print("Número invalido")