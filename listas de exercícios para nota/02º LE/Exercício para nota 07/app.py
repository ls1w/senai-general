#***************************************************************************************************************************************
# Objetivo: Determinar entre 5 números o maior e o menor
# Data: 29/08/2023
# Autor: Lucas
# Versão: 1.0
#***************************************************************************************************************************************
# Título
print('')
print('Qual a ordem dos valores')
print('')

while True:
    try:
        valor1 = input('Digite o primeiro valor: ')
        valor1 = float(valor1.replace(',','.'))
    except ValueError:
        print('')
        print('ERRO: DIGITE SOMENTE VALORES VÁLIDOS!')
        print('')
        continue
    else:
        break

while True:
    try:
        print('')
        valor2 = input('Digite o segundo valor: ')
        valor2 = float(valor2.replace(',','.'))
    except ValueError:
        print('')
        print('ERRO: DIGITE SOMENTE VALORES VÁLIDOS!')
        print('')
        continue
    else:
        break

while True:
    try:
        print('')
        valor3 = input('Digite o terceiro valor: ')
        valor3 = float(valor3.replace(',','.'))
    except ValueError:
        print('')
        print('ERRO: DIGITE SOMENTE VALORES VÁLIDOS!')
        print('')
        continue
    else:
        break


print('')

if(valor1 < valor2 and valor2 < valor3):
    print('A ordem crescente dos valores é',valor1,',',valor2,'e',valor3)
elif(valor2 < valor1 and valor1 < valor3):
    print('A ordem crescente dos valores é',valor2,',',valor1,'e',valor3)
elif(valor3 < valor2 and valor2 < valor1):
    print('A ordem crescente dos valores é',valor3,',',valor2,'e',valor1)
elif(valor1 < valor3 and valor3 < valor2):
    print('A ordem crescente dos valores é',valor1,',',valor3,'e',valor2)
elif(valor2 < valor3 and valor3 < valor1):
    print('A ordem crescente dos valores é',valor2,',',valor3,'e',valor1)
elif(valor3 < valor1 and valor1 < valor2):
    print('A ordem crescente dos valores é',valor3,',',valor1,'e',valor2)
else:
    print('Por favor, não coloque valores iguais')

print('')