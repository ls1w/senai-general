#***************************************************************************************************************************************
# Objetivo: Fazer uma calculadora
# Data: 23/08/2023
# Autor: Lucas
# Versão: 1.0
#***************************************************************************************************************************************
import math
# Título
print('')
print('Calculadora em python')
print('')


# entrada
entrada_a = input('Digite o primeiro número: ')
operacao = input('Digite em minusculo a primeira letra da operação desejada: a(dição), m(ultiplicação), d(ivisão), s(ubtração): ')
entrada_b = input('Digite o segundo número: ')
resultado = ''



# verificando validade dos valores digitados

if(not(entrada_a.isnumeric()) or not(entrada_b.isnumeric())): # Se a ou b for vazio, siga por aqui
    if(entrada_a == ''):
        print('ERROR: Não foi digitado nenhum valor válido na primeira entrada, por favor digite.')
    else:
        print('ERRO: Não foi digitado nenhum valor válido na segunda entrada, por favor digite.')
else: # Se a ou b não for vazio, siga por aqui
    if(operacao != 'a' and operacao != 'm' and operacao != 'd' and operacao != 's'): 
        print('ERROR: Não foi digitada uma operação válida, por favor digite.')
    else: # Fim da maioria da maioria das validações
        valor_a = float(entrada_a.replace(',','.'))
        valor_b = float(entrada_b.replace(',','.'))
        if(operacao == 'a' or operacao == 's'): # se for adição ou subtração, siga por aqui
            if(operacao == 'a'): 
                resultado = valor_a + valor_b
            else: 
                resultado = valor_a - valor_b
        else: # se não for nem adição, nem subtração então siga por aqui
            if(operacao == 'm'):
                resultado = valor_a * valor_b
            else:
                if(valor_b != 0 and valor_a != 0): # Se nenhum valor digitado for 0, faça isso
                    resultado = valor_a / valor_b
                else: # Se algum valor digitado for 0 numa divisão, faça isso (ultima validação)
                    print('')
                    print('ERRO: Imagine que você tem 0 cookies e você divide eles igualmente entre 0 amigos. Quantos cookies cada pessoa ganha? Viu? Não faz sentido.')
                    print('O Cookie Monster está triste porque não há cookies, e você está triste porque não tem amigos.')
        print(resultado)
