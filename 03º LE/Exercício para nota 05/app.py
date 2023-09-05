#***************************************************************************************************************************************
# Objetivo: Criar um sistema para gerenciar o cálculo de uma tabuada, conforme requisitos abaixo:  O sistema deverá solicitar as seguintes entradas:  •A tabuada inicial e tabuada final a ser calculada; •O número inicial e final do contador da tabuada;  Requisitos do Sistema  •A entrada da tabuada deverá ser entre 2 e 100, não sendo permitido outros valores;  •Nenhuma entrada de dados deverá ficar sem preenchimento;  •O valor até onde será calculada a tabuada deverá ser entre 1 e 50
# Data: 04/09/2023
# Autor: Lucas
# Versão: 1.0
#***************************************************************************************************************************************
# Título
print('')
print('Calculando uma tabuada')
print('')

while True:
    try:
        tabuada_inicial = int(input('Digite a tabuada inicial (entre 2 e 100): '))
        print('')
    except ValueError:
        print('ERRO: Dgite somente valores numéricos inteiros')
        continue
    else:
        if(tabuada_inicial < 2 or tabuada_inicial > 100):
            print('ERRO: Os valores tem que ser entre 2 e 100')
            continue
        else:
            break

while True:
    try:
        tabuada_final = int(input('Digite a tabuada final (entre 2 e 100): '))
        print('')
    except ValueError:
        print('ERRO: Dgite somente valores numéricos inteiros')
        continue
    else:
        if(tabuada_final < 2 or tabuada_final > 100):
            print('ERRO: Os valores tem que ser entre 2 e 100')
            continue
        elif(tabuada_final < tabuada_inicial):
            print('ERRO: O valor final da tabuada tem que ser maior ou igual ao valor inicial')
            continue
        else:
            break

while True:
    try:
        numero_inicial = int(input('Digite o valor inicial na tabuada (entre 1 e 50): '))
        print('')
    except ValueError:
        print('ERRO: Dgite somente valores numéricos inteiros')
        continue
    else:
        if(numero_inicial < 1 or numero_inicial > 50):
            print('ERRO: Os valores tem que ser entre 1 e 50')
            continue
        else:
            break

while True:
    try:
        numero_final = int(input('Digite o valor final na tabuada (entre 1 e 50): '))
        print('')
    except ValueError:
        print('ERRO: Dgite somente valores numéricos inteiros')
        continue
    else:
        if(numero_final < 1 or numero_final > 50):
            print('ERRO: Os valores tem que ser entre 1 e 50')
            continue
        elif(numero_final < numero_inicial):
            print('ERRO: O valor final tem que ser maior ou igual ao valor inicial')
            continue
        else:
            break



contador_while = tabuada_inicial
contador_if = numero_inicial

print('Primeira tabuada')
while(contador_while <= tabuada_final):
    if(contador_if <= numero_final):
        resultado = contador_if * contador_while
        print(contador_while,'X',contador_if,'=',resultado)
        contador_if = contador_if + 1
    else:
        print('')
        print('Procurando próxima tabuada')
        contador_while = contador_while + 1
        contador_if = numero_inicial

print('Fim, nenhuma tabuada a mais')