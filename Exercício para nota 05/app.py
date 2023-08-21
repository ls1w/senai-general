#***************************************************************************************************************************************
# Objetivo: Ler quatro valores numéricos inteiros e apresentar o resultado das adições e das multiplicações utilizando a propriedade distributiva para máxima combinação possível entre quatro variáveis
# Data: 15/08/2023
# Autor: Lucas
# Versão: 1.0
#***************************************************************************************************************************************

# Entrada de dados
entradaValorA = int(input('Digite o primeiro valor: '))
entradaValorB = int(input('Digite o segundo valor: '))
entradaValorC = int(input('Digite o terceiro valor: '))
entradaValorD = int(input('Digite o quarto valor: '))

# Processamento

resultado_soma_AB = entradaValorA + entradaValorB
resultado_soma_AC = entradaValorA + entradaValorC
resultado_soma_AD = entradaValorA + entradaValorD
resultado_soma_BC = entradaValorB + entradaValorC
resultado_soma_BD = entradaValorB + entradaValorD
resultado_soma_CD = entradaValorC + entradaValorD

resultado_multiplicação_AB = entradaValorA * entradaValorB
resultado_multiplicação_AC = entradaValorA * entradaValorC
resultado_multiplicação_AD = entradaValorA * entradaValorD
resultado_multiplicação_BC = entradaValorB * entradaValorC
resultado_multiplicação_BD = entradaValorB * entradaValorD
resultado_multiplicação_CD = entradaValorC * entradaValorD

print('Os seis resultados de soma são',resultado_soma_AB,resultado_soma_AC,resultado_soma_AD,resultado_soma_BC,resultado_soma_BD, resultado_soma_CD,'e os seis resultados de multiplicação são',resultado_multiplicação_AB,resultado_multiplicação_AC,resultado_multiplicação_AD,resultado_multiplicação_BC,resultado_multiplicação_BD,resultado_multiplicação_CD)