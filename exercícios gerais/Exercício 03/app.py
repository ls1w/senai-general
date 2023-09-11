#*************************************************************************************************************************************************************************************
# Objetivo: Realizar calculo da média de um aluno e status de aprovação de um aluno
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

# processamento
nota1 = float(entrada_nota1.replace(',','.'))
nota2 = float(entrada_nota2.replace(',','.'))
nota3 = float(entrada_nota3.replace(',','.'))
nota4 = float(entrada_nota4.replace(',','.'))

media = (nota1 + nota2 + nota3 + nota4)/4

if(media >= 7):
    print('A média do aluno',nome,'foi:',media)
    print('O aluno está APROVADO.')
else:
    print('A média do aluno',nome,'foi:',media)
    print('O aluno está REPROVADO.')