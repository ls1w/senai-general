#***************************************************************************************************************************************
# Objetivo: Realizar calculo da distância e da quantidade de litros usados
# Data: 15/08/2023
# Autor: Lucas
# Versão: 1.0
#***************************************************************************************************************************************

# entrada de dados
entrada_da_velocidade_media = int(input('Digite em km/h a velocidade média: '))
entrada_do_tempo = int(input('Digite o tempo de viagem em minutos: '))
entrada_do_consumo = input('Digite o consumo de combustível de seu carro: ')

# processamento
consumo = float(entrada_do_consumo.replace(',','.'))

tempo_em_horas = float(entrada_do_tempo)/60

distancia = tempo_em_horas*entrada_da_velocidade_media
litros_usados = distancia/consumo

# saída de dados
print('Um carro com velocidade média de',entrada_da_velocidade_media,'km/h, por',entrada_do_tempo,'minutos, em uma distância de',distancia,'km, consumiria',litros_usados,'L')