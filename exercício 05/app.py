# **********************************************************************************************************************************************
# Objetivo: Calcular uma tabuada
# Data: 31/08/2023
# Autor: Lucas
# Versão: 1.0
# **********************************************************************************************************************************************
# Título
print('')
print('Fazendo uma tabuada')

# ENTRADA DE DADOS
tabuada = int(input('Escolha a tabuada desejada: '))
limiteMaximo = int(input('Escolha o limite máximo da tabuada: '))

# PROCESSAMENTO
contador = 0
while(contador <= limiteMaximo):
    resultado = tabuada * contador
    print(tabuada, 'X', contador, '=', resultado)
    contador = contador + 1
