# **************************************************************************************************************************************************************************************
# Objetivo: Realizar calculo da médoa de um aluno
# Data: 14/08/2023
# Autor: Lucas
# Versão: 1.1
# **************************************************************************************************************************************************************************************

# TÍTULO
print('Exercício 02 - Calculando média do aluno')




# ENTRADA DE DADOS

nome_do_aluno = input('Digite o nome do aluno: ')

entrada_nota_1 = input('Digite a primeira nota: ')

entrada_nota_2 = input('Digite a segunda nota: ')

entrada_nota_3 = input('Digite a terceira nota: ')

entrada_nota_4 = input('Digite a quarta nota: ')




# PROCESSAMENTO

# replace - permite localizar um caracter(só a string tem caracterers) e substituir por outro
nota1 = entrada_nota_1.replace(',','.')
nota2 = entrada_nota_2.replace(',','.')
nota3 = entrada_nota_3.replace(',','.')
nota4 = entrada_nota_4.replace(',','.')

media = (float(nota1)+float(nota2)+float(nota3)+float(nota4))/4


# SAÍDA DE DADOS
print('A média do aluno',nome_do_aluno,'é',media)