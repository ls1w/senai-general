#*************************************************************************************************************************************************************************************
# Objetivo: Realizar calculo da média de um aluno e status de aprovação por nota ou frequência de um aluno
# Data: 14/08/2023
# Autor: Lucas
# Versão: 1.3
#*************************************************************************************************************************************************************************************
# Título
print('Realizando calculo da média de um aluno e status de aprovação')


# entrada de dados
nome = input('Digite o nome do aluno: ')
entrada_nota1 = input('Digite a primeira nota: ')
entrada_nota2 = input('Digite a segunda nota: ')
entrada_nota3 = input('Digite a terceira nota: ')
entrada_nota4 = input('Digite a quarta nota: ')
frequencia = int(input('Digite a frequência do aluno: '))

# processamento
nota1 = float(entrada_nota1.replace(',','.'))
nota2 = float(entrada_nota2.replace(',','.'))
nota3 = float(entrada_nota3.replace(',','.'))
nota4 = float(entrada_nota4.replace(',','.'))

media = (nota1 + nota2 + nota3 + nota4)/4

if(nota1 >=0 and nota1 <= 10 and nota2 >= 0 and nota2 <= 10 and nota3 >= 0 and nota3 <= 10 and nota4 >= 0 and nota4 <= 10 and frequencia >= 0 and frequencia <= 100):
    if(media >= 7 and media <= 10 and frequencia >=75 and frequencia <=100):
        print('A média do aluno',nome,'foi:',media)
        print('Sua frequência foi:',frequencia,'%')
        print('O aluno está APROVADO.')
    else:
        print('A média do aluno',nome,'foi:',media)
        print('Sua frequência foi:',frequencia,'%')
        print('O aluno está REPROVADO.')
else:
    print('ERROR, dados inválidos colocados, notas tem que ser entre 0 e 10, a frequência entre 0% e 100%')