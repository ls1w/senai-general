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

fatorial = 1
try:
    contador = int(input('Digite o número fatorial a ser calculado: '))
except ValueError:
    print('Digite somente números inteiros')
else:
    if(contador <= 0):
        print('Digite somente valores positívos')
    else:
        while(contador > 0):
            fatorial = contador * fatorial
            print(contador,'X')
            contador = contador - 1

print('=',fatorial)