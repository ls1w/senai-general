#***************************************************************************************************************************************
# Objetivo: Realizar calculo do volume de uma lata de óleo
# Data: 15/08/2023
# Autor: Lucas
# Versão: 1.0
#***************************************************************************************************************************************

# entrada de dados

entrada_do_raio = input('digite o raio da lata: ')
entrada_da_altura = input('digite a altura da lata em cm: ')


# processamento

raio = float(entrada_do_raio.replace(',','.'))
altura = float(entrada_da_altura.replace(',','.'))

volume = 3.14159*(raio**2)*altura

# saída de dados

print('O volume da lata de óleo foi',f'{volume:.4f}','cm³')