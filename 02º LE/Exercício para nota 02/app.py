#***************************************************************************************************************************************
# Objetivo: Requisitar nome e sexo da pessoa e responder com base nisso
# Data: 23/08/2023
# Autor: Lucas
# Versão: 1.0
#***************************************************************************************************************************************
# Título
print('')
print('Mensagem feliz')
print('')

nome = input('Digite o seu nome: ')
sexo = input('Digite o seu sexo, f(feminino) ou m(masculino): ')

if(sexo.lower() == 'f'):
    print('')
    print('Bem-vinda Ilma. Sra.',nome)
    print('')
elif(sexo.lower() == 'm'):
    print('')
    print('Bem-vindo Ilmo. Sr.',nome)
    print('')
else:
    print('')
    print('ERRO: Digite somente F para feminino ou M para masculino')
    print('')