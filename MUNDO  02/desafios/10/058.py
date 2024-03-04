""" Desafio 058
Melhore o jogo do desafio 028 onde o computador vai "pensar" em um numero entre 0 e 10 . So que agora o jogador vai tentar adivinhar ate acertar, mostrando no final quantos palpites foram necessarios para vencer. """


import random

from time import sleep

random_number = random.randint(1, 5)

tentativas = 0 

print('Digite um número de 1 a 5 e veja se você adivinhou o numero que a maquina pensou !!')
while True:

    print('-=' * 20)

    user_number = int(input('AGORA DIGITE UM NUMERO : '))

    print('PROCESSANDO ....')

    sleep(2)
        #Verifica se o usuario digitou um numero entre 1 ao 5
    if 1 <= user_number <= 5 :
        if random_number == user_number :
            print(f'PARABÉNS ! ! O número que a máquina pensou foi {random_number} e você acertou {user_number}, você precisou de {tentativas} tentativas para acertar')
            break
        else :
            tentativas+=1
            print(f'A QUE PENA ! !, A maquina pensou no {random_number} e você digitou {user_number}')
            print('MAIS SORTE DA PROXIMA VEZ !!!')

    else :

        print('ATENÇÃO O NÚMERO DEVE SER DE 1 A 5')
