notas = [7.5, 8.0, 6.5, 9.0, 5.5, 8.5]
media = 0
soma = 0
cont = 0

for nota in notas:
    soma += nota
    print(f"Notas: {nota}")
    media = soma / len(notas)
    if nota >= 7:
        cont += 1

print(f"\nQuantidade de alunos que conseguiram media maior ou igual a 7: {cont}")