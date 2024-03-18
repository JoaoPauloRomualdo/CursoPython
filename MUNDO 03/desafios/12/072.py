""" Desafio 72

Crie um programa que tenha um tupla totalmente preechida com uma contagem por extenção de zero ate vinte.Seu programa deverá ler um numero pelo teclado (entre 0 e 20) e mostra-lo por extenso. """

numeros = ('Zero',
           'Um',
           'Dois',
           'Três', 
           'Quatro',
           'Cinco',
           'Seis',
           'Sete',
           'Oito',
           'Nove',
           'Dez',
           'Onze',
           'Doze',
           'Treze',
           'Quatorze',
           'Quinze',
           'Dezeseis',
           'Dezesete',
           'Dezoito',
           'Dezenove',
           'Vinte')
while True:
    n = int(input('Digite um numero entre 0 - 20: '))
    if 0 <= n <= 20:
        print('Tente novamente ....')
        n = int(input('Digite um numero entre 0 - 20: '))   
        print(f'Número digitado foi {n}, e ele escrito por extenso fica {numeros[n]}')
        break
    else :
        print('Número fora do intervalo permitido.')
            