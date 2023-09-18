'''
Auto: Tux
Objetivo: Calcular as duas raízes da eq. do 2º grau
        chamando o arquivo equação_segundo_grau.py
Data: 14/09/2023 
Versão: 1.0
'''
from os import system
from modulo.equacao_segundo_grau import calcular_raizes

system('clear')
numeros = [float(var) for var in input("Digite 'a', 'b' e 'c' separados por vírgula sem espaço('a,b,c'): ").split(',')]

x1, x2 = calcular_raizes(numeros[0], numeros[1], numeros[2])
print("O valor de x1 = ", x1)
print("O valor de x2 = ", x2)