#***************************************************************************************************************************************
# Objetivo: Ler dois valores numéricos inteiros e apresentar o resultado das quatro operações aritméticas básicas
# Data: 15/08/2023
# Autor: Lucas
# Versão: 1.0
#***************************************************************************************************************************************

# entrada de dados

valorA = int(input('Digite o primeiro valor: '))
valorB = int(input('Digite o segundo valor: '))


# processamento

resultado_soma = valorA + valorB
resultado_subtracao = valorA - valorB
resultado_multiplicao = valorA * valorB
resultado_divisao = valorA / valorB


# saída de dados

print('Os resultado são para soma',resultado_soma,'para subtração',resultado_subtracao,'para multiplicação',resultado_multiplicao,'e para divisão',f'{resultado_divisao:.2f}')