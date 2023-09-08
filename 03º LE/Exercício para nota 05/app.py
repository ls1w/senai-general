#***************************************************************************************************************************************
# Objetivo: Criar um sistema para gerenciar o cálculo de uma tabuada, conforme requisitos abaixo:  O sistema deverá solicitar as seguintes entradas:  •A tabuada inicial e tabuada final a ser calculada; •O número inicial e final do contador da tabuada;  Requisitos do Sistema  •A entrada da tabuada deverá ser entre 2 e 100, não sendo permitido outros valores;  •Nenhuma entrada de dados deverá ficar sem preenchimento;  •O valor até onde será calculada a tabuada deverá ser entre 1 e 50
# Data: 04/09/2023
# Autor: Lucas
# Versão: 2.1
#***************************************************************************************************************************************
# Título
print('')
print('Calculando uma tabuada')
print('')

status = True
while(status):
    try:
        tabuada_inicial = int(input('Digite a tabuada inicial (entre 2 e 100): '))
        if(tabuada_inicial < 2 or tabuada_inicial > 100):
            print('')
            print('ERRO: Os valores tem que estar entre 2 e 100')
        else:
            status = False
    except ValueError:
        print('')
        print('ERRO: Digite somente valores numéricos inteiros')
        continue

status = True
while(status):
    try:
        tabuada_final = int(input('Digite a tabuada final (entre 2 e 100): '))
        if(tabuada_final < 2 or tabuada_final > 100 or tabuada_final < tabuada_inicial):
            print('')
            print('ERRO: Os valores tem que estar entre 2 e 100 e ser maior que',tabuada_inicial)
        else:
            status = False
    except ValueError:
        print('')
        print('ERRO: Digite somente valores numéricos inteiros')
        continue

status = True
while(status):
    try:
        numero_inicial = int(input('Digite o valor inicial na tabuada (entre 1 e 50): '))
        if(numero_inicial < 1 or numero_inicial > 50):
            print('')
            print('ERRO: Os valores tem que estar entre 1 e 50')
        else:
            status = False
    except ValueError:
        print('')
        print('ERRO: Digite somente valores numéricos inteiros')
        continue

status = True
while(status):
    try:
        numero_final = int(input('Digite o valor final na tabuada (entre 1 e 50): '))
        if(numero_final < 1 or numero_final > 50 or numero_final < numero_inicial):
            print('')
            print('ERRO: Os valores tem que estar entre 1 e 50 e ser maior que',numero_inicial)
        else:
            status = False
    except ValueError:
        print('')
        print('ERRO: Digite somente valores numéricos inteiros')
        continue



contador_tabuada = tabuada_inicial
while(contador_tabuada <= tabuada_final):
    contador_numero = numero_inicial
    print('')
    print('Tabuada do',contador_tabuada)
    while(contador_numero <= numero_final):
        resultado = contador_numero * contador_tabuada
        print(contador_tabuada,'X',contador_numero,'=',resultado)
        contador_numero += 1
    contador_tabuada += 1

print('')
print('Fim, nenhuma tabuada a mais.')