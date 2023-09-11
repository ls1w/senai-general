#***************************************************************************************************************************************
# Objetivo: Apresentar os quadrados dos números de 15 a 200
# Data: 04/09/2023
# Autor: Lucas
# Versão: 1.0
#***************************************************************************************************************************************
# Título
print('')
print('Apresentando os quadrados')
print('')

contador = 15

while(contador <= 200):
    quadrado = contador ** 2
    print(str(contador)+'² =',quadrado)
    contador = contador + 1