# *****************************************************************************************
# Objetivo: Criar as funções necessárias para uma agenda
# Data: 19/09/2023
# Autor: ls1w
# Versão: 2.0
# *****************************************************************************************

from os import system
from sys import exit as sysex

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
        print('|  Telefone:',contato[i]['telefone'],', Email:',contato[i]['email'])

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
    print('')
    input('Digite qualquer tecla para voltar ao menu')
    
    return contato







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
            sysex()

        elif opcao == '3':
            lastActionWork = listarTodosOsUsuarios(contato)
        elif opcao == '2':
            buscarUsuario(contato)
        elif opcao == '1':
            contato = cadastrarUsuario(contato)
        else:
            print('ERRO: Reposta inválida, por favor, digite somente o número desejado da operação.')

