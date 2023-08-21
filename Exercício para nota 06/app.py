#***************************************************************************************************************************************
# Objetivo: Converter os valores em dolar para real
# Data: 17/08/2023
# Autor: Lucas
# Versão: 1.0
#***************************************************************************************************************************************

# entrada de dados

entrada_cotação_dolar = input('Digite a cotação atual de dolares em real: ')
entrada_de_dolares = input('Digite a quantidade de dolares a converter: ')

# processamento

cotação_dolar = float(entrada_cotação_dolar.replace(',','.'))
dolares = float(entrada_de_dolares.replace(',','.'))

reais = cotação_dolar * dolares

# saída de dados

print("US$",entrada_de_dolares,"em R$ é cerca de R$",f'{reais:.2f}',"na cotação de US$ 1,00 para R$",entrada_cotação_dolar)