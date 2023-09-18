import sys

import modulo.tabuada as tabuada

status = False
while(not(status)):
    numeroTabuadaInicial    = input('Digite o valor da tabuada inicial: ')
    numeroTabuadaFinal      = input('Digite o valor da tabuada final: ')

    numeroContadorInicial   = input ('Digite o valor inicial do contador da tabuada: ')
    numeroContadorFinal     = input('Digite o valor final do contador da tabuada: ')


    status = tabuada.calcularTabuada(numeroTabuadaInicial, numeroTabuadaFinal, numeroContadorInicial, numeroContadorFinal)