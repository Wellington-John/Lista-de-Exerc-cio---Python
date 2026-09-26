
def cadastrar_estudante(lista_turma):
    print("\n--- Novo Cadastro ---")
    nome = input("Digite o nome do estudante: ")
    nota = float(input(f"Digite sua nota: "))

    estudante = {"nome": nome, "nota": nota}
    lista_turma.append(estudante)
    print("Estudante cadastrado !")


def calcular_media(lista_turma):
    if len(lista_turma) == 0:
        print("\n Nenhum estudante cadastrado")
        return

    soma_notas = 0
    for estudante in lista_turma:
        soma_notas += estudante["nota"]

    media_geral = soma_notas / len(lista_turma)
    print(f"\nA média da turma: {media_geral:.1f}")

def maior_nota(lista_turma):
    if len(lista_turma) == 0:
        print("\nNenhum estudante cadastrado.")
        return

    nota_maxima = -1
    aluno_destaque = ""

    for estudante in lista_turma:
        if estudante["nota"] > nota_maxima:
            nota_maxima = estudante["nota"]
            aluno_destaque = estudante["nome"]

    print(f"\nA maior nota é de {aluno_destaque} | {nota_maxima:.1f}!")

def listar_aprovados(lista_turma):
    if len(lista_turma) == 0:
        print("\nNenhum estudante cadastrado.")
        return

    print("\n--- Estudantes Aprovados ---")
    encontrou_alguem = False

    for estudante in lista_turma:
        if estudante["nota"] >= 7.0:
            print(f" {estudante['nome']} | Nota: {estudante['nota']:.1f}")
            encontrou_alguem = True

    if encontrou_alguem == False:
        print("Nenhum estudante foi aprovado.")

turma = []
while True:
    print("\n1 - Cadastrar estudante")
    print("2 - Exibir média da turma")
    print("3 - Exibir estudante com maior nota")
    print("4 - Listar aprovados")
    print("5 - Sair")

    opcao = int(input("\nEscolha uma opção: "))
    match opcao:
        case 1:
            cadastrar_estudante(turma)
        case 2:
            calcular_media(turma)
        case 3:
            maior_nota(turma)
        case 4:
            listar_aprovados(turma)
        case 5:
            print("\nEncerrando o sistema de análise... Até logo!")
            break
        case _:
            print("\nOpção inválida!")