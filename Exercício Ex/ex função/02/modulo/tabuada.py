# *********************************************************************************************************************************
# Objetivo: Criar uma função que realiza uma função da tabuada inicial até a final
# Autor: Lucas
# Data: 12/09/2023
# Versão 1.0
# *********************************************************************************************************************************


def calcularTabuada(tabuadaInicial, tabuadaFinal, contadorInicial, contadorFinal):
    tabInicial  = tabuadaInicial
    tabFinal    = tabuadaFinal
    contInicial = contadorInicial
    contFinal   = contadorFinal

    resultado   = ''
    status = False

    if(tabInicial == '' or tabFinal == '' or contInicial == '' or contFinal == ''):
        print('ERRO: Não é possível calcular sem preenchimento de todas as entradas.')
    elif(int(tabInicial) < 2 or int(tabInicial) > 100 or int(tabFinal) < 2 or int(tabFinal) > 100):
        print('ERRO: Atabuada a ser calculada deve estar entre 2 e 100.')
    elif(int(contInicial) < 1 or int(contInicial) > 50 or int(contFinal) < 1 or int(contFinal) > 50):
        print('ERRO: O valor do contador da tabuada deve estar entre 1 e 50.')
    else:
        # Conversão para int
        contInicial = int(contInicial)
        contFinal   = int(contFinal)
        tabInicial  = int(tabInicial)
        tabFinal    = int(tabFinal)
        
        # Processamento para gerar o calculo de várias tabuadas
        while(tabInicial <= tabFinal):
            print('')
            print('Tabuada [', tabInicial,']')
            
            #Processamento para gerar o calculo de uma tabuada
            while(contInicial <= contFinal):
                resultado = tabInicial * contInicial
                print(tabInicial, 'X', contInicial, '=', resultado)
                status = True
                contInicial += 1
            
            contInicial = int(contadorInicial)
            tabInicial += 1
    return status