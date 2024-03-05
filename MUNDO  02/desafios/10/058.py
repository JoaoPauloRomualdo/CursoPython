""" Desafio 058
Melhore o jogo do desafio 028 onde o computador vai "pensar" em um numero entre 0 e 10 . So que agora o jogador vai tentar adivinhar ate acertar, mostrando no final quantos palpites foram necessarios para vencer. """


from random import randint

from time import sleep

computador = randint(0, 10)

print('-=' * 20)
print('Sou seu computador ... Acabei de pensar em um número entre 0 e 10 !!!')
print('Será que você consegue adivinhar qual foi ?')
print('-=' * 20)

acertou = False
tentativas = 0
while not acertou:

    jogador = int(input('Qual e seu palpite : '))
    tentativas+=1
    print('PROCESSANDO ....')

    sleep(2)
        #Verifica se o usuario digitou um numero entre 1 ao 5
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Pensei em um numero maior , Tente mais uma vez !')
        elif jogador > computador:
            print('Pensei em um numero menor, Tente mais uma vez ')

print(f'Acertou com {tentativas} tentativas')
