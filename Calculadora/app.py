#***************************************************************************************************************************************
# Objetivo: Fazer uma calculadora
# Data: 23/08/2023
# Autor: Lucas
# Versão: 1.0
#***************************************************************************************************************************************
# Título
print('Calculador em python')


# entrada
entrada_a = input('Digite o primeiro número: ')
operacao = input('Digite em minusculo a primeira letra da operação desejada, a(dição), m(ultiplicação), d(ivisão), s(ubtração): ')
entrada_b = input('Digite o segundo número: ')


# verificando validade dos valores digitados

if(entrada_a == '' or entrada_b == ''): # Se a ou b for vazio, siga por aqui
    if(entrada_a == ''):
        print('ERROR: Não foi digitado nenhum valor na primeira entrada, por favor digite.')
    else:
        print('ERRO: Não foi digitado nenhum valor na segunda entrada, por favor digite.')
else: # Se a ou b não for vazio, siga por aqui
    if(operacao != 'a' and operacao != 'm' and operacao != 'd' and operacao != 's'): 
        print('ERROR: Não foi digitada uma operação válida, por favor digite.')
    else: # Fim da maioria da maioria das validações
        valor_a = float(entrada_a.replace(',','.'))
        valor_b = float(entrada_b.replace(',','.'))
        if(operacao == 'a' or operacao == 's'): # se for adição ou subtração, siga por aqui
            if(operacao == 'a'): 
                resultado = valor_a + valor_b
                print(resultado)
            else: 
                resultado = valor_a - valor_b
                print(resultado)
        else: # se não for nem adição, nem subtração então siga por aqui
            if(operacao == 'm'):
                resultado = valor_a * valor_b
                print(resultado)
            else:
                if(valor_b != 0 and valor_a != 0): # Se nenhum valor digitado for 0, faça isso
                    resultado = valor_a / valor_b
                    print(resultado)
                else: # Se algum valor digitado for 0 numa divisão, faça isso (ultima validação)
                    print('ERRO: Imagine que você tem 0 cookies e você divide eles igualmente entre 0 amigos. Quantos cookies cada pessoa ganha? Viu? Não faz sentido.')
                    print('O Cookie Monster está triste porque não há cookies, e você está triste porque não tem amigos.')
