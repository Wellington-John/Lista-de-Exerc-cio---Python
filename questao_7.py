def analisarTexto(frase):
    totalCaracter = len(frase)
    totalPalavras = len(frase.split())

    totalNumeros = 0
    totalEspacos = 0
    totalLetra = 0

    indice = 0
    while indice < len(frase):
        caracter = frase[indice]
        if caracter.isalpha():
            totalLetra += 1
        elif caracter.isdigit():
            totalNumeros += 1
        elif caracter.isspace():
            totalEspacos += 1
        indice += 1

    print(f"\nTotal de Caracter: {totalCaracter}")
    print(f"Total de Letras: {totalLetra}")
    print(f"Total de Numero: {totalNumeros}")
    print(f"Total de Espaço: {totalEspacos}")
    print(f"Total de Palavra: {totalPalavras}")

frase = input("Digite uma frase: ")
analisarTexto(frase)