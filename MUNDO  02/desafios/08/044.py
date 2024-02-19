""" Exercício Python 044: 
    Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
    - à vista dinheiro/cheque: 10% de desconto
    - à vista no cartão: 5% de desconto
    - em até 2x no cartão: preço formal
    - 3x ou mais no cartão: 20% de juros """
import locale

    # Configura o locale para o Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def avista(preco):
    desconto = preco * (10/100)
    preco_final = preco - desconto
    print(f'O preço do produto original {locale.currency(preco, grouping=True)}, desconto aplicado de {locale.currency(desconto,grouping=True)}, valor total a ser pago sera: {locale.currency(preco_final,grouping=True)} ')

def avista_cartao(preco):
    desconto = preco * (5/100)
    preco_final = preco - desconto
    print(f'O preço do produto original {locale.currency(preco, grouping=True)}, desconto aplicado de {locale.currency(desconto,grouping=True)}, valor total a ser pago sera: {locale.currency(preco_final,grouping=True)} ')

def parcelado_cartao(preco):
    parcela = preco / 2
    print(f'O preço do produto original {locale.currency(preco, grouping=True)}, o produto parcelado em 2x saira com parcelas de {parcela}')

def cartao(preco):
    parcelado = int(input('Quantas vezes o cliente deseja parcelar : '))
    parcela = preco / parcelado
    juros = parcela * (20/100)
    preco_final = parcela + juros
    print(f'O preço do produto original {locale.currency(preco, grouping=True)},o produto sera parcelado em {parcelado}X , as parcelas sera de {locale.currency(preco_final, grouping=True)}, com acrecimos de 20%') 

def menu():
    while True:
        print('-'*20)
        print('BEM VINDO AO NOSSO SISTEMA DE PAGAMENTOS')
        print('-'*20)
        print()
        preco = float(input('Iforme o valor do produto a ser comprado : '))
        print('[1] - À vista dinheiro/cheque: 10% de desconto')
        print('[2] - À vista no cartão: 5% de desconto')
        print('[3] - Em até 2x no cartão: preço formal')
        print('[4] - 3x ou mais no cartão: 20% de juros ')
        print()
        opcao = int(input('Digite a opção desejada : '))

        if opcao == 1 :
            avista(preco)
            
            print('DESEJA REALIZAR OUTRA SIMULAÇÃO ? : ')
            print()
            print('[1] - SIM ')
            print('[2] - NÃO')
            resposta = int(input('DIGITE A OPÇÃO DESEJADA : '))
            
            if resposta == 1 :
                menu()

            elif resposta == 2 :
                break
        
        elif opcao == 2 :
            avista_cartao(preco)

            print('DESEJA REALIZAR OUTRA SIMULAÇÃO ? : ')
            print()
            print('[1] - SIM ')
            print('[2] - NÃO')
            resposta = int(input('DIGITE A OPÇÃO DESEJADA : '))
            
            if resposta == 1 :
                menu()

            elif resposta == 2 :
                break
        
        elif opcao == 3 :
            parcelado_cartao(preco)

            print('DESEJA REALIZAR OUTRA SIMULAÇÃO ? : ')
            print()
            print('[1] - SIM ')
            print('[2] - NÃO')
            resposta = int(input('DIGITE A OPÇÃO DESEJADA : '))
            
            if resposta == 1 :
                menu()

            elif resposta == 2 :
                break
        
        elif opcao == 4 :
            cartao(preco)

            print('DESEJA REALIZAR OUTRA SIMULAÇÃO ? : ')
            print()
            print('[1] - SIM ')
            print('[2] - NÃO')
            resposta = int(input('DIGITE A OPÇÃO DESEJADA : '))
            
            if resposta == 1 :
                menu()

            elif resposta == 2 :
                break
        
        else:
            break

menu()