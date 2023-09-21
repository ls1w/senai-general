# *****************************************************************************************
# Objetivo: Criar as funções necessárias para uma agenda
# Data: 19/09/2023
# Autor: ls1w
# Versão: 2.3
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
            status = True

    return contato

def listarTodosOsUsuarios(contatos):
    finished_ok = False
    system('clear')
    contato = contatos

    print('Listando todos os usuários')
    print('')
    if contato != {}:
        for i in contato:
            print(i)
            print('|  Telefone:',contato[i]['telefone'],'- Email:',contato[i]['email'])
        finished_ok = True
    else:
        print('Lista vazia')
        finished_ok = True

    print('')
    input('Digite qualquer tecla para voltar ao menu')
    return finished_ok

def buscarUsuario(contatos):
    finished_ok = False
    system('clear')
    contato = contatos

    print('Buscando Contato')
    print('')

    if contato == {}:
        print('')
        print('Nenhum usuário na agenda.')
        finished_ok = False
    else:
        procurar = input('Digite o nome do contato que deseja buscar: ').lower()

        for i in contato:
            if procurar == i:
                print('')
                print(procurar)
                print('| Telefone: ',contato[procurar]['telefone'],' - E-mail: ',contato[procurar]['email'])
                finished_ok = True

        if not(finished_ok):
            print('')
            print('Nenhum usuário encontrado com o nome',procurar,'encontrado.')
            finished_ok = True
        
    print('')
    input('Digite qualquer tecla para voltar ao menu')
    return finished_ok

def excluirUsuario(contatos):
    system('clear')
    contato = contatos
    finished_ok = False

    print('Excluindo contatos')
    print('')
    if contato == {}:
        print('Lista vazia')
    else:
        procurar = input('Digite o nome do contato que deseja excluir: ')

        for nomeContato in contato:
            if procurar == nomeContato:
                finished_ok = True
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

        if not(finished_ok):
            print('')
            print('Nenhum usuário encontrado com o nome',procurar,'encontrado.')
            finished_ok = True

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
    return not(status)

if __name__ == "__main__":
    menu()