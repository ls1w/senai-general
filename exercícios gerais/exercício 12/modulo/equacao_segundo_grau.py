'''
Auto: Tux
Objetivo: Calcular as duas raízes da eq. do 2º grau
Data: 14/09/2023 
Versão: 1.0
'''

'''
ax² + bx + c = 0

1. Calcular o delta
delta = b² - 4ac

2. Calcular x1 e x2
x = (-b + ou - raiz(delta)) / (2a)

3. Considerações
- 'a' não pode ser zero. Caso o 'a' seja zero, irá ser o um

- Caso o delta seja negativo, exiba mensagem 
"Não há raizes reais", e o programa termina.
'''

import sys
from math import sqrt

def calcular_delta(a, b, c):    
    delta = b ** 2 - 4 * a * c
    if ( delta < 0):
        print("Não pode delta negativo")
        sys.exit()
    return delta


def calcular_raizes(a, b, c): 
    if (a == 0):
        a = 1   
    x1 = (-b + sqrt(calcular_delta(a, b, c))) / (2*a)
    x2 = (-b - sqrt(calcular_delta(a, b, c))) / (2*a)

    return x1, x2


if __name__ == "__main__":
    a = 2
    b = 3
    c = 5

    print(calcular_raizes(a,b,c))
    