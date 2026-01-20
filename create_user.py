from database import carregar_dados, salvar_dados

def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")

    usuarios = carregar_dados()

    novo_usuario = {
        "nome": nome,
        "email": email
    }

    usuarios.append(novo_usuario)
    salvar_dados(usuarios)

    print("Usuário cadastrado com sucesso!")

if __name__ == "__main__":
    criar_usuario()


