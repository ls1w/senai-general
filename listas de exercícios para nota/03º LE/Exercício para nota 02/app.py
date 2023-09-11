#***************************************************************************************************************************************
# Objetivo: Apresentar o total da soma obtida dos cem primeiros números inteiros (1+2+3+5+...+99+100).
# Data: 04/09/2023
# Autor: Lucas
# Versão: 1.0
#***************************************************************************************************************************************
# Título
print('')
print('Apresentando o total da soma')
print('')

contador = 1
soma = 0

while(contador <= 100):
    soma = contador + soma
    print('+',contador,' = ',soma)
    contador = contador + 1
