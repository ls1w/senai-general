from math import sqrt
import modulo.delta as delta

def calc_raizes(valorDeA,valorDeB,valorDeC):
    valorA = valorDeA
    valorB = valorDeB
    valorC = valorDeC
    valorDelta = delta.calcDelta(valorA,valorB,valorC)

    x1 = (-valorB + sqrt(valorDelta))/(2*valorA)

    x2 = (-valorB - sqrt(valorDelta))/(2*valorA)

    return x1,x2

if __name__ == "__main__":
    a = 2
    b = 3
    c = 5

    print(calc_raizes)