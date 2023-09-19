from os import system
import sys

def cadastrarUsuario(contatos):
    system('clear')

    contato = contatos

    print('Cadastrar usuário')
    print('')

    nome = input('Digite o nome do novo contato: ').lower()
    telefone = input('Digite o telefone do novo contato: ')
    email = input('Digite o email do novo contato: ')

    contato[nome] = {'telefone':telefone,'email':email}

    print('')
    print('Usuário cadastrado com sucesso')
    input('pressione qualquer tecla para voltar ao menu.')

    return contato


def listarTodosOsUsuarios(contatos):
    work = False
    system('clear')
    contato = contatos

    print('Listando todos os usuários')
    print('')
    for i in contato:
        print(i)
        print('|  Telefone:',contato[i]['telefone'],', Email:',contato[i]['email'])

    print('')
    input('Digite qualquer tecla para voltar ao menu')
    work = True
    return work

def buscarUsuario(contatos):
    work = False
    system('clear')
    contato = contatos
    print('Buscando Contato')
    print('')
    procurar = input('Digite o nome do contato que deseja buscar: ').lower()

    print('')
    print(procurar)
    print('| Telefone: ',contato[procurar]['telefone'],' - E-mail: ',contato[procurar]['email'])
    print('')
    input('Digite qualquer tecla para voltar ao menu')
    work = True
    return work




if __name__ == "__main__":
    contato = {}

    status = True
    while(status):
        system('clear')
        print('Agenda')

        print('')
        print('1 Cadastrar usuário')
        print('2 Buscar Usuário')
        print('3 Listar todos os usuários')
        print('4 Sair')
        print('')

        opcao = input('Escolha uma opção a cima(1/2/3/4): ')
        if opcao == '4':
            system('clear')
            print('Saindo da agenta')
            print('')
            status = False
            sys.exit()

        elif opcao == '3':
            lastActionWork = listarTodosOsUsuarios(contato)
        elif opcao == '2':
            buscarUsuario(contato)
        elif opcao == '1':
            contato = cadastrarUsuario(contato)
        else:
            print('ERRO: Reposta inválida, por favor, digite somente o número desejado da operação.')

