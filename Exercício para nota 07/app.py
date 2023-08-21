#***************************************************************************************************************************************
# Objetivo: Converter os valores em real para dolar
# Data: 17/08/2023
# Autor: Lucas
# Versão: 1.0
#***************************************************************************************************************************************

# entrada de dados

entrada_cotação_real = input('Digite a cotação atual de reais em dolar: ')
entrada_de_reais = input('Digite a quantidade de reais a converter: ')

# processamento

cotação_real = float(entrada_cotação_real.replace(',','.'))
reais = float(entrada_de_reais.replace(',','.'))

dolares = cotação_real * reais

# saída de dados

print("R$",entrada_de_reais,"em US$ é cerca de US$",f'{dolares:.2f}',"na cotação de R$ 1,00 para US$",entrada_cotação_real)