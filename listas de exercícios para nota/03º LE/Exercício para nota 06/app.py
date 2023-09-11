#***************************************************************************************************************************************
# Objetivo: Criar um sistema que gerencie números pares e impares conforme os requisitos abaixo: O sistema deverá solicitar as seguintes entradas:  •Número Inicial;  •Número Final;  Requisitos do Sistema  •O número inicial deverá ser limitado a entrada de valores entre 0 até 500;  •O número final deverá ser limitado a entrada de valores entre 100 até 1000;  •O usuário deve obrigatoriamente digitar números nas duas entradas, assim não podem ficar vazias;  •Se o usuário digitar um número inicial MAIOR do que o final o sistema deve impedir o cálculo e apresentar uma mensagem de erro para o usuário;  •O sistema também deve impedir que o usuário digite dois números iguais em ambas as entradas;  •Ao final de cada lista a quantidade de números pares e impares calculados deverá ser exibida;  •O sistema deverá apresentar uma sequência de números pares e outra sequência de números ímpares;
# Data: 05/09/2023
# Autor: Lucas
# Versão: 1.5
#***************************************************************************************************************************************
# Título
print('')
print('Calculando os impares e pares')
print('')

status = True
while(status):
    try:
        numero_inicial = int(input('Digite o número inicial (entre 0 e 500): '))
        if(numero_inicial < 0 or numero_inicial > 500):
            print('')
            print('ERRO: O número tem que estar entre 0 e 500')
        else:
            status = False
    except ValueError:
        print('')
        print('ERRO: Digite somente valores numéricos inteiros')
        continue

status = True
while(status):
    try:
        numero_final = int(input('Digite o número final (entre 100 e 1000): '))
        print('')
        if(numero_final < 100 or numero_final > 1000 or numero_final <= numero_inicial):
            print('')
            print('ERRO: O valor tem que estar entre 100 e 1000, e ser maior que',numero_inicial)
        else:
            status = False
    except ValueError:
        print('')
        print('ERRO: Dgite somente valores numéricos inteiros')
        continue

contador_pares = numero_inicial
qtde_de_pares = 0
print('Lista de números pares')
while(contador_pares <= numero_final):
    if(contador_pares % 2 == 0):
        print(contador_pares)
        print('')
        contador_pares = contador_pares + 1
        qtde_de_pares = qtde_de_pares + 1
    else:
        contador_pares = contador_pares + 1
print('Quantidade de números pares encontrados:',qtde_de_pares)
print('')



contador_impares = numero_inicial
qtde_de_impares = 0
print('Lista de números impares')
while(contador_impares <= numero_final):
    if(contador_impares % 2 == 0):
        contador_impares = contador_impares + 1
    else:
        print(contador_impares)
        print('')
        contador_impares = contador_impares + 1
        qtde_de_impares = qtde_de_impares + 1
print('Quantidade de números impares encontrados:',qtde_de_impares)
print('')