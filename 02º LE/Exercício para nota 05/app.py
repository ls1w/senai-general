#***************************************************************************************************************************************
# Objetivo: Determinar se um aluno foi aprovado ou reprovado
# Data: 29/08/2023
# Autor: Lucas
# Versão: 1.0
#***************************************************************************************************************************************
# Título
print('')
print('Situação do aluno')
print('')


# entrada de dados

nome = input('Digite o nome do aluno: ')

while True:
    try:
        nota1 = input('Digite a primeira nota do aluno: ')
        nota1 = float(nota1.replace(',','.'))
    except ValueError:
        print('')
        print('ERRO: DIGITE SOMENTE VALORES VÁLIDOS!')
        print('')
        continue
    else:
        if(nota1 < 0 or nota1 > 10):
            print('')
            print('ERRO: DIGITE SOMENTE VALORES ENTRE 0 E 10!')
            print('')
            continue
        else:
            break

while True:
    try:
        nota2 = input('Digite a segunda nota do aluno: ')
        nota2 = float(nota2.replace(',','.'))
    except ValueError:
        print('')
        print('ERRO: DIGITE SOMENTE VALORES VÁLIDOS!')
        print('')
        continue
    else:
        if(nota2 < 0 or nota2 > 10):
            print('')
            print('ERRO: DIGITE SOMENTE VALORES ENTRE 0 E 10!')
            print('')
            continue
        else:
            break

while True:
    try:
        nota3 = input('Digite a terceira nota do aluno: ')
        nota3 = float(nota3.replace(',','.'))
    except ValueError:
        print('')
        print('ERRO: DIGITE SOMENTE VALORES VÁLIDOS!')
        print('')
        continue
    else:
        if(nota3 < 0 or nota3 > 10):
            print('')
            print('ERRO: DIGITE SOMENTE VALORES ENTRE 0 E 10!')
            print('')
            continue
        else:
            break

while True:
    try:
        nota4 = input('Digite a quarta nota do aluno: ')
        nota4 = float(nota4.replace(',','.'))
    except ValueError:
        print('')
        print('ERRO: DIGITE SOMENTE VALORES VÁLIDOS!')
        print('')
        continue
    else:
        if(nota4 < 0 or nota4 > 10):
            print('')
            print('ERRO: DIGITE SOMENTE VALORES ENTRE 0 E 10!')
            print('')
            continue
        else:
            break

resultado = ''

# processamento

media = (nota1 + nota2 + nota3 + nota4)/4


# saída de dados

if(media >= 7):
    print('')
    print('Aluno',nome,'APROVADO com média de',media)
    print('')
elif(media < 4):
    print('')
    print('Aluno',nome,'REPROVADO NO SEMESTRE com média de',media)
    print('')
else:
    while True:
        try:
            nota_exame = input('Digite a nota do exame do aluno: ')
            nota_exame = float(nota_exame.replace(',','.'))
        except ValueError:
            print('')
            print('ERRO: DIGITE SOMENTE VALORES VÁLIDOS!')
            print('')
            continue
        else:
            if(nota4 < 0 or nota4 > 10):
                print('')
                print('ERRO: DIGITE SOMENTE VALORES ENTRE 0 E 10!')
                print('')
                continue
            else:
                break
    media_final = (media + nota_exame)/2
    
    if(media_final >= 5):
        print('')
        print('Aluno',nome,'APROVADO em exame com média final de',media_final)
        print('')
    else:
        print('')
        print('Aluno',nome,'REPROVAOD em exame com média final de',media_final)