import hashlib  # Para criptografia de senha

# Dicionário para armazenar os usuários e senhas
usuarios = {
    "usuario1": hashlib.sha256("senha1".encode()).hexdigest(),
    # Adicione mais usuários e senhas conforme necessário
}

# Lista para armazenar os alunos
alunos = []

# Função para realizar o login
def fazer_login():
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")

    # Verifique se o usuário existe e a senha está correta
    if usuario in usuarios and hashlib.sha256(senha.encode()).hexdigest() == usuarios[usuario]:
        print("Login bem-sucedido!\n")
        menu_principal()
    else:
        print("Usuário ou senha incorretos. Tente novamente.\n")

# Função para cadastrar um novo aluno
def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = input("Digite a idade do aluno: ")
    nome_pais = input("Digite o nome dos pais do aluno: ")
    endereco = input("Digite o endereço do aluno: ")
    telefone = input("Digite o telefone de contato do aluno: ")

    aluno = {
        "Nome": nome,
        "Idade": idade,
        "Nome dos Pais": nome_pais,
        "Endereço": endereco,
        "Telefone de Contato": telefone,
    }

    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso!\n")

# Função para listar todos os alunos cadastrados
def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado ainda.\n")
    else:
        print("\nLista de Alunos:")
        for index, aluno in enumerate(alunos, start=1):
            print(f"Aluno {index}:")
            for key, value in aluno.items():
                print(f"{key}: {value}")
            print("\n")

# Função para excluir um aluno
def excluir_aluno():
    listar_alunos()
    if alunos:
        try:
            aluno_numero = int(input("Digite o número do aluno que deseja excluir: ")) - 1
            if 0 <= aluno_numero < len(alunos):
                aluno_excluido = alunos.pop(aluno_numero)
                print(f"Aluno {aluno_excluido['Nome']} excluído com sucesso!\n")
            else:
                print("Número de aluno inválido. Tente novamente.\n")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.\n")

# Função para exibir o menu principal
def menu_principal():
    while True:
        print("Menu Principal:")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Excluir Aluno")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            excluir_aluno()
        elif opcao == "4":
            print('Saindo do programa...')
            break
        else:
            print("Opção inválida, tente novamente.\n")

# Função principal
def main():
    print("Bem-vindo ao Automatizando Caminhos: Plataforma de Cadastro Escolar")
    while True:
        fazer_login()

if __name__ == '__main__':
    main()
