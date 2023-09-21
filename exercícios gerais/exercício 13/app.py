# *****************************************************************************************
# Objetivo: Criar uma agenda
# Data: 20/09/2023
# Autor: ls1w
# Versão: 2.1
# *****************************************************************************************
import modulo.agenda as agenda

agenda.menu()

# while(status):
#     system('clear')
#     print('Agenda')

#     print('')
#     print('1 Cadastrar usuário.')
#     print('2 Buscar Usuário.')
#     print('3 Listar todos os usuários.')
#     print('4 Excluir um usuário.')
#     print('5 Sair.')
#     print('')

#     opcao = input('Escolha uma opção a cima(1/2/3/4): ')
#     if opcao == '5':
#         system('clear')
#         print('Saindo da agenta')
#         print('')
#         status = False
#         sys.exit()

#     elif opcao == '4':
#         dAgendas = agenda.excluirUsuario(dAgendas)

#     elif opcao == '3':
#         lastActionWork = agenda.listarTodosOsUsuarios(dAgendas)
#     elif opcao == '2':
#         lastActionWork = agenda.buscarUsuario(dAgendas)
#     elif opcao == '1':
#         dAgendas = agenda.cadastrarUsuario(dAgendas)

#     else:
#         system('clear')
#         print('ERRO: Reposta inválida, por favor, digite somente o número desejado da operação.')
#         print('')
#         input('Digite qualquer coisa para voltar ao menu.')