#***************************************************************************************************************************************
# Objetivo: Realizar conversão de graus celsius para Fahrenheit
# Data: 14/08/2023
# Autor: Lucas
# Versão: 1.0
#***************************************************************************************************************************************

# ENTRADA DE DADOS

entrada_em_celsius = input('Digite o valor em graus Celsius a ser convertido: ')



# PROCESSAMENTO
celsius = entrada_em_celsius.replace(',','.')
fahrenheit = (9*float(celsius)+160)/5

# SAÍDA DE DADOS

print('O valor convertido é:',f'{fahrenheit:.1f}','ºF')