AGENDA = {}
def mostrarContatos():
    if AGENDA:
        for contato in AGENDA:
            buscarContato(contato)
    else:
        print("Agenda vazia")


def buscarContato(contato):
    try:
        print()
        print(f"Nome: {contato}")
        print(f"Telefone: {AGENDA[contato]["telefone"]}")
        print(f"E-mail: {AGENDA[contato]["email"]}")
        print(f"Endereço: {AGENDA[contato]["endereco"]}")
        print()
    except KeyError:
        print("Contato inexistente ")
    except Exception as error:
        print("Um erro inesperado ocorreu")
        print(error)


def lerDetalhesContato():
    email = input("Digite o e-mail: ")
    telefone = input("Digite o telefone: ")
    endereco = input("Digite o endereço: ")
    return (telefone, email, endereco)


def incluirContato(nome, email, telefone, endereco):
    AGENDA[nome] = {
        "telefone": telefone,
        "email": email,
        "endereco": endereco
    }
    salvar()
    print()
    print(f"Contato {nome} adicionado com sucesso")
    print()


def editarContato(nome, email, telefone, endereco):
    AGENDA[nome] = {
        "telefone": telefone,
        "email": email,
        "endereco": endereco
    }
    salvar()
    print()
    print(f"Contato {nome} editado com sucesso")
    print()


def excluirContato(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print()
        print(f"Contato {contato} foi apagado com sucesso")
        print()
    except KeyError:
        print("Contato inexistente ")
    except Exception as error:
        print("Um erro inesperado ocorreu")
        print(error)


def exportarContatos(nomeArquivo):
    try:
        with open(nomeArquivo, "w") as file:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                file.write(f"{contato},{telefone},{email},{endereco}\n")
        print("Agenda exportada com sucesso")
    except:
        print("Algum erro ocorreu ao exportar os contato")


def importarContatos(nomeArquivo):
    try:
        with open(nomeArquivo, 'r') as file:
            linhas = file.readlines()
            for linha in linhas:
                detalhes  = linha.strip().split(",")
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                incluirContato(nome, telefone, email, endereco)

    except FileNotFoundError:
        print("Arquivo não encontrado")
    except Exception as error:
        print("Algum erro inesperado ocorreu")
        print(error)


def salvar():
    exportarContatos('database.csv')


def carregar():
    importarContatos('database.csv')


def imprimir_menu():
    print("------------------------------------")
    print('1 - Mostrar todos os Contatos')
    print('2 - Buscar Contato')
    print('3 - Incluir Contato')
    print('4 - Editar Contato')
    print('5 - Excluir Contato')
    print('6 - Exportar contatos para CSV')
    print('7 - Importar contatos CSV')
    print('0 - Fechar agenda')
    print("------------------------------------")


# Inicio Programa
carregar()
while True:
    imprimir_menu()
    op = input("Escolha uma opção: ")

    if op == "1":
        mostrarContatos()

    elif op == "2":
        nome = input("Digite o nome do contato: \n")
        buscarContato(nome)

    elif op == "3":
        nome = input("Digite o nome: ")
        telefone, email, endereco = lerDetalhesContato()
        incluirContato(nome, email, telefone, endereco)

    elif op == "4":
        nome = input("Digite o nome: ")
        try:
            telefone, email, endereco = lerDetalhesContato()
            editarContato(nome, email, telefone, endereco)
        except:
            print("Um erro ocorreu ao tentar editar o contato")

    elif op == "5":
        nome = input("Digite o nome do contato que deseja excluir: ")
        excluirContato(nome)

    elif op == "6":
        nomeDoArquivo = input("Digite o nome do arquivo a ser importado: ")
        exportarContatos(nomeDoArquivo)

    elif op == "7":
        nomeDoArquivo = input("Digite o nome do arquivo a ser importado: ")
        importarContatos(nomeDoArquivo)

    elif op == "0":
        print("Fechando o programa")
        break

    else:
        print("Opção invalida")