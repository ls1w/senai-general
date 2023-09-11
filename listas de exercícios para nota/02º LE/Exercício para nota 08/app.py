#***************************************************************************************************************************************
# Objetivo: Programa para calcular o IMC
# Data: 30/08/2023
# Autor: Lucas
# Versão: 1.0
#***************************************************************************************************************************************
# Título
print('')
print('Calculando IMC')
print('')


# Entrada de dados
nome = input('Digite o nome da pessoa: ')

while True:
    try:
        print('')
        peso = int(input('Digite o peso da pessoa: '))
    except ValueError:
        print('')
        print('ERRO: DIGITE SOMENTE NÚMEROS INTEIROS!')
        continue
    else:
        if(peso <= 0):
            print('')
            print('ERRO: Digite somente valores positivos')
        else:
            break

while True:
    try:
        print('')
        altura = input('Digite a altura da pessoa: ')
        altura = float(altura.replace(',','.'))
    except ValueError:
        print('')
        print('ERRO: DIGITE SOMENTE NÚMEROS INTEIROS!')
        continue
    else:
        if(altura <= 0):
            print('')
            print('ERRO: Digite somente valores positivos')
        else:
            break



# processamento
imc = peso / (altura*altura)


# Saída de dados

print('')
print('O IMC foi de',f'{imc:.2f}','kg/m²')


if(imc < 17):
    print('A pessoa de nome',nome,'está muito abaixo do peso')
elif(imc >= 17 and imc < 18.5):
    print('A pessoa de nome',nome,'está abaixo do peso')
elif(imc >= 18.5 and imc < 25):
    print('A pessoa de nome',nome,'está com o peso normal')
elif(imc >= 25 and imc < 30):
    print('A pessoa de nome',nome,'está acima do peso')
elif(imc >= 30 and imc < 35):
    print('A pessoa de nome',nome,'tem obesidade grau I')
elif(imc >= 35 and imc < 40):
    print('A pessoa de nome',nome,'tem obesidade grau II')
elif(imc >= 40):
    print('A pessoa de nome',nome,'tem obesidade grau III')
else:
    print('ERRO')


print('')