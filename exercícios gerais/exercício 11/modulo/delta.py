import sys

def calcDelta(valorDeA,valorDeB,valorDeC):
    valorA = valorDeA
    valorB = valorDeB
    valorC = valorDeC
    if(valorA == 0):
        valorA = 1
    valorDelta = (valorB ** 2) - (4*valorA*valorC)

    print('')
    print('Delta =',valorDelta)
    if(valorDelta < 0):
        print('Não há raízes reais para delta negatívo.')
        sys.exit()
    print(valorDelta)
    return valorDelta

if __name__ == "__main__":
    a = 2
    b = 3
    c = 5
    print(calcDelta(a,b,c))