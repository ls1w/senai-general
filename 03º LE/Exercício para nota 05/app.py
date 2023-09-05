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
        tabuada_inicial = int(input('Digite o valor inicial da tabuada (entre 2 e 99): '))
    except ValueError:
        print('ERRO: Dgite somente valores numéricos inteiros')
        continue
    else:
        if(tabuada_inicial < 2 or tabuada_inicial >= 100):
            print('Os valores tem que ser entre 2 e 99')
            continue
        else:
            break

while True:
    try:
        tabuada_final = int(input('Digite o valor inicial da tabuada (entre 3 e 100): '))
    except ValueError:
        print('ERRO: Dgite somente valores numéricos inteiros')
        continue
    else:
        if(tabuada_final <= 2 or tabuada_final > 100):
            print('Os valores tem que ser entre 3 e 100')
            continue
        elif(tabuada_final <= tabuada_inicial):
            print('O valor final da tabuada tem que ser maior que o valor inicial')
            continue
        else:
            break

while True:
    try:
        numero_inicial = int(input('Digite o valor inicial da tabuada (entre 1 e 49): '))
    except ValueError:
        print('ERRO: Dgite somente valores numéricos inteiros')
        continue
    else:
        if(numero_inicial < 1 or numero_inicial >= 50):
            print('Os valores tem que ser entre 1 e 49')
            continue
        else:
            break

while True:
    try:
        numero_final = int(input('Digite o valor inicial da tabuada (entre 2 e 50): '))
    except ValueError:
        print('ERRO: Dgite somente valores numéricos inteiros')
        continue
    else:
        if(numero_final <= 1 or numero_final > 50):
            print('Os valores tem que ser entre 2 e 50')
            continue
        elif(numero_final <= numero_inicial):
            print('O valor final tem que ser maior que o valor inicial')
            continue
        else:
            break

contador_while = tabuada_inicial
contador_if = numero_inicial
while(contador_while <= tabuada_final):
    if(contador_if <= numero_final):
        print('conta da mesma tabuada')
        resultado = contador_if * contador_while
        print(contador_while,'X',contador_if,'=',resultado)
        contador_if = contador_if + 1
    else:
        print('')
        print('próxima tabuada')
        contador_while = contador_while + 1
        contador_if = numero_inicial

print('Fim, nenhuma tabuada a mais')