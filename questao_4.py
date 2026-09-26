def calcularMedia(dicionario, nomeP, nota1, nota2, nota3):
     media = (nota1 + nota2 + nota3) / 3

     dicionario[nomeP] = {
         "Nota 1: ": nota1,
         "Nota 2: ": nota2,
         "Nota 3: ": nota3,
         "Media: ": media}
     return media

dicionarioCadastros = {}

while True:
    nome = input("Digite seu nome ou (sair para fechar): ")
    if nome == "sair":
        break
    nota1 = float(input("Digite sua nota: "))
    nota2 = float(input("Digite sua nota: "))
    nota3 = float(input("Digite sua nota: "))

    calcularMedia(dicionarioCadastros, nome, nota1, nota2, nota3)

print("\n----Cadastros----")
print("{")
for nome, notas, in dicionarioCadastros.items():
    media = notas["Media: "]
    if media >= 7:
        print(f"{nome} {notas} | Aluno Aprovado<<<<")
    elif media >= 5 and media < 7:
        print(f"{nome} {notas}  | Aluno de Recuperação<<<<")
    else:
        print(f"{nome} {notas}  | Aluno Reprovado<<<<")
print("}")