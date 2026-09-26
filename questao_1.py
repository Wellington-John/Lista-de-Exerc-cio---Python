
def autenticar(usuarioP, senhaP):
    usuarioCorreto= "JohnSoares"
    senhaCorreta = "John@0123"

    if usuarioP == usuarioCorreto and senhaP == senhaCorreta:
        return True
    else:
        return False

cont = 0
while cont < 3:
    usuario = str(input("\nDigite o nome do usuario: "))
    senha = str(input("Digite sua senha: "))

    if autenticar(usuario, senha):
        print("\n>>>>Acesso Autorizado<<<<")
        break
    else:
        cont += 1
        print("\nAcesso negado")
        if cont < 3:
            print(f"Tentativas restantes: {3-cont}!<<<<<")
if cont == 3:
    print("Acesso Bloqueado<<<<<")



