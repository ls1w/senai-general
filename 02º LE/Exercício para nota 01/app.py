#***************************************************************************************************************************************
# Objetivo: Receber dois valores inteiros e apresenta a diferença dos valores
# Data: 28/08/2023
# Autor: Lucas
# Versão: 1.0
#***************************************************************************************************************************************
# Título
print('')
print('Calculando a diferença entre os valores')
print('')

# entrada de dados
while True:
    try:
        nota1 = int(input('Digite o primeiro número inteiro: '))
    except ValueError:
        print('')
        print('ERRO: DIGITE SOMENTE VALORES VÁLIDOS!')
        print('')
        continue
    else:
        break

while True:
    try:
        nota2 = int(input('Digite o segundo número inteiro: '))
    except ValueError:
        print('')
        print('ERRO: DIGITE SOMENTE VALORES VÁLIDOS!')
        print('')
        continue
    else:
        break
resultado = ''

# processamento

if(nota1 > nota2):
    resultado = nota1 - nota2
else:
    resultado = nota2 - nota1

# saída de dados
print('')
print('A diferença entre os valores', nota1,'e', nota2,' é de: ',resultado)
print('')