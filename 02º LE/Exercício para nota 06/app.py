#***************************************************************************************************************************************
# Objetivo: Determinar entre 5 números o maior e o menor
# Data: 29/08/2023
# Autor: Lucas
# Versão: 1.0
#***************************************************************************************************************************************
# Título
print('')
print('Descobrindo o maior número')
print('')

# entrada de dados

while True:
    try:
        valor1 = int(input('Digite o primeiro valor: '))
    except ValueError:
        print('')
        print('ERRO: DIGITE SOMENTE VALORES VÁLIDOS!')
        print('')
        continue
    else:
        break

while True:
    try:
        valor2 = int(input('Digite o segundo valor: '))
    except ValueError:
        print('')
        print('ERRO: DIGITE SOMENTE VALORES VÁLIDOS!')
        print('')
        continue
    else:
        break

while True:
    try:
        valor3 = int(input('Digite o terceiro valor: '))
    except ValueError:
        print('')
        print('ERRO: DIGITE SOMENTE VALORES VÁLIDOS!')
        print('')
        continue
    else:
        break

while True:
    try:
        valor4 = int(input('Digite o quarto valor: '))
    except ValueError:
        print('')
        print('ERRO: DIGITE SOMENTE VALORES VÁLIDOS!')
        print('')
        continue
    else:
        break

while True:
    try:
        valor5 = int(input('Digite o quinto valor: '))
    except ValueError:
        print('')
        print('ERRO: DIGITE SOMENTE VALORES VÁLIDOS!')
        print('')
        continue
    else:
        break



# teste maior

if(valor1 >= valor2 and valor1 >= valor3 and valor1 >= valor4 and valor1 >= valor5):
    maior = valor1
elif(valor2 >= valor1 and valor2 >= valor3 and valor2 >= valor4 and valor2 >= valor5):
    maior = valor2
elif(valor3 >= valor1 and valor3 >= valor2 and valor3 >= valor4 and valor3 >= valor5):
    maior = valor3
elif(valor4 >= valor1 and valor4 >= valor2 and valor4 >= valor3 and valor4 >= valor5):
    maior = valor4
else:
    maior = valor5



# teste menor

if(valor1 <= valor2 and valor1 <= valor3 and valor1 <= valor4 and valor1 <= valor5):
    menor = valor1
elif(valor2 <= valor1 and valor2 <= valor3 and valor2 <= valor4 and valor2 <= valor5):
    menor = valor2
elif(valor3 <= valor1 and valor3 <= valor2 and valor3 <= valor4 and valor3 <= valor5):
    menor = valor3
elif(valor4 <= valor1 and valor4 <= valor2 and valor4 <= valor3 and valor4 <= valor5):
    menor = valor4
else:
    menor = valor5


print('')
print('O maior valor digitado foi de',maior)
print('E o menor valor digitado foi de', menor)
print('')