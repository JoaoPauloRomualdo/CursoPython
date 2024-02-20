""" Desafios 036
Exercício Python 036: 
    Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
    A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado. """
import locale

    # Configura o locale para o Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def cinco_anos(salario,valor_casa):
        #Calcula o valor das parcelas por mes
    parcela_mes = valor_casa / (5*12)
        #Calcula a porcentagem da parcela se excede 30%
    quantidade_financiamento = salario * (30/100)
        #Verifica se a parcela não esta maior do que 30% ao mes
    if parcela_mes <= quantidade_financiamento :
        print(f'SALARIO INFORMADO FOI {locale.currency(salario, grouping=True)}')
        print(f'\033[1;30;43mPARABÉNS !!! SEU FINANCIAMENTO FOI APROVADO COM PARCELAS DE {locale.currency(parcela_mes, grouping=True)} AO MES POR 5 ANOS\033[m')
    else :
        print(f'SALARIO INFORMADO FOI {locale.currency(salario, grouping=True)}')
        print(f'\033[1;30;41mPRECISAMOS INFORMAR QUE INFELIZMENTE SUAS CONDIÇÕES NÃO SE ENQUADRA EM NOSSAS CONDIÇÕES\033[m')

def dez_anos(salario,valor_casa):
        #Calcula o valor das parcelas por mes
    parcela_mes = valor_casa / (10*12)
        #Calcula a porcentagem da parcela se excede 30%
    quantidade_financiamento = salario * (30/100)
        #Verifica se a parcela não estar maior do que 30% ao mes
    if parcela_mes <= quantidade_financiamento :
        print(f'\033[1;30;43mSALARIO INFORMADO FOI {locale.currency(salario, grouping=True)}\033[m')
        print(f'\033[1;30;43mPARABÉNS !!! SEU FINANCIAMENTO FOI APROVADO COM PARCELAS DE {locale.currency(parcela_mes, grouping=True)} AO MES POR 10 ANOS\033[m')
    else :
        print(f'SALARIO INFORMADO FOI {locale.currency(salario, grouping=True)}')
        print(f'\033[1;30;41mPRECISAMOS INFORMAR QUE INFELIZMENTE SUAS CONDIÇÕES NÃO SE ENQUADRA EM NOSSAS CONDIÇÕES\033[m')

def quinze_anos(salario,valor_casa):
        #Calcula o valor das parcelas por mes 
    parcela_mes = valor_casa / (15*12)
        #Calcula a porcentagem da parcela se excede 30%
    quantidade_financiamento = salario * (30/100)
        #Verifica se a parcela não estar maior do que 30% ao mes
    if parcela_mes <= quantidade_financiamento :
        print(f'\033[1;30;43mSALARIO INFORMADO FOI {locale.currency(salario, grouping=True)}\033[m')
        print(f'\033[1;30;43mPARABÉNS !!! SEU FINANCIAMENTO FOI APROVADO COM PARCELAS DE {locale.currency(parcela_mes, grouping=True)} AO MES POR 15 ANOS\033[m')
    else :
        print(f'SALARIO INFORMADO FOI {locale.currency(salario, grouping=True)}')
        print(f'\033[1;30;41mPRECISAMOS INFORMAR QUE INFELIZMENTE SUAS CONDIÇÕES NÃO SE ENQUADRA EM NOSSAS CONDIÇÕES\033[m')

def custom(salario,valor_casa):
    print('OLÁ QUEREMOS INFRMAR QUE A PERSONALIZAÇÃO DE FINANCIAMENTO SO E VALIDA COM MAIS DE 15 ANOS')
    anos = int(input('Digite a quantidade de anos desejada para o financiamento: '))
        #VERIFICA SE A QUANTIDADES DE ANOS DIGITADO FOI MAIOR QUE 15
    if anos > 15 :
            #Calcula o valor das parlas por mes 
        parcela_mes = valor_casa / (anos * 12)
            #Calcula a porcentagem da parcela se excede 30%
        quantidade_financiamento = salario * (30/10)
                #Verifica se a parcela não estar maior do que 30% ao mes
        if parcela_mes <= quantidade_financiamento :
                print(f'\033[1;30;43mSALARIO INFORMADO FOI {locale.currency(salario, grouping=True)}\033[m')
                print(f'\033[1;30;43mPARABÉNS !!! SEU FINANCIAMENTO FOI APROVADO COM PARCELAS DE {locale.currency(parcela_mes, grouping=True)} AO MES POR {anos} ANOS\033[m')
        else :
                print(f'SALARIO INFORMADO FOI {locale.currency(salario, grouping=True)}')
                print(f'\033[1;30;41mPRECISAMOS INFORMAR QUE INFELIZMENTE SUAS CONDIÇÕES NÃO SE ENQUADRA EM NOSSAS CONDIÇÕES\033[m')

    else:
        print('\033[1;30;41mLAMENTAMOS INFORMAR MAS REALIZAMOS FINANCIAMENTO SOMENTE ACIMA DE 15 ANOS')

def menu ():
    valor_casa = float(input('Qual o valor do imovel que desaja financiar : '))
    salario = float(input('Qual o valor do seu sálario atualmente : '))
    while True:
        print('='*20)
        print('BEM VINDO AO NOSSO SISTEMA DE EMPRESTIMOS ')
        print('='*20)
        print()
        print()
        print('Agora informe em quantos anos você deseja realizar seu emprestimo: ')
        print('[1] : 5 anos')
        print('[2] : 10 anos')
        print('[3] : 15 anos')
        print('[4] : informar uma tempo de emprestimo')
        print('[5] : encerar simulação')
        
        resp = int(input('Digite sua opção : '))
        if resp == 1 :
            cinco_anos(salario, valor_casa)
            print('Deseja realizar outra simulação ?')
            print('[1] - S I M') 
            print('[2] - N Ã O') 
            opcao = int(input('Digite sua opção : '))
            if opcao == 1 :
                menu()
            elif opcao == 2:
                break
            else:
                print ('Opção invalida')
                return menu()
                      
        elif resp == 2 :
            dez_anos(salario, valor_casa)
            print('Deseja realizar outra simulação ?')
            print('[1] - S I M ')
            print('[2] - N Ã O ')
            opcao = int(input('Digite sua opção : '))
            if opcao == 1 :
                menu()
            elif opcao == 2:
                break
            else:
                print ('Opção invalida')
                return menu()

        elif resp == 3 :
            quinze_anos(salario, valor_casa)
            print('Deseja realizar outra simulação ?')
            print('[1] - S I M ')
            print('[2] - N Ã O ')
            opcao = int(input('Digite sua opção : '))
            if opcao == 1 :
                menu()
            elif opcao == 2:
                break
            else:
                print ('Opção invalida')
                return menu()

        elif resp == 4 :
            custom(salario, valor_casa)
            print('Deseja realizar outra simulação ?')
            print('[1] - S I M ')
            print('[2] - N Ã O ')
            opcao = int(input('Digite sua opção : '))
            if opcao == 1 :
                menu()
            elif opcao == 2:
                break
            else:
                print ('Opção invalida')
                return menu()

        elif resp == 5:
            break

        else:
            print('Opação invalida !!!')

menu()
