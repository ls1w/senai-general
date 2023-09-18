'''
Auto: Tux
Objetivo: Calcular as duas raízes da eq. do 2º grau
          chamando o arquivo equação_segundo_grau.py
Data: 14/09/2023 
Versão: 1.0
'''

import modulo.equacao_segundo_grau as r2

a = float(input("Informe o valor de 'a': "))
b = float(input("Informe o valor de 'b': "))
c = float(input("Informe o valor de 'c': "))

x1, x2 = r2.calcular_raizes(a, b, c)
print("O valor de x1 = ", x1)
print("O valor de x2 = ", x2)











