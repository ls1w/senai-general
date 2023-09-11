#***************************************************************************************************************************************
# Objetivo: Determinar se um número é impar ou par
# Data: 28/08/2023
# Autor: Lucas
# Versão: 1.0
#***************************************************************************************************************************************
# Título
print('')
print('Determinando se um número é impar ou par')
print('')

# entrada de dados
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

# processamento e saída

if(numero % 2 == 0):
    print('')
    print('O número digitado foi par.')
    print('')
else:
    print('')
    print('O número digitado foi impar.')
    print('')