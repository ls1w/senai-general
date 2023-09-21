# *****************************************************************************************
# Objetivo: Criar as funções necessárias para uma agenda
# Data: 19/09/2023
# Autor: ls1w
# Versão: 2.1
# *****************************************************************************************

from os import system
import sys

def cadastrarUsuario(contatos):
    status = True

    while status:
        system('clear')

        contato = contatos

        print('Cadastrar usuário')
        print('')

        nome = input('Digite o nome do novo contato: ').lower()
        telefone = input('Digite o telefone do novo contato: ')
        email = input('Digite o email do novo contato: ')

        contato[nome] = {'telefone':telefone,'email':email}

        system('clear')
        print('Usuário cadastrado com sucesso')
        print('')

        print('Deseja adicionar mais um usuário?')
        next = input('Digite[y/N]: ').lower()

        if( next != 'y'):
            status = False

    return contato




def listarTodosOsUsuarios(contatos):
    status = False
    system('clear')
    contato = contatos

    print('Listando todos os usuários')
    print('')
    for i in contato:
        print(i)
        print('|  Telefone:',contato[i]['telefone'],'- Email:',contato[i]['email'])

    print('')
    input('Digite qualquer tecla para voltar ao menu')

    status = True
    return status




def buscarUsuario(contatos):
    status = False
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

    status = True
    return status




def excluirUsuario(contatos):
    system('clear')
    contato = contatos

    print('Excluindo contatos')
    print('')
    procurar = input('Digite o nome do contato que deseja excluir: ')

    print('')
    print(procurar)
    print('')
    next = input('Tem certeza que deseja EXCLUIR o contato a cima?[y/N]')
    if next == 'y':
        next = input('Tem certeza mesmo que deseja EXCLUIR?[y/N]').lower()
        if next == 'y':
            contato.pop(procurar)
            print('Usuário',procurar,'excluido com sucesso.')
        else:
            print('Operação de exclusão cancelada.')
    else:
        print('Operação de exclusão cancelada.')
    print('')
    input('Digite qualquer tecla para voltar ao menu')
    
    return contato




def menu():
    status = True
    agenda = {}
    while(status):
        system('clear')
        print('Agenda')

        print('')
        print('1 Cadastrar usuário.')
        print('2 Buscar Usuário.')
        print('3 Listar todos os usuários.')
        print('4 Excluir um usuário.')
        print('5 Sair.')
        print('')

        opcao = input('Escolha uma opção a cima [1/2/3/4/5]: ')
        if opcao == '5':
            system('clear')
            print('Saindo da agenta')
            print('')
            status = False
            sys.exit()

        elif opcao == '4':
            agenda = excluirUsuario(agenda)

        elif opcao == '3':
            lastActionWork = listarTodosOsUsuarios(agenda)
        elif opcao == '2':
            lastActionWork = buscarUsuario(agenda)
        elif opcao == '1':
            agenda = cadastrarUsuario(agenda)

        else:
            system('clear')
            print('ERRO: Reposta inválida, por favor, digite somente o número desejado da operação.')
            print('')
            input('Digite qualquer coisa para voltar ao menu.')





if __name__ == "__main__":
    menu()

