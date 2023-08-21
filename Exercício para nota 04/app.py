#***************************************************************************************************************************************
# Objetivo: Realizar cálculo e a apresentação do valor de uma prestação em atraso
# Data: 15/08/2023
# Autor: Lucas
# Versão: 1.0
#***************************************************************************************************************************************

# entrada de dados

entrada_do_valor = input('Digite o valor inicial: ')
entrada_da_taxa = input('Digite a taxa ao mês: ')
entrada_do_tempo = int(input('Digite a quantidade de meses: '))

# processamento

valor = float(entrada_do_valor.replace(',','.'))
taxa = float(entrada_da_taxa.replace(',','.'))

prestação = valor+(valor*(taxa/100)*entrada_do_tempo)

print(prestação)