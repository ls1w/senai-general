'''
Objetivo: Calcular as duas raízes da eq do 2º gráu
Data: 14/09/2023
Autor: Lucas
Versão: 1.0
'''

'''
ax² + bx + c = 0

1. Calcular o delta
delta = b² - 4ac

2. Calcular as raízes (x1 e x2)
x = (-b +- raiz(delta)) / (2a)

3. Considerações

* O 'a' não pode ser zero. Caso o 'a' seja zero 

* Caso o delta seja negativa, exiba a mensagem: 'Não há raizes reais', e o programa encerra.
'''
from math import sqrt
import sys

def calcDelta(valorDeA,valorDeB,valorDeC):
    valorA = valorDeA
    valorB = valorDeB
    valorC = valorDeC

    valorDelta = (valorB ** 2) - (4*valorA*valorC)
    return valorDelta


def calcX1EX2(valorDeA,valorDeB,valorDeDelta):
    valorA = valorDeA
    valorB = valorDeB
    valorDelta= valorDeDelta

    x1 = (-valorB + sqrt(valorDelta))/(2*valorA)

    x2 = (-valorB - sqrt(valorDelta))/(2*valorA)

    return x1,x2

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

if(a == 0):
    a = 1

delta = calcDelta(a,b,c)

print('')
print('O valor de delta foi',delta)

if(delta < 0 ):
    print('Não há raízes reais para delta negatívo.')
    sys.exit
else:
    work = calcX1EX2(a,b,delta)
    print('Os valores de x1 e x2 são respectivamente:')
    print(work)
