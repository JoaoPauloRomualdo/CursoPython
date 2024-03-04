""" Desafio 059
Crie um progama que leia dois valores e mostre um menu na tela :

[1]- somar
[2]- multiplicar
[3]- maior
[4]- novos numeros
[5]- sair do programa

Seu programa devera realizar a operação solicitada em cada caso .
 """

def soma(primeiro_numero,segundo_numero):
    print('-='*15)
    resultado = primeiro_numero + segundo_numero
    print(f'A soma entre {primeiro_numero} + {segundo_numero} = {resultado}')


def multiplicacao(primeiro_numero, segundo_numero):
    print('-='*15)
    resultado = primeiro_numero * segundo_numero
    print(f'A multiplicação entre {primeiro_numero} x {segundo_numero} = {resultado}')


def maior(primeiro_numero, segundo_numero):
    print('-='*15)
    if primeiro_numero > segundo_numero:
        print(f'O primeiro valor {primeiro_numero} e o maior numero digitado entre {primeiro_numero} e {segundo_numero}')
    elif segundo_numero > primeiro_numero :
        print(f'O segundo valor {segundo_numero} e o maior numero digitado entre {primeiro_numero} e {segundo_numero}')
    else :
        print(f'Parece que os valores digitados sao iguais {primeiro_numero} e {segundo_numero}')


def menu():
    primeiro_numero = float(input('Digite o primeiro valor : '))
    segundo_numero = float(input('Digite o valor do segundo valor : '))

    while True:
        opcao = int(input(' [1]- somar\n [2]- multiplicar\n [3]- maior\n [4]- novos numeros\n [5]- sair do programa \n Informe a opção desejada: '))
        
        if opcao == 1:
            soma(primeiro_numero,segundo_numero)
        elif opcao == 2 :
            multiplicacao(primeiro_numero, segundo_numero)
        elif opcao == 3 : 
            maior(primeiro_numero, segundo_numero)
        elif opcao == 4 :
            menu()
        else:
            break

menu()