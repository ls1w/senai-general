#***************************************************************************************************************************************
# Objetivo: Fazer uma calculadora revisão
# Data: 24/08/2023
# Autor: Lucas
# Versão: 1.0
#***************************************************************************************************************************************
# Entrada de dados
valor1 = input('Digite o primeiro valor: ')
valor2 = input('Digite o segundo valor: ')
operacao = input('Escolha a operação a ser realizada [SOMAR | SUBTRAIR | MULTIPLICAR | DIVIDIR]')
resultado = ''

# upper() - converte o conteúdo de uma string para MAIUSCULO
# lower() - converte o conteúdo de uma string para minusculo


# Validação dos dados colocados
if(not(valor1.isnumeric()) or not(valor2.isnumeric())):
    print('ERRO: Não é possível calcular se não digitar valores válidos')
else:
    # Tratamento da virgula
    valor1 = float(valor1.replace(',','.'))
    valor2 = float(valor2.replace(',','.'))

    if(operacao.upper() == 'SOMAR'):
        resultado = valor1 + valor2
    elif(operacao.upper() == 'SUBTRAIR'):
        resultado = valor1 - valor2
    elif(operacao.upper() == 'MULTIPLICAR'):
        resultado = valor1 * valor2
    elif(operacao.upper() == 'DIVIDIR'):
        if(valor2 == 0):
            print('ERRO: Não existe divisão por 0')
        else:
            resultado = valor1 / valor2
    else:
        print('ERRO: Operação escolhida inválida')

    print(resultado)