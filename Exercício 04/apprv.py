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

# upper() - converte o conteúdo de uma string para MAIUSCULO
# lower() - converte o conteúdo de uma string para minusculo

if(operacao.upper() == 'SOMAR'):
    resultado = valor1 + valor2
else:
    if(operacao.upper() == 'SUBTRAIR'):
        resultado = valor1 - valor2
    else:
        if(operacao.upper() == 'MULTIPLICAR'):
            resultado = valor1 * valor2
        else:
            if(operacao.upper() == 'DIVIDIR'):
                resultado = valor1 / valor2
                