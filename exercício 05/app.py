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

# PROCESSAMENTO
contador = 0
while(contador <= 10):
    resultado = tabuada * contador
    print(tabuada, 'X', contador, '=', resultado)
    contador = contador + 1
