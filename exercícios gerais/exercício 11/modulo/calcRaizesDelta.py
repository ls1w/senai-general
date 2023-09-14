import sys
from math import sqrt
import delta

def calc_raizes(valorDeA,valorDeB,valorDeC):
    valorA = valorDeA
    valorB = valorDeB
    valorC = valorDeC
    valorDelta = delta.calcDelta(valorA,valorB,valorC)

    if(valorDelta < 0):
        print('')
        sys.exit
        
    x1 = (-valorB + sqrt(valorDelta))/(2*valorA)

    x2 = (-valorB - sqrt(valorDelta))/(2*valorA)

    return x1,x2