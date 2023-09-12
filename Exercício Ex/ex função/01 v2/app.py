# ********************************************************************************************************************
# Objetivo: Realizar um calculo de um fatorial conforme um número informado pelo usuário
# Data: 11/09/2023
# Autor: Lucas
# Versão: 1.0
# *********************************************************************************************************************

import sys
# sys.path.insert() permite acrescentar na memória do projeto um diretório a ser utilizado
# Obs: O ./ significa o diretório atual do projeto
sys.path.insert(1,'./modulo')

import fatorial

# ENTRADA DE DADOS
numero = int(input('Digite um número para calcular fatorial: '))

# PROCESSAMENTO
resultado = fatorial.calcular_fatorial(numero)

# SAÍDA DO RESULTADO
print(numero,'! =',resultado)