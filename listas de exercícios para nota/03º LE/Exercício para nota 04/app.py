#***************************************************************************************************************************************
# Objetivo: Elaborar um programa que efetue a leitura de valores positivos inteiros até que um valor negativo seja informado. Ao final deverão ser apresentados o maior e o menor valores informados pelo usuário
# Data: 04/09/2023
# Autor: Lucas
# Versão: 1.5
#***************************************************************************************************************************************
# Título
print('')
print('Calculando os maiores valores até ser digitado um negativo')
print('')

status = True
while (status):
    try:
        contador = int(input('Digite um valor inteiro positivo: '))
        if(contador < 0):
            print('')
            print('ERRO: Valor inválido, digite somente valores positivos')
        else:
            status = False
    except ValueError:
        print('')
        print('ERRO: Valor inválido, digite somente valores numéricos inteiros')
        continue

menor = contador
maior = contador



while(contador >= 0):
    if(contador >= maior):
        maior = contador
        print('O último valor numérico inteiro digitado foi o MAIOR valor até então')
    elif(contador <= menor):
        menor = contador
        print('O ultimo valor numérico inteiro digitado foi o MENOR valor até então')
    try:
        print('')
        print('Nota: Numeros negativos param o programa')
        contador = int(input('Digite um valor inteiro: '))
    except ValueError:
        print('')
        print('ERRO: Só digite valores numéricos inteiros')
        continue

print('O maior foi',maior,'e o menor foi', menor)