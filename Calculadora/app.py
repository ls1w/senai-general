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

if(entrada_a == '' or entrada_b == ''):
    print('ERROR: Não foi digitado nenhum valor em algum dos números, por favor digite.')
    erro = 1
else:
    if(operacao != 'a' and operacao != 'm' and operacao != 'd' and operacao != 's'):
        print('ERROR: Não foi digitada uma operação válida, por favor digite.')
        erro = 1
    else:
        va = float(entrada_a.replace(',','.'))
        vb = float(entrada_b.replace(',','.'))
        erro = 0


if(erro == 1): # se ocorreu um erro na verificação, faça isso
    print('ERRO: Impossível de terminar o calculo por causa do erro.')
else: # Se não ocorreu nenhum erro até aqui, siga por aqui
    if(operacao == 'a' or operacao == 's'): # se for adição ou subtração, siga por aqui
        if(operacao == 'a'): # se for adição, faça isso
            resultado = va + vb
            print(resultado)
        else: # se for subtração, faça isso
            resultado = va - vb
            print(resultado)
    else: # se não for nem adição, nem subtração então siga por aqui
        if(operacao == 'm'): # se for multiplicação, faça iso
            resultado = va * vb
            print(resultado)
        else: # se for divisão, siga por aqui
            if(vb != 0 and va != 0): # se nenhum valor digitado for 0, faça isso
                resultado = va / vb
                print(resultado)
            else: # se algum valor digitado for 0 numa divisão, faça isso
                print('ERRO: Imagine que você tem 0 cookies e você divide eles igualmente entre 0 amigos. Quantos cookies cada pessoa ganha? Viu? Não faz sentido.')
                print('O Cookie Monster está triste porque nao há cookies, e você está triste porque não tem amigos.')
