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
import modulo.calcRaizesDelta as r2



a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

if(a == 0):
    a = 1

x1, x2 = r2.calc_raizes(a,b,c)
print('Os valores de x1 e x2 são respectivamente:')
print('O valor de x1 é:',x1)
print('O valor de x2 é:',x2)