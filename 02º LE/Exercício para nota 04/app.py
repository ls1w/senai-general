#***************************************************************************************************************************************
# Objetivo: Determinar se um número é impar ou par
# Data: 23/08/2023
# Autor: Lucas
# Versão: 1.0
#***************************************************************************************************************************************
# Título
print('')
print('Determinando se um número é impar ou par')
print('')

while True:
    try:
        numero = int(input('Digite o número inteiro: '))
    except ValueError:
        print('')
        print('ERRO: DIGITE SOMENTE VALORES VÁLIDOS!')
        print('')
        continue
    else:
        break

if(numero % 2 == 0):
    print('')
    print('O número digitado foi par.')
else:
    print('')
    print('O número digitado foi impar.')