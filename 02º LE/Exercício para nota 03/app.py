#***************************************************************************************************************************************
# Objetivo: Ler  um  valor  numérico  inteiro  que  esteja  na  faixa  de  valores  de  1  até  9
# Data: 23/08/2023
# Autor: Lucas
# Versão: 1.0
#***************************************************************************************************************************************
# Título
print('')
print('Número dentro dos permitidos')
print('')

# entrada de dados
while True:
    try:
        numero = int(input('Digite o primeiro número inteiro: '))
    except ValueError:
        print('')
        print('ERRO: DIGITE SOMENTE VALORES VÁLIDOS!')
        print('')
        continue
    else:
        break

if(numero >= 0 or numero <= 9):
    print('O valor está na faixa permitida')
else:
    print('O valor está fora da faixa permitida')