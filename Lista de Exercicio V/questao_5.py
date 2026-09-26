def validarSenha(senhaP):
    if len(senhaP) < 8:
        return False

    temMaiuscula = False
    temMinuscula = False
    temNumero = False

    for caracter in senhaP:
        if caracter.isupper():
            temMaiuscula = True
        elif caracter.islower():
             temMinuscula = True
        elif caracter.isdigit():
            temNumero = True

    if temMaiuscula == True and temMinuscula == True and temNumero == True:
        return True
    else:
        return False

while True:
    senha = input("Crie uma senha: ")

    if validarSenha(senha):
        print(f"Senha criada com sucesso: {senha}")
        break
    else:
        print("\nPrecisa ter uma letra maiúscula")
        print("Precisa ter uma letra minúscula")
        print("Precisa ter um número")
        print("Precisa ter no minimo 8 caracteres\n")