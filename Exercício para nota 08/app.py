#***************************************************************************************************************************************
# Objetivo: Fazer um programa que calcula o reajuste de salário  de um funcionário
# Data: 15/08/2023
# Autor: Lucas
# Versão: 1.0
#***************************************************************************************************************************************

# entrada de dados

entrada_percentual_de_reajuste = input('Digite a taxa de reajuste: ')
entrada_do_salario_mensal_antigo = input('Digite o valor do salário mensal que irá sofrer reajuste: ')

# processamento

percentual_de_reajuste = float(entrada_percentual_de_reajuste.replace(',','.'))
salario_mensal_antigo = float(entrada_do_salario_mensal_antigo.replace(',','.'))

salario_mensal_novo = salario_mensal_antigo * ((percentual_de_reajuste/100)+1)

# saída de dados
print(salario_mensal_novo)
print('O valor de reajuste de um salário de R$',f'{salario_mensal_antigo:.2f}','em uma taxa de',entrada_percentual_de_reajuste,'%, será de R$',f'{salario_mensal_novo:.2f}')