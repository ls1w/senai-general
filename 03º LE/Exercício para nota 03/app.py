#***************************************************************************************************************************************
# Objetivo: Calcular o Fatorial de um número fornecido pelo usuário
# Data: 04/09/2023
# Autor: Lucas
# Versão: 1.0
#***************************************************************************************************************************************
# Título
print('')
print('Calculando fatoriais')
print('')

resultado_fatorial = 1
status = True
while(status):
    try:
        contador = int(input('Digite o número fatorial a ser calculado: '))
        if(contador <= 0):
            print('')
            print('ERRO: Digite somente valores positívos')
        else:
            status = False
    except ValueError:
        print('')
        print('ERRO: Digite somente números inteiros')

while(contador > 1):
    resultado_fatorial = contador * resultado_fatorial
    print(contador,'X')
    contador = contador - 1
print(1)
print('=',resultado_fatorial)