#***************************************************************************************************************************************
# Objetivo: Programa para auxiliar na venda
# Data: 29/08/2023
# Autor: Lucas
# Versão: 1.0
#***************************************************************************************************************************************
# Título
print('')
print('Maquininha de pagamentos')
print('')

# entrada de dados


while True:
    try:
        valor_da_compra = input('Digite o primeiro valor: ')
        valor_da_compra = float(valor_da_compra.replace(',','.'))
    except ValueError:
        print('')
        print('ERRO: DIGITE SOMENTE VALORES NUMÉRICOS!')
        print('')
        continue
    else:
        if(valor_da_compra <= 0):
            print('ERRO: DIGITE SOMENTE VALORES POSITIVOS')
        else:
            break

while True:
    try:
        print('')
        print('Codigo 1 = À vista, desconto de 8%')
        print('Codigo 2 = À vista no cartão, desconto de 4%')
        print('Codigo 3 = Em 2x sem juros')
        print('Codigo 4 = Em 4x com juros de 8%')
        print('')
        codigo = int(input('Digite o codigo: '))
    except ValueError:
        print('')
        print('ERRO: DIGITE SOMENTE VALORES VÁLIDOS!')
        continue
    else:
        if(codigo < 1 or codigo > 4):
            print('')
            print('Opção inválida, escolha os codigos somente entre 1 e 4')
        else:
            break


#processamento
if(codigo == 1):
    total_a_pagar = valor_da_compra - (valor_da_compra/12.5)
elif(codigo == 2):
    total_a_pagar = valor_da_compra - (valor_da_compra/25)
else:
    if(codigo == 3):
        total_a_pagar = valor_da_compra

        valor_das_parcelas = total_a_pagar/2

    elif(codigo == 4):
        total_a_pagar = valor_da_compra + (valor_da_compra/12.5)

        valor_das_parcelas = total_a_pagar/4
    
    # Saída de dados
    print('O valor das parcelas será R$',valor_das_parcelas)


print('O total a pagar será R$',total_a_pagar)