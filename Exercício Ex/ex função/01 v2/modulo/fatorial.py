# ********************************************************************************************************************
# Objetivo: Arquivo responsável por geral o calculo do Fatorial
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