import sys

def calcDelta(valorDeA,valorDeB,valorDeC):
    valorA = valorDeA
    valorB = valorDeB
    valorC = valorDeC
    if(valorA == 0):
        valorA = 1
    valorDelta = (valorB ** 2) - (4*valorA*valorC)

    if(valorDelta < 0):
        print('')
        print('Não há raízes reais para delta negatívo.')
        sys.exit()
    print(valorDelta)
    return valorDelta