# ********************************************************************************************************************
# Objetivo: Realizar um calculo de um fatorial conforme um número informado pelo usuário
# Data: 11/09/2023
# Autor: Lucas
# Versão: 1.0
# *********************************************************************************************************************


# FUNÇÃO PARA CALCULAR O FÁTORIAL DE UM NÚMERO 
def calcular_fatorial(numero_do_fatorial):
    
    # Recebe o argumento encaminhado da função
    # variável locar =  argumento
    numero_fatorial  =  numero_do_fatorial
    
    # Variáveis locais para o processamento
    contador = 1
    fatorial = 1
    while(contador <= numero_fatorial):
        fatorial = fatorial * contador
        contador += 1
    
    return fatorial # Retorna o valor calculado do fatorial

# ENTRADA DE DADOS
numero = int(input('Digite um número para calcular fatorial: '))

# PROCESSAMENTO
resultado = calcular_fatorial(numero)

# SAÍDA DO RESULTADO
print(numero,'! =',resultado)
