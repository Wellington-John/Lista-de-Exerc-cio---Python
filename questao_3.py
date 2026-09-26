def contarPalavras(frase):
    fraseMinuscula = frase.lower()
    listaPalavras = fraseMinuscula.split()
    dicionario = {}
    for palavra in listaPalavras:
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1
    return dicionario

fraseDigitada = (input("Digite uma frase: "))

resultado = contarPalavras(fraseDigitada)

print("\n{")
for palavra, quantidade in resultado.items():
    print(f" {palavra}: {quantidade}")
print("}")